from typing import List
import pygame
from base.geometry.Rectangle import Rectangle

from base.object.GameObject import GameObject
from base.object.Group import Group

class MovableObject(GameObject):
    def __init__(self) -> None:
        super().__init__()
        self.speed = 10
    

    # Creates a block of the same height of this object
    # Then check where the first collision will be, by the nearest
    # pos: new position of uLC of object 
    # Direction Class
    def move(self, pos: pygame.Vector2):
        # movedRect = self.cRect.get(pos, pygame.Vector2(pos.x + self.cRect.width, pos.y + self.cRect.height))
        # colliding = wallGroup.colliding(movedRect)
        
        # if len(colliding) == 0:
        self.updatePos(pos)

    