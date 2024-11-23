import sympy as sp
import re

def parse_equation(equation: str):
    # Replace ^ with ** for exponentiation
    equation = equation.replace("^", "**")
    
    # Add multiplication symbol (*) where necessary
    # This regex adds multiplication between numbers and variables (e.g., 2x -> 2*x)
    equation = re.sub(r"(\d)([a-zA-Z])", r"\1*\2", equation)
    equation = re.sub(r"([a-zA-Z])(\d)", r"\1*\2", equation)  # This handles cases like x2 -> x*2

    # Handle implicit multiplication (e.g., x(x+1) -> x*(x+1))
    equation = re.sub(r"([a-zA-Z])\(", r"\1*", equation)
    equation = re.sub(r"\)([a-zA-Z])", r")*\1", equation)
    
    # SymPy equation parsing
    try:
        # Separate the left-hand side and right-hand side
        lhs, rhs = equation.split("=")
        lhs = sp.sympify(lhs)
        rhs = sp.sympify(rhs)
        return lhs - rhs  # Return the equation as lhs - rhs = 0
    except Exception as e:
        raise ValueError(f"Error parsing equation: {equation}. {str(e)}")
