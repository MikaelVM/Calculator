"""Execution of the command line interface."""

import typer
from calculator import Calculator

app = typer.Typer()

@app.command()
def greet(name: str):
    """Greets the user with a given name."""
    print(f"Hello, {name}! Welcome to the calculator CLI.")

@app.command()
def calculate(equation: str):
    """Calculates the result of a given equation."""
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