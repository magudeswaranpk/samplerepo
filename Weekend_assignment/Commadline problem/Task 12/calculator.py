''' 12. Build a command-line calculator that accepts a mathematical expression as a string argument and evaluates it, then prints the result. '''
import sys

def calculate(expression):
    try:
        result = eval(expression)
        print(f"Result: {result}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python calculator.py <expression>")
    else:
        expression = sys.argv[1]
        calculate(expression)

