"""A calculator that can perform basic arithmetic operations."""
import re


class Calculator:
    """A calculator that can perform basic arithmetic operations."""

    def __init__(self):
        """Initialize the calculator."""
        self.memory: list[str] = []

    def execute_equation(self, equation: str) -> str:
        """Execute an equation and return the result.

        Args:
            equation (str): The equation to execute.

        Returns:
            str: The result of the equation.

        Raises:
            ZeroDivisionError: If the equation contains a division by zero.
            ValueError: If the equation is invalid.
        """
        # Tokenizer. Separates numbers and operators.
        # TODO: Make a separate function that also validates input.
        self.memory = re.findall('[+-/*//()]|\\d+', equation)

        while '*' in self.memory:
            index = self.memory.index('*')
            result = self.multiplication(float(self.memory[index - 1]), float(self.memory[index + 1]))

            self.memory.pop(index - 1)
            self.memory.pop(index - 1)
            self.memory.pop(index - 1)

            self.memory.insert(index - 1, str(result))

        while '/' in self.memory:
            index = self.memory.index('/')

            if float(self.memory[index + 1]) == 0:
                raise ZeroDivisionError()

            result = self.division(float(self.memory[index - 1]), float(self.memory[index + 1]))

            self.memory.pop(index - 1)
            self.memory.pop(index - 1)
            self.memory.pop(index - 1)

            self.memory.insert(index - 1, str(result))

        while '-' in self.memory:
            index = self.memory.index('-')
            result = self.subtraction(float(self.memory[index - 1]), float(self.memory[index + 1]))

            self.memory.pop(index - 1)
            self.memory.pop(index - 1)
            self.memory.pop(index - 1)

            self.memory.insert(index - 1, str(result))

        while '+' in self.memory:
            index = self.memory.index('+')
            result = self.addition(float(self.memory[index - 1]), float(self.memory[index + 1]))

            self.memory.pop(index - 1)
            self.memory.pop(index - 1)
            self.memory.pop(index - 1)

            self.memory.insert(index - 1, str(result))

        if len(self.memory) > 1:
            raise ValueError("Current input caused an error")

        return self.memory[0]

    @staticmethod
    def multiplication(number1: float, number2: float) -> float:
        """Multiply two numbers."""
        return number1 * number2

    @staticmethod
    def division(number1: float, number2: float) -> float:
        """Divide two numbers."""
        return number1 / number2

    @staticmethod
    def addition(number1: float, number2: float) -> float:
        """Add two numbers."""
        return number1 + number2

    @staticmethod
    def subtraction(number1: float, number2: float) -> float:
        """Subtract two numbers."""
        return number1 - number2
