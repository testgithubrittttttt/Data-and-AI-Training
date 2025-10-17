import pika
import json

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare queue
channel.queue_declare(queue='order_queue', durable=True)

# Example new orders
new_orders = [
    {"OrderID": "O005", "CustomerID": "C002", "ProductID": "P103", "Quantity": 2, "OrderDate": "2025-10-10"},
    {"OrderID": "O006", "CustomerID": "C001", "ProductID": "P104", "Quantity": 1, "OrderDate": "2025-10-11"},
]

for order in new_orders:
    message = json.dumps(order)
    channel.basic_publish(
        exchange='',
        routing_key='order_queue',
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent
        ))
    print(f"Sent order {order['OrderID']}")

connection.close()
