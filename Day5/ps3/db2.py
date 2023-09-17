''' 2. Customer Order Processing

Scenario: You are building a customer order processing system for an e-commerce company. The system needs to interact with a MySQL database to store customer orders, products, and order details.

1. Design a MySQL database schema for the order processing system, including tables for customers, products, and orders.

2. Write a Python program that connects to the database and allows customers to place new orders.

3. Implement a feature that calculates the total cost of an order and updates product quantities in the database.

4. How would you handle cases where a product is no longer available when a customer places an order?

5. Develop a function to generate order reports for the company's finance department. '''


import mysql.connector

# Connect to the MySQL database
connection = mysql.connector.connect(
    host="DESKTOP-171E2L7",
    user="root",
    password="johncena",
    database="pythonproject"
)

if connection.is_connected():
    print("Connected to MySQL")

    # Function to place a new order
    def place_order(customer_id, product_id, quantity):
        try:
            cursor = connection.cursor()

            # Check product availability
            cursor.execute("SELECT quantity_available FROM Products WHERE product_id = %s", (product_id,))
            available_quantity = cursor.fetchone()[0]

            if available_quantity >= quantity:
                # Calculate total cost
                cursor.execute("SELECT price FROM Products WHERE product_id = %s", (product_id,))
                price = cursor.fetchone()[0]
                total_cost = price * quantity

                # Insert order details
                cursor.execute("""
                    INSERT INTO Orders (customer_id, order_date)
                    VALUES (%s, CURDATE())
                """, (customer_id,))
                order_id = cursor.lastrowid

                cursor.execute("""
                    INSERT INTO OrderDetails (order_id, product_id, quantity, total_price)
                    VALUES (%s, %s, %s, %s)
                """, (order_id, product_id, quantity, total_cost))

                # Update product quantity
                new_quantity = available_quantity - quantity
                cursor.execute("UPDATE Products SET quantity_available = %s WHERE product_id = %s",
                               (new_quantity, product_id))

                connection.commit()
                print("Order placed successfully.")
            else:
                print("Product is not available in the requested quantity.")

        except mysql.connector.Error as e:
            print(f"Error placing order: {e}")

    # Example usage:
    place_order(1, 1, 5)

    # Close the database connection
    cursor.close()
    connection.close()
    print("MySQL connection is closed")
else:
    print("Failed to connect to MySQL")



def generate_order_report():
    try:
        cursor = connection.cursor()

        # Fetch order data
        cursor.execute("""
            SELECT Customers.name, Orders.order_id, OrderDetails.product_id, Products.name,
                   OrderDetails.quantity, OrderDetails.total_price
            FROM Customers
            JOIN Orders ON Customers.customer_id = Orders.customer_id
            JOIN OrderDetails ON Orders.order_id = OrderDetails.order_id
            JOIN Products ON OrderDetails.product_id = Products.product_id
        """)

        order_data = cursor.fetchall()

        # Generate and format the report
        report = "Order Report:\n"
        for row in order_data:
            report += f"Customer: {row[0]}, Order ID: {row[1]}\n"
            report += f"Product ID: {row[2]}, Product Name: {row[3]}\n"
            report += f"Quantity: {row[4]}, Total Price: {row[5]}\n"
            report += "\n"

        print(report)

    except mysql.connector.Error as e:
        print(f"Error generating order report: {e}")

# Example usage:
generate_order_report()


