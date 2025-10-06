import csv
import logging

# Set up logging
logging.basicConfig(filename='sales.log', level=logging.INFO, format='%(levelname)s - %(message)s')

try:
    with open('sales.csv', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                price = int(row['price'])
                quantity = int(row['quantity'])
                total = price * quantity
                print(f"{row['product']} total = {total}")
                logging.info(f"{row['product']} total sales = {total}")
            except ValueError:
                logging.error(f"Invalid numeric value for {row}")
except FileNotFoundError:
    logging.error("sales.csv not found")
    print("Sales file not found.")
