import pandas as pd #library used for handling CSV files and dataframes easily.
import sqlite3 #built-in Python module that allows you to create and interact with SQL and databases

# Connect to SQLite DB (or create it)
conn = sqlite3.connect("retail.db") #Creating a file named retail.db that acts as the database.
cursor = conn.cursor() #with the help of cursor we can now be able to use and execute the sql commands in the databases

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS products ( #this line is good to right for ensuring that this table will not be created again if it is excisting already
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
products_df.to_sql("products", conn, if_exists="replace", index=False) #if_exists = is table exists then replace it with completely new data
customers_df.to_sql("customers", conn, if_exists="replace", index=False) #index=False prevents Pandas from adding an extra index column.

conn.commit() #saves) all changes made so far to the database file.

# Add a new product
cursor.execute("INSERT INTO products VALUES (?, ?, ?, ?)", #using placeholder instaedof directly writing because placeholders are safer(prevents sql injection) and are reusable(same query for different products)
               ("P105", "Webcam", "Accessories", 70)) #placeholder when using it takes input as a tuple
conn.commit()

# Update product price
cursor.execute("UPDATE products SET Price = ? WHERE ProductID = ?",
               (900, "P101"))
conn.commit()

# Delete a customer
cursor.execute("DELETE FROM customers WHERE CustomerID = ?",
               ("C002",))# we use comma(,) because its not string its a tuple
conn.commit()

# List all customers from India
cursor.execute("SELECT * FROM customers WHERE Country = ?",
               ("India",))
print("Customers from India:")
for row in cursor.fetchall():
    print(row)


