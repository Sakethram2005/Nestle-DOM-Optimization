"""
=========================================================
Nestlé DOM Quantum Optimization
QAOA Implementation

Compatible with:

qiskit                 2.4.1
qiskit-aer             0.17.2
qiskit-algorithms      0.4.0
qiskit-optimization    0.7.0

=========================================================
"""


# ==============================
# IMPORTS
# ==============================

from qiskit_optimization import QuadraticProgram

from qiskit_optimization.algorithms import (
    MinimumEigenOptimizer
)

from qiskit_algorithms import QAOA

from qiskit_algorithms.optimizers import COBYLA

from qiskit.primitives import StatevectorSampler



# ==============================
# CREATE DOM PROBLEM
# ==============================

def create_problem():

    problem = QuadraticProgram(
        name="Nestle_DOM_QAOA"
    )


    # --------------------------
    # Binary Variables
    # --------------------------

    problem.binary_var(
        name="Order_1"
    )

    problem.binary_var(
        name="Order_2"
    )

    problem.binary_var(
        name="Order_3"
    )


    # --------------------------
    # Objective Function
    #
    # Maximize Revenue
    #
    # --------------------------

    problem.maximize(

        linear={

            "Order_1":100,

            "Order_2":120,

            "Order_3":90

        }

    )


    # --------------------------
    # Capacity Constraint
    #
    # Maximum 2 orders
    #
    # --------------------------

    problem.linear_constraint(

        linear={

            "Order_1":1,

            "Order_2":1,

            "Order_3":1

        },

        sense="<=",

        rhs=2,

        name="Capacity"

    )


    return problem



# ==============================
# RUN QAOA
# ==============================

def run_qaoa(problem):


    sampler = StatevectorSampler()


    optimizer = COBYLA(

        maxiter=100

    )


    qaoa = QAOA(

        sampler=sampler,

        optimizer=optimizer,

        reps=2

    )


    solver = MinimumEigenOptimizer(

        min_eigen_solver=qaoa

    )


    result = solver.solve(problem)


    return result



# ==============================
# DISPLAY RESULT
# ==============================

def show_result(result):


    print("\n")
    print("="*40)

    print(
        "Quantum Optimization Result"
    )

    print("="*40)


    print(
        "\nObjective Value:",
        result.fval
    )


    print(
        "\nSelected Orders:"
    )


    for name,value in zip(

        result.variables,

        result.x

    ):

        print(
            name,
            "=",
            int(value)
        )


    print(
        "\nSolution:",
        result.x
    )



# ==============================
# MAIN
# ==============================

if __name__ == "__main__":


    print("\n")
    print("="*50)

    print(
        "Nestlé Distributed Order Management"
    )

    print(
        "QAOA Quantum Optimization"
    )

    print("="*50)



    # Create Optimization Model

    problem = create_problem()



    print("\nOptimization Problem:\n")

    print(problem)



    # Execute QAOA

    result = run_qaoa(problem)




    # Display

    show_result(result)
