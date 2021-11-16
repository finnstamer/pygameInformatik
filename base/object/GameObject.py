from __future__ import annotations
from typing import Any, Dict, Tuple
from base.core.Event.Event import Event
from base.geometry.Rectangle import Rectangle
from settings import screen
import pygame

# Ein Objekt, welchem eine Position im Raum, sowie eine eigenes Rechteck gehört.
# Wenn Position geändert werden sollte, benutze .updatePos(x, y) oder .editPosBy(xD, yD)  (d = Delta = Differenz)
class GameObject():
    def __init__(self) -> None:
        self.id = 0
        self._active = True
        self.image = None
        self.altRect = None
        self._pos = pygame.math.Vector2(0, 0);
        self._width = 0
        self._height = 0
        self.color = None
        self.solid = False

    @property
    def active(self) -> bool:
        return self._active

    @active.setter
    def active(self, value: bool):
        self._active = value
        self.onActivation()

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value
        self.updateRect()
    
    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value
        self.updateRect()
    
    @property
    def pos(self) -> int:
        return self._pos

    @pos.setter
    def pos(self, value: pygame.Vector2):
        self._pos = value
        self.updateRect()
    
    
    # Overrideable Function that runs whenever the object is activated
    def onActivation(self):
        pass

    def receiveEvent(self, e: Event):
        raise NotImplementedError(f"Event '{e.name}' is subscribed but not implemented in '{self.__class__.__name__}'. Remove subscription or add the 'receiveEvent' function.")
    
    def setImage(self, image: str):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self._width, self._height)).convert()
        return self
    
    # pygame.draw überträgt das Rechteck des Objektes auf den Bildschirm.
    def draw(self):
        if self.active:
            if self.image:
                screen.blit(self.image, self.rect)
            else:
                pygame.draw.rect(screen, self.color, self.rect)

    def buildRect(self):
        return pygame.Rect(self._pos.x, self._pos.y, self._width, self._height)

    def updateRect(self):            
        self.rect = self.buildRect()
        self.cRect = Rectangle().byRect(self.rect)

    def distanceTo(self, obj: GameObject):
        return self._pos.distance_to(obj._pos)
    
    def rectCorners(self) -> Tuple(pygame.Vector2):
        return (
            self._pos, 
            self.getVectorPos(y=self._height), 
            self.getVectorPos(self._width), 
            self.getVectorPos(self._width, self._height)
        )
    
    def updatePos(self, pos: pygame.Vector2):
        self._pos = pos
        self.updateRect()

    def getPositionChange(self, x=0, y=0):
        vec = pygame.Vector2(self._pos.x, self._pos.y) # Cloning
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

    