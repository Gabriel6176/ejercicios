#cargar archivo json

import json
import os

path, _ = os.path.split(os.path.abspath(__file__))

with open(path+"/archivo.json") as file:
    data = json.load(file)

print(type(data))

for client in data["Clients"]:
    print("")
    print("First Name: ", client ["first_name"])
    print("Last Name: ", client ["last_name"])
    print("Age: ", client ["age"])
    print("Ammount: ", client ["ammount"])

