import pandas as pd

# Load CSV files
products = pd.read_csv("products.csv")
customers = pd.read_csv("customers.csv")
orders = pd.read_csv("orders.csv")

# Merge orders with products on ProductID
orders_products = pd.merge(orders, products, on="ProductID", how="left")

# Merge the above with customers on CustomerID
full_data = pd.merge(orders_products, customers, on="CustomerID", how="left")

# Calculate TotalPrice = Quantity * Price
full_data["TotalPrice"] = full_data["Quantity"] * full_data["Price"]

# Extract OrderMonth from OrderDate
full_data["OrderDate"] = pd.to_datetime(full_data["OrderDate"])
full_data["OrderMonth"] = full_data["OrderDate"].dt.month

# Reorder columns for clarity (optional)
final_columns = [
    "OrderID", "CustomerID", "Name", "Email", "Country",
    "ProductID", "ProductName", "Category", "Price",
    "Quantity", "TotalPrice", "OrderDate", "OrderMonth"
]
processed_orders = full_data[final_columns]

# Save processed orders to CSV
processed_orders.to_csv("processed_orders.csv", index=False)

print("ETL processing complete. 'processed_orders.csv' created.")
