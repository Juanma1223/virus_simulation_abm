from classes.device.computer import Computer
from classes.device.phone import Phone
from classes.device.iot import IoT


def CalcInfectedDevices(buildings):
    totalInfected = 0
    for building in buildings:
        for router in building.routers:
            if router.devices != None and router.nexus == False:
                for device in router.devices:
                    if device.virus != None:
                        totalInfected += 1
    return totalInfected


def CalcMostInfectedBuilding(buildings):
    maxInfected = ""
    maxInfectedAmount = 0
    for building in buildings:
        currentInfected = 0
        for router in building.routers:
            if router.devices != None and router.nexus == False:
                for device in router.devices:
                    if device.virus != None:
                        currentInfected += 1
        if currentInfected > maxInfectedAmount:
            maxInfectedAmount = currentInfected
            maxInfected = building.name
    return maxInfected


def CalcTotalDevices(buildings):
    totalDevices = 0
    for building in buildings:
        for router in building.routers:
            if router.devices != None and router.nexus == False:
                for device in router.devices:
                    totalDevices += 1
    return totalDevices


def CalcMostInfectedDeviceType(buildings):
    deviceTypes = ["Computer", "Phone", "IoT"]
    deviceTypesInfections = [0, 0, 0]
    for building in buildings:
        for router in building.routers:
            if router.devices != None and router.nexus == False:
                for device in router.devices:
                    if device.virus != None:
                        if type(device) is Computer:
                            deviceTypesInfections[0] += 1
                        elif type(device) is Phone:
                            deviceTypesInfections[1] += 1
                        elif type(device) is IoT:
                            deviceTypesInfections[2] += 1

    maxTypeInfections = 0
    maxTypeIndex = 0
    i = 0
    for amount in deviceTypesInfections:
        if amount > maxTypeInfections:
            maxTypeInfections = amount
            maxTypeIndex = i
        i += 1

    return deviceTypes[maxTypeIndex]
