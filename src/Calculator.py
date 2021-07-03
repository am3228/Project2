import math

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def division(a, b):
    return a / b

def multiply(a, b):
    return a * b

def square_root(num):
    return num**0.5

def sqr(a):
    a = int(a)
    c = a * a
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

    def division(self, a, b):
        self.result = division(a, b)
        return self.result
    def multiply(self, a, b):
        self.result = multiply(a, b)
        return self.result

    def square_root(self, num):
        self.result = square_root(num)
        return self.result

    def square(self, a):
        self.result = sqr(a)
        return self.result