# 📦 Quantum Optimization for Distributed Order Management (DOM)

## Executive Summary

This project presents a **Hybrid Classical + Quantum-inspired Distributed Order Management (DOM)** platform developed for the **WISER–Nestlé Optimization Challenge**.

The platform intelligently assigns customer orders to warehouses by combining optimization techniques with business constraints. It maximizes revenue, improves order fulfillment, balances warehouse workloads, reduces logistics costs, and provides explainable recommendations through an interactive dashboard.

Instead of making allocation decisions manually, the system evaluates every order using multiple operational factors such as inventory availability, shipping cost, warehouse capacity, delivery priority, penalties, and business value before selecting the most suitable fulfillment strategy.

---

# Problem Statement

Large companies like Nestlé receive thousands of customer orders every day.

Each order can potentially be fulfilled from multiple warehouses.

Choosing the wrong warehouse can lead to:

- High transportation costs
- Inventory shortages
- Warehouse overload
- Late deliveries
- Poor customer satisfaction
- Increased carbon emissions

Traditional rule-based assignment methods cannot always optimize these conflicting objectives simultaneously.

This project addresses that challenge by using optimization techniques to automatically generate better order allocation decisions.

---

# Project Objectives

The project aims to:

- Maximize order fulfillment
- Improve Fill Rate
- Maximize revenue
- Reduce logistics cost
- Reduce penalty costs
- Balance warehouse utilization
- Improve inventory utilization
- Generate explainable recommendations
- Prepare the workflow for future quantum optimization

---

# Solution Overview

The workflow consists of the following stages:

```
Customer Orders
        │
        ▼
Data Loading
        │
        ▼
Data Cleaning
        │
        ▼
Business Constraints
        │
        ▼
Classical Optimization
(OR-Tools)
        │
        ▼
Warehouse Selection
        │
        ▼
Performance Evaluation
        │
        ▼
Interactive Dashboard
        │
        ▼
Business Decision Support
```

---

# System Architecture

```
                 Customer Orders

                        │

                        ▼

               Data Preprocessing

                        │

                        ▼

            Constraint Generation

        Inventory
        Shipping Cost
        Penalty
        Capacity
        Priority

                        │

                        ▼

        Classical Optimization Engine

               (Google OR-Tools)

                        │

                        ▼

        Selected Warehouse Allocation

                        │

                        ▼

      Performance Evaluation Module

                        │

                        ▼

          Streamlit Dashboard

                        │

                        ▼

      Planner Decision Support
```

---

# Dataset

The project uses operational logistics data containing:

- Plant
- Material Number
- Order Quantity
- Inventory
- Shipping Cost
- Revenue
- Warehouse Capacity
- Delivery Priority
- Penalty Cost
- Fill Rate Threshold
- Risk Score
- Carbon Emissions

These attributes are used to optimize warehouse allocation.

---

# Optimization Approach

The optimization engine evaluates each order using business constraints.

Objective:

- Maximize revenue
- Maximize fulfilled orders
- Minimize shipping cost
- Minimize penalties
- Balance warehouse utilization

Constraints include:

- Inventory availability
- Warehouse capacity
- Delivery priority
- Fill rate requirements
- Logistics limitations

---

# Classical Optimization

The current implementation uses **Google OR-Tools**.

OR-Tools solves the warehouse assignment problem using mathematical optimization while satisfying all operational constraints.

The optimizer selects the best warehouse for every order.

---

# Quantum Optimization

The architecture has been designed to support future quantum optimization using **Qiskit**.

The future implementation can replace the classical optimizer with algorithms such as:

- QAOA
- Quantum Annealing
- Hybrid Quantum-Classical Optimization

This enables scalability for increasingly complex optimization problems.

---

# Dashboard Features

The Streamlit dashboard provides:

### KPI Dashboard

- Total Orders
- Selected Orders
- Revenue
- Fill Rate

### Analytics

- Revenue Trend
- Warehouse Utilization
- Capacity Utilization
- Shipping Cost Analysis
- Risk Score
- Carbon Emission Analysis

### Simulations

- What-if Analysis
- Batch Optimization
- Split Fulfillment
- SLA Analysis
- Sensitivity Analysis

### Reports

- Benchmark Report
- Planner Decision Summary
- Automated Alerts
- Explainable Recommendations

### AI Assistant

Qora AI answers questions about:

- Distributed Order Management
- Optimization
- OR-Tools
- QAOA
- Fill Rate
- Business Metrics

---

# Business Benefits

The solution provides measurable business value:

- Higher order fulfillment
- Increased revenue
- Better warehouse utilization
- Lower logistics cost
- Reduced penalties
- Improved customer satisfaction
- Better planner decision support
- Sustainability through carbon emission estimation

---

# Technology Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Data Processing | Pandas |
| Visualization | Plotly |
| Optimization | Google OR-Tools |
| Quantum (Future Ready) | Qiskit |
| Programming Language | Python |

---

# Installation

```bash
git clone https://github.com/Sakethram2005/Nestle-DOM-Optimization

pip install -r requirements.txt

# Generates/refreshes data/quantum_result_cache.json (takes a few minutes —
# includes a 10-run QAOA reliability check)
python quantum_optimizer.py

# Prints the full-scale and reassignment benchmark tables
python benchmark.py

# Launches the dashboard
streamlit run streamlit_app.py
```

---

# Future Enhancements

- Real QAOA optimization using Qiskit
- Live ERP integration
- Demand forecasting using AI
- Vehicle Routing Optimization
- Digital Twin for warehouse simulation
- Multi-objective quantum optimization
- Cloud deployment with IBM Quantum Runtime

---

# Authors

**Bushra Faizi Shaik**
B.Tech – Artificial Intelligence & Machine Learning  
Hindu College of Engineering & Technology

**Pavan Kumar**
B.Tech – ECE  
Hindu College of Engineering & Technology

**Thammandra Saketh Ram**
B.Tech – DSAI  
IIT Bhilai


---
