# scheduled_etl.py
import pandas as pd
from datetime import datetime
import os

# Load data
orders = pd.read_csv("orders.csv")
products = pd.read_csv("products.csv")
customers = pd.read_csv("customers.csv")

# Merge data
df = orders.merge(products, on="ProductID", how="left")
df = df.merge(customers, on="CustomerID", how="left")

# Calculate TotalPrice and extract OrderMonth
df["TotalPrice"] = df["Quantity"] * df["Price"]
df["OrderMonth"] = pd.to_datetime(df["OrderDate"]).dt.to_period("M").astype(str)

# Create output filename with timestamp
timestamp = datetime.now().strftime("%Y_%m_%d")
output_filename = f"daily_orders_report_{timestamp}.csv"

# Save file to output directory
output_path = os.path.join("reports", output_filename)
os.makedirs("reports", exist_ok=True)
df.to_csv(output_path, index=False)

print(f" Report saved as {output_path}")
