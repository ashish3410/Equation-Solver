import sys
import os

# Add the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from solver.parser import parse_equation

# Test cases
test_equations = [
    "2x - 3 = 0",  # Linear equation
    "x^2 - 4x + 3 = 0",  # Quadratic equation
    "3x^2 + 2x - 8 = 0",  # Quadratic equation
    "3x = 12",  # Linear equation
    "x^2 + x = 0"  # Quadratic equation
]

for eq in test_equations:
    try:
        parsed = parse_equation(eq)
        print(f"Equation: {eq} -> Parsed: {parsed}")
    except ValueError as e:
        print(f"Equation: {eq} -> Error: {e}")
