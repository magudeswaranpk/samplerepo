''' 16. Create a Python module named calculator.py that contains functions for each of the four operations (addition, subtraction, multiplication, and division). Each function should take two arguments, perform the respective operation, and return the result. '''
# calculator.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Division by zero is not allowed.")
    return x / y
