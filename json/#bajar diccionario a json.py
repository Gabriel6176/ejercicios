#bajar diccionarios a archivo json

import json
import os

path, _ = os.path.split(os.path.abspath(__file__))

data = {}

data["Empresa"] = "Python"

data["Clients"] = []

data["Clients"].append({
    "first_name": "XXX",
    "last_name": "Gomez",
    "age": "28",
    "ammount" : 7.17}) 

data["Clients"].append({
    "first_name": "YYY",
    "last_name": "Perez",
    "age": "29",
    "ammount" : 8.18}) 

data["Clients"].append({
    "first_name": "ZZZ",
    "last_name": "Ruiz",
    "age": "30",
    "ammount" : 9.19}) 

with open(path+f"/archivo.json", "w") as file:
    json.dump(data, file, indent=4)

    
