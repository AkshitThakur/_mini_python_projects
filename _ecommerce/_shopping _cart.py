#  Shopping Cart System 
import json
import logging
import colorlog

REQUIRED_FEILDS = ('name', 'price', 'quantity', 'total_cost')

from pathlib import Path
DIR = Path("_ecommerce")
FILE_NAME = DIR / "_shopping_cart.json"
LOG_FILE = DIR / "_shopping_cart.log"

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


def load_carts():
    """
    Function to load carts from json file!!!
    """
    if not FILE_NAME.exists():
        return {}
    try:
        with open(FILE_NAME, 'r') as file:
            carts = json.load(file)
            logger.info("Carts loaded successfully")
            return carts
    except json.JSONDecodeError:
        logger.warning(f"File is empty.")
        return {}

def save_cart(cart):
    """
    Function to save cart to json file!!!
    """
    with open(FILE_NAME, 'w', encoding="utf-8") as file:
        json.dump(cart, file, indent=4)
        logger.info("Cart saved successfully")

def validate_cart_fields(cart):
    """
    Function to validate fields!!!
    """
    for field in REQUIRED_FEILDS:
        if field not in cart:
            logger.warning(f"Validation failed. Missing field: {field}")
            return f"Invalid Field {field}"

def validate_stock(id, quantity, available_stock):
    """
    Function to check the availability in stock
    """
    if quantity > available_stock:
        logger.warning(f"ID {id} : buying {quantity} stocks but available {available_stock}")
        return f"Not enough Stocks are available"
    logger.info(f"Stocks are available for ID: {id}!!!")

def add_to_cart(id, name, price, quantity, available_stock): 
    """
    Function to add new cart!!!
    """  
    carts = load_carts()
    if id in carts:
        logger.info(f"Cart {name} already exists!!!")
        return f"{name} already exists."
    if alert := validate_stock(id, quantity, available_stock):
        return alert
    cart = {
        'name' : name,
        'price' : price,
        'quantity' : quantity,
        'total_cost' : round(price*quantity, 2)
    }
    if alert := validate_cart_fields(cart):
        return alert
    carts[id] = cart
    save_cart(carts)
    logger.info(f"Cart added. ID={id}, Name={name}, Quantity={quantity}")
    return f"Cart {name} added successfully!!!"

def view_carts():
    """
    Function to view all items in carts
    """
    if carts := load_carts():
        logger.info(f"Cart have {len(carts)} items.")
        return carts
    return f"Cart have {len(carts)} items."
    

def update_cart(id, quantity, available_stock):
    """
    Function to update quantity of a specific item
    """
    carts = load_carts()
    cart = carts.get(id)
    if not cart:
        logger.warning(f"Cart ID:{id} does not exists!!!")
        return f"Cart ID:{id} does not exists."
    if alert := validate_stock(id, quantity, available_stock):
        return alert
    cart["quantity"] = quantity
    cart["total_cost"] = round(cart["price"]*quantity, 2)
    carts[id] = cart
    save_cart(carts)
    logger.info(f"Cart {cart["name"]} updated successfully")
    return f"Cart {cart} updated successfully "

def remove_from_cart(id):
    """
    Function to remove an item from the cart
    """
    carts = load_carts()
    if not carts.get(id):
        logger.warning(f"Cart ID:{id} does not exists!!!")
        return f"Cart ID:{id} does not exists."
    del carts[id]
    save_cart(carts)
    logger.info(f"Card {id} removed successfully!!!")
    return f"Card {id} removed successfully."

def checkout():
    """
    Function for checkout amount of all items
    """
    carts = load_carts()
    if not carts:
        logger.info("Cart is empty!!!")
        return f"Cart is empty."
    total_checkout = sum(
        item["total_cost"]
        for item in carts.values()
    )
    logger.info(f"Total checkout amount: {total_checkout}, items: {len(carts)}")
    return f"Total checkout amount : {total_checkout}"

cart1 = ("M001", "Laptop", 1000, 1, 2)
cart2 = ("M002", "Smartphone", 500, 2, 3)
cart3 = ("M003", "Headphones", 100, 3, 1)
cart4 = ("M004", "Keyboard", 50, 1, 3)
cart5 = ("M005", "Mouse", 25, 2, 0)
cart6 = ("M006", "Monitor", 200, 1, 1)
cart_list = [cart1, cart2, cart3, cart4, cart5, cart6]

for cart in cart_list:
    print(add_to_cart(*cart))
print(view_carts())
print(update_cart("M002", 3, 2))
print(remove_from_cart("M006"))
print(checkout())
print(validate_stock("M002", 5, 10))
print(validate_stock("M004", 7, 5)) 