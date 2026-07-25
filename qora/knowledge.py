# ==========================================================
# QORA AI KNOWLEDGE BASE
# Version 1.0
# Part 1
# ==========================================================
knowledge = {

# ==========================================================
# PROJECT OVERVIEW
# ==========================================================

"project_summary":{

"keywords":[
"project",
"project summary",
"summarize project",
"summary",
"about project",
"tell me about project",
"project overview",
"overview",
"what is this project",
"what does this project do",
"explain project",
"project details"
],

"answer":"""
This project develops an AI-powered Distributed Order Management (DOM) system for Nestlé.

The system recommends the best warehouse (Distribution Center) for fulfilling customer orders while minimizing shipping cost, reducing penalties, maximizing revenue and improving fill rate.

The project compares Classical Optimization with Quantum-inspired Optimization techniques and provides explainable recommendations through an interactive Streamlit dashboard.
"""
},

# ==========================================================
# DOM
# ==========================================================

"dom":{

"keywords":[
"dom",
"distributed order management",
"what is dom",
"define dom",
"meaning of dom",
"dom meaning",
"explain dom",
"tell me about dom",
"what is distributed order management",
"distributed order management system",
"dom explanation"
],

"answer":"""
Distributed Order Management (DOM) is the process of selecting the best warehouse to fulfill customer orders.

The optimizer considers inventory availability, warehouse capacity, shipping cost, penalties, revenue and business constraints before recommending the best warehouse.
"""
},

# ==========================================================
# OBJECTIVE
# ==========================================================

"objective":{

"keywords":[
"objective",
"objective function",
"goal",
"optimization goal",
"project objective",
"what is objective",
"objective of project",
"business objective"
],

"answer":"""
The objective of this project is to maximize overall business value by:

• Maximizing fulfilled orders
• Increasing revenue
• Minimizing shipping cost
• Reducing penalty cost
• Improving warehouse utilization
• Increasing fill rate
"""
},

# ==========================================================
# OR TOOLS
# ==========================================================

"ortools":{

"keywords":[
"or tools",
"ortools",
"google or tools",
"google ortools",
"what is ortools",
"what is or tools",
"define ortools",
"explain ortools",
"classical optimization",
"google optimization"
],

"answer":"""
Google OR-Tools is an optimization library.

It is used as the classical optimization baseline for solving the warehouse assignment problem.

It provides efficient algorithms for linear programming, mixed integer programming, routing and scheduling.
"""
},

# ==========================================================
# QAOA
# ==========================================================

"qaoa":{

"keywords":[
"qaoa",
"quantum approximate optimization algorithm",
"what is qaoa",
"define qaoa",
"explain qaoa",
"quantum optimization algorithm"
],

"answer":"""
QAOA (Quantum Approximate Optimization Algorithm) is a quantum optimization algorithm designed to solve combinatorial optimization problems.

Our project compares Quantum-inspired optimization against the Classical OR-Tools baseline.
"""
},

# ==========================================================
# QUANTUM
# ==========================================================

"quantum":{

"keywords":[
"quantum",
"quantum computing",
"quantum optimization",
"quantum algorithm",
"what is quantum",
"explain quantum",
"why quantum"
],

"answer":"""
Quantum optimization uses quantum principles to search for better solutions to difficult optimization problems.

Although current quantum hardware is limited, quantum-inspired algorithms provide valuable research insights for future logistics optimization.
"""
},

# ==========================================================
# CLASSICAL VS QUANTUM
# ==========================================================

"classical_quantum":{

"keywords":[
"classical vs quantum",
"compare classical and quantum",
"classical comparison",
"quantum comparison",
"difference between classical and quantum",
"why quantum is better"
],

"answer":"""
Classical Optimization:
• Mature technology
• Fast for many practical problems
• Reliable

Quantum Optimization:
• Designed for complex combinatorial optimization
• Potentially explores larger solution spaces
• Currently limited by hardware but promising for future supply chains

This project compares both approaches using the same objective function.
"""
},

# ==========================================================
# FILL RATE
# ==========================================================

"fill_rate":{

"keywords":[
"fill rate",
"fillrate",
"fill percentage",
"order fill rate",
"what is fill rate",
"define fill rate",
"fill rate meaning",
"fill rate explanation"
],

"answer":"""
Fill Rate is the percentage of customer demand successfully fulfilled.

Higher Fill Rate means more customer orders are delivered successfully and customer satisfaction improves.
"""
},

# ==========================================================
# REVENUE
# ==========================================================

"revenue":{

"keywords":[
"revenue",
"sales",
"income",
"order revenue",
"business revenue",
"project revenue",
"what is revenue",
"explain revenue"
],

"answer":"""
Revenue is the total value generated from fulfilled customer orders.

The optimizer attempts to maximize revenue while reducing operational costs.
"""
},

# ==========================================================
# SHIPPING COST
# ==========================================================

"shipping_cost":{

"keywords":[
"shipping",
"shipping cost",
"delivery cost",
"transport cost",
"logistics cost",
"freight",
"shipping charges"
],

"answer":"""
Shipping Cost represents the transportation expense for delivering products from warehouses to customers.

The optimization model attempts to minimize this cost while maintaining service quality.
"""
},

# ==========================================================
# PENALTY
# ==========================================================

"penalty":{

"keywords":[
"penalty",
"penalty cost",
"unfulfilled orders",
"missed demand",
"penalties",
"penalty explanation"
],

"answer":"""
Penalty Cost represents the business loss caused by partially fulfilled or unfulfilled customer orders.

Reducing penalties improves customer satisfaction and business performance.
"""
},

# ==========================================================
# INVENTORY
# ==========================================================

"inventory":{

"keywords":[
"inventory",
"stock",
"warehouse stock",
"available inventory",
"inventory availability",
"inventory management"
],

"answer":"""
Inventory represents the available stock at each warehouse.

Orders can only be assigned if sufficient inventory exists for the requested SKU.
"""
},

# ==========================================================
# SKU
# ==========================================================

"sku":{

"keywords":[
"sku",
"material",
"material number",
"product code",
"stock keeping unit",
"what is sku"
],

"answer":"""
SKU (Stock Keeping Unit) is a unique identifier for each product.

The optimizer uses SKU information to verify inventory availability before assigning warehouses.
"""
},

# ==========================================================
# DISTRIBUTION CENTER
# ==========================================================

"dc":{

"keywords":[
"dc",
"distribution center",
"warehouse",
"plant",
"fulfillment center",
"what is dc",
"what is warehouse"
],

"answer":"""
A Distribution Center (DC) stores inventory and fulfills customer orders.

The optimizer selects the most suitable DC based on inventory, cost and operational constraints.
"""
},

# ==========================================================
# CAPACITY
# ==========================================================

"capacity":{

"keywords":[
"capacity",
"warehouse capacity",
"dock capacity",
"throughput",
"warehouse utilization",
"capacity utilization"
],

"answer":"""
Warehouse Capacity defines the maximum number of orders or inventory that can be handled.

Capacity constraints prevent warehouses from being overloaded.
"""
},

# ==========================================================
# END OF PART 1
# ==========================================================

# ==========================================================
# WAREHOUSE UTILIZATION
# ==========================================================

"warehouse_utilization":{

"keywords":[
"warehouse utilization",
"utilization",
"plant utilization",
"warehouse usage",
"warehouse load",
"capacity usage",
"warehouse performance",
"highest utilization",
"lowest utilization"
],

"answer":"""
Warehouse Utilization shows how efficiently each warehouse is being used.

High utilization means the warehouse is handling many orders.

Very high utilization may lead to congestion, while very low utilization indicates underused resources.

A balanced utilization across warehouses improves efficiency and reduces operational risk.
"""
},

# ==========================================================
# RISK SCORE
# ==========================================================

"risk_score":{

"keywords":[
"risk",
"risk score",
"warehouse risk",
"operational risk",
"high risk warehouse",
"risk analysis"
],

"answer":"""
Risk Score estimates the operational risk of each warehouse.

It is primarily based on warehouse utilization.

Higher utilization generally leads to higher operational risk because overloaded warehouses are more likely to experience delays.
"""
},

# ==========================================================
# CARBON EMISSIONS
# ==========================================================

"carbon":{

"keywords":[
"carbon",
"carbon emission",
"carbon emissions",
"co2",
"co₂",
"greenhouse gas",
"sustainability",
"environment",
"environmental impact",
"green logistics"
],

"answer":"""
Carbon Emissions estimate the environmental impact of transporting products.

Longer transportation routes usually produce higher emissions.

Reducing transportation distance helps lower carbon emissions and supports sustainable logistics operations.
"""
},

# ==========================================================
# SLA
# ==========================================================

"sla":{

"keywords":[
"sla",
"service level agreement",
"delivery time",
"delivery days",
"sla status",
"within sla",
"delayed"
],

"answer":"""
SLA (Service Level Agreement) measures whether deliveries are completed within the required delivery time.

Orders delivered within the target time improve customer satisfaction.
"""
},

# ==========================================================
# COST TO SERVE
# ==========================================================

"cost_to_serve":{

"keywords":[
"cost to serve",
"cost-to-serve",
"serve cost",
"serving cost",
"logistics expense",
"cost analysis"
],

"answer":"""
Cost-to-Serve estimates the operational cost required to fulfill customer orders.

It includes logistics, transportation and warehouse handling costs.

Lower Cost-to-Serve improves profitability.
"""
},

# ==========================================================
# BENCHMARK
# ==========================================================

"benchmark":{

"keywords":[
"benchmark",
"benchmark report",
"comparison",
"classical vs quantum",
"performance comparison",
"optimization comparison",
"evaluation"
],

"answer":"""
The Benchmark Report compares Classical Optimization and Quantum-inspired Optimization.

It evaluates:

• Fill Rate
• Revenue
• Runtime
• Shipping Cost
• Penalty Cost

This demonstrates the effectiveness of the proposed optimization approach.
"""
},

# ==========================================================
# RUNTIME
# ==========================================================

"runtime":{

"keywords":[
"runtime",
"execution time",
"processing time",
"speed",
"optimization time",
"algorithm runtime"
],

"answer":"""
Runtime measures how long the optimization algorithm takes to produce a solution.

Lower runtime allows planners to make decisions faster, especially in real-time environments.
"""
},

# ==========================================================
# SCALABILITY
# ==========================================================

"scalability":{

"keywords":[
"scalability",
"scale",
"large data",
"bigger dataset",
"large orders",
"future scaling"
],

"answer":"""
Scalability refers to how well the optimization algorithm performs as the number of orders, warehouses and products increases.

A scalable solution maintains good performance even for very large supply chain problems.
"""
},

# ==========================================================
# NOISE ANALYSIS
# ==========================================================

"noise":{

"keywords":[
"noise",
"noise analysis",
"quantum noise",
"hardware noise",
"error",
"noisy quantum"
],

"answer":"""
Current quantum computers are affected by hardware noise.

Noise can reduce solution quality.

Quantum simulators and hybrid optimization techniques are commonly used to overcome these limitations.
"""
},

# ==========================================================
# DECISION VARIABLES
# ==========================================================

"decision_variables":{

"keywords":[
"decision variable",
"decision variables",
"binary variable",
"optimization variable",
"xij",
"variables"
],

"answer":"""
Decision variables represent whether an order is assigned to a warehouse.

Typically,

x(i,j)=1

means order i is assigned to warehouse j.

Otherwise,

x(i,j)=0.
"""
},

# ==========================================================
# CONSTRAINTS
# ==========================================================

"constraints":{

"keywords":[
"constraints",
"constraint",
"optimization constraints",
"capacity constraint",
"inventory constraint",
"business constraints"
],

"answer":"""
The optimization model includes several constraints:

• Inventory availability
• Warehouse capacity
• One warehouse per order
• Demand satisfaction
• Business rules

These constraints ensure all recommendations are feasible.
"""
},

# ==========================================================
# MATHEMATICAL FORMULATION
# ==========================================================

"mathematical_model":{

"keywords":[
"mathematical formulation",
"mathematical model",
"optimization model",
"binary optimization",
"model formulation"
],

"answer":"""
The project is formulated as a binary optimization problem.

Decision variables represent warehouse assignments.

The objective maximizes business value while satisfying inventory, capacity and assignment constraints.
"""
},

# ==========================================================
# GREEDY BASELINE
# ==========================================================

"greedy":{

"keywords":[
"greedy",
"greedy algorithm",
"baseline",
"classical baseline",
"default assignment"
],

"answer":"""
The Greedy Baseline assigns each order sequentially to the best available warehouse.

Although simple and fast, it may not find the globally optimal solution.
"""
},

# ==========================================================
# REVENUE TREND GRAPH
# ==========================================================

"revenue_trend":{

"keywords":[
"revenue trend",
"revenue graph",
"revenue chart",
"line graph",
"sales trend",
"daily revenue",
"explain revenue trend"
],

"answer":"""
The Revenue Trend graph displays how total revenue changes over time.

It helps planners identify:
• Peak sales periods
• Low revenue days
• Seasonal demand
• Business growth

A steadily increasing trend indicates better order fulfillment and improved business performance.
"""
},

# ==========================================================
# FILL RATE GAUGE
# ==========================================================

"fill_rate_chart":{

"keywords":[
"fill rate gauge",
"fill rate graph",
"fill rate chart",
"gauge",
"gauge chart",
"explain fill rate gauge"
],

"answer":"""
The Fill Rate Gauge shows the percentage of customer demand that has been successfully fulfilled.

Green indicates healthy fulfillment.

Yellow suggests moderate performance.

Red indicates many customer orders are not being fulfilled.
"""
},

# ==========================================================
# WAREHOUSE CHART
# ==========================================================

"warehouse_chart":{

"keywords":[
"warehouse chart",
"warehouse graph",
"plant chart",
"plant graph",
"warehouse orders",
"orders by warehouse",
"warehouse utilization graph"
],

"answer":"""
This chart shows how customer orders are distributed among warehouses.

It helps planners identify overloaded warehouses and balance workloads across distribution centers.
"""
},

# ==========================================================
# CAPACITY UTILIZATION
# ==========================================================

"capacity_chart":{

"keywords":[
"capacity chart",
"capacity utilization",
"capacity graph",
"warehouse capacity graph",
"capacity dashboard"
],

"answer":"""
Capacity Utilization measures how much of each warehouse's available capacity is currently being used.

High utilization may increase operational risk, while low utilization indicates spare capacity.
"""
},

# ==========================================================
# SHIPPING COST CHART
# ==========================================================

"shipping_chart":{

"keywords":[
"shipping chart",
"shipping graph",
"shipping cost graph",
"logistics graph",
"transportation graph"
],

"answer":"""
The Shipping Cost chart compares transportation expenses across warehouses.

The optimization algorithm attempts to reduce total shipping cost while maintaining customer service.
"""
},

# ==========================================================
# CARBON GRAPH
# ==========================================================

"carbon_graph":{

"keywords":[
"carbon graph",
"carbon emissions graph",
"co2 graph",
"green graph",
"sustainability graph"
],

"answer":"""
The Carbon Emissions graph estimates environmental impact caused by transportation.

Lower transportation distance usually results in lower carbon emissions.

This helps planners make environmentally sustainable decisions.
"""
},

# ==========================================================
# RISK GRAPH
# ==========================================================

"risk_graph":{

"keywords":[
"risk graph",
"risk chart",
"warehouse risk graph",
"risk dashboard"
],

"answer":"""
The Risk Score graph highlights warehouses that are approaching operational limits.

Higher scores indicate warehouses that may require additional monitoring or workload balancing.
"""
},

# ==========================================================
# BENCHMARK GRAPH
# ==========================================================

"benchmark_graph":{

"keywords":[
"benchmark graph",
"benchmark chart",
"classical graph",
"quantum graph",
"comparison graph",
"compare graph"
],

"answer":"""
The Benchmark graph compares Classical Optimization with Quantum-inspired Optimization.

It evaluates:
• Revenue
• Fill Rate
• Runtime
• Shipping Cost
• Penalty Cost

This demonstrates whether the proposed optimization provides measurable business improvements.
"""
},

# ==========================================================
# SENSITIVITY ANALYSIS
# ==========================================================

"sensitivity":{

"keywords":[
"sensitivity",
"sensitivity analysis",
"demand increase",
"penalty weight",
"scenario analysis",
"what if",
"what-if analysis"
],

"answer":"""
Sensitivity Analysis evaluates how the optimization responds when business conditions change.

Examples include:
• Higher demand
• Increased penalty costs
• Inventory shortages
• Capacity changes

This helps determine the robustness of the optimization model.
"""
},

# ==========================================================
# BATCH OPTIMIZATION
# ==========================================================

"batch":{

"keywords":[
"batch",
"batch optimization",
"multiple orders",
"group optimization",
"order batch"
],

"answer":"""
Batch Optimization processes multiple customer orders together instead of one at a time.

This often produces better overall warehouse assignments and improves optimization quality.
"""
},

# ==========================================================
# SPLIT FULFILLMENT
# ==========================================================

"split":{

"keywords":[
"split fulfillment",
"split order",
"multiple warehouses",
"warehouse a",
"warehouse b"
],

"answer":"""
Split Fulfillment allows a customer order to be supplied by multiple warehouses when a single warehouse lacks sufficient inventory.

This improves service levels while reducing stock shortages.
"""
},

# ==========================================================
# WHAT IF ANALYSIS
# ==========================================================

"what_if":{

"keywords":[
"what if",
"what-if",
"what if analysis",
"demand simulation",
"future demand",
"forecast"
],

"answer":"""
What-if Analysis simulates different business scenarios.

Examples include:

• Demand increase
• Capacity reduction
• Shipping cost changes
• Inventory shortages

Managers can evaluate future performance before implementing operational changes.
"""
},

# ==========================================================
# ALERTS
# ==========================================================

"alerts":{

"keywords":[
"alerts",
"warnings",
"notifications",
"warehouse alerts",
"system alerts"
],

"answer":"""
The Alert system automatically identifies operational issues.

Examples include:
• High warehouse utilization
• High shipping costs
• Low fill rate
• High carbon emissions
• Capacity violations

These alerts help planners react quickly.
"""
},

# ==========================================================
# DASHBOARD
# ==========================================================

"dashboard":{

"keywords":[
"dashboard",
"streamlit",
"dashboard overview",
"dashboard features",
"analytics page"
],

"answer":"""
The dashboard provides a complete operational view of the optimization results.

It includes:

• KPI Metrics
• Revenue Trend
• Fill Rate
• Warehouse Utilization
• Shipping Cost
• Carbon Emissions
• Risk Analysis
• Benchmark Report
• Planner Recommendations
• Analytics
"""
},

# ==========================================================
# PLANNER VIEW
# ==========================================================

"planner":{

"keywords":[
"planner",
"planner view",
"planner summary",
"business planner"
],

"answer":"""
Planner View translates optimization results into business language.

Instead of mathematical equations, it explains:

• Why each warehouse was selected
• Expected business benefits
• Risks
• Operational recommendations
"""
},
# ==========================================================
# REAL-TIME DATA
# ==========================================================

"realtime_data":{

"keywords":[
"real time",
"real-time",
"live data",
"real time data",
"dynamic data",
"live dashboard",
"latest data",
"data refresh",
"automatic update"
],

"answer":"""
Qora is designed to support real-time data.

Instead of static CSV files, the system can later connect to SQL databases, SAP, REST APIs, Excel uploads, or cloud storage.

Whenever new data arrives, optimization can be rerun automatically and the dashboard updates with the latest results.
"""
},

# ==========================================================
# SQL DATABASE
# ==========================================================

"sql":{

"keywords":[
"sql",
"database",
"mysql",
"postgres",
"postgresql",
"sql server",
"oracle database",
"connect database"
],

"answer":"""
The optimization system can read live order and inventory data directly from SQL databases.

This removes the need for manually uploading CSV files and enables continuous optimization.
"""
},

# ==========================================================
# SAP
# ==========================================================

"sap":{

"keywords":[
"sap",
"sap integration",
"sap hana",
"erp",
"enterprise resource planning"
],

"answer":"""
SAP is one of the most widely used Enterprise Resource Planning (ERP) systems.

In production, Qora can retrieve orders, inventory levels and warehouse information directly from SAP before running optimization.
"""
},

# ==========================================================
# API
# ==========================================================

"api":{

"keywords":[
"api",
"rest api",
"web api",
"json api",
"integration api"
],

"answer":"""
REST APIs allow Qora to exchange information with external systems.

Orders, inventory, shipping costs and optimization results can be exchanged automatically using APIs.
"""
},

# ==========================================================
# CSV
# ==========================================================

"csv":{

"keywords":[
"csv",
"csv file",
"upload csv",
"comma separated values"
],

"answer":"""
CSV files provide a simple way to import order, inventory and warehouse data.

Qora supports CSV input and can easily be extended to automatically process uploaded files.
"""
},

# ==========================================================
# EXCEL
# ==========================================================

"excel":{

"keywords":[
"excel",
"xlsx",
"spreadsheet",
"excel upload",
"upload excel"
],

"answer":"""
Excel spreadsheets are commonly used by planners.

Qora can read Excel files containing order information, warehouse capacity and inventory before running optimization.
"""
},

# ==========================================================
# AI ASSISTANT
# ==========================================================

"qora_ai":{

"keywords":[
"qora",
"ai",
"assistant",
"chatbot",
"ai chatbot",
"what is qora",
"who are you",
"help me"
],

"answer":"""
I am Qora, the AI assistant for the Distributed Order Management project.

I can:
• Answer project questions
• Explain optimization concepts
• Explain dashboard charts
• Summarize results
• Compare Classical and Quantum methods
• Generate planner summaries
• Provide business recommendations
"""
},

# ==========================================================
# RECOMMENDATIONS
# ==========================================================

"recommendations":{

"keywords":[
"recommend",
"recommendation",
"suggestions",
"improvements",
"how can i improve",
"business recommendation"
],

"answer":"""
Typical recommendations include:

• Improve warehouse balance
• Reduce shipping cost
• Increase fill rate
• Lower penalty costs
• Reduce carbon emissions
• Prevent warehouse overload
• Improve inventory allocation
"""
},

# ==========================================================
# QUANTUM HARDWARE
# ==========================================================

"hardware":{

"keywords":[
"quantum hardware",
"hardware",
"ibm quantum",
"ionq",
"quantum computer",
"real quantum"
],

"answer":"""
Current quantum hardware is still developing.

Because of limited qubits and hardware noise, many optimization experiments are performed using simulators or hybrid quantum-classical approaches.
"""
},

# ==========================================================
# FUTURE WORK
# ==========================================================

"future":{

"keywords":[
"future work",
"future improvements",
"next steps",
"future scope",
"extensions"
],

"answer":"""
Future improvements include:

• Live optimization
• Voice-controlled assistant
• Interactive warehouse maps
• Automatic report generation
• Real-time SAP integration
• Multi-objective optimization
• Predictive demand forecasting
• Explainable AI recommendations
"""
},

# ==========================================================
# TROUBLESHOOTING
# ==========================================================

"troubleshooting":{

"keywords":[
"error",
"problem",
"bug",
"issue",
"not working",
"troubleshoot",
"fix"
],

"answer":"""
If something isn't working:

• Check the uploaded data.
• Verify inventory values.
• Ensure required columns exist.
• Restart the Streamlit app.
• Review error messages in the terminal.
• Confirm optimization completed successfully before viewing analytics.
"""
},

# ==========================================================
# PRESENTATION
# ==========================================================

"presentation":{

"keywords":[
"presentation",
"ppt",
"slides",
"presentation summary",
"judge presentation"
],

"answer":"""
For presentations, focus on:

• Business problem
• Mathematical formulation
• Classical baseline
• Quantum approach
• Results comparison
• Dashboard demonstration
• Business impact
• Future improvements
"""
},
# ==========================================================
# ORDER ASSIGNMENT
# ==========================================================

"order_assignment":{

"keywords":[
"order assignment",
"assign orders",
"warehouse assignment",
"how orders are assigned",
"order allocation",
"allocation logic"
],

"answer":"""
Each customer order is evaluated against all available warehouses.

The optimizer considers:

• Inventory availability
• Warehouse capacity
• Shipping cost
• Penalty cost
• Revenue
• Business constraints

The warehouse with the best feasible score is selected.
"""
},

# ==========================================================
# INVENTORY CHECK
# ==========================================================

"inventory_check":{

"keywords":[
"inventory check",
"inventory availability",
"stock availability",
"available stock",
"stock check"
],

"answer":"""
Before assigning an order, Qora verifies whether the warehouse has sufficient inventory.

Warehouses without enough stock are automatically excluded from consideration.
"""
},

# ==========================================================
# CUSTOMER DEMAND
# ==========================================================

"demand":{

"keywords":[
"demand",
"customer demand",
"demand forecast",
"demand planning",
"market demand"
],

"answer":"""
Customer demand represents the quantity of products requested by customers.

The optimizer attempts to satisfy maximum demand while minimizing logistics cost.
"""
},

# ==========================================================
# OPTIMIZATION
# ==========================================================

"optimization":{

"keywords":[
"optimization",
"optimize",
"optimization process",
"how optimization works"
],

"answer":"""
Optimization is the process of finding the best warehouse allocation while satisfying all business constraints.

The objective is to maximize business value while reducing operational costs.
"""
},

# ==========================================================
# BUSINESS BENEFITS
# ==========================================================

"business_benefits":{

"keywords":[
"business benefits",
"benefits",
"advantages",
"why use this project",
"business value"
],

"answer":"""
Business benefits include:

• Higher customer satisfaction
• Better warehouse utilization
• Reduced logistics cost
• Lower penalties
• Increased revenue
• Faster planning
• Better operational decisions
"""
},

# ==========================================================
# NESTLE
# ==========================================================

"nestle":{

"keywords":[
"nestle",
"nestlé",
"why nestle",
"nestle use case"
],

"answer":"""
Nestlé operates a large global supply chain with multiple factories and warehouses.

Distributed Order Management helps determine the best fulfillment location for every customer order while reducing cost and improving service.
"""
},

# ==========================================================
# QUANTUM ADVANTAGE
# ==========================================================

"quantum_advantage":{

"keywords":[
"quantum advantage",
"benefits of quantum",
"why quantum optimization",
"future of quantum"
],

"answer":"""
Quantum optimization has the potential to solve certain large combinatorial optimization problems more efficiently than classical methods.

Although current hardware is limited, it represents a promising direction for future supply chain optimization.
"""
},

# ==========================================================
# KPI
# ==========================================================

"kpi":{

"keywords":[
"kpi",
"key performance indicators",
"performance metrics",
"metrics",
"important metrics"
],

"answer":"""
Important KPIs in this project include:

• Fill Rate
• Revenue
• Shipping Cost
• Penalty Cost
• Runtime
• Warehouse Utilization
• Carbon Emissions
• Risk Score
"""
},

# ==========================================================
# JUDGE QUESTION
# ==========================================================

"judge_question":{

"keywords":[
"why should we choose your project",
"why this project",
"what makes this project unique",
"innovation",
"novelty"
],

"answer":"""
This project combines business optimization with quantum-inspired techniques and an interactive AI assistant.

It provides explainable recommendations, business dashboards, benchmarking, scalability discussion, and can be extended to real-time enterprise systems such as SAP and SQL databases.
"""
},

# ==========================================================
# EXPLAIN ALL GRAPHS
# ==========================================================

"graphs":{

"keywords":[
"explain graph",
"explain graphs",
"all graphs",
"dashboard graphs",
"charts"
],

"answer":"""
The dashboard includes:

• Revenue Trend – tracks revenue over time.
• Fill Rate Gauge – shows order fulfillment percentage.
• Warehouse Utilization – shows warehouse workload.
• Capacity Utilization – shows warehouse capacity usage.
• Shipping Cost – compares logistics costs.
• Carbon Emissions – estimates environmental impact.
• Risk Score – highlights overloaded warehouses.
• Benchmark Report – compares Classical and Quantum optimization.
• Sensitivity Analysis – evaluates different business scenarios.
"""
},

# ==========================================================
# SUPPLY CHAIN
# ==========================================================

"supply_chain":{

"keywords":[
"supply chain",
"logistics",
"supply network",
"distribution",
"distribution network",
"fulfillment network",
"warehouse network"
],

"answer":"""
A supply chain is the complete network involved in producing, storing and delivering products.

This project improves supply chain efficiency by selecting the best warehouse for every customer order while reducing cost and improving service levels.
"""
},

# ==========================================================
# DISTRIBUTED ORDER MANAGEMENT BENEFITS
# ==========================================================

"dom_benefits":{

"keywords":[
"benefits of dom",
"advantages of dom",
"why distributed order management",
"importance of dom"
],

"answer":"""
Distributed Order Management provides several benefits:

• Faster order fulfillment
• Better inventory utilization
• Lower transportation costs
• Higher customer satisfaction
• Reduced stock shortages
• Improved warehouse balancing
• Better business decisions
"""
},

# ==========================================================
# INVENTORY OPTIMIZATION
# ==========================================================

"inventory_optimization":{

"keywords":[
"inventory optimization",
"inventory planning",
"stock optimization",
"inventory management"
],

"answer":"""
Inventory optimization ensures products are available where they are needed while minimizing excess stock.

The optimizer considers inventory availability before assigning customer orders.
"""
},

# ==========================================================
# CUSTOMER SATISFACTION
# ==========================================================

"customer_satisfaction":{

"keywords":[
"customer satisfaction",
"customer experience",
"service quality",
"happy customers"
],

"answer":"""
Higher fill rates, faster delivery and lower delays improve customer satisfaction.

The optimization model is designed to maximize service quality while minimizing operational costs.
"""
},

# ==========================================================
# ORDER FULFILLMENT
# ==========================================================

"order_fulfillment":{

"keywords":[
"order fulfillment",
"fulfillment",
"fulfill order",
"order processing"
],

"answer":"""
Order fulfillment is the complete process of receiving, processing and delivering customer orders.

Qora recommends the best warehouse to fulfill each order efficiently.
"""
},

# ==========================================================
# MULTI OBJECTIVE OPTIMIZATION
# ==========================================================

"multi_objective":{

"keywords":[
"multi objective",
"multi objective optimization",
"multiple objectives",
"optimization objectives"
],

"answer":"""
This project optimizes multiple business objectives simultaneously, including:

• Maximizing revenue
• Maximizing fill rate
• Minimizing shipping cost
• Minimizing penalty cost
• Balancing warehouse utilization
"""
},

# ==========================================================
# DECISION SUPPORT
# ==========================================================

"decision_support":{

"keywords":[
"decision support",
"business decision",
"planner decision",
"decision making"
],

"answer":"""
Qora acts as a decision support system.

Instead of replacing planners, it provides optimized recommendations that help planners make faster and better business decisions.
"""
},

# ==========================================================
# EXPLAINABLE AI
# ==========================================================

"explainable_ai":{

"keywords":[
"explainable ai",
"xai",
"why was this warehouse selected",
"explain recommendation",
"why this result"
],

"answer":"""
Qora provides explainable recommendations.

Instead of only showing the selected warehouse, it explains why the warehouse was chosen based on inventory, capacity, revenue, shipping cost and business constraints.
"""
},

# ==========================================================
# DIGITAL TWIN
# ==========================================================

"digital_twin":{

"keywords":[
"digital twin",
"simulation",
"virtual warehouse",
"digital model"
],

"answer":"""
A Digital Twin is a virtual representation of the supply chain.

The optimization dashboard can act as a digital twin by simulating warehouse operations before implementing real-world decisions.
"""
},

# ==========================================================
# AI FEATURES
# ==========================================================

"ai_features":{

"keywords":[
"ai features",
"what can qora do",
"features",
"assistant features",
"capabilities"
],

"answer":"""
Qora AI can:

• Answer project questions
• Explain every dashboard graph
• Explain optimization concepts
• Compare Classical vs Quantum
• Generate planner summaries
• Provide recommendations
• Explain KPIs
• Support future real-time integrations
• Assist during project presentations
"""
},

# ==========================================================
# DEMAND FORECASTING
# ==========================================================

"demand_forecasting":{

"keywords":[
"demand forecasting",
"forecast",
"future demand",
"predict demand",
"demand prediction",
"forecasting"
],

"answer":"""
Demand Forecasting predicts future customer demand using historical sales and trends.

Accurate demand forecasts help maintain optimal inventory, reduce stock shortages, and improve warehouse planning.
"""
},

# ==========================================================
# ROUTE OPTIMIZATION
# ==========================================================

"route_optimization":{

"keywords":[
"route optimization",
"best route",
"delivery route",
"routing",
"transport route",
"shipping route"
],

"answer":"""
Route Optimization finds the most efficient delivery path between warehouses and customers.

Optimized routes reduce transportation costs, delivery time and carbon emissions.
"""
},

# ==========================================================
# WAREHOUSE SELECTION
# ==========================================================

"warehouse_selection":{

"keywords":[
"why plant selected",
"why warehouse selected",
"selected warehouse",
"warehouse selection",
"best warehouse",
"which warehouse"
],

"answer":"""
The warehouse is selected using optimization.

Selection depends on:

• Inventory availability
• Capacity
• Shipping cost
• Penalty cost
• Revenue
• Distance
• Business constraints

The warehouse with the highest overall business value is recommended.
"""
},

# ==========================================================
# DISTANCE
# ==========================================================

"distance":{

"keywords":[
"distance",
"shipping distance",
"delivery distance",
"warehouse distance",
"travel distance"
],

"answer":"""
Distance affects transportation cost, delivery time and carbon emissions.

Shorter delivery distances generally lead to lower operational costs and faster customer service.
"""
},

# ==========================================================
# LOGISTICS COST
# ==========================================================

"logistics_cost":{

"keywords":[
"logistics cost",
"transport cost",
"distribution cost",
"operational cost",
"freight cost"
],

"answer":"""
Logistics Cost includes transportation, handling, warehouse operations and delivery expenses.

Reducing logistics cost is one of the primary objectives of this optimization model.
"""
},

# ==========================================================
# DELIVERY TIME
# ==========================================================

"delivery_time":{

"keywords":[
"delivery time",
"delivery days",
"estimated delivery",
"shipping time",
"transit time"
],

"answer":"""
Delivery Time represents the estimated number of days required to deliver an order.

The optimizer attempts to minimize delivery time while satisfying business constraints.
"""
},

# ==========================================================
# BUSINESS IMPACT
# ==========================================================

"business_impact":{

"keywords":[
"business impact",
"project impact",
"business value",
"impact",
"benefits to company"
],

"answer":"""
This project improves business performance by:

• Increasing revenue
• Improving customer satisfaction
• Reducing shipping costs
• Lowering penalty costs
• Improving warehouse utilization
• Supporting data-driven decisions
"""
},

# ==========================================================
# WHY AI
# ==========================================================

"why_ai":{

"keywords":[
"why ai",
"why use ai",
"artificial intelligence",
"importance of ai",
"ai benefits"
],

"answer":"""
AI helps automate decision making by analyzing multiple business factors simultaneously.

It provides faster, more consistent and data-driven recommendations than manual planning.
"""
},

# ==========================================================
# HYBRID OPTIMIZATION
# ==========================================================

"hybrid":{

"keywords":[
"hybrid optimization",
"hybrid quantum",
"classical and quantum",
"hybrid algorithm"
],

"answer":"""
Hybrid Optimization combines classical optimization with quantum-inspired techniques.

This approach leverages the strengths of both methods and is practical with today's quantum technology.
"""
},

# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

"executive_summary":{

"keywords":[
"executive summary",
"management summary",
"project summary for manager",
"brief summary",
"overall summary"
],

"answer":"""
Executive Summary

• AI-powered Distributed Order Management system.
• Optimizes warehouse selection.
• Compares Classical and Quantum-inspired optimization.
• Improves revenue and fill rate.
• Reduces shipping and penalty costs.
• Provides explainable AI recommendations.
• Ready for future real-time enterprise integration.
"""
},

# ==========================================================
# PROJECT FEATURES
# ==========================================================

"project_features":{

"keywords":[
"features",
"project features",
"all features",
"dashboard features",
"system features"
],

"answer":"""
Major Features:

• Dashboard
• Analytics
• Order Explorer
• AI Assistant (Qora)
• Benchmark Comparison
• Carbon Emission Analysis
• Risk Analysis
• What-if Analysis
• Batch Optimization
• Split Fulfillment
• SLA Monitoring
• Planner Recommendations
• Explainable AI
• Real-time Ready Architecture
"""
},

# ==========================================================
# PROJECT CONCLUSION
# ==========================================================

"conclusion":{

"keywords":[
"conclusion",
"project conclusion",
"final conclusion",
"summary conclusion"
],

"answer":"""
The project demonstrates how AI and optimization can improve Distributed Order Management.

It combines optimization algorithms, business analytics and an intelligent assistant to support warehouse planning, reduce costs and improve customer satisfaction while remaining scalable for future enterprise deployment.
"""
},
# ==========================================================
# FILL RATE CALCULATION
# ==========================================================

"fill_rate_calculation":{

"keywords":[
"how fill rate calculated",
"fill rate formula",
"calculate fill rate",
"fill rate equation",
"fill rate computation"
],

"answer":"""
Fill Rate (%) =

(Fulfilled Orders / Total Orders) × 100

Example:

Total Orders = 100

Fulfilled Orders = 94

Fill Rate = 94%
"""
},

# ==========================================================
# REVENUE CALCULATION
# ==========================================================

"revenue_calculation":{

"keywords":[
"revenue formula",
"calculate revenue",
"revenue calculation",
"how revenue calculated"
],

"answer":"""
Total Revenue is calculated as the sum of revenue generated from all fulfilled orders.

Revenue = Σ(Order Revenue)

The optimizer attempts to maximize total revenue while minimizing operational costs.
"""
},

# ==========================================================
# PENALTY CALCULATION
# ==========================================================

"penalty_calculation":{

"keywords":[
"penalty formula",
"penalty calculation",
"how penalty calculated",
"calculate penalty"
],

"answer":"""
Penalty Cost is applied when customer demand cannot be fulfilled.

Penalty =

(Number of Unfulfilled Orders × Penalty Value)

Lower penalty indicates better optimization performance.
"""
},

# ==========================================================
# SHIPPING COST CALCULATION
# ==========================================================

"shipping_calculation":{

"keywords":[
"shipping formula",
"shipping cost calculation",
"logistics formula",
"transport cost calculation"
],

"answer":"""
Shipping Cost depends on:

• Distance
• Transportation rate
• Number of products
• Warehouse location

The optimizer minimizes total shipping cost while satisfying all constraints.
"""
},

# ==========================================================
# WHY STREAMLIT
# ==========================================================

"streamlit":{

"keywords":[
"streamlit",
"why streamlit",
"dashboard framework",
"python dashboard"
],

"answer":"""
Streamlit is used because it enables rapid development of interactive dashboards entirely in Python.

It supports charts, KPIs, tables, filters and AI interfaces without requiring web development expertise.
"""
},

# ==========================================================
# WHY PYTHON
# ==========================================================

"python":{

"keywords":[
"why python",
"python language",
"python benefits",
"why use python"
],

"answer":"""
Python provides powerful libraries for optimization, machine learning, data analysis and visualization.

Its ecosystem makes it ideal for supply chain optimization and AI applications.
"""
},

# ==========================================================
# LIBRARIES
# ==========================================================

"libraries":{

"keywords":[
"libraries",
"python libraries",
"used libraries",
"dependencies",
"technology stack"
],

"answer":"""
Major libraries used include:

• Pandas
• NumPy
• Plotly
• Streamlit
• OR-Tools
• Matplotlib
• Seaborn
• Scikit-learn (future)
"""
},

# ==========================================================
# WHY PLOTLY
# ==========================================================

"plotly":{

"keywords":[
"plotly",
"why plotly",
"interactive charts",
"plotly graphs"
],

"answer":"""
Plotly provides interactive visualizations including zooming, filtering, tooltips and dynamic dashboards.

It is ideal for business analytics applications.
"""
},

# ==========================================================
# PROJECT ARCHITECTURE
# ==========================================================

"architecture":{

"keywords":[
"architecture",
"system architecture",
"project architecture",
"workflow",
"design"
],

"answer":"""
Project Architecture:

User Data
↓

Data Preprocessing
↓

Optimization Engine

↓

Business Rules

↓

Analytics Engine

↓

Dashboard

↓

Qora AI Assistant
"""
},

# ==========================================================
# WORKFLOW
# ==========================================================

"workflow":{

"keywords":[
"workflow",
"process flow",
"how project works",
"execution flow",
"pipeline"
],

"answer":"""
Workflow:

1. Load order data
2. Validate inventory
3. Apply optimization
4. Generate recommendations
5. Create analytics
6. Display dashboard
7. Answer user questions through Qora AI
"""
},

# ==========================================================
# WHY THIS PROJECT
# ==========================================================

"why_project":{

"keywords":[
"why this project",
"problem statement",
"business problem",
"what problem does it solve"
],

"answer":"""
This project solves warehouse selection challenges in Distributed Order Management.

Instead of manually assigning warehouses, optimization automatically selects the best fulfillment center based on business objectives and operational constraints.
"""
},

# ==========================================================
# PROJECT LIMITATIONS
# ==========================================================

"limitations":{

"keywords":[
"limitations",
"project limitations",
"constraints of project",
"current limitations"
],

"answer":"""
Current limitations include:

• Sample dataset
• Simulated quantum comparison
• Static CSV input
• Estimated shipping cost
• Simulated carbon emissions

Future versions will support real enterprise data and live optimization.
"""
},

# ==========================================================
# PROJECT ACHIEVEMENTS
# ==========================================================

"achievements":{

"keywords":[
"achievements",
"project achievements",
"results",
"success",
"what achieved"
],

"answer":"""
Project Achievements:

• AI-powered DOM dashboard
• Optimization engine
• Classical vs Quantum benchmark
• Explainable AI
• Interactive analytics
• Carbon analysis
• Risk analysis
• Planner recommendations
• Offline Qora AI assistant
• Real-time ready architecture
"""
},

# ==========================================================
# INVENTORY
# ==========================================================

"inventory":{

"keywords":[
"inventory",
"stock",
"warehouse stock",
"available inventory",
"inventory management",
"inventory availability",
"product stock"
],

"answer":"""
Inventory represents the available quantity of products in each warehouse.

Before assigning an order, the optimizer checks whether sufficient inventory is available.

This prevents stock shortages and ensures feasible warehouse assignments.
"""
},

# ==========================================================
# WAREHOUSE CAPACITY
# ==========================================================

"warehouse_capacity":{

"keywords":[
"warehouse capacity",
"capacity",
"capacity limit",
"maximum capacity",
"plant capacity"
],

"answer":"""
Warehouse Capacity defines the maximum number of orders or products that a warehouse can handle.

The optimizer ensures no warehouse exceeds its capacity while assigning orders.
"""
},

# ==========================================================
# CUSTOMER DEMAND
# ==========================================================

"customer_demand":{

"keywords":[
"customer demand",
"demand",
"order demand",
"market demand",
"demand quantity"
],

"answer":"""
Customer Demand is the quantity of products requested by customers.

The objective of Distributed Order Management is to satisfy as much demand as possible while minimizing operational cost.
"""
},

# ==========================================================
# ORDER PRIORITY
# ==========================================================

"order_priority":{

"keywords":[
"priority",
"order priority",
"high priority order",
"urgent order",
"priority orders"
],

"answer":"""
Order Priority determines which orders should be fulfilled first.

Priority may depend on customer importance, delivery deadlines, product value or business rules.

Higher-priority orders receive preference during optimization.
"""
},

# ==========================================================
# CUSTOMER SATISFACTION
# ==========================================================

"customer_satisfaction":{

"keywords":[
"customer satisfaction",
"customer experience",
"satisfaction",
"service quality"
],

"answer":"""
Customer Satisfaction improves when:

• Orders are delivered on time.
• Products are available.
• Delivery delays are minimized.
• Fill Rate is high.

The optimization model aims to improve customer satisfaction through better warehouse decisions.
"""
},

# ==========================================================
# DEMAND SPIKE
# ==========================================================

"demand_spike":{

"keywords":[
"demand spike",
"high demand",
"peak demand",
"seasonal demand",
"demand increase"
],

"answer":"""
Demand Spike refers to a sudden increase in customer orders.

The optimizer redistributes orders across warehouses to maintain service levels during peak demand periods.
"""
},

# ==========================================================
# OVERLOADED WAREHOUSE
# ==========================================================

"overloaded_warehouse":{

"keywords":[
"overloaded warehouse",
"warehouse overload",
"busy warehouse",
"high utilization warehouse"
],

"answer":"""
An overloaded warehouse is operating close to or above its capacity.

This can lead to delivery delays, increased operational risk and reduced service quality.

The optimizer attempts to balance workload across warehouses.
"""
},

# ==========================================================
# UNDERUTILIZED WAREHOUSE
# ==========================================================

"underutilized_warehouse":{

"keywords":[
"underutilized warehouse",
"low utilization",
"idle warehouse",
"unused warehouse"
],

"answer":"""
An underutilized warehouse handles fewer orders than its available capacity.

Balanced utilization improves efficiency and reduces unnecessary operational costs.
"""
},

# ==========================================================
# SHIPPING ROUTE
# ==========================================================

"shipping_route":{

"keywords":[
"shipping route",
"delivery route",
"transport route",
"route selection"
],

"answer":"""
Shipping Routes connect warehouses to customers.

Efficient routes reduce transportation cost, delivery time and carbon emissions.

Future versions of the project can display these routes on an interactive map.
"""
},

# ==========================================================
# REAL-TIME DATA
# ==========================================================

"real_time_data":{

"keywords":[
"real time",
"live data",
"real-time data",
"dynamic data",
"live updates",
"automatic refresh"
],

"answer":"""
The current project reads data from CSV files.

The architecture is designed so the same optimization engine can later connect to:

• SAP
• SQL Database
• REST APIs
• Excel uploads
• Live IoT systems

This makes the solution ready for real-time enterprise deployment.
"""
},

# ==========================================================
# EXPLAINABLE AI
# ==========================================================

"explainable_ai":{

"keywords":[
"explainable ai",
"xai",
"why selected",
"explain decision",
"decision explanation"
],

"answer":"""
Explainable AI helps users understand why a warehouse was selected.

Instead of providing only a recommendation, Qora explains the business reasons such as inventory, capacity, revenue and shipping cost.

This increases user trust and transparency.
"""
},

# ==========================================================
# DIGITAL TWIN
# ==========================================================

"digital_twin":{

"keywords":[
"digital twin",
"simulation",
"virtual warehouse",
"warehouse simulation"
],

"answer":"""
A Digital Twin is a virtual representation of warehouse operations.

Although not fully implemented, the project architecture can support future digital twin simulations for testing warehouse strategies before real deployment.
"""
},

# ==========================================================
# OR-TOOLS
# ==========================================================

"or_tools_advanced":{

"keywords":[
"or tools",
"google or tools",
"operations research",
"cp sat",
"solver",
"optimization solver",
"how does or-tools work"
],

"answer":"""
Google OR-Tools is an optimization library developed by Google.

In this project it solves the warehouse allocation problem while satisfying business constraints such as inventory, warehouse capacity and customer demand.

It searches millions of possible assignments and returns the best feasible solution.
"""
},

# ==========================================================
# QAOA
# ==========================================================

"qaoa_advanced":{

"keywords":[
"qaoa",
"quantum approximate optimization algorithm",
"how qaoa works",
"quantum optimization algorithm"
],

"answer":"""
QAOA (Quantum Approximate Optimization Algorithm) is a quantum algorithm designed for combinatorial optimization problems.

It alternates between cost and mixer operators to gradually improve the probability of finding high-quality solutions.

Although current quantum hardware is limited, QAOA is considered one of the most promising optimization algorithms.
"""
},

# ==========================================================
# QUANTUM COMPUTING
# ==========================================================

"quantum_computing":{

"keywords":[
"quantum computing",
"quantum computer",
"what is quantum",
"qubits",
"quantum technology"
],

"answer":"""
Quantum computing uses qubits instead of classical bits.

Unlike classical bits, qubits can exist in multiple states simultaneously using superposition.

This allows quantum algorithms to explore many possible solutions more efficiently for certain optimization problems.
"""
},

# ==========================================================
# SUPERPOSITION
# ==========================================================

"superposition":{

"keywords":[
"superposition",
"quantum superposition",
"what is superposition"
],

"answer":"""
Superposition allows a qubit to exist in multiple states at the same time.

This is one of the key principles that gives quantum computing its computational potential.
"""
},

# ==========================================================
# ENTANGLEMENT
# ==========================================================

"entanglement":{

"keywords":[
"entanglement",
"quantum entanglement",
"what is entanglement"
],

"answer":"""
Quantum entanglement links two or more qubits together.

Changing the state of one entangled qubit influences the other, enabling powerful quantum computations.
"""
},

# ==========================================================
# QUBITS
# ==========================================================

"qubits":{

"keywords":[
"qubit",
"qubits",
"what is qubit"
],

"answer":"""
A qubit is the basic unit of quantum information.

Unlike a classical bit (0 or 1), a qubit can represent both states simultaneously through superposition.
"""
},

# ==========================================================
# CLASSICAL VS QUANTUM
# ==========================================================

"classical_vs_quantum":{

"keywords":[
"classical vs quantum",
"difference between classical and quantum",
"classical optimization",
"quantum optimization"
],

"answer":"""
Classical Optimization:
• Mature and reliable
• Fast for small and medium problems

Quantum-inspired Optimization:
• Promising for very large optimization problems
• Explores many possible solutions
• Future-ready technology

This project compares both approaches to evaluate their business performance.
"""
},

# ==========================================================
# WHY QORA
# ==========================================================

"why_qora":{

"keywords":[
"why qora",
"what is qora",
"why did you build qora",
"purpose of qora"
],

"answer":"""
Qora was developed as an intelligent assistant for the Distributed Order Management project.

It helps users understand optimization results, explain graphs, answer technical questions, generate summaries and guide decision-making through a conversational interface.
"""
},

# ==========================================================
# PROJECT INNOVATION
# ==========================================================

"innovation":{

"keywords":[
"innovation",
"unique feature",
"what is innovative",
"project innovation"
],

"answer":"""
Key innovations include:

• AI-powered project assistant (Qora)
• Explainable optimization
• Classical vs Quantum benchmarking
• Interactive analytics dashboard
• Future-ready real-time architecture
• Business-focused recommendations
"""
},

# ==========================================================
# FINAL SUMMARY
# ==========================================================

"final_summary":{

"keywords":[
"final summary",
"overall project",
"complete summary",
"summarize everything"
],

"answer":"""
This project combines AI, optimization and business analytics to improve Distributed Order Management.

It automatically recommends the best warehouse for each order, explains every decision through Qora AI, provides interactive dashboards and is designed for future enterprise deployment with live data integration.
"""
},

# ==========================================================
# JUDGE QUESTIONS
# ==========================================================

"judge_q1":{

"keywords":[
"why should we choose your project",
"why choose this project",
"what makes your project unique",
"why is your project better"
],

"answer":"""
This project combines AI, Operations Research and Quantum-inspired Optimization into one business-ready solution.

Unlike traditional dashboards, it not only optimizes warehouse selection but also explains every decision through Qora AI, making it easier for planners and business users to understand and trust the recommendations.
"""
},

# ==========================================================
# JUDGE QUESTIONS
# ==========================================================

"judge_q2":{

"keywords":[
"why did you use quantum",
"why quantum",
"why qaoa",
"importance of quantum"
],

"answer":"""
Supply chain optimization is a combinatorial optimization problem.

Quantum-inspired algorithms such as QAOA are designed for these types of problems and represent a promising direction for solving larger optimization challenges in the future.
"""
},

# ==========================================================
# JUDGE QUESTIONS
# ==========================================================

"judge_q3":{

"keywords":[
"why ai assistant",
"why qora",
"why chatbot",
"importance of chatbot"
],

"answer":"""
Qora makes the dashboard interactive.

Instead of searching manually through reports, users can ask questions in natural language, receive explanations, summaries and business recommendations instantly.
"""
},

# ==========================================================
# BUSINESS VALUE
# ==========================================================

"business_value":{

"keywords":[
"business value",
"value",
"roi",
"return on investment",
"company benefits"
],

"answer":"""
Business Value includes:

• Higher Fill Rate
• Lower Shipping Cost
• Better Warehouse Utilization
• Reduced Penalty Cost
• Faster Planning
• Better Customer Satisfaction
• Lower Carbon Emissions
• Data-driven Decision Making
"""
},

# ==========================================================
# WHY OFFLINE AI
# ==========================================================

"offline_ai":{

"keywords":[
"offline ai",
"offline chatbot",
"without internet",
"local ai"
],

"answer":"""
The current version of Qora works completely offline using a built-in knowledge base.

This ensures fast responses, no internet dependency and reliable demonstrations.

The architecture can later be connected to cloud-based Large Language Models if required.
"""
},

# ==========================================================
# SECURITY
# ==========================================================

"security":{

"keywords":[
"security",
"data security",
"privacy",
"secure data",
"enterprise security"
],

"answer":"""
Enterprise deployments can protect business data using:

• User authentication
• Role-based access
• Database encryption
• Secure APIs
• HTTPS communication
• Audit logs

These features help protect sensitive operational information.
"""
},

# ==========================================================
# SCALABLE ARCHITECTURE
# ==========================================================

"architecture_scalability":{

"keywords":[
"architecture scalability",
"scalable architecture",
"large company",
"enterprise deployment"
],

"answer":"""
The project follows a modular architecture.

Components such as the optimization engine, analytics dashboard and Qora AI can be independently extended, making the system suitable for larger enterprise deployments.
"""
},

# ==========================================================
# CLOUD DEPLOYMENT
# ==========================================================

"cloud":{

"keywords":[
"cloud",
"aws",
"azure",
"google cloud",
"deployment",
"cloud deployment"
],

"answer":"""
The application can be deployed on cloud platforms such as AWS, Microsoft Azure or Google Cloud.

Cloud deployment enables multi-user access, scalability and integration with enterprise databases.
"""
},

# ==========================================================
# PERFORMANCE
# ==========================================================

"performance":{

"keywords":[
"performance",
"system performance",
"optimization performance",
"speed"
],

"answer":"""
Performance depends on:

• Number of orders
• Number of warehouses
• Number of products
• Optimization algorithm
• Available computing resources

Efficient optimization enables planners to make faster operational decisions.
"""
},

# ==========================================================
# FAQ
# ==========================================================

"faq":{

"keywords":[
"faq",
"help",
"support",
"common questions",
"documentation"
],

"answer":"""
Frequently Asked Questions:

• What is Distributed Order Management?
• How does optimization work?
• Why was this warehouse selected?
• What is Fill Rate?
• What is QAOA?
• What is OR-Tools?
• Can the project use live data?
• Can it connect to SAP?
• Can it generate reports?
• Can Qora explain graphs?

Qora is designed to answer all of these directly.
"""
},

# ==========================================================
# MACHINE LEARNING
# ==========================================================

"machine_learning":{

"keywords":[
"machine learning",
"ml",
"artificial intelligence",
"ai model",
"predictive model",
"learning model"
],

"answer":"""
Machine Learning enables systems to learn patterns from historical data.

In future versions of this project, ML can be used for:

• Demand Forecasting
• Inventory Prediction
• Delay Prediction
• Risk Prediction
• Customer Demand Analysis
"""
},

# ==========================================================
# DEMAND PREDICTION
# ==========================================================

"demand_prediction":{

"keywords":[
"predict demand",
"demand prediction",
"future demand",
"forecast demand",
"predict orders"
],

"answer":"""
Demand Prediction estimates future customer orders using historical sales data.

Better predictions help reduce stock shortages and improve warehouse planning.
"""
},

# ==========================================================
# INVENTORY FORECASTING
# ==========================================================

"inventory_forecasting":{

"keywords":[
"inventory forecasting",
"future inventory",
"stock prediction",
"inventory prediction"
],

"answer":"""
Inventory Forecasting estimates future inventory requirements.

It helps businesses maintain enough stock while avoiding unnecessary inventory costs.
"""
},

# ==========================================================
# DELAY PREDICTION
# ==========================================================

"delay_prediction":{

"keywords":[
"delay prediction",
"late delivery",
"delivery delay",
"predict delay"
],

"answer":"""
Delay Prediction identifies orders that are likely to miss delivery deadlines.

This allows planners to take preventive actions before delays occur.
"""
},

# ==========================================================
# RISK PREDICTION
# ==========================================================

"risk_prediction":{

"keywords":[
"risk prediction",
"predict risk",
"future risk",
"warehouse risk prediction"
],

"answer":"""
Risk Prediction estimates operational risks using historical utilization and business trends.

High-risk warehouses can be identified before problems occur.
"""
},

# ==========================================================
# DEMO QUESTIONS
# ==========================================================

"demo_questions":{

"keywords":[
"sample questions",
"demo questions",
"what can i ask",
"help questions",
"example questions"
],

"answer":"""
Try asking Qora:

• What is Distributed Order Management?
• Explain QAOA.
• Explain OR-Tools.
• Explain Fill Rate.
• Explain Carbon Emissions.
• Explain Warehouse Utilization.
• Why was Plant 3 selected?
• Compare Classical vs Quantum.
• Summarize the project.
• Explain this dashboard.
• Explain this graph.
• What are the business benefits?
"""
},

# ==========================================================
# PROJECT TECHNOLOGIES
# ==========================================================

"technology_stack":{

"keywords":[
"technology stack",
"technologies",
"tools used",
"software used",
"frameworks"
],

"answer":"""
Technologies used include:

• Python
• Streamlit
• Pandas
• NumPy
• Plotly
• OR-Tools
• Matplotlib
• Seaborn

Future support:

• SQL
• SAP
• REST APIs
• Cloud Deployment
"""
},

# ==========================================================
# ENTERPRISE READINESS
# ==========================================================

"enterprise_ready":{

"keywords":[
"enterprise",
"production ready",
"enterprise ready",
"industrial deployment",
"company deployment"
],

"answer":"""
The project is designed with enterprise deployment in mind.

Future enhancements include:

• Live databases
• User authentication
• SAP integration
• Cloud deployment
• Automatic scheduling
• API integration
• Real-time optimization
"""
},

# ==========================================================
# AI RECOMMENDATIONS
# ==========================================================

"ai_recommendations":{

"keywords":[
"recommend warehouse",
"recommendation",
"best warehouse",
"ai recommendation",
"suggest warehouse"
],

"answer":"""
Qora generates recommendations by analyzing:

• Inventory
• Capacity
• Revenue
• Shipping Cost
• Fill Rate
• Risk
• Carbon Emissions

It recommends the warehouse that provides the best overall business outcome.
"""
},

# ==========================================================
# PROJECT GOAL
# ==========================================================

"project_goal":{

"keywords":[
"goal",
"objective",
"main objective",
"project goal",
"aim"
],

"answer":"""
The main goal is to optimize Distributed Order Management by intelligently selecting the best warehouse for every customer order.

The solution aims to maximize revenue and fill rate while minimizing shipping costs, penalties, carbon emissions and operational risk.
"""
},

# ==========================================================
# THANK YOU
# ==========================================================

"thanks":{

"keywords":[
"thank you",
"thanks",
"good job",
"bye",
"goodbye",
"see you"
],

"answer":"""
You're welcome!

I'm Qora, your AI assistant for the Distributed Order Management project.

Feel free to ask me anything about the project, optimization, analytics, graphs or business concepts.
"""
},

# ==========================================================
# DASHBOARD FILTERS
# ==========================================================

"dashboard_filters":{

"keywords":[
"filters",
"dashboard filters",
"plant filter",
"warehouse filter",
"date filter",
"product filter"
],

"answer":"""
The dashboard provides interactive filters to explore optimization results.

Users can filter by:
• Warehouse
• Plant
• Product
• Customer
• Order Date
• Region

These filters help analyze specific business scenarios.
"""
},

# ==========================================================
# WHAT-IF ANALYSIS
# ==========================================================

"what_if_analysis":{

"keywords":[
"what if",
"what-if",
"scenario analysis",
"increase demand",
"decrease inventory",
"simulation"
],

"answer":"""
What-If Analysis allows planners to simulate different business conditions.

Examples:
• Increase demand by 20%
• Reduce warehouse capacity
• Increase shipping costs
• Inventory shortage

The optimizer recalculates recommendations for each scenario.
"""
},

# ==========================================================
# REPORT GENERATION
# ==========================================================

"reports":{

"keywords":[
"report",
"generate report",
"pdf report",
"planner report",
"executive report",
"powerpoint",
"ppt"
],

"answer":"""
Qora can generate different reports such as:

• Planner Summary
• Executive Summary
• PDF Report
• PowerPoint Presentation
• Optimization Results
• Business Recommendations

These reports help communicate optimization results to stakeholders.
"""
},

# ==========================================================
# DATA VALIDATION
# ==========================================================

"data_validation":{

"keywords":[
"validate data",
"data validation",
"missing values",
"incorrect data",
"data quality"
],

"answer":"""
Before optimization, the system validates the dataset.

It checks:
• Missing values
• Invalid warehouse IDs
• Negative inventory
• Duplicate orders
• Incorrect capacities

This ensures reliable optimization results.
"""
},

# ==========================================================
# OPTIMIZATION OBJECTIVE
# ==========================================================

"objective_function":{

"keywords":[
"objective function",
"optimization objective",
"goal function",
"objective equation"
],

"answer":"""
The optimization objective is to maximize overall business performance.

It considers:

• Maximize Revenue
• Maximize Fill Rate
• Minimize Shipping Cost
• Minimize Penalty Cost
• Balance Warehouse Utilization
• Reduce Carbon Emissions
"""
},

# ==========================================================
# BUSINESS CONSTRAINTS
# ==========================================================

"business_rules":{

"keywords":[
"business rules",
"business constraints",
"rules",
"optimization rules"
],

"answer":"""
Business constraints include:

• Inventory availability
• Warehouse capacity
• One warehouse per order
• Product availability
• Delivery requirements
• Operational policies

These ensure all recommendations are practical and feasible.
"""
},

# ==========================================================
# AI DECISION MAKING
# ==========================================================

"ai_decision":{

"keywords":[
"how does ai decide",
"decision making",
"ai decision",
"recommendation logic"
],

"answer":"""
Qora combines optimization results with business metrics.

It evaluates inventory, capacity, revenue, shipping cost, penalties, utilization and risk before recommending the most suitable warehouse.
"""
},

# ==========================================================
# EXPLAIN DASHBOARD
# ==========================================================

"dashboard_explanation":{

"keywords":[
"explain dashboard",
"dashboard overview",
"dashboard",
"what is on dashboard"
],

"answer":"""
The dashboard contains:

• KPIs
• Revenue Trend
• Fill Rate
• Warehouse Utilization
• Capacity Analysis
• Shipping Cost
• Carbon Emissions
• Risk Analysis
• Benchmark Comparison
• AI Recommendations
• Interactive Filters
"""
},

# ==========================================================
# PROJECT STRENGTHS
# ==========================================================

"project_strengths":{

"keywords":[
"strengths",
"advantages",
"best features",
"project strengths"
],

"answer":"""
Key strengths of the project are:

• AI-powered assistant
• Explainable recommendations
• Interactive dashboard
• Optimization engine
• Classical vs Quantum comparison
• Modular architecture
• Real-time ready design
• Business-focused analytics
"""
},

# ==========================================================
# FINAL MESSAGE
# ==========================================================

"about_qora":{

"keywords":[
"who are you",
"introduce yourself",
"about qora",
"your capabilities"
],

"answer":"""
Hello! I'm Qora, your AI assistant for the Distributed Order Management project.

I can help you by:

• Answering project questions
• Explaining optimization concepts
• Explaining dashboard charts
• Explaining business metrics
• Generating summaries
• Providing recommendations
• Supporting presentations
• Guiding users through the dashboard

I'm designed to make the project easier to understand and interact with.
"""
},

}

