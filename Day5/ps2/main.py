''' 2. Virtual Environment Management

Scenario: You are working on multiple Python projects with different dependencies and versions. To avoid conflicts and ensure project isolation, you decide to use virtual environments.

Create a Python program that demonstrates the following:

1. Create a virtual environment for a specific project.

2. Activate and deactivate virtual environments.

3. Install, upgrade, and uninstall packages within a virtual environment.

4. List the installed packages in a virtual environment.

5. Implement error handling for virtual environment operations.  '''


import subprocess
import sys
import os

# Function to create a virtual environment for a specific project
def create_virtualenv(env_name):
    try:
        subprocess.run([sys.executable, "-m", "venv", env_name])
        print(f"Virtual environment '{env_name}' created successfully.")
    except Exception as e:
        print(f"Error creating virtual environment: {e}")

# Function to activate a virtual environment
def activate_virtualenv(env_name):
    try:
        activate_script = os.path.join(env_name, "Scripts" if sys.platform == "win32" else "bin", "activate")
        subprocess.run([activate_script], shell=True)
        print(f"Activated virtual environment '{env_name}'.")
    except Exception as e:
        print(f"Error activating virtual environment: {e}")

# Function to deactivate the currently active virtual environment
def deactivate_virtualenv():
    try:
        subprocess.run(["deactivate"], shell=True)
        print("Deactivated virtual environment.")
    except Exception as e:
        print(f"Error deactivating virtual environment: {e}")

# Function to install a package within the active virtual environment
def install_package(package_name):
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", package_name])
        print(f"Package '{package_name}' installed successfully.")
    except Exception as e:
        print(f"Error installing package: {e}")

# Function to upgrade a package within the active virtual environment
def upgrade_package(package_name):
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", package_name])
        print(f"Package '{package_name}' upgraded successfully.")
    except Exception as e:
        print(f"Error upgrading package: {e}")

# Function to uninstall a package within the active virtual environment
def uninstall_package(package_name):
    try:
        subprocess.run([sys.executable, "-m", "pip", "uninstall", "-y", package_name])
        print(f"Package '{package_name}' uninstalled successfully.")
    except Exception as e:
        print(f"Error uninstalling package: {e}")

# Function to list installed packages within the active virtual environment
def list_installed_packages():
    try:
        installed_packages = subprocess.check_output([sys.executable, "-m", "pip", "list"]).decode("utf-8")
        print("Installed packages in the active virtual environment:")
        print(installed_packages)
    except Exception as e:
        print(f"Error listing installed packages: {e}")

# 1. Create a virtual environment for a specific project.
create_virtualenv("my_project_env")

# 2. Activate the virtual environment.
activate_virtualenv("my_project_env")

# 3. Install a package within the virtual environment.
install_package("requests")

# 4. Upgrade a package within the virtual environment.
upgrade_package("requests")

# 5. Uninstall a package within the virtual environment.
uninstall_package("requests")

# Deactivate the virtual environment.
deactivate_virtualenv()

# List installed packages in the virtual environment.
list_installed_packages()
