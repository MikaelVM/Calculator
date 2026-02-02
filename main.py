import re

class Calculator:
    """A calculator"""

    def __init__(self):
        self.memory : list[str] = []

    def execute_equation(self, equation : str):
        """Execute an equation in the form of a string"""
        self.memory = re.findall('[+-/*//()]|\\d+', equation)

        while '*' in self.memory:
            index = self.memory.index('*')
            result = self.multiplication(float(self.memory[index-1]), float(self.memory[index+1]))

            self.memory.pop(index - 1)
            self.memory.pop(index - 1)
            self.memory.pop(index - 1)

            self.memory.insert(index - 1, str(result))

        while '/' in self.memory:
            index = self.memory.index('/')

            if float(self.memory[index+1]) == 0:
                raise ZeroDivisionError()

            result = self.division(float(self.memory[index-1]), float(self.memory[index+1]))

            self.memory.pop(index - 1)
            self.memory.pop(index - 1)
            self.memory.pop(index - 1)

            self.memory.insert(index - 1, str(result))

        while '-' in self.memory:
            index = self.memory.index('-')
            result = self.subtraction(float(self.memory[index-1]), float(self.memory[index+1]))

            self.memory.pop(index - 1)
            self.memory.pop(index - 1)
            self.memory.pop(index - 1)

            self.memory.insert(index - 1, str(result))

        while '+' in self.memory:
            index = self.memory.index('+')
            result = self.addition(float(self.memory[index-1]), float(self.memory[index+1]))

            self.memory.pop(index - 1)
            self.memory.pop(index - 1)
            self.memory.pop(index - 1)

            self.memory.insert(index - 1, str(result))

        if len(self.memory) > 1:
            raise ValueError("Current input caused an error")

        return self.memory[0]

    @staticmethod
    def multiplication(number1 : float, number2 : float):
        return number1 * number2

    @staticmethod
    def division(number1 : float, number2 : float):
        return number1 / number2

    @staticmethod
    def addition(number1 : float, number2 : float):
        return number1 + number2

    @staticmethod
    def subtraction(number1 : float, number2 : float):
        return number1 - number2




if __name__ == "__main__":
    calculator = Calculator()

    print(
        calculator.execute_equation(
            input()
        )
    )
