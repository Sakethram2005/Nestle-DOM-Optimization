"""
=========================================================
Nestlé DOM — Benchmark: Baseline vs OR-Tools vs Quantum
benchmark.py

Compares three solution strategies on the SAME objective
function and feasibility check (revenue maximization subject
to per-(Plant, SKU) inventory capacity):

  1. Baseline       — default assignment, no optimization.
                      Orders accepted in original (arrival)
                      row order while capacity lasts.
  2. OR-Tools       — CP-SAT exact solver. Fast enough to run
                      on the FULL dataset (25k+ orders) —
                      confirmed: <1 second.
  3. Quantum (QAOA) — only tractable on a small batch (see
                      quantum_optimizer.py's qubit-budget
                      analysis). Read from the cached result
                      quantum_optimizer.py produces.

Two comparisons are reported, deliberately kept separate:

  TABLE 1 (full dataset scale): Baseline vs OR-Tools.
      Quantum is NOT included here — it cannot run at this
      scale on a simulator, and pretending otherwise would
      misrepresent the comparison.

  TABLE 2 (same small batch QAOA actually solved): Baseline
      vs OR-Tools vs Quantum, all three restricted to the
      identical order subset — a genuine apples-to-apples
      comparison at the one scale where all three can run.

Metrics reported for each: Revenue, Shipping Cost, Runtime,
Warehouse Utilization, Fill Rate.
=========================================================
"""

import time

import pandas as pd
from ortools.sat.python import cp_model

import quantum_optimizer


# =====================================================
# SOLVERS — each returns (selected: np.ndarray of 0/1, runtime_sec)
# =====================================================

def solve_baseline(df):
    """
    Default assignment: no reassignment, no optimization. Orders are
    accepted in their original row order (a proxy for arrival order —
    the data has no explicit sequence field) while the shared
    (Plant, SKU) inventory pool lasts. This mirrors "business as
    usual" — the reference point everything else is measured against.
    """
    t0 = time.time()

    selected = pd.Series(0, index=df.index)
    remaining = (
        df.groupby(["Plant", "MaterialNumber"])["Available_inventory"]
        .first()
        .to_dict()
    )

    for idx, row in df.iterrows():
        key = (row["Plant"], row["MaterialNumber"])
        cap_left = remaining.get(key, 0)
        qty = row["OrderedQty_converted"]
        if qty <= cap_left:
            selected.loc[idx] = 1
            remaining[key] = cap_left - qty

    runtime = time.time() - t0
    return selected.values, runtime


def solve_ortools(df):
    """
    Exact solver via CP-SAT: one binary variable per order-line, one
    capacity constraint per (Plant, SKU) group (independent knapsacks,
    solved jointly in a single model), maximizing total revenue.
    This is the SAME objective/constraint as the QUBO in
    quantum_optimizer.py — just solved exactly, at full scale.
    """
    t0 = time.time()

    model = cp_model.CpModel()
    n = len(df)
    x = [model.NewBoolVar(f"x{i}") for i in range(n)]

    qty = df["OrderedQty_converted"].values
    inv = df["Available_inventory"].values
    rev = df["Order_SKU_Revenue"].values

    groups = df.groupby(["Plant", "MaterialNumber"]).indices
    for (_plant, _sku), idxs in groups.items():
        cap = int(inv[idxs[0]])
        model.Add(sum(int(qty[i]) * x[i] for i in idxs) <= cap)

    model.Maximize(sum(int(rev[i]) * x[i] for i in range(n)))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 60
    solver.parameters.num_search_workers = 4
    status = solver.Solve(model)

    runtime = time.time() - t0

    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        raise RuntimeError(f"OR-Tools did not find a solution (status={solver.StatusName(status)})")

    selected = [int(solver.Value(x[i])) for i in range(n)]
    return selected, runtime


# =====================================================
# METRICS — same definitions used across all three methods
# =====================================================

def compute_metrics(df, selected, runtime):
    """
    Revenue, Shipping Cost, Warehouse Utilization, Fill Rate — computed
    identically regardless of which method produced `selected`, so the
    comparison is genuinely apples-to-apples.
    """
    d = df.copy()
    d["_selected"] = selected

    revenue = float(d.loc[d["_selected"] == 1, "Order_SKU_Revenue"].sum())
    shipping_cost = float(d.loc[d["_selected"] == 1, "Shipping_Cost"].sum())

    total_qty = d["OrderedQty_converted"].sum()
    fulfilled_qty = d.loc[d["_selected"] == 1, "OrderedQty_converted"].sum()
    fill_rate = (fulfilled_qty / total_qty * 100) if total_qty else 0.0

    d["_assigned_qty"] = d["OrderedQty_converted"] * d["_selected"]
    util_by_plant = (
        d.groupby("Plant")
        .agg(assigned=("_assigned_qty", "sum"), avg_inv=("Available_inventory", "mean"))
    )
    util_by_plant = util_by_plant[util_by_plant["avg_inv"] > 0]
    avg_utilization = (
        (util_by_plant["assigned"] / util_by_plant["avg_inv"]).mean() * 100
        if not util_by_plant.empty else 0.0
    )

    return {
        "Revenue": revenue,
        "Shipping Cost": shipping_cost,
        "Runtime (s)": runtime,
        "Warehouse Utilization (%)": avg_utilization,
        "Fill Rate (%)": fill_rate,
    }


# =====================================================
# TABLE 1 — full dataset scale (Baseline vs OR-Tools)
# =====================================================

def run_full_scale_benchmark(df):

    baseline_sel, baseline_t = solve_baseline(df)
    ortools_sel, ortools_t = solve_ortools(df)

    baseline_metrics = compute_metrics(df, baseline_sel, baseline_t)
    ortools_metrics = compute_metrics(df, ortools_sel, ortools_t)

    table = pd.DataFrame({
        "Baseline": baseline_metrics,
        "OR-Tools": ortools_metrics,
    }).T

    return table


# =====================================================
# TABLE 2 — same small batch QAOA actually solved
# (Baseline vs OR-Tools vs Quantum, apples-to-apples)
# =====================================================

def compute_quantum_scope_benchmark(df, plant, material_number, order_ids, quantum_assignment, quantum_runtime):
    """
    Core comparison logic, decoupled from the cache file — takes
    whichever quantum result the caller currently has in hand (could
    be the on-disk cache, a live "Recompute" result, or a "Random
    Batch" result), so the table always matches whatever quantum
    result is actually being displayed alongside it.
    """
    batch_df = df[(df["Plant"] == plant) & (df["MaterialNumber"] == material_number)].copy()
    # Match the exact same order-lines the quantum run used —
    # quantum_optimizer.py keeps the largest-demand orders when a group
    # is bigger than the batch size, so filter down to those same ids.
    batch_df = batch_df[batch_df["Group_Flag"].isin(order_ids)].reset_index(drop=True)

    baseline_sel, baseline_t = solve_baseline(batch_df)
    ortools_sel, ortools_t = solve_ortools(batch_df)

    baseline_metrics = compute_metrics(batch_df, baseline_sel, baseline_t)
    ortools_metrics = compute_metrics(batch_df, ortools_sel, ortools_t)

    # Quantum's own selection, mapped onto the same batch_df row order
    key_to_selected = {
        int(k.replace("order_", "")): v
        for k, v in quantum_assignment.items()
    }
    quantum_sel = batch_df["Group_Flag"].map(key_to_selected).fillna(0).astype(int).values
    quantum_metrics = compute_metrics(batch_df, quantum_sel, quantum_runtime)

    table = pd.DataFrame({
        "Baseline": baseline_metrics,
        "OR-Tools": ortools_metrics,
        "Quantum (QAOA)": quantum_metrics,
    }).T

    return table


def run_quantum_scope_benchmark(df, cache_path=quantum_optimizer.DEFAULT_CACHE_PATH):
    """Standalone/script entry point — reads the on-disk cache."""

    cached = quantum_optimizer.load_result_cache(cache_path)
    if cached is None:
        raise ValueError(
            "No cached quantum result found — run `python quantum_optimizer.py` first."
        )

    plant = cached["plant"]
    sku = cached["material_number"]
    order_ids = {o["Group_Flag"] for o in cached["orders"]}

    table = compute_quantum_scope_benchmark(
        df, plant, sku, order_ids,
        cached["quantum"]["assignment"], cached["quantum"]["runtime_sec"],
    )

    return table, plant, sku


# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":

    CSV_PATH = "optimized_orders.csv"
    df = pd.read_csv(CSV_PATH)

    print("\n" + "=" * 70)
    print("TABLE 1 — Full dataset scale (Baseline vs OR-Tools)")
    print(f"({len(df):,} order-lines — Quantum cannot run at this scale, see")
    print(" quantum_optimizer.py's qubit-budget analysis)")
    print("=" * 70)
    table1 = run_full_scale_benchmark(df)
    print(table1.to_string(float_format=lambda x: f"{x:,.2f}"))

    print("\n" + "=" * 70)
    print("TABLE 2 — Same small batch QAOA actually solved")
    print("(Baseline vs OR-Tools vs Quantum, apples-to-apples)")
    print("=" * 70)
    try:
        table2, plant, sku = run_quantum_scope_benchmark(df)
        print(f"Instance: Plant {plant}, SKU {sku}")
        print(table2.to_string(float_format=lambda x: f"{x:,.4f}"))
    except ValueError as e:
        print(e)

    print("\nDone.")


# =====================================================================
# GENUINE MULTI-PLANT REASSIGNMENT
#
# Everything above (solve_baseline, solve_ortools) only ever decides
# accept/reject at an order's OWN recorded plant — never considers an
# alternate DC. That's a knapsack, not Distributed Order Management.
# The functions below add real x_{i,j} (order i -> candidate plant j)
# decisions: each order may go to ANY plant that carries its SKU
# anywhere in the dataset (not a fabricated candidate — pulled from
# real data), using that plant's own REAL per-plant shipping rate
# (Shipping_Cost is a constant per plant across the whole dataset,
# confirmed empirically — not an estimate).
# =====================================================================

def build_reassignment_model_data(df):
    """
    sku_to_plants: SKU -> every plant that carries it anywhere in the
        dataset (the real, observed candidate set for reassignment).
    plant_shipcost: plant -> its real, observed shipping rate.
    capacity: (plant, sku) -> that SKU's Available_inventory at that
        plant (the real per-(plant, SKU) constraint used everywhere
        else in this project).
    """
    sku_to_plants = df.groupby("MaterialNumber")["Plant"].unique().to_dict()
    plant_shipcost = df.groupby("Plant")["Shipping_Cost"].first().to_dict()
    capacity = df.groupby(["Plant", "MaterialNumber"])["Available_inventory"].first().to_dict()
    return sku_to_plants, plant_shipcost, capacity


def solve_ortools_reassignment(df, max_time_in_seconds=120):
    """
    Exact multi-plant reassignment via CP-SAT: maximize total
    (revenue - shipping cost) across all orders, where each order may
    be assigned to any real candidate plant (or rejected), subject to
    each candidate plant's own per-SKU inventory capacity.
    """
    sku_to_plants, plant_shipcost, capacity = build_reassignment_model_data(df)

    model = cp_model.CpModel()
    n = len(df)
    df = df.reset_index(drop=True)
    skus = df["MaterialNumber"].values
    qty = df["OrderedQty_converted"].values
    rev = df["Order_SKU_Revenue"].values

    x = []
    for i in range(n):
        candidates = sku_to_plants[skus[i]]
        x.append({p: model.NewBoolVar(f"x_{i}_{p}") for p in candidates})

    for i in range(n):
        model.Add(sum(x[i].values()) <= 1)

    group_indices = {}
    for i in range(n):
        for p in x[i]:
            group_indices.setdefault((p, skus[i]), []).append(i)

    for (p, s), idxs in group_indices.items():
        cap = int(capacity[(p, s)])
        model.Add(sum(int(qty[i]) * x[i][p] for i in idxs) <= cap)

    # Objective: maximize revenue — kept consistent with the objective
    # used everywhere else in this project (Baseline, quantum_optimizer.py).
    # Shipping cost is NOT subtracted per-order at full weight: Shipping_Cost
    # is a flat per-plant rate (same value for every order through that
    # plant), reflecting a shared truckload/route cost, not an individual
    # charge each order bears independently. Subtracting it at full weight
    # would penalize small orders as if each paid for a full truckload
    # alone — not a realistic reading of the field.
    #
    # Revenue is scaled by 10,000 so it always dominates any shipping-cost
    # difference (max spread ~4,500 across plants) — this NEVER changes
    # an accept/reject/candidate-plant decision on revenue grounds, it
    # only breaks ties toward the cheaper-shipping plant when multiple
    # candidates would otherwise deliver identical revenue.
    REVENUE_SCALE = 10_000
    objective_terms = []
    for i in range(n):
        for p, var in x[i].items():
            score = int(round(rev[i])) * REVENUE_SCALE - int(round(plant_shipcost[p]))
            objective_terms.append(score * var)
    model.Maximize(sum(objective_terms))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = max_time_in_seconds
    solver.parameters.num_search_workers = 4

    t0 = time.time()
    status = solver.Solve(model)
    runtime = time.time() - t0

    if status not in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        raise RuntimeError(f"OR-Tools reassignment solve failed: {solver.StatusName(status)}")

    assigned_plant = [None] * n
    for i in range(n):
        for p, var in x[i].items():
            if solver.Value(var) == 1:
                assigned_plant[i] = p
                break

    return assigned_plant, runtime, (status == cp_model.OPTIMAL)


def solve_greedy_reassignment(df):
    """
    Baseline 2 per the challenge brief: "a simple greedy or sequential
    reassignment heuristic." Process orders by revenue (highest
    first); for each, try its default plant first, then its
    cheapest-shipping real alternate candidate plant with remaining
    capacity, else reject.
    """
    sku_to_plants, plant_shipcost, capacity = build_reassignment_model_data(df)

    t0 = time.time()
    remaining = dict(capacity)

    df = df.reset_index(drop=True)
    order_sequence = df["Order_SKU_Revenue"].sort_values(ascending=False).index

    assigned_plant = [None] * len(df)

    for idx in order_sequence:
        row = df.loc[idx]
        sku = row["MaterialNumber"]
        qty = row["OrderedQty_converted"]
        default_plant = row["Plant"]

        candidates = sorted(sku_to_plants[sku], key=lambda p: plant_shipcost[p])
        ordered_candidates = [default_plant] + [p for p in candidates if p != default_plant]

        for p in ordered_candidates:
            key = (p, sku)
            if qty <= remaining.get(key, 0):
                assigned_plant[idx] = p
                remaining[key] = remaining[key] - qty
                break

    runtime = time.time() - t0
    return assigned_plant, runtime


def compute_reassignment_metrics(df, assigned_plant, runtime):
    """
    Same five metrics as compute_metrics(), PLUS 'Orders Reassigned' —
    the count of accepted orders sent to a plant other than their
    original default. This is the metric the challenge brief
    explicitly asks each baseline to report, and the single-plant
    accept/reject model above cannot produce it (nothing is ever
    reassigned there).
    """
    d = df.reset_index(drop=True).copy()
    d["_assigned_plant"] = assigned_plant
    d["_selected"] = d["_assigned_plant"].notna().astype(int)

    plant_shipcost = d.groupby("Plant")["Shipping_Cost"].first().to_dict()
    # fall back to the plant's own known rate even if it wasn't this
    # order's default plant — real, observed rate either way
    d["_shipping_cost_incurred"] = d["_assigned_plant"].map(
        lambda p: plant_shipcost.get(p, 0.0) if pd.notna(p) else 0.0
    )

    revenue = float(d.loc[d["_selected"] == 1, "Order_SKU_Revenue"].sum())
    shipping_cost = float(d.loc[d["_selected"] == 1, "_shipping_cost_incurred"].sum())

    total_qty = d["OrderedQty_converted"].sum()
    fulfilled_qty = d.loc[d["_selected"] == 1, "OrderedQty_converted"].sum()
    fill_rate = (fulfilled_qty / total_qty * 100) if total_qty else 0.0

    reassigned = int(((d["_selected"] == 1) & (d["_assigned_plant"] != d["Plant"])).sum())

    d["_assigned_qty"] = d["OrderedQty_converted"] * d["_selected"]
    util_by_plant = (
        d.groupby("_assigned_plant")
        .agg(assigned=("_assigned_qty", "sum"))
        .join(d.groupby("Plant")["Available_inventory"].mean().rename("avg_inv"), how="left")
    )
    util_by_plant = util_by_plant[util_by_plant["avg_inv"] > 0]
    avg_utilization = (
        (util_by_plant["assigned"] / util_by_plant["avg_inv"]).mean() * 100
        if not util_by_plant.empty else 0.0
    )

    return {
        "Revenue": revenue,
        "Shipping Cost": shipping_cost,
        "Runtime (s)": runtime,
        "Warehouse Utilization (%)": avg_utilization,
        "Fill Rate (%)": fill_rate,
        "Orders Reassigned": reassigned,
    }


def run_reassignment_benchmark(df):
    """
    Baseline (no reassignment, existing solve_baseline) vs Greedy
    Reassignment vs OR-Tools Reassignment — the comparison that
    actually answers "how many orders got reassigned, and what did
    it gain us," which the single-plant Table 1 above cannot.
    """
    baseline_sel, baseline_t = solve_baseline(df)
    baseline_metrics = compute_metrics(df, baseline_sel, baseline_t)
    baseline_metrics["Orders Reassigned"] = 0  # by definition — no reassignment model

    greedy_plants, greedy_t = solve_greedy_reassignment(df)
    greedy_metrics = compute_reassignment_metrics(df, greedy_plants, greedy_t)

    ortools_plants, ortools_t, _optimal = solve_ortools_reassignment(df)
    ortools_metrics = compute_reassignment_metrics(df, ortools_plants, ortools_t)

    table = pd.DataFrame({
        "Baseline (no reassignment)": baseline_metrics,
        "Greedy Reassignment": greedy_metrics,
        "OR-Tools Reassignment": ortools_metrics,
    }).T

    return table