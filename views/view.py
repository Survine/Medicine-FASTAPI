import json
from datetime import date
from pathlib import Path

DB_FILE = Path("database.json")

def read_data():
    if not DB_FILE.exists():
        return []
    with open(DB_FILE, "r") as f:
        return json.load(f)

def write_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4, default=str)

# CREATE
def create_medicine(name, price, quantity, power, mfd, exp):
    data = read_data()
    new_id = max((med["id"] for med in data), default=0) + 1
    new_medicine = {
        "id": new_id,
        "name": name,
        "price": price,
        "quantity": quantity,
        "power": power,
        "mfd": str(mfd),
        "exp": str(exp)
    }
    data.append(new_medicine)
    write_data(data)
    return new_medicine

# READ ALL
def get_all_medicines():
    return read_data()

# READ ONE
def get_medicine_by_id(med_id):
    data = read_data()
    for med in data:
        if med["id"] == med_id:
            return med
    return None

# UPDATE
def update_medicine(med_id, **kwargs):
    data = read_data()
    for med in data:
        if med["id"] == med_id:
            med.update(kwargs)
            write_data(data)
            return med
    return None

# DELETE
def delete_medicine(med_id):
    data = read_data()
    updated_data = [med for med in data if med["id"] != med_id]
    if len(updated_data) == len(data):
        return False  # No match
    write_data(updated_data)
    return True
