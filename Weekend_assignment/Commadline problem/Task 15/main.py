# main.py
import math_functions

num = 5

# Calculate factorial
factorial_result = math_functions.factorial(num)
print(f"The factorial of {num} is {factorial_result}")

# Check if a number is prime
if math_functions.is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
