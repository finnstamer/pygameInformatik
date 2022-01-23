from __future__ import annotations
from gc import callbacks
from typing import Callable, Tuple
from base.core.Dependencies.Movement import Movement
from base.core.Event.Events import Events
from base.core.Game import Game
from base.geometry.Rectangle import Rectangle
from base.core.Object.Factory import Factory
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
        self.solid = False # Solides Objekt => es ist nicht durchlässig
        self.fluid = False # Fluid Objekt => es bewegt sich im Raum (wichtig für NodeGenerator)
        self.speed = 0
        self.health = -1
        self.transparent = False
        self.buildRect()
        Factory.append(self)

    # Getter und Setter
    @property
    def active(self) -> bool:
        return self._active

    @active.setter
    def active(self, value: bool):
        self._active = value
        if value == True:
            Events.dispatch(f"{self.id}.active", self)
            return
        Events.dispatch(f"{self.id}.inactive", self)

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

    # Ermöglicht die Verwendung eines Bildes. Das .rect wird nicht überschrieben
    # image argument soll aus root Sicht      
    def setImage(self, image: str):
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (self._width, self._height)).convert_alpha()
        return self

    # Wenn Objekt aktiv ist, wird .rect oder .image auf den Bildschirm übertragen    
    def draw(self):
        if self.active and not self.transparent:
            if self.image:
                screen.blit(self.image, self.rect)
            else:
                self.drawRect()
        return self

    # Speziell das .rect wird auf den Bildschirm übertragen
    def drawRect(self):
        pygame.draw.rect(screen, self.color, self.rect)
        return self
    
    # Aktualisiert das Rect (bpsw. bei Veränderung der Position oder Dimensionen)
    # Wenn anderes pygame Objekt statt pygame.Rect zur Darstellung verwendet werden soll,
    # kann Funktion überschrieben werden. 
    def updateRect(self):            
        self.rect = self.buildRect()
        return self

    # Überschreibende Funktion zur Bildung einer Darstellungsvariante (hier pygame.Rect)
    def buildRect(self):
        self.rect = pygame.Rect(self.pos.x, self.pos.y, self.width, self.height)
        # self.cRect = Rectangle().byRect(self.rect)
        return self.rect

    # Distanz des Objektes zu einem anderen Objekt nach ihren oberen linken Ecken
    def distanceTo(self, obj: GameObject):
        return self.pos.distance_to(obj.pos)

    # Aktualsiert die Position und aktualisiert die Darstellung
    # Gibt "id.moved" Event aus
    def updatePos(self, pos: pygame.Vector2):
        beforePos = pygame.Vector2(list(self.pos))
        self._pos = pos
        self.updateRect()
        Events.dispatch(f"{self.id}.moved", (self, beforePos))
        return self
    
    def hiddenPosUpdate(self, pos: pygame.Vector2):
        self._pos = pos
        self.updateRect()
        return self

    # Bewegt wenn möglich ein Objekt zur Position. Sonst bis zur nächsten möglichen Stelle
    def move(self, pos: pygame.Vector2):
        furthestPos = Movement.furthestMove(self, pos, objs=Game.level().nonFluidSolids)
        if furthestPos is not None:
            self.updatePos(furthestPos)     
        return self

    def setTransparent(self):
        self.transparent = True
        return self
    
    # Gibt zurück, ob dieses Objekt mit einem pygame.Rect kollidiert.
    def collidesWith(self, rect: pygame.Rect) -> bool:
        colRect = self.rect.clip(rect)
        return colRect.width != 0 and colRect.height != 0

    def drawSpecific(self, rect: pygame.Rect):
        if self.active and not self.transparent:
            if self.image is None:
                pygame.draw.rect(screen, self.color, rect)
                return
            screen.blit(self.image, rect)
    
    # Fügt diesem Objekt schaden zu, wenn das .health nicht -1 ist.
    # Fällt .health unter 0 wird das Objekt deaktiviert und "id.died" Event ausgegeben
    def damage(self, points: int):
        if self.health == -1:
            return self
        self.health -= points
        if self.health <= 0:
            # Unterschied zwischen gestorbenen Schadennehmer und unbesiegbaren im Nachinhein ersichtlich machen
            # unbesigbar = .health < 0; möglich zu sterbender = .health >= 0
            self.health = 0
            self.active = False
            Events.dispatch(f"{self.id}.died", self)
        return self

    # Shorthand, um über die Factory ein Alias für dieses Objekt zu setzen.
    def setAlias(self, alias: str):
        Factory.setAlias(self, alias)
        return self
    
    def subscribe(self, event: str, func: Callable):
        Events.subscribe(event, func, self)