from Calculator.Subtraction import subtraction
from Calculator.Addition import addition
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Square import squaring
from Calculator.SquareRoot import squarerooting

def addition(a, b):
    return int(a) + int(b)

def subtraction(a, b):
    a = int(a)
    b = int(b)
    c = b - a
    return c

def division(a, b):
    c = (b/a)
    c = round(float(c), 9)
    return c

def multiply(a, b):
    return int(a) * int(b)

def square_root(a):
    c = a ** .5
    c = round(float(c), 8)
    return c

def square(a):
    c = a*a
    return c

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def divide(self, a, b):
        self.result = division(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiply(a, b)
        return self.result

    def square_root(self, a):
        self.result = square_root(a)
        return self.result

    def square(self, a):
        self.result = square(a)
        return self.result