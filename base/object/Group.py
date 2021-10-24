import typing
import pygame
from typing import Generic, List, TypeVar

from base.object.GameObject import GameObject

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

    def colliding(self, pos: pygame.Vector2) -> List[O]:
        pass