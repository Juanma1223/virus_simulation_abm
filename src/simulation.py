from classes.virus import Virus
from classes.building import Building
from classes.router import Router
from classes.device.device import Device
from classes.device.computer import Computer
from classes.device.phone import Phone
from classes.device.iot import IoT
import stats
import time

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
        data["virus"]["selfReplicating"],
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
                        "Computer " + str(devicesCurrentId),
                        None,
                        None,
                        newRouter,
                        currentDevice["securityLevel"],
                    )
                elif currentDevice["type"] == 2:
                    newDevice = Phone(
                        devicesCurrentId,
                        "Phone " + str(devicesCurrentId),
                        None,
                        None,
                        newRouter,
                        currentDevice["securityLevel"],
                    )
                elif currentDevice["type"] == 3:
                    newDevice = IoT(
                        devicesCurrentId,
                        "IoT " + str(devicesCurrentId),
                        None,
                        None,
                        newRouter,
                        currentDevice["securityLevel"],
                    )
                if currentDevice["virus"]:
                    newDevice.setVirus(virus, True)
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
        # Set routers neighbors to connect them with each other
        for router in buildingRouters:
            router.setNeighbors(buildingRouters)
        buildings.append(newBuilding)
        buildingsCurrentId += 1
    # Connect buildings using an extra router between them
    for i in range(0, len(buildings) - 1):
        newRouter = Router(routersCurrentId, None, None, None, False)
        buildings[i].addRouter(newRouter)
        buildings[i + 1].addRouter(newRouter)
        routersCurrentId += 1
    StartSimulation(buildings, data["steps"])


def StartSimulation(buildings, steps):
    maxInfected = 0
    maxInfectedTime = 0
    startTime = time.time()
    for i in range(0, steps):
        for building in buildings:
            for router in building.routers:
                if router.devices != None:
                    for device in router.devices:
                        device.randomAction()
        currentInfected = stats.CalcInfectedDevices(buildings)
        if currentInfected > maxInfected:
            maxInfected = currentInfected
            maxInfectedTime = i
        print("############################")
        print("STEP:", i)
        print("############################")

    totalDevices = stats.CalcTotalDevices(buildings)
    
    endTime = time.time()

    totalStats = f"""
    #########################
    #########################
    Simulation statistics:
    -------------------------
    Peak infected devices: {maxInfected}/{totalDevices}
    -------------------------
    Steps to reach peak infection: {maxInfectedTime}/{steps}
    -------------------------
    Final infected devices: {stats.CalcInfectedDevices(buildings)}
    -------------------------
    Most infected building: {stats.CalcMostInfectedBuilding(buildings)}
    -------------------------
    Most infected device type: {stats.CalcMostInfectedDeviceType(buildings)}
    -------------------------
    Simulation total time: {int(endTime-startTime)} seconds
    ########################
    ########################
    """
    
    f = open("stats.txt","w")
    f.write(totalStats)
