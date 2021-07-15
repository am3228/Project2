from Calculator.Subtraction import Subtraction
from Calculator.Addition import Addition
from Calculator.Multiply import Multiply
from Calculator.Division import Division
from Calculator.Square import Square
from Calculator.Squareroot import Squareroot

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = Addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = Subtraction(a, b)
        return self.result

    def divide(self, a, b):
        self.result = Division(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = Multiply(a, b)
        return self.result

    def Squareroot(self, a):
        self.result = Squareroot(a)
        return self.result

    def square(self, a):
        self.result = Square(a)
        return self.result