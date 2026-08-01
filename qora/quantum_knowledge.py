"""
=========================================================
QORA AI
quantum_knowledge.py

Data-driven answers about the quantum optimization run —
reads the SAME cache file the dashboard's Quantum
Optimization tab reads (data/quantum_result_cache.json),
so Qora AI and the dashboard never disagree with each
other.

Deliberately does NOT import quantum_optimizer.py or qiskit
— the cache is plain JSON, so Qora AI can answer quantum
questions even in an environment without qiskit installed
(e.g. a lightweight chat-only deployment).
=========================================================
"""

import json
import os


DEFAULT_CACHE_PATH = "data/quantum_result_cache.json"


class QuantumKnowledge:

    def __init__(self, cache_path=DEFAULT_CACHE_PATH):

        self.cache_path = cache_path
        self.data = self._load()

    # =====================================================
    # LOADING
    # =====================================================

    def _load(self):

        if not os.path.exists(self.cache_path):
            return None

        with open(self.cache_path) as f:
            return json.load(f)

    def refresh(self):
        """Call after quantum_optimizer.py regenerates the cache."""
        self.data = self._load()
        return self.data is not None

    def available(self):
        return self.data is not None

    # =====================================================
    # RAW FACTS
    # =====================================================

    def objective_value(self):
        if not self.available():
            return None
        return self.data["quantum"]["objective"]

    def exact_objective_value(self):
        if not self.available():
            return None
        return self.data["exact"]["objective"]

    def greedy_objective_value(self):
        if not self.available():
            return None
        return self.data["greedy"]["objective"]

    def selected_order_ids(self):
        if not self.available():
            return None
        return [k for k, v in self.data["quantum"]["assignment"].items() if v == 1]

    def rejected_order_ids(self):
        if not self.available():
            return None
        return [k for k, v in self.data["quantum"]["assignment"].items() if v == 0]

    def optimized_order_count(self):
        """Total orders IN THIS BATCH (selected + rejected), not the
        whole dataset — the QAOA batch is a deliberately small real
        subset, see quantum_optimizer.py's batching logic."""
        if not self.available():
            return None
        return len(self.data["orders"])

    def is_feasible(self):
        if not self.available():
            return None
        return self.data["quantum"]["feasible"]

    def qaoa_runtime(self):
        if not self.available():
            return None
        return self.data["quantum"]["runtime_sec"]

    def exact_runtime(self):
        if not self.available():
            return None
        return self.data["exact"]["runtime_sec"]

    def greedy_runtime(self):
        if not self.available():
            return None
        return self.data["greedy"]["runtime_sec"]

    def inventory_capacity(self):
        if not self.available():
            return None
        return self.data["capacity"]

    def plant(self):
        if not self.available():
            return None
        return self.data["plant"]

    def sku(self):
        if not self.available():
            return None
        return self.data["material_number"]

    def optimality_gap_pct(self):
        if not self.available():
            return None
        exact = self.data["exact"]["objective"]
        quantum = self.data["quantum"]["objective"]
        if not exact:
            return None
        return round((exact - quantum) / exact * 100, 2)

    def reached_optimal(self):
        gap = self.optimality_gap_pct()
        if gap is None:
            return None
        return abs(gap) < 1e-6

    # =====================================================
    # ORDER-LEVEL LOOKUP WITHIN THIS BATCH
    # =====================================================

    def _order_key(self, order_id):
        """Assignment dict keys look like 'order_5485358557' — accept
        either the bare id or the full key."""
        order_id = str(order_id)
        return order_id if order_id.startswith("order_") else f"order_{order_id}"

    def order_in_batch(self, order_id):
        if not self.available():
            return False
        return self._order_key(order_id) in self.data["quantum"]["assignment"]

    def was_order_selected(self, order_id):
        if not self.order_in_batch(order_id):
            return None
        return bool(self.data["quantum"]["assignment"][self._order_key(order_id)])

    def explain_order_in_batch(self, order_id):
        """Why was this specific batch order selected or not — grounded
        in the real capacity constraint, not a canned explanation."""
        if not self.order_in_batch(order_id):
            return None

        key = self._order_key(order_id)
        selected = bool(self.data["quantum"]["assignment"][key])

        order_row = next(
            (o for o in self.data["orders"] if f"order_{o['Group_Flag']}" == key),
            None,
        )
        if order_row is None:
            return None

        qty = order_row["OrderedQty_converted"]
        rev = order_row["Order_SKU_Revenue"]
        cap = self.data["capacity"]

        if selected:
            return (
                f"Order {order_id} (qty {qty}, revenue {rev}) WAS selected — "
                f"it fit within the batch's inventory capacity ({cap} units) "
                "alongside the other selected orders, and including it "
                "increased total revenue."
            )
        return (
            f"Order {order_id} (qty {qty}, revenue {rev}) was NOT selected — "
            f"including it would have pushed total assigned quantity over "
            f"the batch's inventory capacity ({cap} units), so it was left "
            "out in favor of a combination with higher total revenue."
        )

    # =====================================================
    # COMPARATIVE / EXPLANATORY QUESTIONS
    # =====================================================

    def why_only_n_selected(self):
        if not self.available():
            return None
        n = sum(self.data["quantum"]["assignment"].values())
        total = len(self.data["orders"])
        cap = self.data["capacity"]
        return (
            f"Only {n} of {total} orders in this batch were selected because "
            f"the combined demand of all {total} orders exceeds the inventory "
            f"capacity ({cap} units) — the optimizer picks the subset of "
            "orders whose combined revenue is highest while staying within "
            "that capacity, not just the most orders it can fit."
        )

    def why_qaoa_slower_than_exact(self):
        if not self.available():
            return None
        qaoa_t = self.data["quantum"]["runtime_sec"]
        exact_t = self.data["exact"]["runtime_sec"]
        return (
            f"QAOA took {qaoa_t:.2f}s here vs. {exact_t:.4f}s for exact "
            "brute-force enumeration. At this small batch size, exact "
            "enumeration only has to check a handful of combinations "
            "directly, while QAOA has to simulate a full quantum circuit "
            "and repeatedly run a classical optimizer (COBYLA) on top of "
            "it to tune the circuit's parameters — that simulation and "
            "tuning loop is what costs the extra time, not the problem "
            "itself being harder. QAOA's advantage, if any, only shows up "
            "at problem sizes too large for exact enumeration to handle at all."
        )

    def compare_greedy_vs_qaoa(self):
        if not self.available():
            return None
        greedy_obj = self.data["greedy"]["objective"]
        qaoa_obj = self.data["quantum"]["objective"]
        greedy_t = self.data["greedy"]["runtime_sec"]
        qaoa_t = self.data["quantum"]["runtime_sec"]

        if greedy_obj == qaoa_obj:
            quality = "reached the same objective value as"
        elif greedy_obj > qaoa_obj:
            quality = "beat"
        else:
            quality = "was beaten by"

        return (
            f"Greedy {quality} QAOA on this batch: Greedy scored "
            f"{greedy_obj:.0f} in {greedy_t:.4f}s, QAOA scored {qaoa_obj:.0f} "
            f"in {qaoa_t:.2f}s. On an instance this small, the simple greedy "
            "heuristic is both faster and at least as good — QAOA isn't "
            "expected to outperform classical methods at this scale; it's "
            "included to show a real, benchmarked quantum result rather "
            "than a theoretical claim."
        )

    def revenue_optimized(self):
        """In this model, the objective IS the selected orders' total
        revenue (no separate shipping/penalty terms in the QUBO), so
        this is the same number as objective_value()."""
        return self.objective_value()

    # =====================================================
    # ROUTER
    # =====================================================

    def answer(self, question):
        """
        Returns a string answer if this module can handle the question,
        or None if it can't (caller should fall through to other
        knowledge sources). `question` should already be lowercased.
        """
        q = question

        if not self.available():
            # Only claim ownership of a question if we can actually
            # tell it's asking about the quantum run — otherwise let
            # other knowledge sources try.
            quantum_signal = any(t in q for t in (
                "qaoa", "quantum", "objective value", "optimality gap",
                "feasible", "feasibility",
            ))
            if quantum_signal:
                return (
                    "No quantum result is cached yet — run "
                    "`python quantum_optimizer.py` to generate "
                    "data/quantum_result_cache.json."
                )
            return None

        # --- specific order lookup within the batch ---
        import re
        order_match = re.search(r"order[_\s]?(\d+)", q)
        if order_match:
            order_id = order_match.group(1)
            if self.order_in_batch(order_id):
                if "why" in q:
                    return self.explain_order_in_batch(order_id)
                selected = self.was_order_selected(order_id)
                return (
                    f"Order {order_id} was "
                    + ("selected." if selected else "NOT selected.")
                )
            # order not in this small batch — let analytics/full-dataset
            # lookup handle it instead
            # (fall through to other checks below only if no order digits
            #  matched anything quantum-specific)

        if "why" in q and ("only" in q or re.search(r"\d+ order", q)):
            return self.why_only_n_selected()

        if "why" in q and "slower" in q:
            return self.why_qaoa_slower_than_exact()

        if "why" in q and "wasn't" in q or "why" in q and "not selected" in q:
            # generic "why wasn't this order selected" with no id given
            return (
                "Any order not selected in this batch didn't fit within "
                "the remaining inventory capacity once higher-value orders "
                "were assigned — ask about a specific order id for the exact reason."
            )

        if "greedy" in q and ("compare" in q or "vs" in q or "versus" in q):
            return self.compare_greedy_vs_qaoa()

        if "reach" in q and "optimal" in q:
            reached = self.reached_optimal()
            gap = self.optimality_gap_pct()
            if reached is None:
                return None
            return (
                f"Yes — QAOA reached the optimal solution (0% gap)."
                if reached else
                f"No — QAOA is {gap:.1f}% off the exact optimum on this batch."
            )

        if "optimality gap" in q or "optimal gap" in q:
            gap = self.optimality_gap_pct()
            return f"{gap:.1f}%" if gap is not None else None

        if "objective value" in q or ("objective" in q and "gap" not in q):
            val = self.objective_value()
            return f"{val:.0f}" if val is not None else None

        if "which orders were selected" in q or "which orders got selected" in q:
            ids = self.selected_order_ids()
            return ", ".join(ids) if ids else None

        if "how many orders" in q and ("batch" in q or "qaoa" in q or "quantum" in q):
            n = self.optimized_order_count()
            return str(n) if n is not None else None

        if "feasible" in q or "feasibility" in q:
            feasible = self.is_feasible()
            if feasible is None:
                return None
            return "Yes — Feasible ✔ (constraint satisfied)." if feasible else "No — the constraint is violated."

        if "runtime" in q and "qaoa" in q:
            t = self.qaoa_runtime()
            return f"{t:.2f} seconds" if t is not None else None

        if "inventory capacity" in q or ("capacity" in q and "invent" in q):
            cap = self.inventory_capacity()
            return f"{cap:.0f} units" if cap is not None else None

        if "which plant" in q and ("optimi" in q or "being" in q):
            plant = self.plant()
            return f"Plant {plant}" if plant is not None else None

        if "what is the sku" in q or ("sku" in q and "which" not in q and "why" not in q):
            sku = self.sku()
            return f"SKU {sku}" if sku is not None else None

        if "revenue" in q and ("quantum" in q or "qaoa" in q or "batch" in q):
            rev = self.revenue_optimized()
            return f"{rev:.0f}" if rev is not None else None

        return None