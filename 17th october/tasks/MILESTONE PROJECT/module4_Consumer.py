import pika
import json
import pandas as pd

# Load products data
products = pd.read_csv("products.csv").set_index("ProductID")

# This will store processed orders in memory
processed_orders = []

def callback(ch, method, properties, body):
    order = json.loads(body)
    print(f"Received order: {order}")

    product_id = order["ProductID"]
    quantity = int(order["Quantity"])

    if product_id in products.index:
        price = products.loc[product_id, "Price"]
        total_price = quantity * price
        order["TotalPrice"] = total_price
        processed_orders.append(order)
        print(f"Processed order {order['OrderID']} with TotalPrice {total_price}")
    else:
        print(f"ProductID {product_id} not found!")

    # Acknowledge message processed
    ch.basic_ack(delivery_tag=method.delivery_tag)

    # Optionally save to CSV after each order processed (or batch save)
    df = pd.DataFrame(processed_orders)
    df.to_csv("processed_orders.csv", index=False)
    print("Saved processed orders to processed_orders.csv")

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare queue (make sure it matches producer)
channel.queue_declare(queue='order_queue', durable=True)

# Consume messages with callback
channel.basic_qos(prefetch_count=1)  # fair dispatch
channel.basic_consume(queue='order_queue', on_message_callback=callback)

print('Waiting for orders. To exit press CTRL+C')
channel.start_consuming()
