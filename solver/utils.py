# utils.py: Helper functions for the solver module

def validate_equation(equation_str):
    """
    Validate the input equation string for basic correctness.
    This function checks if the equation string contains an '=' sign.
    
    Parameters:
    - equation_str (str): The equation string (e.g., "x + 2 = 5")
    
    Returns:
    - bool: Returns True if the equation is valid (contains an '=' sign), otherwise raises an error.
    """
    if '=' not in equation_str:
        raise ValueError("Equation must contain an '=' sign.")
    return True
