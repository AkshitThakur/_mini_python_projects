# Medicine Stock Management
import json

from pathlib import Path
DIR = Path("_health")
FILE_NAME = DIR / "medicine_stock.json"
LOG_FILE = DIR / "medicine_stock.log"
DATE_FORMAT = "%Y-%m-%d"
DEFAULT_THRESHOLD = 100
from datetime import datetime
REQUIRED_FIELDS = ("name", "quantity", "expiry_date", "supplier")
import logging


logging.basicConfig(
    filename= LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)

def load_stocks():
    try:
        with FILE_NAME.open('r', encoding="utf-8") as file:
            medicines =  json.load(file)
            logger.info("Medicine stock loaded successfully.")
            return medicines
    except (FileNotFoundError, json.JSONDecodeError):
        logger.error("medicine_stock.json is corrupted.")
        return {}

def save_stock(_medicines):
    with FILE_NAME.open('w', encoding="utf-8") as file:
        json.dump(_medicines, file, indent=4, ensure_ascii=False)
    logger.info("Medicine stock saved successfully.")

def validate_medicine_data(_medicine):
    for field in REQUIRED_FIELDS:
        if field not in _medicine:
            logger.warning(f"Validation failed. Missing field: {field}")
            return f"Invalid Field {field}"

def add_medicine(_load_medicine_stocks, _medicine_id, _name, _quantity, _expiry_date, _supplier):
    if _medicine_id in _load_medicine_stocks.keys():
        logger.warning(f"Duplicate medicine attempted. ID={_medicine_id}")
        return f"Medicine {_name} already exists !!!"
    if _quantity < 0:
        raise ValueError("Quantity cannot be negative")
    if not _supplier.strip():
        raise ValueError("Supplier cannot be empty.")
    _medicine = {
        "name" : _name,
        "quantity" : _quantity,
        "expiry_date" : _expiry_date,
        "supplier" : _supplier
    }
    if alert := validate_medicine_data(_medicine):
        return alert
    _load_medicine_stocks[_medicine_id] = _medicine
    save_stock(_load_medicine_stocks)
    logger.info(f"Medicine added. ID={_medicine_id}, Name={_name}, Quantity={_quantity}")
    return f"Medicine {_name} added successfully !!!"

def get_medicine(_load_medicine_stocks, _medicine_id):
    medicine = _load_medicine_stocks.get(_medicine_id)
    if medicine:
        logger.info(f"Medicine searched: {_medicine_id}")
        return medicine
    logger.warning(f"Medicine not found: {_medicine_id}")
    return "Medicine Record Not Found"

def check_expired_medicines(_load_medicine_stocks):
    expired_medicines = [
        _id 
        for _id, _details in _load_medicine_stocks.items()
        if datetime.strptime(_details["expiry_date"], DATE_FORMAT).date() < datetime.today().date()
    ]
    logger.info(f"Expired medicines checked. Found {len(expired_medicines)} medicines.")
    return expired_medicines

def remove_expired_medicines(_load_medicine_stocks):
    expired_medicines_ids = check_expired_medicines(_load_medicine_stocks)
    for _id in expired_medicines_ids:
        logger.info(f"Removing expired medicine {_id}")
        del _load_medicine_stocks[_id]
    save_stock(_load_medicine_stocks)
    logger.info(f"{len(expired_medicines_ids)} expired medicines removed.")
    return f"{len(expired_medicines_ids)} expired medicines are removed form the stock"

def check_low_stocks(_load_medicine_stocks, _medicine_id, _threshold):
    if _medicine_id not in _load_medicine_stocks.keys():
        return "Medicine record not sfound"
    if _load_medicine_stocks[_medicine_id]["quantity"] < _threshold:
        logger.warning(f"Low stock detected for {_medicine_id}")
        return f"Low stock for medicine {_load_medicine_stocks[_medicine_id]["name"]}"
    return "Stock level are sufficient"

_load_medicine_stocks = load_stocks()

_medicine1 = ("M001", "Paracetamol", 100, "2025-12-31", "ABC Pharma")
_medicine2 = ("M002", "Ibuprofen", 50, "2028-06-30", "XYZ Pharma")
_medicine3 = ("M003", "Amoxicillin", 200, "2026-03-15", "LMN Pharma")
_medicine4 = ("M004", "Cetirizine", 75, "2023-09-30", "PQR Pharma")
_medicine5 = ("M005", "Metformin", 150, "2024-11-30", "DEF Pharma")
_medicine6 = ("M006", "Aspirin", 80, "2027-08-31", "GHI Pharma")

_medicines = [_medicine1, _medicine2, _medicine3, _medicine4, _medicine5, _medicine6]

print(validate_medicine_data({
    "name": "Aspirin",
    "quantity": 80,
    "expir_date": "2027-08-31",
    "supplier": "GHI Pharma"
}))

print(remove_expired_medicines(_load_medicine_stocks))

for medicine in _medicines:
    print(check_low_stocks(_load_medicine_stocks, medicine[0], DEFAULT_THRESHOLD))

print(check_expired_medicines(_load_medicine_stocks))

for medicine in _medicines:
    print(get_medicine(_load_medicine_stocks, medicine[0]))

for medicine in _medicines:
    print(add_medicine(_load_medicine_stocks, *medicine))


