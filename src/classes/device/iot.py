from classes.device.device import Device


# Device type 3
class IoT(Device):
    def __init__(self, id, name, virus, neighbors, gateway, securityLevel):
        super().__init__(self, id, name, virus, neighbors, gateway, securityLevel)
