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


class DashboardAnalytics:
    """
    Dashboard Analytics Engine
    """

    def __init__(self, df):
        self.df = df.copy()

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

    def total_revenue(self):
        if self.column_exists("Revenue"):
            return float(self.df["Revenue"].sum())
        return None

    def total_shipping_cost(self):
        if self.column_exists("Shipping Cost"):
            return float(self.df["Shipping Cost"].sum())
        return None

    def total_penalty(self):
        if self.column_exists("Penalty Cost"):
            return float(self.df["Penalty Cost"].sum())
        return None

    def average_fill_rate(self):
        if self.column_exists("Fill Rate"):
            return round(self.df["Fill Rate"].mean(), 2)
        return None

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

    def highest_utilization(self):

        if not self.column_exists("Warehouse"):
            return None

        if not self.column_exists("Warehouse Utilization"):
            return None

        util = (
            self.df
            .groupby("Warehouse")["Warehouse Utilization"]
            .mean()
        )

        return util.idxmax()

    def lowest_utilization(self):

        if not self.column_exists("Warehouse"):
            return None

        if not self.column_exists("Warehouse Utilization"):
            return None

        util = (
            self.df
            .groupby("Warehouse")["Warehouse Utilization"]
            .mean()
        )

        return util.idxmin()

    # ======================================================
    # SHIPPING ANALYTICS
    # ======================================================

    def highest_shipping_cost(self):

        if not self.column_exists("Warehouse"):
            return None

        if not self.column_exists("Shipping Cost"):
            return None

        cost = (
            self.df
            .groupby("Warehouse")["Shipping Cost"]
            .sum()
        )

        return cost.idxmax()

    def lowest_shipping_cost(self):

        if not self.column_exists("Warehouse"):
            return None

        if not self.column_exists("Shipping Cost"):
            return None

        cost = (
            self.df
            .groupby("Warehouse")["Shipping Cost"]
            .sum()
        )

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
    # AI QUESTION ANSWERING
    # ======================================================

    def answer(self, question):

        q = question.lower()

        if "total orders" in q:
            return self.total_orders()

        if "revenue" in q:
            return self.total_revenue()

        if "shipping" in q:
            return self.total_shipping_cost()

        if "penalty" in q:
            return self.total_penalty()

        if "fill rate" in q:
            return self.average_fill_rate()

        if "best warehouse" in q:
            return self.best_warehouse()

        if "worst warehouse" in q:
            return self.worst_warehouse()

        if "best plant" in q:
            return self.best_plant()

        if "top product" in q:
            return self.top_product()

        if "summary" in q:
            return self.planner_summary()

        if "recommendation" in q:
            return "\n".join(self.recommendations())

        return "Sorry, I couldn't understand that analytics question."

    # ======================================================
    # END OF CLASS
    # ======================================================