import pygame
from typing import Any, Dict, List

from pygame.constants import KEYDOWN, KEYUP
from base.core.Event.Event import Event

from base.core.Event.Events import Events
from base.core.Level.Level import Level
from settings import screen

class Game():
    tickDelta = 0
    dependencies: List[Any] = []
    level: Level = Level(-1)
    notes: Dict[str, Any] = {}

    def __init__(self) -> None:
        self.active = True
        self.notes: Dict[str, Any] = {}
        self.levels: Dict[int, Level] = {}
        Events.subscribe(self, "game.stop", "game.level.switch")

    def receiveEvent(self, event: Event):
        name = event.name
        if name == "game.stop":
            self.active = False
            pygame.quit()
            exit()
        if name == "game.level.switch":
            self.setLevel(event.value)

    # Verknüpfe unabhängige Dependencies mit dem Game Lifecycle
    # Diese werden vor dem game.start Event geladen.
    @staticmethod
    def use(*dependencies: object):
        for dependency in list(dependencies):
            if dependency not in Game.dependencies:
                Game.dependencies.append(dependency)

    @staticmethod
    def initDependencies():
        for dependency in Game.dependencies:
            dependency()

    def start(self):
        pygame.init()
        pygame.event.set_allowed([KEYDOWN, KEYUP])
        clock = pygame.time.Clock()
        Game.initDependencies()

        Events.dispatch("game.start")
        while self.active:  
            clock.tick(60)
            Events.dispatch("game.dependency.tick")
            Events.dispatch("game.tick")

            screen.fill(pygame.Color(0, 0, 0));
            self.level.draw()
            
            pygame.display.flip()

    def addLevel(self, *levels: Level) -> None:
        for level in list(levels):
            level.deactivate()
            self.levels[level.id] = level
    
    def setLevel(self, levelId: int) -> None:
        Game.level.deactivate()

        if levelId in self.levels:
            Game.level = self.levels[levelId]
            return Game.level.activate()
        raise LookupError(f"Level '{levelId}' not found.")
