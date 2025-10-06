import logging

# Configure logging
logging.basicConfig(
    filename='app.log',    # log file name
    level=logging.INFO,    # log level
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Example logs
logging.debug("This is a debug message")
logging.info("Application started")
logging.warning("Low memory warning")
logging.error("File not found error")
logging.critical("Critical system failure")
