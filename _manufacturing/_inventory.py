# Inventory Management System
import json

import logging
import colorlog
from pathlib import Path
DIR = Path("_manufacturing")
FILE_NAME = DIR / "_inventory.json"
LOG_FILE = DIR / "_inventory.log"

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console_handler = colorlog.StreamHandler()
console_handler.setFormatter(
    colorlog.ColoredFormatter(
        "%(log_color)s%(levelname)-8s%(reset)s | %(blue)s%(funcName)s%(reset)s | %(message)s",
        log_colors={
            "DEBUG": "cyan",
            "INFO": "green",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )
)
logger.addHandler(console_handler)
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s | %(levelname)s | %(funcName)s | %(message)s"
    )
)
logger.addHandler(file_handler)

REQUIRED_FIELDS = ["name", "quantity", "reorder_level", "supplier"]

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

def validate_product_fields(inventory):
    for field in REQUIRED_FIELDS:
        if field not in inventory:
            logger.error(f"Missing required field: {field}")
            return f"Missing required field: {field}"
    if not isinstance(inventory["quantity"], int) or inventory["quantity"] < 0:
        logger.error("Quantity must be a non-negative integer")
        return "Quantity must be a non-negative integer"
    if not isinstance(inventory["reorder_level"], int) or inventory["reorder_level"] < 0:
        logger.error("Reorder level must be a non-negative integer")
        return "Reorder level must be a non-negative integer"
    logger.debug("Product fields validated successfully")
    return None

def add_product(id, name, quantity, reorder_level, supplier):
    inventories = load_inventory()
    if id in inventories:
        logger.warning(f"Product with ID {id} already exists. Skipping addition.")
        return "Product already exists"
    inventory = {
        "name": name,
        "quantity": quantity,
        "reorder_level": reorder_level,
        "supplier": supplier
    }
    if alert := validate_product_fields(inventory):
        return alert
    inventories[id] = inventory
    save_inventory(inventories)
    logger.info(f"Added product {name} with ID {id} to inventory.")
    return f"Product {name} added successfully"

def get_product(id):
    inventories = load_inventory()
    inventory = inventories.get(id)
    if not inventory:
        logger.warning(f"Product with ID {id} not found.")
        return "Product not found"
    logger.info(f"Retrieved product with ID {id}.")
    return inventory

def view_inventory():
    inventories = load_inventory()
    if not inventories:
        logger.info("Inventory is empty.")
        return "Inventory is empty"
    logger.info("Viewing all inventory items.")
    return inventories

def update_product_stock(id, quantity_used):
    inventories = load_inventory()
    inventory = inventories.get(id)
    if not inventory:
        logger.warning(f"Product with ID {id} not found.")
        return "Product not found"
    if inventory["quantity"] < quantity_used:
        logger.warning(f"Not enough stock for product ID {id}. Available: {inventory['quantity']}, Required: {quantity_used}")
        return "Not enough stock"
    inventory["quantity"] -= quantity_used
    if inventory["quantity"] <= inventory["reorder_level"]:
        logger.warning(f"Stock for product ID {id} is low. Current quantity: {inventory['quantity']}")
        return f"Stock for {inventory['name']} is low. Please reorder from {inventory['supplier']}."
    save_inventory(inventories)
    logger.info(f"Updated stock for product ID {id}. New quantity: {inventory['quantity']}")
    return f"Stock updated for {inventory['name']}."

#id, name, quantity, reorder_level, supplier
inventory1 = ("P001", "Steel Rods", 100, 20, "Steel Co.")
inventory2 = ("P002", "Aluminum Sheets", 50, 10, "Aluminum Inc.")
inventory3 = ("P003", "Copper Wires", 200, 30, "Copper Ltd.")
inventory4 = ("P004", "Plastic Pellets", 300, 50, "Plastic Corp.")
inventory5 = ("P005", "Rubber Gaskets", 150, 25, "Rubber Co.")
inventory6 = ("P006", "Glass Panels", 80, 15, "Glass Inc.")
inventory7 = ("P007", "Wooden Planks", 120, 20, "Wood Co.")

inventory_list = [inventory1, inventory2, inventory3, inventory4, inventory5, inventory6, inventory7]

# for inventory in inventory_list:
#     print(add_product(*inventory))

# print(get_product("P001"))

# print(update_product_stock("P001", 85))
# print(update_product_stock("P001", 15))

# print(view_inventory())