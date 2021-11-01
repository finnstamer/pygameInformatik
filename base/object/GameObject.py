from __future__ import annotations
from typing import Tuple
from base.geometry.Rectangle import Rectangle
from base.object.collision import Collision;
from settings import screen
import pygame

# Ein Objekt, welchem eine Position im Raum, sowie eine eigenes Rechteck gehört.
# Wenn Position geändert werden sollte, benutze .updatePos(x, y) oder .editPosBy(xD, yD)  (d = Delta = Differenz)
class GameObject():
    def __init__(self) -> None:
        self.pos = pygame.math.Vector2(0, 0);
        self.width = 0
        self.height = 0
        self.color = None
        self.updateRect()

        self.solid = False

    def edit(self, property: str, val: any):
        self[property] = val
        self.updateRect()
        return self

    # pygame.draw überträgt das Rechteck des Objektes auf den Bildschirm.
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
            self.getVectorPos(y=self.height), 
            self.getVectorPos(self.width), 
            self.getVectorPos(self.width, self.height)
        )
    
    def getVectorPos(self):
        return pygame.Vector2(self.pos.x, self.pos.y)
    
    def updatePos(self, pos: pygame.Vector2):
        self.pos = pos
        self.updateRect()

    def editPosBy(self, x=0, y=0):
        vec = self.getVectorPos()
        vec.x += x;
        vec.y += y
        self.updatePos(vec)
        
    def collidesWith(self, obj: GameObject) -> bool:
        collision = Collision()
        return collision.check(self.cRect, obj.cRect)

    