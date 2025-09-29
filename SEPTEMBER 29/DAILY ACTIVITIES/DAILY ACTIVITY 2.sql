CREATE DATABASE RETAILDB;
USE RETAILDB;

CREATE TABLE CUSTOMERS(
    customer_id INT auto_increment primary key,
    name VARCHAR(50),
    city varchar(50),
    phone varchar(50)
);

CREATE TABLE PRODUCTS(
    product_id INT auto_increment primary key,
    product_name VARCHAR(50),
    category varchar(50),
    price varchar(50)
);

CREATE TABLE ORDERS(
    order_id INT auto_increment primary key,
    customer_id int,
    order_date date,
    foreign key (customer_id) references customers(customer_id)
);

CREATE TABLE ORDERSDETAILS(
    order_detail_id INT auto_increment primary key,
    order_id int,
    product_id int,
    quantity int,
	foreign key (order_id) references ORDERS(order_id),
    foreign key (product_id) references PRODUCTS(product_id)
);

INSERT INTO Customers (name, city, phone) VALUES
('Rahul', 'Mumbai', '9876543210'),
('Priya', 'Delhi', '9876501234'),
('Arjun', 'Bengaluru', '9876512345'),
('Neha', 'Hyderabad', '9876523456');


INSERT INTO Products (product_name, category, price) VALUES
('Laptop', 'Electronics', 60000.00),
('Smartphone', 'Electronics', 30000.00),
('Headphones', 'Accessories', 2000.00),
('Shoes', 'Fashion', 3500.00),
('T-Shirt', 'Fashion', 1200.00);


INSERT INTO Orders (customer_id, order_date) VALUES
(1, '2025-09-01'),
(2, '2025-09-02'),
(3, '2025-09-03'),
(1, '2025-09-04');


INSERT INTO ORDERSDETAILS (order_id, product_id, quantity) VALUES
(1, 1, 1),   -- Rahul bought 1 Laptop
(1, 3, 2),   -- Rahul bought 2 Headphones
(2, 2, 1),   -- Priya bought 1 Smartphone
(3, 4, 1),   -- Arjun bought 1 Shoes
(4, 5, 3);   -- Rahul bought 3 T-Shirts

SELECT * FROM ORDERSDETAILS;

DELIMITER $$ -- --IT IS LIKE UNITL I CHANGE IT BACK TREAT $$ AS THE END OF THE COMMAND INSTAED OF ;
-- WE CAN USE ANY SYMNBOL AS A DELIMITER BUT FOR EASE WE USE $$.
CREATE PROCEDURE GETALLPRODUCTS()
BEGIN
     SELECT product_id,product_name,category,price
     FROM Products;
END$$

DELIMITER ;

CALL GETALLPRODUCTS();

DELIMITER $$ 
CREATE PROCEDURE GETORDERWITHCUSTOMERS()
BEGIN
     SELECT o.order_id,o.order_date,c.name as customer_name
     FROM Orders o
     Join Customers c
     On o.customer_id = c.customer_id;
END$$

DELIMITER ;
call GETORDERWITHCUSTOMERS();
