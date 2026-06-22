from config import FILE_NAME
from logger import logger
import json

def load_inventory():
    if not FILE_NAME.exists():
        logger.warning(f"Inventory file {FILE_NAME} not found. Starting with an empty inventory.")
        return {}
    try:
        with open(FILE_NAME, "r") as file:
            inventories =  json.load(file)
            logger.info(f"Loaded inventory from {FILE_NAME}")
            return inventories
    except json.JSONDecodeError:
        logger.error(f"Error decoding JSON from {FILE_NAME}")
        return {}

def save_inventory(inventory):
    with open(FILE_NAME, "w") as file:
        json.dump(inventory, file, indent=4)
    logger.info(f"Saved inventory to {FILE_NAME}")