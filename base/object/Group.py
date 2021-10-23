import pygame
from typing import Generic, List, TypeVar
from base.object.GameObject import GameObject

O = TypeVar('O', GameObject)

class Group(Generic[O]):
    def __init__(self) -> None:
        self.objects: List[O] = []
    
    def add(self, obj: O):
        self.objects.append(obj)
    
    def remove(self, obj):
        self.objects.remove(obj)

    def length(self):
        return len(self.objects)
    
    def nearest(self, pos: pygame.math.Vector2) -> O:
        pass

    def colliding(self, pos: pygame.Vector2) -> List[O]:
        pass