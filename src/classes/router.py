import random


class Router:

    def __init__(self, id, virus, neighbors, devices, firewall):
        self.id = id
        self.virus = virus
        # Neighbor routers
        self.neighbors = neighbors
        self.devices = devices
        self.firewall = firewall

    def setVirus(self, virus):
        self.virus = virus

    def setDevices(self, devices):
        self.devices = devices

    def setNeighbors(self, neighbors):
        self.neighbors = neighbors

    # This method simulates the process of routing an IP package through the Internet
    def routePackage(self, virus):
        # If we are sending a virus, calculate where it is heading to
        if virus != None:
            routingProbability = random.randrange(0, 100)
            # 50% probability to route package outside the system (geographically far away)
            if routingProbability > 50:
                # 50% probability to route package to a neighbor network
                if routingProbability > 95:
                    # 5% probability to route package to a device on the same network
                    if self.devices != None:
                        targetDevice = self.devices[
                            random.randrange(0, len(self.devices))
                        ]
                        targetDevice.setVirus(virus)
                else:
                    if self.neighbors != None:
                        targetRouter = self.neighbors[
                            random.randrange(0, len(self.neighbors))
                        ]
                        # Check if target router has a firewall
                        if not (targetRouter.firewall):
                            targetRouter.routePackage(virus)
