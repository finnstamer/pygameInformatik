from typing import List

# Klasse zur Verwahrung aller nötigen Objekte und des Übertragens auf den Bildschirm, sowie der De- und Aktivierung dieser.
class Level():
    def __init__(self, id: int, *objects: object) -> None:
        self.active = False
        self.id = id
        self.objects = []
        self.nonFluidSolids = []
        self.solids = []
        self.add(*list(objects))

    def draw(self):
        for obj in self.objects:
            obj.draw()

    def add(self, *objs: object):
        for obj in list(objs):
            if obj not in self.objects:
                self.objects.append(obj)
        self.update()
    
    def set(self, *objs: object):
        self.objects = []
        self.add(*objs)
    
    def remove(self, *objs: object):
        for obj in list(objs):
            if obj in self.objects:
                self.objects.remove(obj)
        self.update()
    
    def deactivate(self):
        self.active = False
        for obj in self.objects:
            obj.active = False

    def activate(self):
        self.active = True
        for obj in self.objects:
            obj.active = True

    def update(self):
        self.updateNonFluidSolids()
        self.updateSolids()
        
    def updateNonFluidSolids(self):
        self.nonFluidSolids = list(filter(lambda x: x.solid and not x.fluid and x.active, self.objects))
        return self
        
    def updateSolids(self):
        self.solids = list(filter(lambda x: x.solid and x.active, self.objects))
        return self

    def negativeObjects(self, objs: List[object], allObjects = None) -> object:
        return list(filter(lambda x: x not in objs, self.objects if allObjects is None else allObjects))