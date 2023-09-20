''' Database programming with MySQL:

1. Implement Inventory Management in Python with MySQL

a) Inventory management, a critical element of the supply chain, is the tracking of inventory from manufacturers to warehouses and from these facilities to a point of sale. The goal of inventory management is to have the right products in the right place at the right time.

b) The required Database is Inventory, and the required Tables are Purchases, Sales and Inventory

c) Note: Apply your thoughts to demonstrate the DB Operation in Python.  '''


import mysql.connector
from datetime import date

# Initialize the database connection
connection = mysql.connector.connect(
    host="DESKTOP-171E2L7",
    user="root",
    password="johncena",
    database="pythonproject"
)

if connection.is_connected():
    cursor = connection.cursor()
    print("Connected to MySQL")

    # Function to add a purchase record
    def add_purchase(product_name, quantity):
        today = date.today()
        purchase_date = today.strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO Purchases (product_name, quantity, purchase_date) VALUES (%s, %s, %s)",
                       (product_name, quantity, purchase_date))
        cursor.execute("INSERT INTO Inventory (product_name, quantity) VALUES (%s, %s) "
                       "ON DUPLICATE KEY UPDATE quantity = quantity + VALUES(quantity)",
                       (product_name, quantity))
        connection.commit()

    # Function to add a sale record
    def add_sale(product_name, quantity):
        today = date.today()
        sale_date = today.strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO Sales (product_name, quantity, sale_date) VALUES (%s, %s, %s)",
                       (product_name, quantity, sale_date))
        cursor.execute("UPDATE Inventory SET quantity = quantity - %s WHERE product_name = %s",
                       (quantity, product_name))
        connection.commit()

    # Function to check inventory
    def check_inventory():
        cursor.execute("SELECT * FROM Inventory")
        inventory_data = cursor.fetchall()
        print("Inventory:")
        for item in inventory_data:
            print(f"{item[0]} - Quantity: {item[1]}")

    # Example usage
    add_purchase("Product A", 100)
    add_purchase("Product B", 50)
    add_sale("Product A", 30)
    check_inventory()

    # Close the database connection
    cursor.close()
    connection.close()
    print("MySQL connection is closed")
else:
    print("Failed to connect to MySQL")
