class Device:
    
    
    def __init__(self, id, name, virus, neighbors, gateway, securityLevel):
        self.id = id
        self.name = name
        self.virus = virus
        self.neighbors = neighbors
        self.gateway = gateway
        self.securityLevel = securityLevel

    # This function is called when a step goes forward, representing the agent's action
    # This should be implemented independently for each device
    def randomAction(self):
        pass
    
    def setVirus(self,virus):
        self.virus = virus
