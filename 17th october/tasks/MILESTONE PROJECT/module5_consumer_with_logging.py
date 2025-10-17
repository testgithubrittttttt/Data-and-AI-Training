import pika
import json
import pandas as pd
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(
    filename='order_processing.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

logging.info("Starting order consumer...")

# Load products data
products = pd.read_csv("products.csv").set_index("ProductID")

processed_orders = []

def callback(ch, method, properties, body):
    start_time = datetime.now()
    try:
        order = json.loads(body)
        logging.info(f"Received order: {order}")

        product_id = order["ProductID"]
        quantity = int(order["Quantity"])

        if product_id not in products.index:
            err_msg = f"Validation error: ProductID {product_id} not found"
            logging.error(err_msg)
            # Reject message without requeue (could also choose to requeue)
            ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)
            return

        price = products.loc[product_id, "Price"]
        total_price = quantity * price
        order["TotalPrice"] = total_price
        processed_orders.append(order)

        # Save processed orders after every order
        df = pd.DataFrame(processed_orders)
        df.to_csv("processed_orders.csv", index=False)

        logging.info(f"Processed order {order['OrderID']} with TotalPrice {total_price}")
        logging.info(f"Saved processed orders to processed_orders.csv")

        # Acknowledge message processed
        ch.basic_ack(delivery_tag=method.delivery_tag)

    except Exception as e:
        logging.exception(f"Error processing order: {e}")
        # Reject message without requeue to avoid infinite loop on bad message
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)

    end_time = datetime.now()
    duration = (end_time - start_time).total_seconds()
    logging.info(f"Order processing time: {duration:.3f} seconds")

# Setup RabbitMQ connection and consumer (same as before)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='order_queue', durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='order_queue', on_message_callback=callback)

logging.info("Waiting for orders. To exit press CTRL+C")
channel.start_consuming()
