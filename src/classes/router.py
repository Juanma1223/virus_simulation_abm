class Router:
    
    def __init__(self,id,virus,neighbors,devices,firewall):
        self.id = id
        self.virus = virus
        self.neighbors = neighbors
        self.devices = devices
        self.firewall = firewall
        
    def setVirus(self,virus):
        self.virus = virus
        
    def setDevices(self,devices):
        self.devices = devices