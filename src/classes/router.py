import random


class Router:

    def __init__(self, id, virus, neighbors, devices, firewall, nexus):
        self.id = id
        self.virus = virus
        # Neighbor routers
        self.neighbors = neighbors
        self.devices = devices
        self.firewall = firewall
        self.nexus = nexus

    def setVirus(self, virus):
        self.virus = virus

    def setDevices(self, devices):
        self.devices = devices

    def setNeighbors(self, neighbors):
        self.neighbors = neighbors

    # This method simulates the process of routing an IP package through the Internet
    def routePackage(self, virus, visitedRouters=[], ttl=10):
        # If we are sending a virus, calculate where it is heading to
        if virus != None and ttl > 0:
            routingProbability = random.randrange(0, 100)
            # 50% probability to route package outside the system (geographically far away)
            if routingProbability > 30:
                # 50% probability to route package to a neighbor network
                if routingProbability > 50:
                    # 5% probability to route package to a device on the same network
                    if self.devices != None:
                        targetDevice = self.devices[
                            random.randrange(0, len(self.devices))
                        ]
                        targetDevice.setVirus(virus)
                else:
                    if self.neighbors != None:
                        # Avoid already visisted routers to create a new path
                        targetRouter = self.neighbors[
                            random.randrange(0, len(self.neighbors))
                        ]
                        # while targetRouter.id in visitedRouters:
                        #     targetRouter = self.neighbors[
                        #         random.randrange(0, len(self.neighbors))
                        #     ]
                        # Check if target router has a firewall
                        if not (targetRouter.firewall):
                            visitedRouters.append(targetRouter.id)
                            targetRouter.routePackage(virus, visitedRouters, ttl - 1)
