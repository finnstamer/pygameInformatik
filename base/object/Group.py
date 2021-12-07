import typing
import pygame
from typing import Generic, List, TypeVar

from base.object.GameObject import GameObject
from base.geometry.Rectangle import Rectangle

# O Ist ein Datentyp, dass aus einem GameObject (oder einer Abwandlung daraus besteht: bspw. Player)
O = TypeVar('O', bound=GameObject)

# Mit dieser Klasse werden mehrere am besten sehr ähnliche Objekte zusammengefasst und unter anderem verglichen.
class Group(Generic[O]):
    def __init__(self, name: str) -> None:
        self.name = name
        self.constructor = None
        self.objects: List[O] = []
    
    # Das * for einem Parameter bedeutet, dass man von da an unendlich objekte anhängen kann. Der Paramter obj ist dann eine List aus Objekten
    # bspw: Group().add(obj1, obj2, obj3, obj4, ...)
    def add(self, *obj: O):
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

    # Erstellt eine neue Instanz des Gruppenobjektes. Bspw. eine neue Wall
    # Wenn Parameter mitgliefert werden sollen, werden sie als Parameter in create eingetragen
    def create(self, *args) -> O:
        instance = self.constructor(args)
        self.add(instance)
        return instance
        
    # Wende eine Funktion auf alle Objekte an
    # Bsp: WallGroup.applyOnEach(lambda w: w.set('color', (0, 0, 0)); Dies würde die Farbe aller Wände schwarz machen. 
    def applyOnEach(self, apply: typing.Callable[[GameObject], None]):
        for i in range(self.length()):
            apply(self.objects[i])
        return self

    def indexOf(self, obj: O):
        return self.objects.index(obj)
    
    # Berechnet das nächste Objekt aus der Gruppe zu einem Punkt
    def nearest(self, pos: pygame.math.Vector2) -> GameObject:
        if self.length() == 0:
            raise pygame.error(f"Group for {self.name} cannot check for nearest object. List is empty.")
        return sorted(self.objects, key=lambda obj: obj.pos.distance_to(pos))[0]

    # Gibt eine Liste an Objekten zurück, die mit dem Parameter "rect" kollidieren. (In absteigender Reihenfolge nach Überschneindungsfläche)
    def colliding(self, rect: Rectangle) -> List[O]:
        colliding = []
        for i in self.objects:
            print(i.rect)
            # collided = Rectangle.byRect(i.rect.clip(rect))
            collided = i.collidesWith(rect)
            if collided:
                colliding.append(i)

        # return list(map(
        #     lambda x: x[0],
        #     sorted(colliding, key=lambda c: c[1].area, reverse=True)
        # ))
        return colliding