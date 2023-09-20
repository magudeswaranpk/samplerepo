CREATE DATABASE pythonproject;
USE pythonproject;
CREATE TABLE Purchases (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    purchase_date DATE NOT NULL
);

CREATE TABLE Sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product_name VARCHAR(255) NOT NULL,
    quantity INT NOT NULL,
    sale_date DATE NOT NULL
);

CREATE TABLE Inventory (
    product_name VARCHAR(255) PRIMARY KEY,
    quantity INT NOT NULL
);
