from __future__ import annotations
from typing import Tuple
from base.object.Rectangle import Rectangle;
from settings import screen
import pygame

class GameObject():
    def __init__(self) -> None:

        #Object itself
        self.pos = pygame.math.Vector2(0, 0);
        self.width = 0
        self.height = 0
        self.color = None
        self.updateRect()

        #Internal properties
        self.solid = False

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def updateRect(self):
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.width, self.height)
        self.cRect = Rectangle().byRect(self.rect)

    def distanceTo(self, obj: GameObject):
        return self.pos.distance_to(obj.pos)
    
    def rectCorners(self) -> Tuple(pygame.Vector2):
        return (
            self.pos, 
            self.getPos(y=self.height), 
            self.getPos(self.width), 
            self.getPos(self.width, self.height)
        )
    
    def getPos(self, x=0, y=0):
        return pygame.Vector2(self.pos.x + x, self.pos.y + y)
    
    def updatePos(self, pos: pygame.Vector2):
        self.pos = pos
        self.updateRect()

    def editPosBy(self, x=0, y=0):
        self.updatePos(self.getPos(x, y))
        
    def collidesWith(self, obj: GameObject) -> bool:
        pass

    