from functools import reduce
from typing import List
import pygame

from pygame.sprite import groupcollide
from base.object.GameObject import GameObject
from base.object.Group import Group


class Level():
    def __init__(self, id: int, groups: List[Group]) -> None:
        self.id = id
        self.groups = groups
    
    def deactivate(self):
        for g in self.groups:
            g.deactivate()

    def activate(self):
        for g in self.groups:
            g.activate()
    
    def allObjects(self):
        return reduce(lambda x,y:x+y, map(lambda x:x.objects, self.groups))
    
    def allSolidObjects(self):
        return filter(lambda x: x.solid, self.allObjects()) 
    
    def allowMove(self, obj: GameObject, pos: pygame.Vector2) -> bool:
        solidObjs = filter(lambda x: x != obj, self.allSolidObjects())
        movedRect = obj.cRect.get(pos, pygame.Vector2(pos.x + obj.cRect.width, pos.y + obj.cRect.height)).toPyRect()
        for obj in solidObjs:
            if obj.collidesWith(movedRect):
                return False
        return True