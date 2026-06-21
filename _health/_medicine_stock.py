# Medicine Stock Management
import json
from pathlib import Path
from datetime import datetime
FILE_NAME = Path('_health/medicine_stock.json')
THRESHOLD = 100
REQUIRED_FIELDS = ("name", "quantity", "expiry_date", "supplier")

def load_stocks():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_stock(_medicines):
    with open(FILE_NAME, 'w') as file:
        json.dump(_medicines, file, indent=4)

def validate_medicine_data(_medicine):
    for field in REQUIRED_FIELDS:
        if field not in _medicine.keys():
            return f"Invalid Field {field}"


def add_medicine(_load_medicine_stocks, _medicine_id, _name, _quantity, _expiry_date, _supplier):
    if _medicine_id in _load_medicine_stocks.keys():
        return f"Medicine {_name} already exists !!!"
    _medicine = {
        "name" : _name,
        "quantity" : _quantity,
        "expiry_date" : _expiry_date,
        "supplier" : _supplier
    }
    if alert := validate_medicine_data(_medicine):
        return f"{alert}"
    _load_medicine_stocks[_medicine_id] = _medicine
    save_stock(_load_medicine_stocks)
    return f"Medicine {_name} added successfully !!!"

def get_medicine(_load_medicine_stocks, _medicine_id):
    return _load_medicine_stocks.get(_medicine_id, "Medicine Record Not Found")

def check_expired_medicines(_load_medicine_stocks):
    today = datetime.today().strftime("%Y-%m-%d")
    expired_medicines = {
        _id : _details
        for _id, _details in _load_medicine_stocks.items()
        if _details["expiry_date"] < today
    }
    return (
        list(expired_medicines)
        if expired_medicines
        else
        "No expired medicine found"
    )

def remove_expired_medicines(_load_medicine_stocks):
    expired_medicines_ids = check_expired_medicines(_load_medicine_stocks)
    for medicine_id in expired_medicines_ids:
        del _load_medicine_stocks[medicine_id]
    save_stock(_load_medicine_stocks)
    return f"{len(expired_medicines_ids)} expired medicines are removed form the stock"

def check_low_stocks(_load_medicine_stocks, _medicine_id, _threshold):
    if _medicine_id not in _load_medicine_stocks.keys():
        return "Medicine record not sfound"
    if _load_medicine_stocks[_medicine_id]["quantity"] < _threshold:
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

def sync_inventory_with_database(medicine):
    sql_query = f"INSERT INTO medicine_stock (name, quantity, expiry_date, supplier) VALUES ('{medicine['name']}', {medicine['quantity']}, '{medicine['expiry_date']}', '{medicine['supplier']}')"
    return f"Medicine record synced with database: {sql_query}"


# print(validate_medicine_data({
#     "name": "Aspirin",
#     "quantity": 80,
#     "expir_date": "2027-08-31",
#     "supplier": "GHI Pharma"
# }))

# print(remove_expired_medicines(_load_medicine_stocks))

# for medicine in _medicines:
#     print(check_low_stocks(_load_medicine_stocks, medicine[0], THRESHOLD))

# print(check_expired_medicines(_load_medicine_stocks))

# for medicine in _medicines:
#     print(get_medicine(_load_medicine_stocks, medicine[0]))

# for medicine in _medicines:
#     print(add_medicine(_load_medicine_stocks, *medicine))


