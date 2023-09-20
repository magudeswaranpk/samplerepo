'''14. Write a Python script that takes two integer command-line arguments and prints their sum. '''
import sys

if len(sys.argv) != 3:
    print("Usage: python add_numbers.py <integer1> <integer2>")
else:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        result = num1 + num2
        print(f"The sum of {num1} and {num2} is {result}")
    except ValueError:
        print("Both arguments should be integers.")
