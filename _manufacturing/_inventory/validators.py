
from logger import logger
from config import REQUIRED_FIELDS

def validate_product_id(id, inventories):
    if id in inventories:
        logger.warning(f"Product with ID {id} already exists. Skipping addition.")
        return "Product already exists"

def validate_product(id, inventories):
    if id not in inventories:
        logger.warning(f"Product with ID {id} not found.")
        return "Product not found"

def validate_product_fields(inventory):
    for field in REQUIRED_FIELDS:
        if field not in inventory:
            logger.warning(f"Missing required field: {field}")
            return f"Missing required field: {field}"
