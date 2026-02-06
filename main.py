"""Execution of the command line interface."""

import typer
from calculator import Calculator

app = typer.Typer()

@app.command()
def hello(name: str):
    """Prints a simple hello for a given name."""
    print(f"Hello {name}")

@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        print(f"Goodbye Ms. {name}. Have a good day.")
    else:
        print(f"Bye {name}!")


if __name__ == "__main__":
    app()