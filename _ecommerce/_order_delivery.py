# Order Processing & Delivery Tracking System,
import json
from datetime import datetime, timedelta

import logging
import colorlog
from pathlib import Path
DIR = Path("_ecommerce")
FILE_NAME = DIR / "_order_delivery.json"
LOG_FILE = DIR / "_order_delivery.log"

DATE_FORMAT = "%Y-%m-%d"
REQUIRED_FIELDS = ("customer_name","product_name","quantity", "status","delivery_date","location")
STATUS_TRANSITIONS = ("Processing", "Shipped", "Out for Delivery", "Delivered")

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


def load_orders():
    """
    Function to load Orders
    """
    if not FILE_NAME.exists():
        logger.info("JSON file does not exist!!!")
        return {}
    try:
        with open(FILE_NAME, 'r') as file:
            orders = json.load(file)
            logger.info("Orders loaded successfully!!!")
            return orders
    except json.JSONDecodeError:
        logger.error("_order_delivery.json is corrupted!!!")
        return {}

def save_order(order):
    """
    Function to save order
    """
    with open(FILE_NAME, 'w') as file:
        json.dump(order, file, indent=4)
    logger.info(f"Order : {order} saved successfully!!!")

def validate_order_fields(order):
    """
    Function to validate order fields
    """
    for field in REQUIRED_FIELDS:
        if field not in order:
            logger.warning(f"Invalid field : {field}")
            return f"Invalid field : {field}"
    logger.info("All field are valid!!!")

def create_order(order_id, customer_name, product_name, quantity, delivery_location):
    """
    Function to create a new order
    """
    orders = load_orders()
    if order_id in orders:
        logger.warning(f"Duplicate order attempted. ID={order_id}")
        return f"Order ID: {order_id} already exists."
    delivery_date = (datetime.today()+timedelta(days=5)).strftime(DATE_FORMAT)
    order = {
        "customer_name": customer_name,
        "product_name": product_name,
        "quantity": quantity,
        "status": "Processing",
        "delivery_date": delivery_date,
        "location": delivery_location 
    }
    if alert := validate_order_fields(order):
        return alert
    orders[order_id] = order
    save_order(orders)
    logger.info(f"Order: {order} added successfully!!!")
    return f"Order ID: {order_id} added successfully."

def update_order_status(order_id, new_status):
    """
    Function to update order status
    """
    orders = load_orders()
    order = orders.get(order_id)
    if not order:
        logger.warning(f"Order ID: {order_id} not found.")
        return f"Order ID: {order_id} not found."
    order["status"] = new_status
    orders[order_id] = order
    save_order(orders)
    logger.info(f"Order ID: {order_id}, status: {new_status} updated successfully!!!")
    return f"Order ID: {order_id}, status: {new_status}  updated successfully."

def track_order(order_id):
    """
    Function to fetch a specific order
    """
    orders = load_orders()
    order = orders.get(order_id)
    if not order:
        logger.warning(f"Order not found for ID:{order_id}")
        return f"Order ID: {order_id} not found"
    logger.info(f"Order ID : {order_id} found successfully")
    return order

def cancel_order(order_id):
    """
    Function to cancel an order
    """
    orders = load_orders()
    order = orders.get(order_id)
    if not order:
        logger.warning(f"Order not found for ID:{order_id}")
        return f"Order ID: {order_id} not found"
    if order["status"] != "Processing":
        logging.warning(f"Order ID:{order_id} cannot be cancelled!!!")
        return f"Order ID:{order_id} cannot be cancelled successfully"
    del orders[order_id]
    save_order(orders)
    logger.info("Order ID:{order_id} cancelled successfully!!!")
    return f"Order {order_id} cancelled successfully"
    
order1 = ("A001", "John Doe", "Laptop", 1, "New York")
order2 = ("A002", "Jane Smith", "Smartphone", 2, "Los Angeles")
order3 = ("A003", "Alice Johnson", "Headphones", 3, "Chicago")
order4 = ("A004", "Bob Brown", "Tablet", 1, "Houston")
order5 = ("A005", "Charlie Davis", "Camera", 2, "Phoenix")
order6 = ("A006", "David Wilson", "Smartwatch", 1, "Philadelphia")
order7 = ("A007", "Eva Martinez", "Printer", 1, "San Antonio")

orders = [order1, order2, order3, order4, order5, order6, order7]

# for order in orders:
#     create_order(*order)

# print(track_order("A007"))

# print(update_order_status("A007", "Shipped"))

# print(cancel_order("A006"))
# print(cancel_order("A007"))