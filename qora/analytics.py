"""
=========================================================
QORA AI
analytics.py

Dashboard Analytics Engine

Reads dashboard data and provides analytics
for Qora AI.

=========================================================
"""

import pandas as pd
import numpy as np
import re


class DashboardAnalytics:
    """
    Dashboard Analytics Engine
    """

    def __init__(self, df):
        self.df = df.copy()
        self._add_column_aliases()

    def _add_column_aliases(self):
        """
        The optimized_orders CSV uses different column names than this
        class was originally written against (e.g. 'Order_SKU_Revenue'
        instead of 'Revenue'). Add alias columns so every method below
        keeps working without rewriting each one, and so this class
        still works unmodified if a future export uses the "nice" names
        directly.
        """
        alias_map = {
            "Revenue": "Order_SKU_Revenue",
            "Shipping Cost": "Shipping_Cost",
            "Warehouse": "Plant",
            "Product": "MaterialNumber",
            "Inventory": "Available_inventory",
            "Carbon Emissions": "Estimated_CO2_kg",
            "Penalty Cost": "Penaltyforpotentialcuts",
        }

        for nice_name, real_name in alias_map.items():
            if nice_name not in self.df.columns and real_name in self.df.columns:
                self.df[nice_name] = self.df[real_name]

        # Fulfilled quantity per row: OrderedQty_converted if Selected,
        # else 0. Used by average_fill_rate() below instead of relying
        # on a (non-existent) precomputed "Fill Rate" column.
        if "OrderedQty_converted" in self.df.columns and "Selected" in self.df.columns:
            self.df["_fulfilled_qty"] = (
                self.df["OrderedQty_converted"] * self.df["Selected"]
            )

        # Real delivery lead time (days) = RequestedDeliveryDate minus
        # transportationplanningdate. There is no distance/lat-long
        # data anywhere in this dataset, so "delivery distance" cannot
        # be computed honestly — only lead time in days, from real
        # date columns, is available. (The dashboard previously had a
        # "Simulated delivery time" using `Order_SKU_Revenue % 5` in
        # the SLA tab — that was a placeholder formula with no real
        # meaning; this is the actual date difference instead.)
        if "transportationplanningdate" in self.df.columns and "RequestedDeliveryDate" in self.df.columns:
            planning = pd.to_datetime(self.df["transportationplanningdate"], format="%m/%d/%y", errors="coerce")
            requested = pd.to_datetime(self.df["RequestedDeliveryDate"], format="%m/%d/%y", errors="coerce")
            self.df["_delivery_lead_days"] = (requested - planning).dt.days

    # ======================================================
    # DEBUG FUNCTIONS
    # ======================================================

    def available_columns(self):
        """
        Return all dataframe columns.
        Useful for debugging.
        """
        return list(self.df.columns)

    def column_exists(self, column):
        """
        Check whether a column exists.
        """
        return column in self.df.columns

    # ======================================================
    # BASIC KPIs
    # ======================================================

    def total_orders(self):
        return len(self.df)

    def total_products(self):
        if self.column_exists("Product"):
            return self.df["Product"].nunique()
        return None

    def total_customers(self):
        if self.column_exists("Customer"):
            return self.df["Customer"].nunique()
        return None

    def total_revenue(self, selected_only=True):
        """
        By default this matches the dashboard's Revenue KPI card, which
        only counts accepted (Selected=1) order-lines. Pass
        selected_only=False for total order value across every line
        (accepted + rejected).
        """
        if not self.column_exists("Revenue"):
            return None

        if selected_only and self.column_exists("Selected"):
            return float(self.df.loc[self.df["Selected"] == 1, "Revenue"].sum())

        return float(self.df["Revenue"].sum())

    def total_order_value(self):
        """Total Order_SKU_Revenue across all lines, accepted or not."""
        return self.total_revenue(selected_only=False)

    def total_shipping_cost(self):
        if self.column_exists("Shipping Cost"):
            return float(self.df["Shipping Cost"].sum())
        return None

    def total_penalty(self):
        """
        Total estimated penalty exposure from REJECTED (unfulfilled)
        orders — using the same per-row estimate as _penalty_estimate()
        (rate x revenue + fixed, clipped to [min, max]).

        NOTE: this used to sum the raw 'Penaltyforpotentialcuts' column
        directly, but that column is a RATE (e.g. 0.03, 0.04), not a
        dollar amount — summing it produced a small, meaningless number
        with no real business interpretation. This computes an actual
        dollar estimate instead.
        """
        if not self.column_exists("Selected"):
            return None

        rejected = self.df[self.df["Selected"] == 0]
        if rejected.empty:
            return 0.0

        estimates = rejected.apply(self._penalty_estimate, axis=1)
        estimates = estimates.dropna()

        return float(estimates.sum()) if not estimates.empty else None

    def average_fill_rate(self):
        """
        There is no precomputed 'Fill Rate' column in the source data —
        the old version of this method always returned None. This
        computes fill rate as fulfilled quantity / total ordered
        quantity across the current (filtered) dataframe.
        """
        if not self.column_exists("_fulfilled_qty"):
            return None
        if not self.column_exists("OrderedQty_converted"):
            return None

        total_qty = self.df["OrderedQty_converted"].sum()
        if not total_qty:
            return None

        fulfilled_qty = self.df["_fulfilled_qty"].sum()
        return round(fulfilled_qty / total_qty * 100, 2)

    def revenue_fill_rate(self):
        """Same idea as average_fill_rate() but weighted by revenue."""
        if not self.column_exists("Revenue") or not self.column_exists("Selected"):
            return None

        total_rev = self.df["Revenue"].sum()
        if not total_rev:
            return None

        fulfilled_rev = self.df.loc[self.df["Selected"] == 1, "Revenue"].sum()
        return round(fulfilled_rev / total_rev * 100, 2)

    def average_delivery_days(self):
        """
        Real average delivery lead time in days (RequestedDeliveryDate
        minus transportationplanningdate) — no distance/lat-long data
        exists in this dataset, so distance can't be computed honestly;
        this is lead time only, from real dates.
        """
        if not self.column_exists("_delivery_lead_days"):
            return None
        return round(float(self.df["_delivery_lead_days"].mean()), 2)

    def average_carbon(self):
        if self.column_exists("Carbon Emissions"):
            return round(self.df["Carbon Emissions"].mean(), 2)
        return None

    # ======================================================
    # REVENUE
    # ======================================================

    def maximum_revenue(self):
        if self.column_exists("Revenue"):
            return self.df["Revenue"].max()
        return None

    def minimum_revenue(self):
        if self.column_exists("Revenue"):
            return self.df["Revenue"].min()
        return None

    def average_revenue(self):
        if self.column_exists("Revenue"):
            return round(self.df["Revenue"].mean(), 2)
        return None

    # ======================================================
    # SHIPPING
    # ======================================================

    def average_shipping_cost(self):
        if self.column_exists("Shipping Cost"):
            return round(self.df["Shipping Cost"].mean(), 2)
        return None

    def maximum_shipping_cost(self):
        if self.column_exists("Shipping Cost"):
            return self.df["Shipping Cost"].max()
        return None

    def minimum_shipping_cost(self):
        if self.column_exists("Shipping Cost"):
            return self.df["Shipping Cost"].min()
        return None

    # ======================================================
    # CARBON
    # ======================================================

    def total_carbon(self):
        if self.column_exists("Carbon Emissions"):
            return self.df["Carbon Emissions"].sum()
        return None

    def maximum_carbon(self):
        if self.column_exists("Carbon Emissions"):
            return self.df["Carbon Emissions"].max()
        return None

    def minimum_carbon(self):
        if self.column_exists("Carbon Emissions"):
            return self.df["Carbon Emissions"].min()
        return None

    # ======================================================
    # INVENTORY
    # ======================================================

    def total_inventory(self):
        if self.column_exists("Inventory"):
            return self.df["Inventory"].sum()
        return None

    def average_inventory(self):
        if self.column_exists("Inventory"):
            return round(self.df["Inventory"].mean(), 2)
        return None

    # ======================================================
    # WAREHOUSE ANALYTICS
    # ======================================================

    def best_warehouse(self):

        if not self.column_exists("Warehouse"):
            return None

        if not self.column_exists("Revenue"):
            return None

        revenue = (
            self.df
            .groupby("Warehouse")["Revenue"]
            .sum()
        )

        return revenue.idxmax()

    def warehouse_most_assignments(self):
        """Warehouse/plant with the most ACCEPTED order-lines (a count,
        distinct from revenue-based best_warehouse() or the qty/inventory
        ratio used by highest_utilization())."""
        if not self.column_exists("Warehouse") or not self.column_exists("Selected"):
            return None

        counts = self.df[self.df["Selected"] == 1].groupby("Warehouse").size()
        if counts.empty:
            return None
        return counts.idxmax()

    def capacity_remaining(self):
        """
        Average remaining dock and throughput capacity across the
        dataset — the two real 'capacity' fields available (there's
        no single combined 'capacity remaining' column).
        Returns a dict, or None if neither field is present.
        """
        dock = self.df["Dock_Remaining"].mean() if self.column_exists("Dock_Remaining") else None
        throughput = self.df["Throughput_Capacity"].mean() if self.column_exists("Throughput_Capacity") else None

        if dock is None and throughput is None:
            return None

        return {"avg_dock_remaining": dock, "avg_throughput_capacity": throughput}

    def worst_warehouse(self):

        if not self.column_exists("Warehouse"):
            return None

        if not self.column_exists("Revenue"):
            return None

        revenue = (
            self.df
            .groupby("Warehouse")["Revenue"]
            .sum()
        )

        return revenue.idxmin()

    def warehouse_revenue(self):

        if not self.column_exists("Warehouse"):
            return None

        if not self.column_exists("Revenue"):
            return None

        return (
            self.df
            .groupby("Warehouse")["Revenue"]
            .sum()
            .sort_values(ascending=False)
        )

    def warehouse_orders(self):

        if not self.column_exists("Warehouse"):
            return None

        return (
            self.df["Warehouse"]
            .value_counts()
            .sort_values(ascending=False)
        )

    def warehouse_inventory(self):

        if not self.column_exists("Warehouse"):
            return None

        if not self.column_exists("Inventory"):
            return None

        return (
            self.df
            .groupby("Warehouse")["Inventory"]
            .sum()
            .sort_values(ascending=False)
        )
        # ======================================================
    # PLANT ANALYTICS
    # ======================================================

    def best_plant(self):

        if not self.column_exists("Plant"):
            return None

        if not self.column_exists("Revenue"):
            return None

        revenue = (
            self.df
            .groupby("Plant")["Revenue"]
            .sum()
        )

        return revenue.idxmax()

    def worst_plant(self):

        if not self.column_exists("Plant"):
            return None

        if not self.column_exists("Revenue"):
            return None

        revenue = (
            self.df
            .groupby("Plant")["Revenue"]
            .sum()
        )

        return revenue.idxmin()

    def plant_revenue(self):

        if not self.column_exists("Plant"):
            return None

        if not self.column_exists("Revenue"):
            return None

        return (
            self.df
            .groupby("Plant")["Revenue"]
            .sum()
            .sort_values(ascending=False)
        )

    def plant_orders(self):

        if not self.column_exists("Plant"):
            return None

        return (
            self.df["Plant"]
            .value_counts()
        )

    # ======================================================
    # PRODUCT ANALYTICS
    # ======================================================

    def top_product(self):

        if not self.column_exists("Product"):
            return None

        return self.df["Product"].value_counts().idxmax()

    def product_sales(self):

        if not self.column_exists("Product"):
            return None

        return (
            self.df["Product"]
            .value_counts()
            .sort_values(ascending=False)
        )

    def product_revenue(self):

        if not self.column_exists("Product"):
            return None

        if not self.column_exists("Revenue"):
            return None

        return (
            self.df
            .groupby("Product")["Revenue"]
            .sum()
            .sort_values(ascending=False)
        )

    # ======================================================
    # UTILIZATION
    # ======================================================

    def utilization_by_warehouse(self):
        """
        There is no 'Warehouse Utilization' column in the source data.
        Utilization is derived as assigned quantity (Selected orders)
        divided by that warehouse's average available inventory.
        Returns a Series indexed by Warehouse, sorted highest first.
        """
        if not self.column_exists("Warehouse"):
            return None
        if not self.column_exists("_fulfilled_qty"):
            return None
        if not self.column_exists("Inventory"):
            return None

        grouped = self.df.groupby("Warehouse").agg(
            assigned_qty=("_fulfilled_qty", "sum"),
            avg_inventory=("Inventory", "mean"),
        )

        grouped = grouped[grouped["avg_inventory"] > 0]
        if grouped.empty:
            return None

        util = (grouped["assigned_qty"] / grouped["avg_inventory"] * 100).round(2)
        return util.sort_values(ascending=False)

    def highest_utilization(self):
        util = self.utilization_by_warehouse()
        if util is None or util.empty:
            return None
        return util.idxmax()

    def lowest_utilization(self):
        util = self.utilization_by_warehouse()
        if util is None or util.empty:
            return None
        return util.idxmin()

    def average_utilization(self):
        """Mean utilization across warehouses (each warehouse weighted
        equally, not by order volume) — same real per-warehouse
        utilization used by highest/lowest_utilization()."""
        util = self.utilization_by_warehouse()
        if util is None or util.empty:
            return None
        return round(float(util.mean()), 2)

    # ======================================================
    # OPTIMIZATION SUMMARY
    # ======================================================

    def orders_optimized_count(self):
        """Orders currently accepted (Selected=1) in the loaded data."""
        if not self.column_exists("Selected"):
            return None
        return int((self.df["Selected"] == 1).sum())

    def orders_rejected_count(self):
        """Orders currently rejected (Selected=0) in the loaded data."""
        if not self.column_exists("Selected"):
            return None
        return int((self.df["Selected"] == 0).sum())

    def constraint_violations(self):
        """
        Checks whether the CURRENT assignment (the 'Selected' column
        already in the data) actually respects the per-(Plant, SKU)
        inventory capacity constraint — the same constraint used
        throughout this project (quantum_optimizer.py, benchmark.py).
        A violation means more quantity is marked Selected for a given
        Plant+SKU than that SKU's Available_inventory at that plant.

        Returns a dict: {count, total_overage_units, details} where
        details is a DataFrame of the violating (Plant, SKU) groups —
        or None if the required columns aren't present.
        """
        required = ("Plant", "MaterialNumber", "OrderedQty_converted", "Available_inventory", "Selected")
        if not all(self.column_exists(c) for c in required):
            return None

        d = self.df.copy()
        d["_assigned_qty"] = d["OrderedQty_converted"] * d["Selected"]

        grouped = d.groupby(["Plant", "MaterialNumber"]).agg(
            assigned_qty=("_assigned_qty", "sum"),
            capacity=("Available_inventory", "first"),
        )

        violations = grouped[grouped["assigned_qty"] > grouped["capacity"]].copy()
        violations["overage"] = violations["assigned_qty"] - violations["capacity"]

        return {
            "count": int(len(violations)),
            "total_overage_units": float(violations["overage"].sum()) if not violations.empty else 0.0,
            "details": violations.reset_index(),
        }

    # ======================================================
    # SHIPPING ANALYTICS
    # ======================================================

    def _avg_shipping_cost_by_warehouse(self):
        if not self.column_exists("Warehouse"):
            return None
        if not self.column_exists("Shipping Cost"):
            return None

        return (
            self.df
            .groupby("Warehouse")["Shipping Cost"]
            .mean()
        )

    def highest_shipping_cost(self):
        cost = self._avg_shipping_cost_by_warehouse()
        if cost is None or cost.empty:
            return None
        return cost.idxmax()

    def lowest_shipping_cost(self):
        cost = self._avg_shipping_cost_by_warehouse()
        if cost is None or cost.empty:
            return None
        return cost.idxmin()

    # ======================================================
    # CARBON ANALYTICS
    # ======================================================

    def highest_carbon(self):

        if not self.column_exists("Warehouse"):
            return None

        if not self.column_exists("Carbon Emissions"):
            return None

        carbon = (
            self.df
            .groupby("Warehouse")["Carbon Emissions"]
            .sum()
        )

        return carbon.idxmax()

    def lowest_carbon(self):

        if not self.column_exists("Warehouse"):
            return None

        if not self.column_exists("Carbon Emissions"):
            return None

        carbon = (
            self.df
            .groupby("Warehouse")["Carbon Emissions"]
            .sum()
        )

        return carbon.idxmin()

    # ======================================================
    # INVENTORY ANALYTICS
    # ======================================================

    def highest_inventory(self):

        if not self.column_exists("Warehouse"):
            return None

        if not self.column_exists("Inventory"):
            return None

        inv = (
            self.df
            .groupby("Warehouse")["Inventory"]
            .sum()
        )

        return inv.idxmax()

    def lowest_inventory(self):

        if not self.column_exists("Warehouse"):
            return None

        if not self.column_exists("Inventory"):
            return None

        inv = (
            self.df
            .groupby("Warehouse")["Inventory"]
            .sum()
        )

        return inv.idxmin()

    # ======================================================
    # TOP / BOTTOM RANKINGS
    # ======================================================

    def top_warehouses(self, n=5):

        revenue = self.warehouse_revenue()

        if revenue is None:
            return None

        return revenue.head(n)

    def bottom_warehouses(self, n=5):

        revenue = self.warehouse_revenue()

        if revenue is None:
            return None

        return revenue.tail(n)

    def top_plants(self, n=5):

        revenue = self.plant_revenue()

        if revenue is None:
            return None

        return revenue.head(n)

    def bottom_plants(self, n=5):

        revenue = self.plant_revenue()

        if revenue is None:
            return None

        return revenue.tail(n)
        # ======================================================
    # DASHBOARD SUMMARY
    # ======================================================

    def dashboard_summary(self):
        """
        Returns all important KPIs in a dictionary.
        """

        return {
            "Total Orders": self.total_orders(),
            "Total Products": self.total_products(),
            "Total Customers": self.total_customers(),
            "Total Revenue": self.total_revenue(),
            "Average Revenue": self.average_revenue(),
            "Shipping Cost": self.total_shipping_cost(),
            "Penalty Cost": self.total_penalty(),
            "Average Fill Rate": self.average_fill_rate(),
            "Average Carbon": self.average_carbon(),
            "Best Warehouse": self.best_warehouse(),
            "Worst Warehouse": self.worst_warehouse(),
            "Best Plant": self.best_plant(),
            "Worst Plant": self.worst_plant(),
            "Top Product": self.top_product(),
            "Highest Utilization": self.highest_utilization(),
            "Lowest Utilization": self.lowest_utilization(),
            "Highest Shipping Cost": self.highest_shipping_cost(),
            "Lowest Shipping Cost": self.lowest_shipping_cost(),
            "Highest Carbon": self.highest_carbon(),
            "Lowest Carbon": self.lowest_carbon(),
            "Highest Inventory": self.highest_inventory(),
            "Lowest Inventory": self.lowest_inventory(),
        }

    # ======================================================
    # PLANNER SUMMARY
    # ======================================================

    def planner_summary(self):

        kpi = self.dashboard_summary()

        summary = f"""
==============================
QORA AI DASHBOARD SUMMARY
==============================

Total Orders           : {kpi['Total Orders']}
Total Products         : {kpi['Total Products']}
Total Customers        : {kpi['Total Customers']}

Revenue                : {kpi['Total Revenue']}
Average Revenue        : {kpi['Average Revenue']}

Shipping Cost          : {kpi['Shipping Cost']}
Penalty Cost           : {kpi['Penalty Cost']}

Average Fill Rate      : {kpi['Average Fill Rate']}
Average Carbon         : {kpi['Average Carbon']}

Best Warehouse         : {kpi['Best Warehouse']}
Worst Warehouse        : {kpi['Worst Warehouse']}

Best Plant             : {kpi['Best Plant']}
Worst Plant            : {kpi['Worst Plant']}

Top Product            : {kpi['Top Product']}

Highest Utilization    : {kpi['Highest Utilization']}
Lowest Utilization     : {kpi['Lowest Utilization']}

Highest Shipping Cost  : {kpi['Highest Shipping Cost']}
Lowest Shipping Cost   : {kpi['Lowest Shipping Cost']}

Highest Carbon         : {kpi['Highest Carbon']}
Lowest Carbon          : {kpi['Lowest Carbon']}

Highest Inventory      : {kpi['Highest Inventory']}
Lowest Inventory       : {kpi['Lowest Inventory']}
"""

        return summary

    # ======================================================
    # EXECUTIVE SUMMARY
    # ======================================================

    def executive_summary(self):

        return f"""
Executive Summary

• Total Orders Processed : {self.total_orders()}

• Total Revenue Generated : {self.total_revenue()}

• Average Fill Rate : {self.average_fill_rate()}%

• Best Warehouse : {self.best_warehouse()}

• Best Plant : {self.best_plant()}

• Top Product : {self.top_product()}

The optimization dashboard indicates overall supply chain performance across
warehouses, inventory, transportation and customer demand.

The current solution helps improve revenue, increase fill rate,
reduce transportation cost and support sustainable logistics.
"""

    # ======================================================
    # AI RECOMMENDATIONS
    # ======================================================

    def recommendations(self):

        tips = []

        if self.average_fill_rate() is not None:
            if self.average_fill_rate() < 90:
                tips.append(
                    "Increase inventory availability to improve Fill Rate."
                )

        if self.highest_utilization() is not None:
            tips.append(
                f"Monitor warehouse '{self.highest_utilization()}' because it has the highest utilization."
            )

        if self.highest_shipping_cost() is not None:
            tips.append(
                f"Review transportation routes from '{self.highest_shipping_cost()}'."
            )

        if self.highest_carbon() is not None:
            tips.append(
                f"Reduce transportation emissions around '{self.highest_carbon()}'."
            )

        if self.lowest_inventory() is not None:
            tips.append(
                f"Replenish inventory at '{self.lowest_inventory()}'."
            )

        if len(tips) == 0:
            tips.append("Dashboard performance looks healthy.")

        return tips

    # ======================================================
    # ORDER-LEVEL EXPLANATION
    # ======================================================

    def explain_order(self, group_flag=None, material_number=None):
        """
        Look up why a specific order (optionally + SKU) was accepted or
        rejected. Reports the four factors a planner actually weighs:
        inventory available, capacity available, shipping cost, and
        penalty avoided (if accepted) or exposed (if rejected) — on
        top of the original Recommendation/Reason columns.
        """
        if not self.column_exists("Group_Flag"):
            return "Order-level lookup isn't available on this dataset (no Group_Flag column)."

        mask = pd.Series(True, index=self.df.index)

        if group_flag is not None:
            mask &= self.df["Group_Flag"].astype(str) == str(group_flag)

        if material_number is not None and self.column_exists("MaterialNumber"):
            mask &= self.df["MaterialNumber"].astype(str) == str(material_number)

        matches = self.df[mask]

        if matches.empty:
            return f"I couldn't find order {group_flag} in the current results."

        # An order with many SKU lines has no single "why was it
        # assigned" answer — dumping every line as one wall of text
        # isn't useful in a chat reply. Summarize instead, and let the
        # person drill into a specific SKU if they want the full detail
        # this method gives for a single line (see below).
        MAX_LINES_BEFORE_SUMMARY = 3

        if material_number is None and len(matches) > MAX_LINES_BEFORE_SUMMARY:
            return self._summarize_multi_line_order(group_flag, matches)

        lines = []
        for _, row in matches.iterrows():

            selected = row.get("Selected") == 1
            status = "assigned to" if selected else "NOT assigned to"
            reason = row.get("Reason", "")
            extra = row.get("Recommendation Reason", "")

            header = (
                f"Order {row.get('Group_Flag')} / SKU {row.get('MaterialNumber')} "
                f"was {status} Plant {row.get('Plant')}. "
                f"Recommendation: {row.get('Recommendation')}. Reason: {reason}"
            )
            if pd.notna(extra) and extra:
                header += f" ({extra})."
            else:
                header += "."

            factors = ["Why this warehouse:"]

            # --- Inventory available ---
            if pd.notna(row.get("Available_inventory")):
                qty = row.get("OrderedQty_converted")
                factors.append(
                    f"  • Inventory available: {row['Available_inventory']:.0f} units "
                    f"(order needs {qty:.0f})"
                )

            # --- Capacity available ---
            cap_bits = []
            if pd.notna(row.get("Dock_Remaining")):
                cap_bits.append(f"dock remaining {row['Dock_Remaining']:.0f}")
            if pd.notna(row.get("Throughput_Capacity")):
                cap_bits.append(f"throughput capacity {row['Throughput_Capacity']:.0f}")
            if cap_bits:
                factors.append(f"  • Capacity available: {', '.join(cap_bits)}")

            # --- Shipping cost ---
            if pd.notna(row.get("Shipping_Cost")):
                factors.append(f"  • Shipping cost: {row['Shipping_Cost']:.2f}")

            # --- Penalty avoided / exposed ---
            penalty_note = self._penalty_estimate(row)
            if penalty_note is not None:
                verb = "Penalty avoided by accepting" if selected else "Penalty exposure from rejecting"
                factors.append(f"  • {verb}: ~{penalty_note:.2f} (estimated)")

            line = header
            if len(factors) > 1:
                line += "\n" + "\n".join(factors)
            lines.append(line)

        return "\n\n".join(lines)

    def _summarize_multi_line_order(self, group_flag, matches):
        """
        Order-level summary for orders with several SKU lines: how many
        accepted/rejected, total revenue, the most common rejection
        reason, and a pointer to ask about a specific SKU for the full
        four-factor breakdown explain_order() gives for a single line.
        """
        n_total = len(matches)
        n_accepted = int((matches["Selected"] == 1).sum())
        n_rejected = n_total - n_accepted

        accepted_revenue = matches.loc[matches["Selected"] == 1, "Order_SKU_Revenue"].sum()
        plant = matches["Plant"].iloc[0] if matches["Plant"].nunique() == 1 else "multiple plants"

        top_reason = None
        if "Reason" in matches.columns:
            rejected_reasons = matches.loc[matches["Selected"] == 0, "Reason"].dropna()
            if not rejected_reasons.empty:
                top_reason = rejected_reasons.value_counts().idxmax()

        sample_skus = matches["MaterialNumber"].head(5).tolist()

        summary = (
            f"Order {group_flag} has {n_total} SKU lines (Plant {plant}): "
            f"{n_accepted} accepted, {n_rejected} rejected. "
            f"Total revenue from accepted lines: {accepted_revenue:,.2f}."
        )
        if top_reason:
            summary += f" Most common rejection reason: {top_reason}."

        summary += (
            f"\n\nAsk about a specific SKU for the full breakdown, e.g. "
            f"\"why was order {group_flag} sku {sample_skus[0]} assigned?\" "
            f"(SKUs on this order include: {', '.join(str(s) for s in sample_skus)}"
            f"{', ...' if n_total > 5 else ''})."
        )

        return summary

    def _penalty_estimate(self, row):
        """
        Estimate the penalty tied to an order, from the documented
        penalty fields (Penaltyforpotentialcuts is a rate applied to
        order revenue; FixedPenalty/MinimumPenalty/MaximumPenalty
        bound it). This is an ESTIMATE — the exact Nestlé penalty
        formula isn't part of the provided data pack, so this
        combines the available fields transparently rather than
        claiming precision the source data doesn't support.
        Returns None if no penalty fields are present for this row.
        """
        rate = row.get("Penaltyforpotentialcuts")
        revenue = row.get("Order_SKU_Revenue")
        fixed = row.get("FixedPenalty")
        min_pen = row.get("MinimumPenalty")
        max_pen = row.get("MaximumPenalty")

        if pd.isna(rate) and pd.isna(fixed):
            return None

        estimate = 0.0
        if pd.notna(rate) and pd.notna(revenue):
            estimate += rate * revenue
        if pd.notna(fixed):
            estimate += fixed

        if pd.notna(min_pen):
            estimate = max(estimate, min_pen)
        if pd.notna(max_pen):
            estimate = min(estimate, max_pen)

        return estimate

    # ======================================================
    # AI QUESTION ANSWERING
    # ======================================================

    def _format_series(self, series, n=5, value_fmt="{:.2f}"):
        """Turn a top-N pandas Series (from warehouse_revenue(), etc.)
        into a readable multi-line string for a chat answer."""
        if series is None or len(series) == 0:
            return None
        lines = []
        for idx, val in series.head(n).items():
            try:
                val_str = value_fmt.format(val)
            except (ValueError, TypeError):
                val_str = str(val)
            lines.append(f"{idx}: {val_str}")
        return "\n".join(lines)

    # Ordered intent table: (name, [phrase groups], handler).
    # A phrase group is a tuple of substrings that must ALL appear in
    # the question for that group to match; an intent matches if ANY
    # of its phrase groups match. Checked top to bottom — most
    # specific / disambiguating intents first, generic single-word
    # ones last, so e.g. "which warehouse has the lowest shipping
    # cost" matches the warehouse-level intent before the generic
    # "total shipping cost" one.
    def _intent_table(self):
        return [
            # --- order-level explanation (handled separately below,
            #     needs regex — kept out of this table) ---

            # --- utilization ---
            ("highest_utilization",
             [("highest", "utilization"), ("highest", "utilized"), ("most utilized",)],
             lambda: self._fmt_plant(self.highest_utilization(), "highest utilization")),
            ("lowest_utilization",
             [("lowest", "utilization"), ("lowest", "utilized"), ("least utilized",)],
             lambda: self._fmt_plant(self.lowest_utilization(), "lowest utilization")),
            ("warehouse_most_assignments",
             [("most assignments",), ("most orders assigned",), ("most orders",)],
             lambda: self._fmt_plant(self.warehouse_most_assignments(), "the most accepted order-lines")),

            # --- shipping cost, by warehouse/plant (disambiguated by
            #     "which"/"warehouse"/"plant" so it doesn't swallow
            #     the generic "total shipping cost" question) ---
            ("lowest_shipping_by_plant",
             [("lowest", "shipping"), ("cheapest",)],
             lambda: self._fmt_plant(self.lowest_shipping_cost(), "the lowest average shipping cost")),
            ("highest_shipping_by_plant",
             [("highest", "shipping"), ("most expensive", "shipping")],
             lambda: self._fmt_plant(self.highest_shipping_cost(), "the highest average shipping cost")),

            # --- carbon, by warehouse ---
            ("highest_carbon_plant",
             [("highest", "carbon"), ("most", "carbon"), ("most", "emissions")],
             lambda: self._fmt_plant(self.highest_carbon(), "the highest carbon emissions")),
            ("lowest_carbon_plant",
             [("lowest", "carbon"), ("least", "carbon"), ("least", "emissions")],
             lambda: self._fmt_plant(self.lowest_carbon(), "the lowest carbon emissions")),

            # --- inventory, by warehouse ---
            ("highest_inventory_plant",
             [("highest", "inventory"), ("most", "inventory"), ("most", "stock")],
             lambda: self._fmt_plant(self.highest_inventory(), "the highest inventory")),
            ("lowest_inventory_plant",
             [("lowest", "inventory"), ("least", "inventory"), ("stock", "short"), ("shortage",)],
             lambda: self._fmt_plant(self.lowest_inventory(), "the lowest inventory")),

            # --- best / worst warehouse & plant (by revenue) ---
            ("best_warehouse",
             [("best", "warehouse"), ("top", "warehouse", "performing"), ("top performing warehouse",)],
             lambda: self._fmt_plant(self.best_warehouse(), "the best overall performance")),
            ("worst_warehouse",
             [("worst", "warehouse")],
             lambda: self._fmt_plant(self.worst_warehouse(), "the weakest overall performance")),
            ("best_plant",
             [("best", "plant"), ("which plant", "best")],
             lambda: self._fmt_plant(self.best_plant(), "the strongest performance")),
            ("worst_plant",
             [("worst", "plant")],
             lambda: self._fmt_plant(self.worst_plant(), "the weakest performance")),

            # --- top/bottom N lists ---
            ("top_warehouses",
             [("top", "warehouses"), ("top 5 warehouse",), ("best warehouses",)],
             lambda: self._format_series(self.top_warehouses())),
            ("bottom_warehouses",
             [("bottom", "warehouses"), ("worst warehouses",)],
             lambda: self._format_series(self.bottom_warehouses())),
            ("top_plants",
             [("top", "plants"), ("best plants",)],
             lambda: self._format_series(self.top_plants())),
            ("bottom_plants",
             [("bottom", "plants"), ("worst plants",)],
             lambda: self._format_series(self.bottom_plants())),

            # --- revenue/orders/inventory BY warehouse or plant
            #     (breakdown, not a single winner) ---
            ("warehouse_revenue_breakdown",
             [("revenue", "by warehouse"), ("warehouse", "revenue breakdown")],
             lambda: self._format_series(self.warehouse_revenue())),
            ("warehouse_orders_breakdown",
             [("orders", "by warehouse"), ("warehouse", "order count")],
             lambda: self._format_series(self.warehouse_orders(), value_fmt="{:.0f}")),
            ("warehouse_inventory_breakdown",
             [("inventory", "by warehouse")],
             lambda: self._format_series(self.warehouse_inventory())),
            ("plant_revenue_breakdown",
             [("revenue", "by plant"), ("plant", "revenue breakdown")],
             lambda: self._format_series(self.plant_revenue())),
            ("plant_orders_breakdown",
             [("orders", "by plant"), ("plant", "order count")],
             lambda: self._format_series(self.plant_orders(), value_fmt="{:.0f}")),

            # --- products ---
            ("top_product",
             [("top product",), ("best selling", "product"), ("best selling", "sku"), ("most popular product",)],
             lambda: str(self.top_product()) if self.top_product() is not None else None),
            ("product_sales",
             [("sales", "by product"), ("product sales",)],
             lambda: self._format_series(self.product_sales(), value_fmt="{:.0f}")),
            ("product_revenue",
             [("revenue", "by product"), ("product revenue",)],
             lambda: self._format_series(self.product_revenue())),

            # --- single-value min/max stats ---
            ("maximum_revenue",
             [("maximum revenue",), ("highest revenue", "order"), ("max revenue",)],
             lambda: self.maximum_revenue()),
            ("minimum_revenue",
             [("minimum revenue",), ("lowest revenue", "order"), ("min revenue",)],
             lambda: self.minimum_revenue()),
            ("average_revenue",
             [("average revenue",), ("mean revenue",)],
             lambda: self.average_revenue()),
            ("maximum_shipping_cost",
             [("maximum shipping",), ("max shipping",), ("highest shipping cost", "order")],
             lambda: self.maximum_shipping_cost()),
            ("minimum_shipping_cost",
             [("minimum shipping",), ("min shipping",), ("lowest shipping cost", "order")],
             lambda: self.minimum_shipping_cost()),
            ("average_shipping_cost",
             [("average shipping",), ("mean shipping",)],
             lambda: self.average_shipping_cost()),
            ("maximum_carbon",
             [("maximum carbon",), ("max carbon",), ("highest carbon value",)],
             lambda: self.maximum_carbon()),
            ("minimum_carbon",
             [("minimum carbon",), ("min carbon",)],
             lambda: self.minimum_carbon()),
            ("average_carbon",
             [("average carbon",), ("mean carbon",)],
             lambda: self.average_carbon()),
            ("total_carbon",
             [("total carbon",), ("total emissions",)],
             lambda: self.total_carbon()),
            ("carbon_emissions_generic",
             [("carbon emission",), ("carbon footprint",), ("co2",)],
             lambda: self.average_carbon()),

            # --- inventory totals ---
            ("total_inventory",
             [("total inventory",)],
             lambda: self.total_inventory()),
            ("average_inventory",
             [("average inventory",), ("mean inventory",)],
             lambda: self.average_inventory()),

            # --- utilization / delivery averages (new KPI cards) ---
            ("average_utilization",
             [("average utilization",), ("average warehouse utilization",), ("mean utilization",)],
             lambda: self.average_utilization()),
            ("average_delivery_days",
             [("average delivery",), ("delivery time",), ("delivery lead time",), ("delivery days",)],
             lambda: self.average_delivery_days()),

            # --- optimization summary (new dashboard section) ---
            ("orders_optimized_count",
             [("orders optimized",), ("orders were optimized",), ("orders accepted",)],
             lambda: self.orders_optimized_count()),
            ("orders_rejected_count",
             [("orders rejected",), ("orders were rejected",)],
             lambda: self.orders_rejected_count()),
            ("constraint_violations",
             [("constraint violation",), ("constraints violated",), ("capacity violated",)],
             lambda: (
                 f"{self.constraint_violations()['count']} constraint violation(s), "
                 f"totaling {self.constraint_violations()['total_overage_units']:.0f} units of overage"
                 if self.constraint_violations() is not None else None
             )),

            # --- fill rate variants ---
            ("revenue_fill_rate",
             [("revenue", "fill rate"), ("revenue based fill rate",), ("revenue weighted fill rate",)],
             lambda: self.revenue_fill_rate()),
            ("average_fill_rate",
             [("fill rate",), ("fulfillment rate",), ("order fulfillment",)],
             lambda: self.average_fill_rate()),

            # --- headline totals / counts ---
            ("total_customers",
             [("total customers",), ("how many customers",), ("number of customers",), ("unique customers",)],
             lambda: self.total_customers()),
            ("total_products",
             [("total products",), ("how many products",), ("number of products",), ("unique products",), ("unique skus",)],
             lambda: self.total_products()),
            ("total_orders",
             [("total orders",), ("how many orders",), ("number of orders",)],
             lambda: self.total_orders()),
            ("total_order_value",
             [("total order value",), ("revenue", "all orders"), ("potential revenue",)],
             lambda: self.total_order_value()),
            ("total_revenue",
             [("total revenue",), ("how much revenue",), ("revenue", "generated"), ("optimized revenue",), ("revenue", "optimized")],
             lambda: self.total_revenue()),
            ("capacity_remaining",
             [("capacity remaining",), ("remaining capacity",)],
             lambda: self._fmt_capacity_remaining()),
            ("total_shipping_cost",
             [("total shipping",), ("shipping cost",)],
             lambda: self.total_shipping_cost()),
            ("total_penalty",
             [("total penalty",), ("penalty cost",), ("penalty",)],
             lambda: self.total_penalty()),

            # --- summaries / recommendations (also handled at a
            #     higher level in qora.py's ask(), kept here too so
            #     DashboardAnalytics.answer() is useful standalone) ---
            ("executive_summary",
             [("executive summary",)],
             lambda: self.executive_summary()),
            ("dashboard_summary",
             [("dashboard summary",), ("summary",)],
             lambda: self.planner_summary()),
            ("recommendations",
             [("recommendation",), ("suggestion",), ("what should", "do")],
             lambda: "\n".join(self.recommendations())),
        ]

    def _fmt_plant(self, value, descriptor):
        if value is None:
            return None
        return f"Plant/Warehouse {value} has {descriptor}."

    def _fmt_capacity_remaining(self):
        cap = self.capacity_remaining()
        if cap is None:
            return None
        parts = []
        if cap["avg_dock_remaining"] is not None:
            parts.append(f"avg dock remaining {cap['avg_dock_remaining']:.2f}")
        if cap["avg_throughput_capacity"] is not None:
            parts.append(f"avg throughput capacity {cap['avg_throughput_capacity']:.2f}")
        return "Capacity remaining — " + ", ".join(parts) if parts else None

    def answer(self, question):

        q = question.lower()

        # Order-level explanation needs regex, not simple substring
        # matching, so it's handled first and separately.
        order_match = re.search(r"order\s+(\w+)", q)
        sku_match = re.search(r"sku\s+(\w+)|material\s+(\w+)", q)

        if "why" in q and order_match:
            gf = order_match.group(1)
            mn = None
            if sku_match:
                mn = sku_match.group(1) or sku_match.group(2)
            return self.explain_order(group_flag=gf, material_number=mn)

        any_intent_matched = False

        for _name, phrase_groups, handler in self._intent_table():
            matched = any(all(phrase in q for phrase in group) for group in phrase_groups)
            if not matched:
                continue
            any_intent_matched = True
            try:
                result = handler()
            except Exception:
                result = None
            if result is not None:
                return result
            # matched but no data for it (e.g. column missing) —
            # keep trying other intents rather than giving up here.

        if any_intent_matched:
            return (
                "That's a question I understand, but this dataset doesn't "
                "have the column needed to answer it (e.g. no customer "
                "identifier is present in this extract)."
            )

        return "Sorry, I couldn't understand that analytics question."

    # ======================================================
    # END OF CLASS
    # ======================================================