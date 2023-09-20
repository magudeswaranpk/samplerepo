'''  4. You are developing an employee management system for a company. The database should store employee information, including name, salary, department, and hire date. Managers should be able to view and update employee details.

1. Design the database schema for the employee management system.

2. Write Python code to connect to the database and retrieve a list of employees in a specific department.

3. Implement a feature to update an employee's salary. '''


import mysql.connector
from mysql.connector import Error

try:
    # Define database connection details
    db_config = {
        "host": "DESKTOP-171E2L7",
        "port": 3306,
        "user": "root",
        "password": "johncena",
        "database": "pythonproject"
    }

    # Connect to the MySQL database
    connection = mysql.connector.connect(**db_config)

    if connection.is_connected():
        print("Connected to MySQL")

        # Create a cursor to interact with the database
        cursor = connection.cursor()

        # Specify the department for which you want to retrieve employees
        target_department = "Sales"  # Replace with the desired department name

        # Retrieve employees in the specified department
        cursor.execute("SELECT * FROM Employees WHERE department = %s", (target_department,))
        employees = cursor.fetchall()

        if employees:
            print(f"Employees in the {target_department} department:")
            for employee in employees:
                employee_id, name, salary, department, hire_date = employee
                print(f"Employee ID: {employee_id}, Name: {name}, Salary: {salary}, Hire Date: {hire_date}")
        else:
            print(f"No employees found in the {target_department} department.")

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        # Close the cursor and database connection
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


# ...

# Function to update an employee's salary
def update_salary(employee_id, new_salary):
    try:
        cursor = connection.cursor()

        # Update the salary of the specified employee
        cursor.execute("UPDATE Employees SET salary = %s WHERE employee_id = %s", (new_salary, employee_id))
        connection.commit()
        print(f"Salary updated for Employee ID {employee_id} to {new_salary}")

    except Error as e:
        print(f"Error updating salary: {e}")

# Example usage:
employee_id_to_update = 1  # Replace with the desired employee ID
new_salary_value = 60000  # Replace with the new salary value
update_salary(employee_id_to_update, new_salary_value)


