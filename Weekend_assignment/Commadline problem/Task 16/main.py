# main.py
import calculator

num1 = 10
num2 = 5

# Perform addition
addition_result = calculator.add(num1, num2)
print(f"{num1} + {num2} = {addition_result}")

# Perform subtraction
subtraction_result = calculator.subtract(num1, num2)
print(f"{num1} - {num2} = {subtraction_result}")

# Perform multiplication
multiplication_result = calculator.multiply(num1, num2)
print(f"{num1} * {num2} = {multiplication_result}")

# Perform division
try:
    division_result = calculator.divide(num1, num2)
    print(f"{num1} / {num2} = {division_result}")
except ValueError as ve:
    print(ve)
