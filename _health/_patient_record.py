# Patient Record Management 
import json
from pathlib import Path
FILE_NAME = Path("_health")/"patient_records.json" 
REQUIRED_FIELDS = ("name", "age", "gender", "medical_history")

def load_records():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_records(_records):
    try:
        with open(FILE_NAME, "w") as file:
            json.dump(_records, file, indent=4)
    except Exception as err:
        print(f"Error : {err}")

def add_patient(_records, _id, _name, _age, _gender, _history):
    if _id in _records:
        return "Patient record already exists." 
    _records[_id] = {
        "name": _name,
        "age": _age,
        "gender": _gender,
        "medical_history": _history 
    }
    save_records(_records)
    return f"Patient {_name} added successfully!" 
    
def get_patient(_records, _id):
    return _records.get(_id, "Patient record not found.")

def update_medical_history(_records, _id, _new_history):
    _patient = _records.get(_id)
    if _patient is None:
        return "Patient record not found."
    _records[_id]["medical_history"].append(_new_history)
    save_records(_records)
    return f"Medical history updated for {_patient['name']}." 

def delete_patient(_records, _id):
    if _id not in _records:
        return "Patient record not found."
    del _records[_id]
    save_records(_records)
    return f"Patient record with ID {_id} deleted successfully."

def validate_patient(_patient):
    _missing = [_field for _field in REQUIRED_FIELDS if _field not in _patient]
    if _missing:
        return f"Missing field {', '.join(_missing)}" 
    return "All fields are valid!"

def store_patient_in_database(patient): 
    sql_query = f"INSERT INTO patients (name, age, gender, medical_history) VALUES ('{patient['name']}', {patient['age']}, '{patient['gender']}', '{','.join(patient['medical_history'])}')" 
    return f"Patient record inserted into database: {sql_query}"

_patient1 = ("001", "John Doe", 32, "Male", ["Diabetes", "Hypertension"])
_patient2 = ("002", "Jane Smith", 28, "Female", ["Asthma"])
_patient3 = ("003", "Alice Johnson", 45, "Female", ["Arthritis"])
_patient4 = ("004", "Bob Brown", 50, "Male", ["Heart Disease"])
_patient5 = ("005", "Charlie Davis", 38, "Male", ["High Cholesterol"])
_records = load_records()

# _patients = [_patient1, _patient2, _patient3, _patient4, _patient5]
# for _pat in _patients:
#     print(add_patient(_records, *_pat))

# print(delete_patient(_records, "002"))

# patient_f1 = {"name": "Alice", "age": 28, "gender": "Female", "medical_history": ["Asthma"]} 
# patient_f2 = {"name": "Bob", "gender": "Male"} 
# print(validate_patient(patient_f1)) 
# print(validate_patient(patient_f2)) 

# print(update_medical_history(_records, "005", "High BP"))
# print(get_patient(_records, "005"))