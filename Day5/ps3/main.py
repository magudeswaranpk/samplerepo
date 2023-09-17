''' 3. Module Dependency Resolution

Scenario: You are developing a Python application that relies on third-party packages. Managing dependencies and ensuring compatibility is crucial for your project's success.

Design a Python program that demonstrates the following:

1. Use a requirements.txt file to specify project dependencies.

2. Automatically install all project dependencies from the requirements.txt file.

3. Ensure that the versions of installed packages are compatible.

4. Implement error handling for dependency resolution and installation.  '''


import subprocess

try:
    # Automatically install all project dependencies from the requirements.txt file.
    subprocess.run(["pip", "install", "-r", "requirements.txt"])
    print("Dependencies installed successfully.")
except subprocess.CalledProcessError as e:
    print(f"Error installing dependencies: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
