import inspect
import pygame
from base.core.Sounds.Sounds import Sounds
from typing import Any, Dict, List
from base.core.Controls.Controls import Controls
from base.core.Event.Event import Event

from base.core.Event.EventDispatcher import EventDispatcher
from base.core.Level.Level import Level
from base.object.GameObject import GameObject
from settings import screen

class Game():
    def __init__(self) -> None:
        self.active = True
        self.notes: Dict[str, Any] = {}
        self.levels: Dict[int, Level] = {}
        self.level = {}
        EventDispatcher.subscribe(self, "G_STOP", "G_SWITCH_L", "G_REM", "G_SETN", "G_GETN")
        EventDispatcher.acceptRequest("G_ALLOW_MOVE", self.allowMove)
        Sounds.start()

    def receiveEvent(self, event: Event):
        name = event.name
        if name == "G_STOP":
            self.active = False
        if name == "G_SWITCH_L":
            self.setLevel(event.value)
        pass
        
    def draw(self):
        if isinstance(self.level, Level):
            for g in self.level.groups:
                g.draw()

    def start(self):
        pygame.init()
        clock = pygame.time.Clock()
        EventDispatcher.dispatch(Event("G_START"))
        while self.active:
            clock.tick(120)
            
            screen.fill(pygame.Color(50, 12, 100));

            Controls.update()
            EventDispatcher.dispatch(Event("G_CONTROLS", Controls.controls))

            self.draw()
            pygame.display.flip()

    def addLevel(self, *level: Level):
        for l in list(level):
            l.deactivate()
            self.levels[l.id] = l
    
    def setLevel(self, id: int):
        if isinstance(self.level, Level):
            self.level.deactivate()

        if id in self.levels:
            self.level = self.levels[id]
            self.level.activate()
            return
        raise LookupError(f"Level {id} not found.")    
    
    def allowMove(self, obj: GameObject, pos: pygame.Vector2):
        solidObjs = filter(lambda x: x != obj, self.level.allSolidObjects())
        movedRect = obj.cRect.get(pos, pygame.Vector2(pos.x + obj.cRect.width, pos.y + obj.cRect.height)).toPyRect()
        for obj in solidObjs:
            if obj.collidesWith(movedRect):
                return False
        return True
