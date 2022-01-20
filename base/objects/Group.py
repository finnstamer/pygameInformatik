import typing
import pygame
from typing import List

from base.core.Object.GameObject import GameObject
from base.geometry.Rectangle import Rectangle

# Klasse zur Gruppierung mehrerer Objekte. 
# Ehemals nötig zur Verwendung von Objekten. Nun eher deprecated.
class Group():
    def __init__(self, *obj: GameObject) -> None:
        self.constructor = None
        self.objects: List[GameObject] = list(obj)
    
    # Das * for einem Parameter bedeutet, dass man von da an unendlich objekte anhängen kann. Der Paramter obj ist dann eine List aus Objekten
    # bspw: Group().add(obj1, obj2, obj3, obj4, ...)
    def add(self, *obj: GameObject):
        self.objects = self.objects + list(obj)
        return self
    
    # Funktion um alle .draw Funktionen der Objekte der Gruppe auszulösen
    def draw(self):
        for obj in self.objects:
            obj.draw()
        return self
    
    def remove(self, obj):
        self.objects.remove(obj)
        return self
    
    # Removes all elements and inserts the given
    def clear(self, obj: List[GameObject] = []):
        self.objects = obj
        return self
    
    def deactivate(self):
        for obj in self.objects:
            obj.active = False
        return self
        
    def activate(self):
        for obj in self.objects:
            obj.active = True
        return self

    def length(self):
        return len(self.objects)
        
    # Wende eine Funktion auf alle Objekte an
    # Bsp: WallGroup.applyOnEach(lambda w: w.set('color', (0, 0, 0)); Dies würde die Farbe aller Wände auf schwarz setzen. 
    def applyOnEach(self, apply: typing.Callable[[GameObject], None]):
        for i in range(self.length()):
            apply(self.objects[i])
        return self
    
    # Berechnet das nächste Objekt aus der Gruppe zu einem Punkt
    def nearest(self, pos: pygame.math.Vector2) -> GameObject:
        if self.length() == 0:
            raise pygame.error(f"Group for {self.__class__.__name__} cannot check for nearest object. List is empty.")
        return sorted(self.objects, key=lambda obj: obj.pos.distance_to(pos))[0]

    # Gibt eine Liste an Objekten zurück, die mit dem Parameter "rect" kollidieren. (In absteigender Reihenfolge nach Überschneindungsfläche)
    def colliding(self, rect: Rectangle) -> List[GameObject]:
        colliding = []
        for i in self.objects:
            collided = i.collidesWith(rect)
            if collided:
                colliding.append(i)
        return colliding