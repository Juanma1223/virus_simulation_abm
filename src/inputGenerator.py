import json
import random

# Amount of simulated buildings
buildingCount = 3
# Amount of routers inside each building
routersPerBuilding = 1
# Amount of devices on each network
devicesPerRouter = 15

data = {
    "buildings": [],
    "virus": {
        "name": "Trojan",
        "sentByMail": True,
        "sentByMessage": True,
        "networkPropagation": True,
        "selfReplicating": True,
    },
    "steps": 10000,
}

device_types = ["Phone", "Computer", "IoT"]
type_mapping = {"Phone": 2, "Computer": 1, "IoT": 3}

for b in range(buildingCount):
    building = {
        "name": f"Building {b+1}",
        "routers": [],
        "isCompany": random.choice([True, False]),
    }
    for r in range(routersPerBuilding):
        router = {
            "devices": [],
            # "firewall": random.choice([True, False]),
            "firewall": False,
            "virus": False,
        }
        for d in range(devicesPerRouter):
            device_type = random.choice(device_types)
            device = {
                "name": f"{device_type} {d+1}",
                "type": type_mapping[device_type],
                # "virus": random.choice([True, False]),
                "virus": False,
                "securityLevel": random.randint(1, 5),
            }
            router["devices"].append(device)
        building["routers"].append(router)
    data["buildings"].append(building)

with open("input.json", "w") as f:
    json.dump(data, f, indent=4)
