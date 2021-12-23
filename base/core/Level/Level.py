from typing import List
from base.object.GameObject import GameObject

class Level():
    def __init__(self, id: int, *objects: GameObject) -> None:
        self.id = id
        self.objects = list(objects)

    def getObject(self, id: int):
        f = list(filter(lambda g: g.id == id, self.objects))
        return f[0] if len(f) > 0 else None

    def draw(self):
        for obj in self.objects:
            obj.draw()

    def add(self, *objs: GameObject):
        for obj in list(objs):
            if obj not in self.objects:
                self.objects.append(obj)
    
    def remove(self, *objs: GameObject):
        for obj in list(objs):
            if obj in self.objects:
                self.objects.remove(obj)
    
    def deactivate(self):
        for obj in self.objects:
            obj.active = False

    def activate(self):
        for obj in self.objects:
            obj.active = True
        
    def allSolidObjects(self):
        return list(filter(lambda x: x.solid, self.objects))

    def negativeObjects(self, objs: List[GameObject]) -> GameObject:
        return list(filter(lambda x: x not in objs, self.objects))