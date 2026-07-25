"""
==========================================================
QORA AI
graphs.py

Explains every dashboard graph with:
1. Graph Title
2. Graph Display
3. Explanation
4. Business Insight
5. Recommendation
==========================================================
"""

import streamlit as st

# ==========================================================
# GRAPH KNOWLEDGE BASE
# ==========================================================

GRAPH_INFO = {

# ----------------------------------------------------------
# Revenue Trend
# ----------------------------------------------------------

"revenue":{

"keywords":[
"revenue",
"revenue graph",
"revenue trend",
"sales",
"income",
"revenue chart",
"earnings"
],

"title":"📈 Revenue Trend",

"explanation":"""
This graph shows how total revenue changes over time.

Revenue is one of the most important business KPIs because it reflects the financial performance of the supply chain.

An upward trend indicates improved optimization performance.
""",

"importance":"""
Why it matters

• Measures business growth
• Tracks optimization success
• Helps compare different planning strategies
• Supports financial decision making
""",

"insight":"""
Higher revenue generally indicates better warehouse allocation, improved inventory utilization and higher order fulfillment.
""",

"recommendation":"""
Continue assigning orders to warehouses that maximize revenue while maintaining high fill rate and low shipping cost.
"""
},

# ----------------------------------------------------------
# Fill Rate
# ----------------------------------------------------------

"fill_rate":{

"keywords":[
"fill rate",
"fillrate",
"service level",
"fulfilled orders",
"order fulfillment"
],

"title":"📦 Fill Rate",

"explanation":"""
Fill Rate measures how many customer orders were successfully fulfilled.

Formula

Fulfilled Orders / Total Orders × 100

Higher values indicate better customer service.
""",

"importance":"""
Why it matters

• Customer Satisfaction
• Better Service Level
• Lower Lost Sales
• Higher Revenue
""",

"insight":"""
A low Fill Rate usually indicates inventory shortages or warehouse capacity limitations.
""",

"recommendation":"""
Increase inventory availability or redistribute warehouse capacity to improve fulfillment.
"""
},

# ----------------------------------------------------------
# Warehouse Utilization
# ----------------------------------------------------------

"warehouse_utilization":{

"keywords":[
"warehouse utilization",
"utilization",
"warehouse usage",
"capacity utilization",
"warehouse load"
],

"title":"🏭 Warehouse Utilization",

"explanation":"""
This graph shows how much capacity each warehouse is currently using.

High utilization means the warehouse is handling many orders.

Low utilization indicates unused capacity.
""",

"importance":"""
Why it matters

• Detect overloaded warehouses
• Balance workload
• Improve warehouse efficiency
• Reduce operational risk
""",

"insight":"""
Balanced utilization improves overall supply chain performance.
""",

"recommendation":"""
Shift orders from overloaded warehouses to underutilized warehouses whenever possible.
"""
},

# ----------------------------------------------------------
# Shipping Cost
# ----------------------------------------------------------

"shipping_cost":{

"keywords":[
"shipping",
"shipping cost",
"transportation",
"logistics cost",
"delivery cost"
],

"title":"🚚 Shipping Cost",

"explanation":"""
This graph displays transportation cost for fulfilling customer orders.

The optimization engine attempts to minimize shipping expenses.
""",

"importance":"""
Why it matters

• Lower operational cost
• Higher profit
• Better warehouse selection
""",

"insight":"""
Long transportation distances generally increase shipping costs.
""",

"recommendation":"""
Assign orders to nearby warehouses whenever inventory is available.
"""
},

# ----------------------------------------------------------
# Carbon Emissions
# ----------------------------------------------------------

"carbon":{

"keywords":[
"carbon",
"co2",
"carbon emissions",
"emissions",
"environment"
],

"title":"🌱 Carbon Emissions",

"explanation":"""
This graph estimates CO₂ emissions generated during transportation.

Long-distance deliveries generally produce higher emissions.
""",

"importance":"""
Why it matters

• Sustainability
• Green Logistics
• ESG Goals
• Environmental Impact
""",

"insight":"""
Reducing transportation distance helps lower emissions.
""",

"recommendation":"""
Use nearby warehouses whenever possible while maintaining customer service.
"""
},

# ----------------------------------------------------------
# Risk Score
# ----------------------------------------------------------

"risk_score":{

"keywords":[
"risk",
"risk score",
"warehouse risk",
"operational risk",
"risk analysis"
],

"title":"⚠️ Risk Score",

"explanation":"""
This graph shows the operational risk level of each warehouse.

Warehouses operating close to their capacity usually have higher risk because delays and congestion become more likely.
""",

"importance":"""
Why it matters

• Prevent warehouse overload
• Reduce delivery delays
• Improve operational stability
• Better planning
""",

"insight":"""
High risk warehouses should be monitored carefully and balanced with lower-risk warehouses.
""",

"recommendation":"""
Redistribute orders to reduce operational risk.
"""
},

# ----------------------------------------------------------
# Capacity Utilization
# ----------------------------------------------------------

"capacity":{

"keywords":[
"capacity",
"capacity utilization",
"plant capacity",
"warehouse capacity"
],

"title":"📊 Capacity Utilization",

"explanation":"""
This graph compares used warehouse capacity with total available capacity.

It helps determine whether warehouses are overloaded or underutilized.
""",

"importance":"""
Why it matters

• Prevent overload
• Improve warehouse balance
• Better resource utilization
""",

"insight":"""
Balanced capacity utilization leads to smoother warehouse operations.
""",

"recommendation":"""
Shift workload from highly utilized warehouses to those with available capacity.
"""
},

# ----------------------------------------------------------
# Benchmark
# ----------------------------------------------------------

"benchmark":{

"keywords":[
"benchmark",
"classical vs quantum",
"comparison",
"performance comparison"
],

"title":"⚖️ Classical vs Quantum Benchmark",

"explanation":"""
This graph compares Classical Optimization with Quantum-inspired Optimization.

Metrics compared include revenue, fill rate, runtime and shipping cost.
""",

"importance":"""
Why it matters

• Compare optimization methods
• Evaluate solution quality
• Support technology decisions
""",

"insight":"""
The comparison helps determine which optimization strategy provides better business performance.
""",

"recommendation":"""
Choose the optimization method that provides the highest business value.
"""
},

# ----------------------------------------------------------
# Order Distribution
# ----------------------------------------------------------

"orders":{

"keywords":[
"orders",
"order distribution",
"order allocation",
"order graph"
],

"title":"📦 Order Distribution",

"explanation":"""
This graph shows how customer orders are distributed among warehouses.

Balanced order allocation improves warehouse efficiency.
""",

"importance":"""
Why it matters

• Detect workload imbalance
• Improve warehouse utilization
• Reduce delays
""",

"insight":"""
Uneven order distribution may overload specific warehouses.
""",

"recommendation":"""
Balance order allocation whenever possible.
"""
},

# ----------------------------------------------------------
# Inventory
# ----------------------------------------------------------

"inventory":{

"keywords":[
"inventory",
"stock",
"inventory graph",
"stock level"
],

"title":"📦 Inventory Levels",

"explanation":"""
This graph displays available inventory across warehouses.

Inventory availability directly affects order fulfillment.
""",

"importance":"""
Why it matters

• Prevent stock shortages
• Improve fill rate
• Better planning
""",

"insight":"""
Warehouses with low inventory require replenishment.
""",

"recommendation":"""
Replenish inventory before shortages affect customers.
"""
},

# ----------------------------------------------------------
# Revenue by Warehouse
# ----------------------------------------------------------

"warehouse_revenue":{

"keywords":[
"warehouse revenue",
"revenue by warehouse",
"plant revenue"
],

"title":"💰 Revenue by Warehouse",

"explanation":"""
This graph compares revenue generated by each warehouse.

It highlights which facilities contribute most to overall business performance.
""",

"importance":"""
Why it matters

• Compare warehouse performance
• Identify top-performing facilities
• Support investment decisions
""",

"insight":"""
Higher revenue generally indicates stronger operational performance.
""",

"recommendation":"""
Study top-performing warehouses and replicate their best practices.
"""
},

# ----------------------------------------------------------
# Product Demand
# ----------------------------------------------------------

"product_demand":{

"keywords":[
"product demand",
"demand graph",
"product sales",
"demand"
],

"title":"📈 Product Demand",

"explanation":"""
This graph displays customer demand for different products.

It helps planners understand which products require more inventory.
""",

"importance":"""
Why it matters

• Inventory planning
• Demand forecasting
• Reduce shortages
""",

"insight":"""
Products with consistently high demand require higher inventory levels.
""",

"recommendation":"""
Maintain sufficient stock for high-demand products.
"""
},

# ----------------------------------------------------------
# Penalty Cost
# ----------------------------------------------------------

"penalty":{

"keywords":[
"penalty",
"penalty cost",
"lost sales",
"unfulfilled orders"
],

"title":"💸 Penalty Cost",

"explanation":"""
Penalty Cost represents losses caused by unfulfilled customer demand.

Lower penalty costs indicate better optimization performance.
""",

"importance":"""
Why it matters

• Reduce business losses
• Improve customer satisfaction
• Increase profitability
""",

"insight":"""
High penalties usually indicate inventory shortages or capacity issues.
""",

"recommendation":"""
Increase inventory availability and improve warehouse allocation.
"""
},

# ----------------------------------------------------------
# SLA Performance
# ----------------------------------------------------------

"sla":{

"keywords":[
"sla",
"delivery performance",
"service level agreement",
"on time delivery"
],

"title":"🚚 SLA Performance",

"explanation":"""
This graph shows whether deliveries meet the required service level agreement.

Higher SLA compliance indicates reliable customer service.
""",

"importance":"""
Why it matters

• Customer satisfaction
• Delivery reliability
• Business reputation
""",

"insight":"""
Late deliveries reduce SLA performance.
""",

"recommendation":"""
Optimize warehouse allocation and transportation planning.
"""
},

# ----------------------------------------------------------
# Runtime
# ----------------------------------------------------------

"runtime":{

"keywords":[
"runtime",
"execution time",
"processing time",
"algorithm speed"
],

"title":"⏱ Runtime Comparison",

"explanation":"""
This graph shows how long each optimization algorithm takes to complete.

Lower execution time enables faster business decisions.
""",

"importance":"""
Why it matters

• Faster planning
• Better responsiveness
• Improved productivity
""",

"insight":"""
Runtime becomes increasingly important for large enterprise datasets.
""",

"recommendation":"""
Select algorithms that balance execution speed and solution quality.
"""
},

}