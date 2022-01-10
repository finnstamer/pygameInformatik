from typing import List

# Klasse zur Verwahrung aller nötigen Objekte und des Übertragens auf den Bildschirm, sowie der De- und Aktivierung dieser.
class Level():
    def __init__(self, id: int, *objects: object) -> None:
        self.id = id
        self.objects = list(objects)

    def draw(self):
        for obj in self.objects:
            obj.draw()

    def add(self, *objs: object):
        for obj in list(objs):
            if obj not in self.objects:
                self.objects.append(obj)
    
    def remove(self, *objs: object):
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
        return list(filter(lambda x: x.solid and x.active, self.objects))

    def negativeObjects(self, objs: List[object]) -> object:
        return list(filter(lambda x: x not in objs, self.objects))