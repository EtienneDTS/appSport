from datetime import datetime
import json
import copy

def get_date()-> str:
    return datetime.today().strftime('%Y-%m-%d')

def extract_data(filename: str)-> dict:
    with open(filename, "r") as f:
        data = json.load(f)
    return data
 
def save_data(data: dict, filename: str)-> None:
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
        
def save_backup(data: dict, date: str)-> None:
    with open(f"./saves/{date}.json", "w") as f:
        json.dump(data, f, indent=4)

def add_set(data: dict, date: str, type: str, exercice: str, reps: int, weight: float)-> dict:
    if date not in data["data"]:
        data["data"][date] = {}
        value = copy.deepcopy(data["head"][type]["builder"])
        data["data"][date][type] = value
    data["data"][date][type][exercice]["Reps"] = reps
    data["data"][date][type][exercice]["Weight"] = weight
    data["data"][date][type][exercice]["RM"] = weight * (1 + 0.0333 * reps)
    data["head"][type]["save"][exercice]["Reps"] = reps
    data["head"][type]["save"][exercice]["Weight"] = weight
    data["head"][type]["save"][exercice]["RM"] = weight * (1 + 0.0333 * reps)

def get_data(data: dict, date: str)-> dict:
    return data["data"][date]

def get_all_exercices(data: dict)-> dict:
    return data["head"]["all_exercices"]

def get_types(data: dict)-> list:
    return data["head"]["types"]

def get_exercices(data: dict, type: str)-> dict:
    return data["head"][type]["exercices"]

def get_save(data: dict, type: str)-> dict:
    return data["head"][type]["save"]