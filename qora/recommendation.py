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
# END OF FILE
# =====================================================