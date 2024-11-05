class Building:

    def __init__(self, id, name, isCompany, routers):
        self.id = id
        self.name = name
        self.isCompany = isCompany
        self.routers = routers

    def addRouter(self, newRouter):
        self.routers.append(newRouter)
        for router in self.routers:
            if router.neighbors != None:
                router.neighbors.append(newRouter)
            else:
                router.neighbors = [newRouter]
