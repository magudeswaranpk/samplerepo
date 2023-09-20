# main_program.py
try:
    import math_operations
    import string_operations

    # Use functions from math_operations
    result_add = math_operations.add(5, 3)
    result_subtract = math_operations.subtract(10, 2)

    # Use functions from string_operations
    reversed_str = string_operations.reverse_string("Hello, World!")
    capitalized_str = string_operations.capitalize_string("python programming")

    print("Result of addition:", result_add)
    print("Result of subtraction:", result_subtract)
    print("Reversed string:", reversed_str)
    print("Capitalized string:", capitalized_str)

except ModuleNotFoundError as e:
    print(f"Error: {e}. Please make sure the module is installed and in the correct directory.")

except AttributeError as e:
    print(f"Error: {e}. Please check the function or variable names in the imported modules.")

except Exception as e:
    print(f"An error occurred: {e}")