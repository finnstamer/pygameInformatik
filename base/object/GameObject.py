from __future__ import annotations
from typing import Tuple
from base.core.Event.Event import Event
from base.geometry.Rectangle import Rectangle
from settings import screen
import pygame

# Ein Objekt, welchem eine Position im Raum, sowie eine eigenes Rechteck gehört.
# Wenn Position geändert werden sollte, benutze .updatePos(x, y) oder .editPosBy(xD, yD)  (d = Delta = Differenz)
class GameObject():
    def __init__(self) -> None:
        self.active = True
        self.image = None
        self.pos = pygame.math.Vector2(0, 0);
        self.width = 0
        self.height = 0
        self.color = None
        self.updateRect()

        self.solid = False

    def receiveEvent(self, e: Event):
        raise NotImplementedError(f"Event '{e.name}' is not implemented in '{self.__class__.__name__}'.")

    def edit(self, property: str, val: any):
        self[property] = val
        self.updateRect()
        return self
    
    def setImage(self, image: str):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self.width, self.height)).convert()
        return self
    
    # pygame.draw überträgt das Rechteck des Objektes auf den Bildschirm.
    def draw(self):
        if self.active:
            if self.image:
                screen.blit(self.image, self.rect)
                pass
            else:
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
    
    
    def updatePos(self, pos: pygame.Vector2):
        self.pos = pos
        self.updateRect()

    def getPositionChange(self, x=0, y=0):
        vec = pygame.Vector2(self.pos.x, self.pos.y) # Cloning
        vec.x += x
        vec.y += y
        return vec

    def editPosBy(self, x=0, y=0):
        vec = self.getVectorPos()
        vec.x += x
        vec.y += y
        self.updatePos(vec)
        
    def collidesWith(self, rect: pygame.Rect) -> bool:
        return Rectangle.byRect(self.rect.clip(rect)).area > 0

    