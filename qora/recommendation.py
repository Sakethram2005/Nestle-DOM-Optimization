"""
=========================================================
QORA AI
recommendations.py

AI Recommendation Engine

Generates intelligent recommendations
based on dashboard analytics.

=========================================================
"""


class RecommendationEngine:

    def __init__(self, analytics):

        """
        analytics = DashboardAnalytics object
        """

        self.analytics = analytics

    # =====================================================
    # FILL RATE
    # =====================================================

    def fill_rate_recommendation(self):

        fill = self.analytics.average_fill_rate()

        if fill is None:
            return "Fill Rate data not available."

        if fill >= 98:
            return "Excellent Fill Rate. Maintain current inventory strategy."

        elif fill >= 95:
            return "Good Fill Rate. Minor improvements can increase customer satisfaction."

        elif fill >= 90:
            return "Moderate Fill Rate. Consider increasing inventory levels."

        else:
            return "Low Fill Rate. Urgent inventory planning is recommended."

    # =====================================================
    # SHIPPING COST
    # =====================================================

    def shipping_recommendation(self):

        warehouse = self.analytics.highest_shipping_cost()

        if warehouse is None:
            return "Shipping data unavailable."

        return (
            f"Shipping costs are highest for '{warehouse}'. "
            "Review transportation routes and carrier selection."
        )

    # =====================================================
    # CARBON
    # =====================================================

    def carbon_recommendation(self):

        warehouse = self.analytics.highest_carbon()

        if warehouse is None:
            return "Carbon data unavailable."

        return (
            f"'{warehouse}' has the highest carbon emissions. "
            "Optimize delivery routes and consolidate shipments."
        )

    # =====================================================
    # INVENTORY
    # =====================================================

    def inventory_recommendation(self):

        warehouse = self.analytics.lowest_inventory()

        if warehouse is None:
            return "Inventory information unavailable."

        return (
            f"Replenish inventory for '{warehouse}' "
            "to reduce stock-out risk."
        )

    # =====================================================
    # UTILIZATION
    # =====================================================

    def utilization_recommendation(self):

        warehouse = self.analytics.highest_utilization()

        if warehouse is None:
            return "Warehouse utilization data unavailable."

        return (
            f"'{warehouse}' is highly utilized. "
            "Consider balancing workload across other warehouses."
        )

    # =====================================================
    # REVENUE
    # =====================================================

    def revenue_recommendation(self):

        warehouse = self.analytics.best_warehouse()

        if warehouse is None:
            return "Revenue data unavailable."

        return (
            f"'{warehouse}' generates the highest revenue. "
            "Analyze its strategy and replicate best practices."
        )

    # =====================================================
    # PENALTY
    # =====================================================

    def penalty_recommendation(self):

        penalty = self.analytics.total_penalty()

        if penalty is None:
            return "Penalty information unavailable."

        return (
            f"Current total penalty cost is {penalty}. "
            "Reducing delivery delays can lower this value."
        )
    
        # =====================================================
    # WAREHOUSE RECOMMENDATIONS
    # =====================================================

    def warehouse_recommendation(self):

        best = self.analytics.best_warehouse()
        worst = self.analytics.worst_warehouse()

        recommendations = []

        if best:
            recommendations.append(
                f"Best performing warehouse: {best}. Continue current operating strategy."
            )

        if worst:
            recommendations.append(
                f"Warehouse {worst} requires operational improvements."
            )

        return recommendations

    # =====================================================
    # PLANT RECOMMENDATIONS
    # =====================================================

    def plant_recommendation(self):

        best = self.analytics.best_plant()
        worst = self.analytics.worst_plant()

        recommendations = []

        if best:
            recommendations.append(
                f"Plant {best} shows the strongest performance."
            )

        if worst:
            recommendations.append(
                f"Review production efficiency at {worst}."
            )

        return recommendations

    # =====================================================
    # PRODUCT RECOMMENDATIONS
    # =====================================================

    def product_recommendation(self):

        product = self.analytics.top_product()

        if product is None:
            return "Product information unavailable."

        return (
            f"'{product}' is currently the top-performing product. "
            "Ensure sufficient inventory and prioritize replenishment."
        )

    # =====================================================
    # CUSTOMER RECOMMENDATIONS
    # =====================================================

    def customer_recommendation(self):

        customers = self.analytics.total_customers()

        if customers is None:
            return "Customer data unavailable."

        return (
            f"The dashboard currently serves {customers} unique customers. "
            "Maintain high service levels to improve customer satisfaction."
        )

    # =====================================================
    # INVENTORY BALANCING
    # =====================================================

    def inventory_balance_recommendation(self):

        high = self.analytics.highest_inventory()
        low = self.analytics.lowest_inventory()

        return (
            f"Consider transferring stock from '{high}' "
            f"to '{low}' if business rules permit."
        )

    # =====================================================
    # TRANSPORTATION
    # =====================================================

    def transportation_recommendation(self):

        return (
            "Optimize delivery routes, consolidate shipments "
            "and reduce unnecessary transportation distance."
        )

    # =====================================================
    # SUSTAINABILITY
    # =====================================================

    def sustainability_recommendation(self):

        return (
            "Reduce carbon emissions by selecting shorter routes, "
            "improving truck utilization and reducing empty trips."
        )

    # =====================================================
    # EXECUTIVE ACTION PLAN
    # =====================================================

    def executive_action_plan(self):

        return [

            "Increase Fill Rate.",

            "Reduce Shipping Cost.",

            "Reduce Carbon Emissions.",

            "Balance Warehouse Utilization.",

            "Improve Inventory Planning.",

            "Reduce Penalty Costs.",

            "Improve Customer Service.",

            "Continue AI-based Optimization."

        ]

    # =====================================================
    # PRIORITY ACTIONS
    # =====================================================

    def priority_actions(self):

        actions = []

        actions.append(self.fill_rate_recommendation())
        actions.append(self.shipping_recommendation())
        actions.append(self.carbon_recommendation())
        actions.append(self.inventory_recommendation())
        actions.append(self.utilization_recommendation())

        return actions

    # =====================================================
    # AI HEALTH SCORE
    # =====================================================

    def ai_score(self):

        score = 100

        fill = self.analytics.average_fill_rate()

        if fill is not None:

            if fill < 95:
                score -= 10

            if fill < 90:
                score -= 15

        if self.analytics.total_penalty():

            if self.analytics.total_penalty() > 10000:
                score -= 10

        return max(score, 0)
    
        # =====================================================
    # OVERALL RECOMMENDATION SUMMARY
    # =====================================================

    def summary(self):

        return {
            "AI Score": self.ai_score(),
            "Priority Actions": self.priority_actions(),
            "Warehouse": self.warehouse_recommendation(),
            "Plant": self.plant_recommendation(),
            "Product": self.product_recommendation(),
            "Customer": self.customer_recommendation(),
            "Executive Plan": self.executive_action_plan()
        }

    # =====================================================
    # RISK ANALYSIS
    # =====================================================

    def risk_analysis(self):

        risks = []

        fill = self.analytics.average_fill_rate()

        if fill is not None and fill < 90:
            risks.append(
                "Low Fill Rate may lead to customer dissatisfaction."
            )

        if self.analytics.highest_utilization():
            risks.append(
                f"High warehouse utilization detected at "
                f"{self.analytics.highest_utilization()}."
            )

        if self.analytics.highest_carbon():
            risks.append(
                f"High carbon emissions from "
                f"{self.analytics.highest_carbon()}."
            )

        if self.analytics.lowest_inventory():
            risks.append(
                f"Low inventory detected at "
                f"{self.analytics.lowest_inventory()}."
            )

        if len(risks) == 0:
            risks.append("No major operational risks detected.")

        return risks

    # =====================================================
    # OPTIMIZATION OPPORTUNITIES
    # =====================================================

    def optimization_opportunities(self):

        return [

            "Optimize warehouse allocation.",

            "Reduce transportation distance.",

            "Improve inventory forecasting.",

            "Balance warehouse utilization.",

            "Increase Fill Rate.",

            "Reduce shipping cost.",

            "Lower carbon emissions.",

            "Improve delivery performance.",

            "Reduce penalty costs.",

            "Increase customer satisfaction."

        ]

    # =====================================================
    # COMPLETE RECOMMENDATION REPORT
    # =====================================================

    def recommendation_report(self):

        report = []

        report.append(f"AI Health Score : {self.ai_score()}")
        report.append("")

        report.append("Priority Actions")
        report.extend(self.priority_actions())
        report.append("")

        report.append("Warehouse Recommendations")
        report.extend(self.warehouse_recommendation())
        report.append("")

        report.append("Plant Recommendations")
        report.extend(self.plant_recommendation())
        report.append("")

        report.append("Risk Analysis")
        report.extend(self.risk_analysis())
        report.append("")

        report.append("Optimization Opportunities")
        report.extend(self.optimization_opportunities())

        return "\n".join(report)

    # =====================================================
    # EXPORT
    # =====================================================

    def export(self):

        return {
            "score": self.ai_score(),
            "summary": self.summary(),
            "risks": self.risk_analysis(),
            "recommendations": self.recommendation_report(),
            "opportunities": self.optimization_opportunities()
        }

    # =====================================================
    # EXPLAINED RECOMMENDATIONS
    #
    # Each entry pairs a real finding (an actual number from the
    # current data) with the business reasoning behind it — why it
    # matters and what it costs — and a concrete recommended action.
    # This replaces generic "improve X" phrasing with "X is currently
    # Y, which means Z, so do W."
    # =====================================================

    def explained_recommendations(self, achievable_fill_rate=None, achievable_utilization=None):
        """
        `achievable_fill_rate` / `achievable_utilization`: optionally
        pass the OR-Tools full-scale benchmark's numbers (from
        benchmark.py) so the fill-rate/utilization findings can state
        what's actually achievable with the same data, not just the
        current state — this is the single most useful insight this
        project has, and it's wasted if displayed as a generic tip.
        """
        items = []

        # --- Fill Rate ---
        fill = self.analytics.average_fill_rate()
        if fill is not None:
            if achievable_fill_rate is not None and achievable_fill_rate - fill > 5:
                reasoning = (
                    f"Current fill rate is only {fill:.2f}%, meaning most ordered "
                    f"demand goes unfulfilled today. Solving the same dataset's "
                    f"inventory-capacity problem exactly (via OR-Tools) reaches "
                    f"{achievable_fill_rate:.2f}% — a gap of "
                    f"{achievable_fill_rate - fill:.1f} points. This shows the "
                    "shortfall is largely an assignment-logic gap, not a real "
                    "inventory shortage: the capacity to fulfill far more orders "
                    "already exists in the data."
                )
                action = (
                    "Adopt exact/optimized assignment logic (see the Full-Scale "
                    "Benchmark) in place of the current default-assignment "
                    "process to close most of this gap without new inventory."
                )
            else:
                reasoning = (
                    f"Current fill rate is {fill:.2f}%. Every unfulfilled order "
                    "represents lost revenue and, if it recurs for the same "
                    "customer, a service-level risk."
                )
                action = "Review inventory allocation for the SKUs driving the shortfall."

            items.append({
                "title": "Fill Rate",
                "finding": f"{fill:.2f}%",
                "reasoning": reasoning,
                "action": action,
            })

        # --- Shipping cost ---
        highest_ship_wh = self.analytics.highest_shipping_cost()
        avg_ship = self.analytics.average_shipping_cost()
        if highest_ship_wh is not None and avg_ship is not None:
            items.append({
                "title": "Shipping Cost",
                "finding": f"Plant/Warehouse {highest_ship_wh} has the highest average shipping cost",
                "reasoning": (
                    f"Average shipping cost across all warehouses is "
                    f"{avg_ship:,.2f}. Plant {highest_ship_wh} sits above that "
                    "average — every order routed through it costs more to "
                    "fulfill than the network average, directly reducing margin "
                    "on those orders."
                ),
                "action": (
                    f"Review carrier contracts and routing for Plant {highest_ship_wh}, "
                    "or reassign eligible orders to a lower-cost warehouse when "
                    "inventory allows."
                ),
            })

        # --- Warehouse utilization ---
        highest_util_wh = self.analytics.highest_utilization()
        lowest_util_wh = self.analytics.lowest_utilization()
        current_util = self.analytics.average_utilization()
        if highest_util_wh is not None and lowest_util_wh is not None:
            if achievable_utilization is not None and current_util is not None:
                reasoning = (
                    f"Current utilization (based on today's existing "
                    f"assignment) averages {current_util:.2f}%, with Plant "
                    f"{highest_util_wh} the most utilized and Plant "
                    f"{lowest_util_wh} the least — but solving the assignment "
                    f"problem optimally (OR-Tools) implies utilization closer to "
                    f"{achievable_utilization:.2f}%. The imbalance today is a "
                    "symptom of the same assignment-logic gap as the fill rate "
                    "finding above, not fixed physical constraints."
                )
            else:
                reasoning = (
                    f"Plant {highest_util_wh} is the most utilized warehouse and "
                    f"Plant {lowest_util_wh} the least. A large gap between the "
                    "two means some warehouses risk congestion and delay while "
                    "others sit underused — both reduce overall network "
                    "efficiency."
                )
            items.append({
                "title": "Warehouse Utilization",
                "finding": f"Highest: Plant {highest_util_wh} — Lowest: Plant {lowest_util_wh}",
                "reasoning": reasoning,
                "action": (
                    f"Shift eligible order volume from Plant {highest_util_wh} "
                    f"toward Plant {lowest_util_wh} where inventory and shipping "
                    "cost allow, to reduce congestion risk and use idle capacity."
                ),
            })

        # --- Penalty cost ---
        penalty = self.analytics.total_penalty()
        revenue = self.analytics.total_revenue()
        if penalty is not None and revenue:
            penalty_pct_of_revenue = penalty / revenue * 100
            items.append({
                "title": "Penalty Cost",
                "finding": f"{penalty:,.2f}",
                "reasoning": (
                    f"Estimated penalty exposure from unfulfilled orders is "
                    f"{penalty:,.2f} — equivalent to {penalty_pct_of_revenue:.2f}% "
                    "of current accepted revenue. This is a direct cost of the "
                    "fill-rate gap above: fewer unfulfilled orders means less "
                    "penalty exposure, not just more revenue."
                ),
                "action": (
                    "Prioritize fulfilling the highest-penalty-rate orders first "
                    "when capacity is constrained, rather than treating all "
                    "unfulfilled demand as equal."
                ),
            })

        # --- Best-performing plant (revenue) ---
        best_plant = self.analytics.best_plant()
        worst_plant = self.analytics.worst_plant()
        if best_plant is not None and worst_plant is not None:
            items.append({
                "title": "Plant Performance",
                "finding": f"Best: Plant {best_plant} — Weakest: Plant {worst_plant}",
                "reasoning": (
                    f"Plant {best_plant} generates the most revenue in the "
                    f"network; Plant {worst_plant} the least. Understanding "
                    f"*why* {best_plant} performs well (product mix, inventory "
                    "depth, location) is more actionable than treating this as "
                    "a ranking — the goal is to replicate what's working, not "
                    "just identify a leaderboard."
                ),
                "action": (
                    f"Compare Plant {best_plant}'s product mix and inventory "
                    f"policy against Plant {worst_plant}'s to identify a "
                    "specific, transferable practice."
                ),
            })

        return items

    def explained_recommendations_text(self, achievable_fill_rate=None, achievable_utilization=None):
        """Plain-text rendering of explained_recommendations(), for
        contexts (chat, plain reports) that want a single string."""
        items = self.explained_recommendations(achievable_fill_rate, achievable_utilization)
        blocks = []
        for item in items:
            blocks.append(
                f"{item['title']}: {item['finding']}\n"
                f"Why it matters: {item['reasoning']}\n"
                f"Recommended action: {item['action']}"
            )
        return "\n\n".join(blocks)

# =====================================================
# END OF FILE
# =====================================================