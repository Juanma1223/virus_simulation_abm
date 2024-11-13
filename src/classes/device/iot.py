from classes.device.device import Device


# Device type 3
class IoT(Device):
    def __init__(self, id, name, virus, neighbors, gateway, securityLevel):
        super().__init__(id, name, virus, neighbors, gateway, securityLevel)

    def randomAction(self):
        # if(self.virus != None):
        #     if self.virus.networkPropagation:
        #         self.gateway.routePackage(self.virus)
        return super().randomAction()
