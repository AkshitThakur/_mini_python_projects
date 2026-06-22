# Discount Calculator
import json

import logging
import colorlog
from pathlib import Path
DIR = Path("_ecommerce")
FILE_NAME = DIR / "_discount.json"
LOG_FILE = DIR / "_discount.log"
DISCOUNT_TYPES = ("percentage", "fixed", "bogo", "bulk" )

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# Console Handler (Colored)
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
# File Handler (No Colors)
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setFormatter(
    logging.Formatter(
        "%(asctime)s | %(levelname)s | %(funcName)s | %(message)s"
    )
)
logger.addHandler(file_handler)

def load_discount_codes():
    if not FILE_NAME.exists():
        logger.warning("JSON file does not exists!!!")
        return {}
    try:
        with open(FILE_NAME, 'r') as file:
            discount_codes = json.load(file)
            logger.info(f"discount codes loaded successfully!!!")
            return discount_codes
    except json.JSONDecodeError:
        logger.error("_discount.json is corrupted!!!")
        return {}

def save_discount_code(discount_code):
    """
    Function to save discount code
    """
    with open(FILE_NAME, 'w') as file:
        json.dump(discount_code, file, indent=4)
    logger.info("Discount saved successfully!!!")

def apply_discount_by_type(price, discount_type, discount_value, quantity):
    """
    Function to apply discount by type
    """
    if price<=0 or quantity<=0:
        logger.warning(f"Invalid Price: {price} and Quantity: {quantity} !!!")
        return f"Invalid Price: {price} and Quantity: {quantity}"
    if discount_type not in DISCOUNT_TYPES:
        logger.warning(f"Invalid discount type {discount_type}")
        return f"Invalid discount type {discount_type}"
    if discount_type == "percentage":
        discount_amount = (discount_value / 100) * price
    elif discount_type == "fixed":
        discount_amount = discount_value
    elif discount_type == "bogo" and quantity >= 2:
        discount_amount = price / 2
    elif discount_type == "bulk" and quantity >= 3:
        discount_amount = (discount_value / 100) * price
    final_price = max(price-discount_amount, 0)
    logger.info(f"Final price after discount: {final_price}")
    return round(final_price, 2)

def apply_discount_code(price, discount_code, quantity=1):
    discounts = load_discount_codes()
    if discount_code not in discounts:
        logger.warning(f"Discount code: {discount_code} does not exists!!!")
        return f"Discount code: {discount_code} does not exists."
    discount_details = discounts[discount_code]
    return apply_discount_by_type(price, discount_details['type'], discount_details['value'], quantity)

discount_codes = {
    "DISC10": {"type": "percentage", "value": 10},
    "FLAT500": {"type": "fixed", "value": 500},
    "BOGO50": {"type": "bogo", "value": 0},
    "BULK20": {"type": "bulk", "value": 20}
}

# save_discount_code(discount_codes)

apply_discount_codes = [
    (5000,"DISC10"), (5000,"FLAT500"), (2000,"BOGO50",2), 
    (6000,"BULK20",3),(6000, "INVALID")
]  

# for code in apply_discount_codes:
#     print(apply_discount_code(*code))
        