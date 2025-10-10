# Import the necessary modules
import pika      # Pika is the RabbitMQ client library
import json      # For parsing JSON messages from the queue
import time      # Used to simulate a delay (like task processing time)

# -----------------------------
# 1. Connect to RabbitMQ Server
# -----------------------------

# Create a connection to RabbitMQ server running on localhost
connection = pika.BlockingConnection(
    pika.ConnectionParameters("localhost")
)

# Open a channel through the established connection
channel = connection.channel()

# ------------------------------------------
# 2. Ensure the Queue 'student_tasks' Exists
# ------------------------------------------

# This ensures that the queue named 'student_tasks' exists.
# If it doesn't exist, it will be created.
channel.queue_declare(queue="student_tasks")

# -----------------------------------------
# 3. Define the Callback Function for Worker
# -----------------------------------------

# This function is called every time a message is received from the queue
def callback(ch, method, properties, body):
    # Decode the message from JSON format
    task = json.loads(body)

    # Print the received message for logging
    print("Received:", task)

    # Simulate doing some time-consuming task (e.g., grading homework)
    time.sleep(2)  # Wait for 2 seconds

    # Print a message after processing
    print("Task processed for student:", task["student_id"])

# -------------------------------------
# 4. Start Listening to the Message Queue
# -------------------------------------

# Tell RabbitMQ to call the callback function whenever a message is received
# auto_ack=True means that the message will be automatically marked as 'acknowledged'
channel.basic_consume(
    queue="student_tasks",              # Queue to consume from
    on_message_callback=callback,       # Function to call when a message is received
    auto_ack=True                       # Automatically acknowledge receipt
)

# Inform the user that the script is now waiting for messages
print("Waiting for messages. Press CTRL+C to exit.")

# Start consuming messages from the queue — this is a blocking call
channel.start_consuming()
