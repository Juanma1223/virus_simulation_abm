from classes.device.device import Device
import random


# Device type 1
class Phone(Device):
    def __init__(self, id, name, virus, neighbors, gateway, securityLevel):
        # This instance parameter defines a random parameter to emulate user's cautiousness
        # If infectionProbability is high then the user is not a cautious one and is more prone to be infected
        self.infectionProbability = random.randrange(1, 100)
        super().__init__(id, name, virus, neighbors, gateway, securityLevel)

    def randomAction(self):
        self.sendMessages()

    def setVirus(self, virus, init=False):
        # If init is true, we are initializing this device as infected and no probability should be calculated
        if init:
            return super().setVirus(virus)
        # Generate a random number and check if it higher than user infectionProbability
        if random.randrange(0, 100) > self.infectionProbability:
            return super().setVirus(virus)

    def sendMessages(self):
        if self.virus:
            messagesQuantity = random.randrange(0, 9)
            for _ in range(0, messagesQuantity):
                # If virus is self replicating it will send itself on each message
                if self.virus.selfReplicating:
                    self.gateway.routePackage(self.virus)
                else:
                    # If not, there is a change the user is sending an infected file
                    sendVirusProbability = random.randrange(0, 100)
                    if sendVirusProbability > 50:
                        self.gateway.routePackage(self.virus)
