"""
=========================================================
Nestlé DOM Quantum Optimization
QAOA Implementation — connected to real order data

Compatible with:

qiskit                 2.4.1
qiskit-aer             0.17.2
qiskit-algorithms      0.4.0
qiskit-optimization    0.7.0

=========================================================

WHAT CHANGED FROM THE ORIGINAL quantum_optimizer.py
----------------------------------------------------
The original file solved a hand-written 3-order toy problem
(Order_1/2/3, made-up revenue 100/120/90, capacity <= 2) that has
no connection to the real dataset — that toy result (objective 220)
is what the dashboard's "Quantum Result" panel was showing.

This version:
  1. Builds the optimization problem from REAL order-lines
     (data/optimized_orders_sample.csv), using actual revenue and
     actual demand vs. actual available inventory as the capacity
     constraint — a genuine 0/1 knapsack, not a toy.
  2. Uses QuadraticProgramToQubo to convert the constrained model
     into a QUBO automatically (proper penalty terms), instead of
     hand-rolling penalty coefficients.
  3. Solves the SAME problem three ways — exact classical
     (NumPyMinimumEigensolver, a real optimum for small instances),
     a simple classical greedy heuristic, and QAOA — and reports
     objective value, feasibility, and optimality gap for each,
     so QAOA's quality is actually benchmarked rather than reported
     in isolation.
"""

import time
import math
import itertools

import pandas as pd
import numpy as np

from qiskit_optimization import QuadraticProgram
from qiskit_optimization.converters import QuadraticProgramToQubo
from qiskit_optimization.algorithms import MinimumEigenOptimizer

from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import COBYLA

from qiskit.primitives import StatevectorSampler


# ==============================
# 1. PICK A REAL FOCUS INSTANCE
# ==============================

def _estimate_qubit_count(n_orders, capacity):
    """
    QuadraticProgramToQubo encodes a `<=` constraint with integer slack
    variables using ceil(log2(capacity + 1)) extra binary variables.
    Total simulated qubits = n_orders + slack bits.
    """
    slack_bits = max(1, math.ceil(math.log2(capacity + 1)))
    return n_orders + slack_bits


def find_capacity_constrained_instance(df, min_orders=3, max_orders=200, max_qubits=9, max_batch_size=4, random_state=None):
    """
    Find a (Plant, MaterialNumber) group where multiple order-lines
    compete for the same inventory pool and total demand exceeds
    available inventory — i.e. a genuine assignment trade-off, not
    a "select everything" or "reject everything" case.

    `max_qubits` caps the estimated QUBO size (order count + slack
    bits for the capacity constraint) so the instance is actually
    solvable by QAOA on a classical simulator in reasonable time —
    simulated statevector cost grows exponentially with qubit count
    (empirically: ~5s at 6 qubits, ~30s at 8, unusable past ~10-11
    in a CPU-only environment), so this is a real constraint, not an
    arbitrary one.

    By default returns the single "best" (largest, most qubit-budget-
    using) qualifying group. Pass `random_state` (any int) to instead
    pick a random qualifying group — used by the dashboard's "try a
    different real order batch" button so it isn't stuck showing the
    same instance every time.

    Returns (plant, material_number), or None if the dataset has no
    qualifying group at all.
    """
    grp = df.groupby(["Plant", "MaterialNumber"]).agg(
        n_orders=("Group_Flag", "count"),
        total_demand=("OrderedQty_converted", "sum"),
        avg_inventory=("Available_inventory", "mean"),
    ).reset_index()

    # count, per group, how many individual orders fit within capacity —
    # need at least 2 for a genuine combinatorial choice (not just
    # "the one order that fits, or nothing")
    fits_count = (
        df.assign(fits=df["OrderedQty_converted"] <= df["Available_inventory"])
        .groupby(["Plant", "MaterialNumber"])["fits"]
        .sum()
        .reset_index()
        .rename(columns={"fits": "n_individually_feasible"})
    )
    grp = grp.merge(fits_count, on=["Plant", "MaterialNumber"])

    candidates = grp[
        (grp["n_orders"] >= min_orders)
        & (grp["n_orders"] <= max_orders)
        & (grp["avg_inventory"] > 0)
        # a genuine trade-off: not everything fits, but at least two
        # different orders individually could (so there's an actual
        # choice to make, not just "the one that fits, or nothing")
        & (grp["total_demand"] > grp["avg_inventory"])
        & (grp["n_individually_feasible"] >= 2)
    ].copy()

    candidates["est_qubits"] = candidates.apply(
        lambda r: _estimate_qubit_count(min(int(r["n_orders"]), max_batch_size), int(r["avg_inventory"])),
        axis=1,
    )
    candidates = candidates[candidates["est_qubits"] <= max_qubits]

    if candidates.empty:
        return None

    if random_state is not None:
        row = candidates.sample(n=1, random_state=random_state).iloc[0]
    else:
        candidates = candidates.sort_values(["est_qubits", "n_orders"], ascending=[False, False])
        row = candidates.iloc[0]

    return int(row["Plant"]), int(row["MaterialNumber"])


def load_focus_orders_from_df(df, plant=None, material_number=None, max_batch_size=4, random_state=None):
    """
    Same as load_focus_orders() below, but takes an already-loaded
    DataFrame instead of a CSV path — use this from callers (like the
    Streamlit app) that already have the orders DataFrame in memory.
    """
    if plant is None or material_number is None:
        found = find_capacity_constrained_instance(df, max_batch_size=max_batch_size, random_state=random_state)
        if found is None:
            raise ValueError("No capacity-constrained instance found in this dataset.")
        plant, material_number = found

    subset = df[(df["Plant"] == plant) & (df["MaterialNumber"] == material_number)].copy()
    subset = subset.reset_index(drop=True)

    if subset.empty:
        raise ValueError(f"No orders found for Plant {plant}, SKU {material_number}.")

    if len(subset) > max_batch_size:
        subset = subset.nlargest(max_batch_size, "OrderedQty_converted").reset_index(drop=True)

    return subset, plant, material_number


def load_focus_orders(csv_path, plant=None, material_number=None, max_batch_size=4):
    """
    Load a real, tractable subset of orders to optimize. If plant/
    material_number aren't given, auto-selects a genuine capacity-
    constrained instance from the data (see above).

    If the selected group has more than `max_batch_size` order-lines,
    it's trimmed down to the `max_batch_size` largest-demand orders.
    This is the "batching" scalability strategy from the project
    write-up applied directly: rather than solving all order-lines
    at once (intractable for a classical QAOA simulator — see
    _estimate_qubit_count), take a real batch small enough to solve,
    keeping the largest-demand orders so the capacity constraint
    still genuinely binds instead of everything trivially fitting.
    """
    df = pd.read_csv(csv_path)
    return load_focus_orders_from_df(df, plant=plant, material_number=material_number, max_batch_size=max_batch_size)


def run_full_comparison(df, plant=None, material_number=None, max_batch_size=4, reps=1, maxiter=15,
                         random_state=None, n_seeds=None):
    """
    One-call entry point for callers (e.g. the Streamlit dashboard)
    that want the full real-data pipeline — pick an instance, build
    the problem, solve all three ways, return everything needed to
    render it. Raises the same ValueErrors as load_focus_orders_from_df
    if no suitable instance exists in the given data.

    Pass `random_state` to get a different real qualifying instance
    each call (used by the dashboard's "try a different order batch"
    button) instead of always the same default one.

    Pass `n_seeds` (e.g. 6-10) to ALSO run QAOA multiple times with
    randomized initial points and report a genuine success rate — a
    single QAOA run is deterministic given a fixed starting point, so
    it proves nothing about reliability on its own (see solve_qaoa's
    docstring). This roughly doubles+ the total runtime, so it's
    off by default; the dashboard's live "Recompute" button does not
    use it, only the offline cache-generation script does.
    """
    orders_df, plant, material_number = load_focus_orders_from_df(
        df, plant=plant, material_number=material_number,
        max_batch_size=max_batch_size, random_state=random_state,
    )
    problem, var_names, capacity = create_problem_from_data(orders_df)

    exact = solve_exact_classical(problem)
    greedy = solve_greedy_classical(problem)
    quantum = solve_qaoa(problem, reps=reps, maxiter=maxiter)

    multi_seed = None
    if n_seeds is not None:
        multi_seed = run_qaoa_multi_seed(
            problem, n_seeds=n_seeds, reps=reps, maxiter=maxiter,
            exact_objective=exact["objective"],
        )

    return {
        "orders_df": orders_df,
        "plant": plant,
        "material_number": material_number,
        "capacity": capacity,
        "exact": exact,
        "greedy": greedy,
        "quantum": quantum,
        "multi_seed": multi_seed,
    }


# ==============================
# RESULT CACHING
# ==============================
#
# QAOA takes ~10-20s even on this small a batch. A live dashboard
# visitor should never wait that long just to open a tab — so the
# result is computed ONCE (via `python quantum_optimizer.py` or the
# "Recompute Live" button) and cached to a JSON file. Every normal
# page load then reads the cache instantly. This is standard practice
# for any demo backed by a slow computation: precompute, cache, serve.

DEFAULT_CACHE_PATH = "data/quantum_result_cache.json"


def _to_jsonable(run_result):
    """Strip the DataFrame and numpy types out of a run_full_comparison()
    result so it can be written as plain JSON."""

    def clean(d):
        return {
            "method": d["method"],
            "objective": float(d["objective"]),
            "assignment": {k: int(v) for k, v in d["assignment"].items()},
            "feasible": bool(d["feasible"]),
            "runtime_sec": float(d["runtime_sec"]),
        }

    out = {
        "generated_at": time.strftime("%Y-%m-%d %H:%M:%S UTC", time.gmtime()),
        "plant": int(run_result["plant"]),
        "material_number": int(run_result["material_number"]),
        "capacity": float(run_result["capacity"]),
        "orders": run_result["orders_df"][
            ["Group_Flag", "OrderedQty_converted", "Order_SKU_Revenue", "Available_inventory"]
        ].to_dict(orient="records"),
        "exact": clean(run_result["exact"]),
        "greedy": clean(run_result["greedy"]),
        "quantum": clean(run_result["quantum"]),
    }

    if run_result.get("multi_seed") is not None:
        ms = run_result["multi_seed"]
        out["multi_seed"] = {
            "n_seeds": ms["n_seeds"],
            "objectives": [float(o) for o in ms["objectives"]],
            "min_objective": float(ms["min_objective"]),
            "max_objective": float(ms["max_objective"]),
            "mean_objective": float(ms["mean_objective"]),
            "n_feasible": int(ms["n_feasible"]),
            "n_optimal": int(ms["n_optimal"]) if ms["n_optimal"] is not None else None,
            "success_rate": float(ms["success_rate"]) if ms["success_rate"] is not None else None,
            "mean_runtime_sec": float(ms["mean_runtime_sec"]),
        }

    return out


def save_result_cache(run_result, path=DEFAULT_CACHE_PATH):
    """Save a run_full_comparison() result to disk for instant reloading."""
    import json
    import os

    os.makedirs(os.path.dirname(path), exist_ok=True) if os.path.dirname(path) else None
    with open(path, "w") as f:
        json.dump(_to_jsonable(run_result), f, indent=2)
    return path


def load_result_cache(path=DEFAULT_CACHE_PATH):
    """
    Load a previously cached result. Returns None if no cache file
    exists yet (caller should fall back to showing a "run it" button).
    """
    import json
    import os

    if not os.path.exists(path):
        return None

    with open(path) as f:
        return json.load(f)


# ==============================
# 2. BUILD THE REAL PROBLEM
# ==============================

def create_problem_from_data(orders_df):
    """
    Build a genuine constrained QuadraticProgram from real order-lines:
      - one binary variable per order-line
      - maximize total Order_SKU_Revenue
      - inventory capacity constraint: sum(qty_i * x_i) <= available inventory
    """
    problem = QuadraticProgram(name="Nestle_DOM_Real_Orders")

    var_names = []
    for i in orders_df.index:
        name = f"order_{orders_df.loc[i, 'Group_Flag']}"
        problem.binary_var(name=name)
        var_names.append(name)

    revenue_terms = {
        name: float(orders_df.loc[i, "Order_SKU_Revenue"])
        for i, name in zip(orders_df.index, var_names)
    }
    problem.maximize(linear=revenue_terms)

    capacity = float(orders_df["Available_inventory"].iloc[0])
    demand_terms = {
        name: float(orders_df.loc[i, "OrderedQty_converted"])
        for i, name in zip(orders_df.index, var_names)
    }
    problem.linear_constraint(
        linear=demand_terms,
        sense="<=",
        rhs=capacity,
        name="inventory_capacity",
    )

    return problem, var_names, capacity


def create_toy_problem():
    """
    Original 3-order toy problem, kept only as a smoke-test /
    reference example — NOT used for the reported quantum result.
    """
    problem = QuadraticProgram(name="Nestle_DOM_Toy")
    problem.binary_var(name="Order_1")
    problem.binary_var(name="Order_2")
    problem.binary_var(name="Order_3")
    problem.maximize(linear={"Order_1": 100, "Order_2": 120, "Order_3": 90})
    problem.linear_constraint(
        linear={"Order_1": 1, "Order_2": 1, "Order_3": 1},
        sense="<=", rhs=2, name="Capacity",
    )
    return problem


# ==============================
# 3. SOLVE — EXACT / GREEDY / QAOA
# ==============================

def solve_exact_classical(problem):
    """
    True optimum via exhaustive enumeration over all 2^n assignments.
    Only tractable for small n (this focus instance: <= ~16 orders) —
    that's the point: it gives ground truth to benchmark QAOA against,
    which the earlier version of this project had no way to do.
    """
    n = problem.get_num_vars()
    var_names = [v.name for v in problem.variables]

    best_val = float("-inf")
    best_assignment = None

    start = time.time()
    for bits in itertools.product([0, 1], repeat=n):
        feasible = True
        for constraint in problem.linear_constraints:
            lhs = sum(
                constraint.linear.to_dict().get(i, 0) * bits[i]
                for i in range(n)
            )
            if constraint.sense.name == "LE" and lhs > constraint.rhs:
                feasible = False
                break
        if not feasible:
            continue

        val = sum(
            problem.objective.linear.to_dict().get(i, 0) * bits[i]
            for i in range(n)
        )
        if val > best_val:
            best_val = val
            best_assignment = bits
    runtime = time.time() - start

    return {
        "method": "Exact classical (brute force)",
        "objective": best_val,
        "assignment": dict(zip(var_names, best_assignment)) if best_assignment else {},
        "feasible": best_assignment is not None,
        "runtime_sec": runtime,
    }


def solve_greedy_classical(problem):
    """
    Simple greedy heuristic: rank orders by revenue-per-unit-demand,
    accept in that order while capacity allows. Fast, transparent,
    business-as-usual style baseline.
    """
    var_names = [v.name for v in problem.variables]
    n = len(var_names)

    revenue = [problem.objective.linear.to_dict().get(i, 0) for i in range(n)]
    constraint = problem.linear_constraints[0]
    demand = [constraint.linear.to_dict().get(i, 0) for i in range(n)]
    capacity = constraint.rhs

    ratio = [
        (revenue[i] / demand[i] if demand[i] > 0 else 0, i)
        for i in range(n)
    ]
    ratio.sort(reverse=True)

    start = time.time()
    remaining = capacity
    assignment = {name: 0 for name in var_names}
    total_value = 0.0

    for _, i in ratio:
        if demand[i] <= remaining:
            assignment[var_names[i]] = 1
            remaining -= demand[i]
            total_value += revenue[i]
    runtime = time.time() - start

    return {
        "method": "Greedy classical heuristic",
        "objective": total_value,
        "assignment": assignment,
        "feasible": True,
        "runtime_sec": runtime,
    }


def solve_qaoa(problem, reps=1, maxiter=15, initial_point=None):
    """
    Solve via QAOA on a noiseless simulator, after converting the
    constrained problem into a QUBO automatically (penalty terms
    generated by QuadraticProgramToQubo rather than hand-written).

    NOTE on determinism: if `initial_point` is left as None, QAOA
    starts from a fixed default point every time — running this
    function repeatedly with no initial_point gives IDENTICAL results
    every run (confirmed empirically), which makes a single run
    meaningless as evidence of reliable convergence. Pass an explicit
    (randomized) initial_point — see run_qaoa_multi_seed() below — to
    get a genuine, varying result across runs.
    """
    converter = QuadraticProgramToQubo()
    qubo = converter.convert(problem)

    sampler = StatevectorSampler()
    optimizer = COBYLA(maxiter=maxiter)
    qaoa = QAOA(sampler=sampler, optimizer=optimizer, reps=reps, initial_point=initial_point)
    solver = MinimumEigenOptimizer(qaoa)

    start = time.time()
    result = solver.solve(problem)  # MinimumEigenOptimizer handles the QUBO conversion internally too
    runtime = time.time() - start

    assignment = dict(zip([v.name for v in problem.variables], (int(v) for v in result.x)))

    # Feasibility check against the ORIGINAL constrained problem —
    # QAOA/QUBO constraints are soft penalties, so this must be
    # verified rather than assumed.
    feasible = True
    for constraint in problem.linear_constraints:
        lhs = sum(
            constraint.linear.to_dict().get(i, 0) * result.x[i]
            for i in range(len(result.x))
        )
        if constraint.sense.name == "LE" and lhs > constraint.rhs + 1e-6:
            feasible = False

    return {
        "method": f"QAOA (Qiskit simulator, reps={reps})",
        "objective": result.fval,
        "assignment": assignment,
        "feasible": feasible,
        "runtime_sec": runtime,
        "qubo_num_vars": qubo.get_num_vars(),
    }


def run_qaoa_multi_seed(problem, n_seeds=10, reps=1, maxiter=15, exact_objective=None, base_seed=0):
    """
    Run QAOA `n_seeds` times, each from an independently randomized
    initial point, and report a genuine success rate — a single QAOA
    run proves nothing about reliability, since it's deterministic
    given a fixed starting point (see solve_qaoa's docstring). This
    is what "evaluation rigor" actually requires for a stochastic
    method: a distribution over runs, not one number.

    `exact_objective`: pass the known true optimum (e.g. from
    solve_exact_classical) to compute a real success rate (fraction
    of runs reaching that optimum) rather than just reporting spread.
    """
    n_params = 2 * reps  # QAOA with `reps` layers has one (gamma, beta) pair per layer

    runs = []
    for seed in range(base_seed, base_seed + n_seeds):
        rng = np.random.default_rng(seed)
        initial_point = rng.uniform(0, 2 * np.pi, size=n_params)

        result = solve_qaoa(problem, reps=reps, maxiter=maxiter, initial_point=initial_point)
        result["seed"] = seed
        runs.append(result)

    objectives = [r["objective"] for r in runs]
    feasible_runs = [r for r in runs if r["feasible"]]

    if exact_objective is not None:
        n_optimal = sum(1 for r in feasible_runs if abs(r["objective"] - exact_objective) < 1e-6)
        success_rate = n_optimal / n_seeds
    else:
        n_optimal = None
        success_rate = None

    return {
        "n_seeds": n_seeds,
        "runs": runs,
        "objectives": objectives,
        "min_objective": min(objectives),
        "max_objective": max(objectives),
        "mean_objective": float(np.mean(objectives)),
        "n_feasible": len(feasible_runs),
        "n_optimal": n_optimal,
        "success_rate": success_rate,
        "mean_runtime_sec": float(np.mean([r["runtime_sec"] for r in runs])),
    }


# ==============================
# 4. COMPARE
# ==============================

def compare_methods(results, exact_objective=None):
    print("\n" + "=" * 72)
    print(f"{'Method':<32}{'Objective':>12}{'Feasible':>12}{'Runtime (s)':>14}")
    print("=" * 72)

    for r in results:
        gap = ""
        if exact_objective and exact_objective != 0:
            gap_pct = (exact_objective - r["objective"]) / exact_objective * 100
            gap = f"  (gap: {gap_pct:.1f}%)"
        print(
            f"{r['method']:<32}{r['objective']:>12.2f}"
            f"{str(r['feasible']):>12}{r['runtime_sec']:>14.4f}{gap}"
        )
    print("=" * 72)


# ==============================
# MAIN
# ==============================

if __name__ == "__main__":

    # Adjust this to wherever your repo's SKU-level order extract lives
    # (e.g. "data/optimized_orders_sample.csv") — this is the file the
    # Streamlit dashboard's Fill Rate / Qora AI logic also reads from,
    # so the same columns need to be present.
    CSV_PATH = "optimized_orders.csv"

    print("\n" + "=" * 60)
    print("Nestlé Distributed Order Management — Quantum Optimization")
    print("=" * 60)

    orders_df, plant, material_number = load_focus_orders(CSV_PATH)

    print(f"\nFocus instance: Plant {plant}, SKU {material_number}")
    print(f"Orders in this instance: {len(orders_df)}")
    print(orders_df[["Group_Flag", "OrderedQty_converted", "Order_SKU_Revenue", "Available_inventory"]]
          .to_string(index=False))

    problem, var_names, capacity = create_problem_from_data(orders_df)
    print(f"\nCapacity constraint: total assigned quantity <= {capacity}")
    print("\nOptimization problem:\n")
    print(problem.prettyprint())

    exact = solve_exact_classical(problem)
    greedy = solve_greedy_classical(problem)
    quantum = solve_qaoa(problem)

    compare_methods([exact, greedy, quantum], exact_objective=exact["objective"])

    print("\nExact classical assignment: ", exact["assignment"])
    print("Greedy classical assignment:", greedy["assignment"])
    print("QAOA assignment:            ", quantum["assignment"])

    # A single QAOA run is deterministic given a fixed starting point
    # (confirmed empirically — see solve_qaoa's docstring) and proves
    # nothing about reliability on its own. Run it N_SEEDS times from
    # independently randomized starting points and report the real
    # success rate. This takes noticeably longer (each run is a full
    # QAOA solve) — reduce N_SEEDS if this is too slow on your machine.
    N_SEEDS = 10
    print(f"\nRunning QAOA from {N_SEEDS} random initial points to check reliability...")
    multi_seed = run_qaoa_multi_seed(
        problem, n_seeds=N_SEEDS, exact_objective=exact["objective"]
    )
    print(f"\nMulti-seed QAOA reliability check ({N_SEEDS} runs):")
    print(f"  Objectives: {multi_seed['objectives']}")
    print(f"  Feasible:   {multi_seed['n_feasible']}/{multi_seed['n_seeds']}")
    print(f"  Optimal:    {multi_seed['n_optimal']}/{multi_seed['n_seeds']} "
          f"(success rate: {multi_seed['success_rate']*100:.0f}%)")
    print(f"  Mean runtime per run: {multi_seed['mean_runtime_sec']:.2f}s")

    # Cache the result so the Streamlit dashboard can load it instantly
    # instead of every visitor waiting ~10-20s for QAOA to run. Re-run
    # this script (or click "Recompute Live" in the dashboard) whenever
    # the underlying order data changes.
    cache_result = {
        "orders_df": orders_df,
        "plant": plant,
        "material_number": material_number,
        "capacity": capacity,
        "exact": exact,
        "greedy": greedy,
        "quantum": quantum,
        "multi_seed": multi_seed,
    }
    cache_path = save_result_cache(cache_result)
    print(f"\nCached result saved to: {cache_path}")
    print("The dashboard's Quantum Optimization tab will load this instantly.")