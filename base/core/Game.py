import inspect
import pygame
from typing import Any, Dict, List
from base.core.Controls.Controls import Controls
from base.core.Event.Event import Event

from base.core.Event.EventDispatcher import EventDispatcher
from base.core.Level.Level import Level
from settings import screen

class Game():
    def __init__(self) -> None:
        self.active = True
        self.notesotes: Dict[str, Any] = {}
        self.levels: Dict[int, Level] = {}
        self.level = {}
        EventDispatcher.subscribe(self, "G_STOP", "G_SWITCH_L", "G_REM", "G_SETN", "G_GETN")


    def receiveEvent(self, event: Event):
        n = event.name
        if n == "G_STOP":
            self.active = False
        if n == "G_SWITCH_L":
            self.setLevel(event.value)
        pass
        
    def draw(self):
        if isinstance(self.level, Level):
            for g in self.level.groups:
                g.draw()

    def start(self):
        pygame.init()
        clock = pygame.time.Clock()
        while self.active:
            clock.tick(120)
            
            screen.fill(pygame.Color(50, 12, 100));

            Controls.update()
            EventDispatcher.dispatch(Event("CONTROLS", Controls.controls))

            self.draw()
            pygame.display.flip()

    def addLevel(self, *level: Level):
        for l in list(level):
            self.levels[l.id] = l
    
    def setLevel(self, id: int):
        if isinstance(self.level, Level):
            print("5")
            self.level.deactivate()

        if id in self.levels:
            self.level = self.levels[id]
            self.level.activate()
            return
        raise LookupError()
        
    