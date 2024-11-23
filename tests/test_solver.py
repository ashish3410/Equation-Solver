# test_solver.py: Unit tests for the solver module
import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from sympy import Eq, symbols
from solver.parser import parse_equation
from solver.solver import solve_equation

# Define the symbol 'x'
x = symbols('x')

def test_solve_linear_equation():
    # Parse the equation string into a symbolic equation
    equation_str = "x + 2 = 5"
    parsed_eq = parse_equation(equation_str)
    
    # Solve the equation
    solutions = solve_equation(parsed_eq, x)
    
    # Expected solution is [3]
    expected_solutions = [3]
    assert solutions == expected_solutions, f"Expected {expected_solutions}, but got {solutions}"

def test_solve_quadratic_equation():
    # Parse the equation string into a symbolic equation
    equation_str = "x**2 + 3*x + 2 = 0"
    parsed_eq = parse_equation(equation_str)
    
    # Solve the equation
    solutions = solve_equation(parsed_eq, x)
    
    # Expected solutions are [-2, -1]
    expected_solutions = [-2, -1]
    assert solutions == expected_solutions, f"Expected {expected_solutions}, but got {solutions}"

def test_solve_quadratic_equation_complex():
    # Parse the equation string into a symbolic equation
    equation_str = "x**2 + 1 = 0"
    parsed_eq = parse_equation(equation_str)
    
    # Solve the equation
    solutions = solve_equation(parsed_eq, x)
    
    # Expected solutions are [I, -I] (complex solutions)
    expected_solutions = [I, -I]
    assert solutions == expected_solutions, f"Expected {expected_solutions}, but got {solutions}"

def test_solve_invalid_equation():
    # Parse the invalid equation string into a symbolic equation
    equation_str = "x + 2 = x +"
    parsed_eq = parse_equation(equation_str)
    
    # Try solving the invalid equation, should raise a ValueError
    with pytest.raises(ValueError):
        solve_equation(parsed_eq, x)
