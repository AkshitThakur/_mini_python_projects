from utils import *
from validators import *
from logger import logger

def add_product(id, name, quantity, reorder_level, supplier):
    inventories = load_inventory()
    if alert := validate_product_id(id, inventories):
        return alert
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
    return (inventory, f"Product {name} added successfully with ID {id}.")

def update_product_stock(id, quantity_used):
    inventories = load_inventory()
    if alert := validate_product(id, inventories):
        return alert
    inventory = inventories.get(id)
    if inventory["quantity"] < quantity_used:
        logger.warning(f"Not enough stock for product ID {id}. Available: {inventory['quantity']}, Required: {quantity_used}")
        return "Not enough stock"
    inventory["quantity"] -= quantity_used
    if inventory["quantity"] <= inventory["reorder_level"]:
        logger.warning(f"Stock for product ID {id} is low. Current quantity: {inventory['quantity']}")
        return f"Stock for {inventory['name']} is low. Please reorder from {inventory['supplier']}."
    save_inventory(inventories)
    logger.info(f"Updated stock for product ID {id}. New quantity: {inventory['quantity']}")
    return (inventory, f"Stock updated for {inventory['name']}.")

def restock_product(id, additional_quantity):
    inventories = load_inventory()
    if alert := validate_product(id, inventories):
        return alert
    inventory = inventories.get(id)
    inventory['quantity'] += additional_quantity
    inventories[id] = inventory
    save_inventory(inventories)
    logger.info(f"Restocked product ID {id}. New quantity: {inventory['quantity']}")
    return (inventory, f"Product {inventory['name']} restocked successfully. New quantity: {inventory['quantity']}")

def get_product(id):
    inventories = load_inventory()
    if alert := validate_product(id, inventories):
        return alert
    inventory = inventories.get(id)
    
    logger.info(f"Retrieved product with ID {id}.")
    return (inventory, f"Product {inventory['name']} retrieved successfully.")

def view_inventory():
    inventories = load_inventory()
    if not inventories:
        logger.info("Inventory is empty.")
        return "Inventory is empty"
    logger.info("Viewing all inventory items.")
    return (inventories, "Viewing all inventory items.")
