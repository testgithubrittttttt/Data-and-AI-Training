import pika #Python client library for RabbitMQ.
import json #to convert Python dictionaries (orders) into JSON strings (so they can be sent as messages).

# Connect to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost')) #Connects to RabbitMQ running locally (localhost).
channel = connection.channel() #its like creating communication line where you send messages.

# Declare queue
channel.queue_declare(queue='order_queue', durable=True) #connects to) a queue named 'order_queue' and ensuring the queue persists even if RabbitMQ restarts thats why we do durable -true.

# Example new orders
new_orders = [
    {"OrderID": "O005", "CustomerID": "C002", "ProductID": "P103", "Quantity": 2, "OrderDate": "2025-10-10"},
    {"OrderID": "O006", "CustomerID": "C001", "ProductID": "P104", "Quantity": 1, "OrderDate": "2025-10-11"},
]

for order in new_orders:
    message = json.dumps(order) #Converts each order dictionary into a JSON string as it is a universal format.
    
    channel.basic_publish( #make this for sending the message to RabbitMQ.
        exchange='', #using the default exchange
        routing_key='order_queue',#specifies which queue to send the message to
        body=message,
        properties=pika.BasicProperties(
            delivery_mode=2,  # make message persistent helps in saving data to disk, not lost if RabbitMQ restarts
        ))
    print(f"Sent order {order['OrderID']}")

connection.close()

