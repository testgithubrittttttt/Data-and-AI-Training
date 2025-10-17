from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()

DB_PATH = "retail.db"

# Pydantic models for validation
class Product(BaseModel):
    ProductID: str
    ProductName: str
    Category: str
    Price: float

class Customer(BaseModel):
    CustomerID: str
    Name: str
    Email: str
    Country: str

# Helper function to get DB connection
def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

### PRODUCTS ###

@app.get("/products")
def get_products():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    conn.close()
    return [dict(p) for p in products]

@app.post("/products")
def add_product(product: Product):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO products (ProductID, ProductName, Category, Price) VALUES (?, ?, ?, ?)",
            (product.ProductID, product.ProductName, product.Category, product.Price)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="ProductID already exists")
    conn.close()
    return {"message": "Product added successfully"}

@app.put("/products/{product_id}")
def update_product(product_id: str, product: Product):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE products SET ProductName = ?, Category = ?, Price = ? WHERE ProductID = ?",
        (product.ProductName, product.Category, product.Price, product_id)
    )
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Product not found")
    conn.close()
    return {"message": "Product updated successfully"}

@app.delete("/products/{product_id}")
def delete_product(product_id: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM products WHERE ProductID = ?", (product_id,))
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Product not found")
    conn.close()
    return {"message": "Product deleted successfully"}

### CUSTOMERS ###

@app.get("/customers")
def get_customers():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customers")
    customers = cursor.fetchall()
    conn.close()
    return [dict(c) for c in customers]

@app.post("/customers")
def add_customer(customer: Customer):
    conn = get_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO customers (CustomerID, Name, Email, Country) VALUES (?, ?, ?, ?)",
            (customer.CustomerID, customer.Name, customer.Email, customer.Country)
        )
        conn.commit()
    except sqlite3.IntegrityError:
        conn.close()
        raise HTTPException(status_code=400, detail="CustomerID already exists")
    conn.close()
    return {"message": "Customer added successfully"}

@app.put("/customers/{customer_id}")
def update_customer(customer_id: str, customer: Customer):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE customers SET Name = ?, Email = ?, Country = ? WHERE CustomerID = ?",
        (customer.Name, customer.Email, customer.Country, customer_id)
    )
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Customer not found")
    conn.close()
    return {"message": "Customer updated successfully"}

@app.delete("/customers/{customer_id}")
def delete_customer(customer_id: str):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers WHERE CustomerID = ?", (customer_id,))
    conn.commit()
    if cursor.rowcount == 0:
        conn.close()
        raise HTTPException(status_code=404, detail="Customer not found")
    conn.close()
    return {"message": "Customer deleted successfully"}
