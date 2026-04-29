"""Execution of the command line interface."""

import typer
from calculator import Calculator

app = typer.Typer()


@app.command()
def greet(name: str) -> None:
    """Greets the user with a given name.

    Args:
        name (str): The name of the user to greet.
    """
    print(f"Hello, {name}! Welcome to the calculator CLI.")


@app.command()
def calculate(equation: str) -> None:
    """Calculate the result of a given equation.

    Supports basic arithmetic operations. For example "2 + 3 * 4" will be calculated as 14, following the order of
     operations.

    Args:
        equation (str): The mathematical equation to be calculated, e.g., "2 + 3 * (4 - 1)".
    """
    calculator = Calculator()
    try:
        result = calculator.execute_equation(equation)
        print(f"The result of the equation '{equation}' is: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except ValueError:
        print("Error: Invalid equation. Please provide a valid mathematical expression.")


if __name__ == "__main__":
    app()
