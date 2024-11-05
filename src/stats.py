def CalcInfectedDevices(buildings):
    totalInfected = 0
    for building in buildings:
        for router in building.routers:
            if router.devices != None:
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
            if router.devices != None:
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
        currentInfected = 0
        for router in building.routers:
            if router.devices != None:
                for device in router.devices:
                   totalDevices += 1
    return totalDevices
