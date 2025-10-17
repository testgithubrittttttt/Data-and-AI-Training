import pandas as pd
import sqlite3

# Connect to SQLite DB (or create it)
conn = sqlite3.connect("retail.db")
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    ProductID TEXT PRIMARY KEY,
    ProductName TEXT,
    Category TEXT,
    Price REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    CustomerID TEXT PRIMARY KEY,
    Name TEXT,
    Email TEXT,
    Country TEXT
)
""")

# Load CSVs into DataFrames
products_df = pd.read_csv("products.csv")
customers_df = pd.read_csv("customers.csv")

# Insert data
products_df.to_sql("products", conn, if_exists="replace", index=False)
customers_df.to_sql("customers", conn, if_exists="replace", index=False)

conn.commit()

# Add a new product
cursor.execute("INSERT INTO products VALUES (?, ?, ?, ?)",
               ("P105", "Webcam", "Accessories", 70))
conn.commit()

# Update product price
cursor.execute("UPDATE products SET Price = ? WHERE ProductID = ?",
               (900, "P101"))
conn.commit()

# Delete a customer
cursor.execute("DELETE FROM customers WHERE CustomerID = ?",
               ("C002",))
conn.commit()

# List all customers from India
cursor.execute("SELECT * FROM customers WHERE Country = ?",
               ("India",))
print("Customers from India:")
for row in cursor.fetchall():
    print(row)

