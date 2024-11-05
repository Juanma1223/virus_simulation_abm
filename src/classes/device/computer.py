from classes.device.device import Device
import random


# Device type 1
class Computer(Device):
    def __init__(self, id, name, virus, neighbors, gateway, securityLevel):
        super().__init__(id, name, virus, neighbors, gateway, securityLevel)
        # This instance parameter defines a random parameter to emulate user's cautiousness
        # If infectionProbability is high then the user is not a cautious one and is more prone to be infected
        self.infectionProbability = random.randrange(1, 100)

    def setVirus(self, virus, init=False):
        # If init is true, we are initializing this device as infected and no probability should be calculated
        if init:
            return super().setVirus(virus)
        # Generate a random number and check if it higher than user infectionProbability
        if random.randrange(0, 100) > self.infectionProbability:
            return super().setVirus(virus)

    def randomAction(self):
        randAction = random.randrange(0,2)
        if(randAction == 0):
            self.sendEmail()
        else:
            self.detectVirus()

    def sendEmail(self):
        if self.virus:
            emailsQuantity = random.randrange(0, 3)
            for _ in range(0, emailsQuantity):
                # If virus is self replicating it will send itself on each email
                if self.virus.selfReplicating:
                    self.gateway.routePackage(self.virus)
                else:
                    # If not, there is a change the user is sending an infected file
                    sendVirusProbability = random.randrange(0, 100)
                    if sendVirusProbability > 50:
                        self.gateway.routePackage(self.virus)

    def detectVirus(self):
        # Virus detection probability is inversely proportional to infectionProbability
        detectionProbability = 100 - self.infectionProbability
        if random.randrange(0, 100) > detectionProbability:
            self.virus = None
            print(f"Computer {self.id} detected the virus and deleted it!")
