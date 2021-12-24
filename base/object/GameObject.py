from __future__ import annotations
from typing import Tuple
from base.core.Dependencies.Movement import Movement
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.geometry.Rectangle import Rectangle
from base.object.Factory.Factory import Factory
from settings import screen
import pygame

# Ein Objekt, welchem eine Position im Raum, sowie eine eigenes Rechteck gehört.
# Wenn Position geändert werden sollte, benutze .updatePos(x, y) oder .editPosBy(xD, yD)  (d = Delta = Differenz)
class GameObject():
    def __init__(self, pos: pygame.Vector2 = pygame.math.Vector2(0, 0), width: int = 0, height: int = 0, color: Tuple = (0, 0, 0)) -> None:
        self.id = -1
        self._active = True
        self.image = None
        self._pos = pos
        self._width = width
        self._height = height
        self.color = color
        self.solid = False
        self.speed = 0
        self.buildRect()
        Factory.append(self)

    @property
    def active(self) -> bool:
        return self._active

    @active.setter
    def active(self, value: bool):
        self._active = value
        Events.dispatch(f"{self.id}.active")

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int):
        self._width = value
        self.buildRect()
    
    @property
    def height(self) -> int:
        return self._height

    @height.setter
    def height(self, value: int):
        self._height = value
        self.buildRect()
    
    @property
    def pos(self) -> pygame.Vector2:
        return self._pos

    @pos.setter
    def pos(self, value: pygame.Vector2):
        self._pos = value
        self.buildRect()
    
    @property
    def rect(self) -> pygame.Rect:
        return self._rect
    
    @rect.setter
    def rect(self, rect: pygame.Rect):
        self._rect = rect
        self.cRect = Rectangle.byRect(rect)
    
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
                self.drawRect()
        return self

    def drawRect(self):
        pygame.draw.rect(screen, self.color, self.rect)
        return self
    
    def updateRect(self):            
        self.rect = self.buildRect()
        return self

    # Overridable Method for custom rect creating methods
    def buildRect(self) -> pygame.Rect:
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.width, self.height)
        self.cRect = Rectangle().byRect(self.rect)
        return self.rect

    def distanceTo(self, obj: GameObject):
        return self._pos.distance_to(obj._pos)

    def updatePos_hidden(self, pos: pygame.Vector2):
        self._pos = pos
        self.updateRect()
        return self

    def updatePos(self, pos: pygame.Vector2):
        self.updatePos_hidden(pos)
        Events.dispatch(f"{self.id}.moved", {"obj": self, "pos": self.pos})
        return self
    
    def move(self, pos: pygame.Vector2):
        furthestPos = Movement.furthestMove(self, pos)
        if furthestPos is not None:
            self.updatePos(furthestPos)     
        
    def collidesWith(self, rect: pygame.Rect) -> bool:
        return Rectangle.byRect(self.rect.clip(rect)).area > 0
    
    def setAlias(self, alias: str):
        Factory.setAlias(self, alias)
        return self