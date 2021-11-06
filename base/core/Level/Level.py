from functools import reduce
from typing import List

from pygame.sprite import groupcollide
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