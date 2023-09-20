''' 3. You are tasked with developing a Python program that connects to a MySQL database, retrieves data from a table, performs some operations on the data, and updates the database with the modified data. Please write Python code to accomplish this task.

Instructions:

1. Assume that you have a MySQL database server running with the following details:

i. Host: localhost

ii. Port: 3306

iii. Username: your username

iv. Password: your password

v. Database Name: your database

vi. Table Name: your_table

vii. The table has the following columns: id (int), name (varchar),quantity (int).

2. Your Python program should:

i. Connect to the MySQL database. ii. Retrieve all records from the your_table table.

iii. Calculate the total quantity of all records retrieved.

iv. Update the quantity column of each record by doubling its value.

V. Commit the changes to the database.

vi. Close the database connection.

3. Handle any potential errors that may occur during the database connection and data manipulation, such as connection failures or SQL errors.

4. Provide comments in your code to explain each step. '''


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

        # Retrieve all records from the your_table table
        cursor.execute("SELECT * FROM your_table")
        records = cursor.fetchall()

        # Calculate the total quantity and update the records
        total_quantity = 0
        for record in records:
            id, name, quantity = record
            total_quantity += quantity
            new_quantity = quantity * 2

            # Update the quantity column with the doubled value
            cursor.execute("UPDATE your_table SET quantity = %s WHERE id = %s", (new_quantity, id))

        # Commit the changes to the database
        connection.commit()
        print(f"Total quantity before doubling: {total_quantity}")

except Error as e:
    print(f"Error: {e}")

finally:
    if connection.is_connected():
        # Close the cursor and database connection
        cursor.close()
        connection.close()
        print("MySQL connection is closed")


