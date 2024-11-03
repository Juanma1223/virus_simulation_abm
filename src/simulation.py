from classes.virus import Virus
from classes.building import Building
from classes.router import Router
from classes.device.device import Device
from classes.device.computer import Computer
from classes.device.phone import Phone
from classes.device.iot import IoT


# This function reads the json input and initializes the simulation with it's initial values
def InitSimulation(data):
    routersCurrentId = 0
    devicesCurrentId = 0
    buildingsCurrentId = 0
    buildings = []
    # Get virus simulated data
    virus = Virus(
        data["virus"]["name"],
        data["virus"]["sentByMail"],
        data["virus"]["networkPropagation"],
    )
    for building in data["buildings"]:
        buildingRouters = []
        for currentRouter in building["routers"]:
            routerDevices = []
            newRouter = Router(
                routersCurrentId, None, None, None, currentRouter["firewall"]
            )
            for currentDevice in currentRouter["devices"]:
                newDevice = None
                if currentDevice["type"] == 1:
                    newDevice = Computer(
                        devicesCurrentId,
                        currentDevice["name"],
                        None,
                        None,
                        newRouter,
                        currentDevice["securityLevel"],
                    )
                elif currentDevice["type"] == 2:
                    newDevice = Phone(
                        devicesCurrentId,
                        currentDevice["name"],
                        None,
                        None,
                        newRouter,
                        currentDevice["securityLevel"],
                    )
                elif currentDevice["type"] == 3:
                    newDevice = IoT(
                        devicesCurrentId,
                        currentDevice["name"],
                        None,
                        None,
                        newRouter,
                        currentDevice["securityLevel"],
                    )
                if currentDevice["virus"]:
                    newDevice.setVirus(virus)
                devicesCurrentId += 1
                routerDevices.append(newDevice)
            routersCurrentId += 1
            newRouter.setDevices(routerDevices)
            # Check if router should start infected
            if currentRouter["virus"]:
                newRouter.setVirus(virus)
            buildingRouters.append(newRouter)
        newBuilding = Building(
            buildingsCurrentId, building["name"], building["isCompany"], buildingRouters
        )
        buildings.append(newBuilding)
        buildingsCurrentId += 1
    StartSimulation(buildings, data["steps"])


def StartSimulation(buildings, steps):
    for i in range(0, steps):
        print(buildings)
