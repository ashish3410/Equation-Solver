# test_parser.py: Unit tests for the parser module
import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pytest
from sympy import Eq, symbols
from solver.parser import parse_equation  # Ensure this import is correct

# Define the symbol 'x'
x = symbols('x')

def test_parse_linear_equation():
    equation_str = "x + 2 = 5"
    parsed_eq = parse_equation(equation_str)
    expected_eq = Eq(x + 2, 5)
    assert parsed_eq == expected_eq, f"Expected {expected_eq}, but got {parsed_eq}"

def test_parse_quadratic_equation():
    equation_str = "x**2 + 3*x + 2 = 0"
    parsed_eq = parse_equation(equation_str)
    expected_eq = Eq(x**2 + 3*x + 2, 0)
    assert parsed_eq == expected_eq, f"Expected {expected_eq}, but got {parsed_eq}"

def test_parse_invalid_equation_missing_equals():
    equation_str = "x + 2 5"
    with pytest.raises(ValueError):
        parse_equation(equation_str)

def test_parse_invalid_equation_invalid_expression():
    equation_str = "x + 2 = x +"
    with pytest.raises(ValueError):
        parse_equation(equation_str)

# import pytest
# from solver.parser import parse_equation

# Test cases for linear and quadratic equations
def test_linear_equation():
    assert parse_equation("2x - 3 = 0") == {'a': 2, 'b': -3, 'c': 0}
    assert parse_equation("3x = 12") == {'a': 3, 'b': 0, 'c': 0}

def test_quadratic_equation():
    assert parse_equation("x^2 - 4x + 3 = 0") == {'a': 1, 'b': -4, 'c': 3}
    assert parse_equation("3x^2 + 2x - 8 = 0") == {'a': 3, 'b': 2, 'c': -8}
    assert parse_equation("x^2 + x = 0") == {'a': 1, 'b': 1, 'c': 0}

# Test invalid equation (should raise ValueError)
def test_invalid_equation():
    with pytest.raises(ValueError):
        parse_equation("x + = 5")
