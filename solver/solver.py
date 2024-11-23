# solver.py: Functions to solve linear and quadratic equations
import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sympy import solve

from solver.parser import parse_equation

def solve_equation(equation_type):
    if equation_type == 1:
        equation = input("\nEnter a linear equation (e.g., 2x + 3 = 7): ").strip()
    elif equation_type == 2:
        equation = input("\nEnter a quadratic equation (e.g., x^2 - 4x + 3 = 0): ").strip()
    else:
        return None

    try:
        parsed_equation = parse_equation(equation)
        if equation_type == 1:
            solution = solve_linear(parsed_equation)
            print(f"\nSolution: x = {solution}")
        elif equation_type == 2:
            solution = solve_quadratic(parsed_equation)
            print(f"\nSolutions: x1 = {solution[0]}, x2 = {solution[1]}")
    except ValueError as e:
        print(f"\nError: {e}")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

import sympy as sp

# import sympy as sp

def solve_linear(equation):
    """
    Solves a linear equation of the form ax + b = c.
    Args:
        equation (sympy.Eq): A sympy Eq object representing the equation.
    Returns:
        float: The solution for x.
    """
    # Ensure 'x' is the symbol in the equation
    x = sp.symbols('x')

    # We solve the equation symbolically
    solution = sp.solve(equation, x)

    # If the solution is valid, return it
    if solution:
        return solution[0]
    else:
        raise ValueError("No valid solution found for the linear equation.")

def solve_quadratic(equation):
    """
    Solves a quadratic equation of the form ax^2 + bx + c = 0.
    Args:
        equation (sympy.Eq): A sympy Eq object representing the quadratic equation.
    Returns:
        list: A list of solutions for x (could be real or complex).
    """
    # Ensure 'x' is the symbol in the equation
    x = sp.symbols('x')

    # We solve the quadratic equation symbolically
    solutions = sp.solve(equation, x)

    # Return all solutions (could be real or complex)
    return solutions

