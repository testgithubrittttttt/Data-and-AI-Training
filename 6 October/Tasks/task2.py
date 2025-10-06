import yaml
import logging

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(levelname)s - %(message)s')

try:
    with open('config.yaml', 'r') as file:
        config = yaml.safe_load(file)
        logging.info("Config loaded successfully")

    db = config['database']
    print(f"Connecting to {db['host']}:{db['port']} as {db['user']}")

except FileNotFoundError:
    logging.error("config.yaml not found")
    print("Configuration file missing.")
