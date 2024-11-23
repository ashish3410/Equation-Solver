import sympy as sp
from solver.solver import solve_linear, solve_quadratic  # Ensure correct import path

def parse_equation(equation_str):
    """
    Converts an equation string to a SymPy equation.
    Args:
        equation_str (str): The equation in string format (e.g., '2*x + 3 = 7')
    Returns:
        sympy.Eq: A SymPy Eq object representing the equation.
    """
    # Define the variable
    x = sp.symbols('x')

    try:
        # Replace '^' with '**' for exponentiation (SymPy uses '**' for powers)
        equation_str = equation_str.replace("^", "**")
        
        # Split input string to lhs and rhs, and sympify both sides
        lhs, rhs = equation_str.split('=')
        lhs = sp.sympify(lhs)
        rhs = sp.sympify(rhs)

        # Return the SymPy equation object
        equation = sp.Eq(lhs, rhs)
        return equation
    except Exception as e:
        raise ValueError(f"Error parsing equation: {equation_str}. {e}")

def display_welcome_message():
    """
    Displays a welcome message to the user.
    """
    print("\n=====================================")
    print(" Welcome to the Equation Solver App!")
    print("=====================================")
    print("You can solve both linear and quadratic equations.")
    print("Please make sure to enter equations in the correct format.")
    print("\nExample formats:")
    print("Linear: 2*x + 3 = 7")
    print("Quadratic: x**2 - 4*x + 3 = 0")
    print("\n=====================================\n")

def get_user_input():
    """
    Prompts the user to choose the type of equation and input it.
    """
    print("Choose the type of equation to solve:")
    print("1. Linear Equation (ax + b = c)")
    print("2. Quadratic Equation (ax^2 + bx + c = 0)")
    
    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        equation_str = input("\nEnter the linear equation (e.g., 2*x + 3 = 7): ")
        return 'linear', equation_str
    elif choice == '2':
        equation_str = input("\nEnter the quadratic equation (e.g., x**2 - 4*x + 3 = 0): ")
        return 'quadratic', equation_str
    else:
        print("Invalid choice. Please select either 1 or 2.")
        return get_user_input()

def solve_equation(equation_type, equation_str):
    """
    Solves the equation based on its type (linear or quadratic).
    """
    try:
        # Parse the equation string into a SymPy Eq object
        equation = parse_equation(equation_str)

        if equation_type == 'linear':
            result = solve_linear(equation)
            return f"The solution for x is: {result}"
        elif equation_type == 'quadratic':
            result = solve_quadratic(equation)
            return f"The solutions for x are: {result}"
        else:
            return "Error: Unsupported equation type."
    except Exception as e:
        return f"Error: {e}"

def main():
    """
    Main function to run the app interactively.
    """
    display_welcome_message()

    while True:
        # Get user input for equation type and equation string
        equation_type, equation_str = get_user_input()

        # Solve the equation and display the result
        result = solve_equation(equation_type, equation_str)
        print(result)
        
        # Ask if the user wants to solve another equation
        continue_choice = input("\nWould you like to solve another equation? (yes/no): ").strip().lower()
        if continue_choice != 'yes':
            print("\nThank you for using the Equation Solver App!")
            break

if __name__ == "__main__":
    main()
