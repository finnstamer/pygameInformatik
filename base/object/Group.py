import typing
import pygame
from typing import Generic, List, TypeVar

from base.object.GameObject import GameObject
from base.object.Rectangle import Rectangle
from base.object.collision import Collision

O = TypeVar('O', bound=GameObject)

# Works as manager and factory of GameObjects
class Group(Generic[O]):
    def __init__(self, name: str, constructor: O) -> None:
        self.name = name
        self.constructor = constructor
        self.objects: List[O] = []
    
    def add(self, *obj: O):
        self.objects = self.objects + list(obj)
        return self
    
    def draw(self):
        for obj in self.objects:
            obj.draw()
        return self
    
    def remove(self, obj):
        self.objects.remove(obj)
        return self

    def length(self):
        return len(self.objects)

    def create(self, *args) -> O:
        instance = self.constructor(args)
        self.add(instance)
        return 
        
    def applyOnEach(self, apply: typing.Callable):
        for i in range(self.length()):
            self.objects[i] = apply(self.objects[i])
        return self

    def indexOf(self, obj: O):
        return self.objects.index(obj)
    
    def nearest(self, pos: pygame.math.Vector2) -> O:
        if self.length() == 0:
            raise pygame.error(f"Group for {self.name} cannot check for nearest object. List is empty.")
        return sorted(self.objects, key=lambda obj: obj.pos.distance_to(pos))[0]

    # Returns a list of all objects, that collides with an rectangle, sorted by the area of intersection (descending)
    def colliding(self, rect: Rectangle) -> List[O]:
        colliding = []
        for i in self.objects:
            collision = Collision()
            collided = collision.isCollided(i.cRect, rect)
            if collided:
                colliding.append([i, collision])

        return list(map(
            lambda x: x[0],
            sorted(colliding, key=lambda c: c[1].collisionRect.area, reverse=True)
        ))