# Production Line Status Monitor 
import json 
from datetime import datetime
FILE_NAME = '_manufacturing/_production/production.json'

def load_status():
    try:
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
    
def save_status(status_data):
    with open(FILE_NAME, 'w') as file:
        json.dump(status_data, file, indent=4)

def get_status(machine_id):
    production_status = load_status()
    status = production_status.get(machine_id, f"Machine {machine_id} not found.")
    return status

def generate_production_report():
    production_status = load_status()
    running_count = sum(1 for machine in production_status.values() if machine['status']=='Running')
    idle_count = sum(1 for machine in production_status.values() if machine['status']=='Idle')
    error_count = sum(1 for machine in production_status.values() if machine['status']=='Error')
    return f"Running: {running_count}, Idle: {idle_count}, Error:{error_count}"

def update_machine_status(machine_id, status, efficiency):
    production_status = load_status()
    if machine_id not in production_status:
        return f"Machine {machine_id} does not exists"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    production_status[machine_id]["status"] = status
    production_status[machine_id]["efficiency"] = efficiency
    production_status[machine_id]["last_updated"] = timestamp
    save_status(production_status)
    if status=="Error":
        return f"Machine {machine_id} failure detected"
    elif efficiency<50:
        return f"Machine {machine_id} have low efficiency"
    return f"Machine {machine_id} updated successfully"

production_data = {
    "M001": {"status": "Running", "efficiency": 85, "last_updated": "2024-02-20 12:30:00"},
    "M002": {"status": "Idle", "efficiency": 60, "last_updated": "2024-02-20 12:35:00"},
    "M003": {"status": "Error", "efficiency": 30, "last_updated": "2024-02-20 12:40:00"}
}
# save_status(production_data) 
# print(update_machine_status("M002", "Error", 80))
# print(update_machine_status("M001", "Running", 20))
# print(get_status("M003"))
# print(generate_production_report())