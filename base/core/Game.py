import pygame
from typing import Any, Dict, List

from pygame.constants import KEYDOWN, KEYUP

from base.core.Event.Events import Events
from base.core.Level.AbstractLevel import AbstractLevel
from base.core.Level.Level import Level
from settings import screen

class Game():
    tickDelta = 0
    dependencies: List[Any] = []
    currentLevel: int = 0
    notes: Dict[str, Any] = {}
    levels: Dict[int, AbstractLevel] = {0: Level(0)}
    active = True

    def __init__(self) -> None:
        self.notes: Dict[str, Any] = {}

    # Verknüpfe unabhängige Dependencies mit dem Game Lifecycle
    # Diese werden vor dem game.start Event initialisiert.
    @staticmethod
    def use(*dependencies: object):
        for dependency in list(dependencies):
            if dependency not in Game.dependencies:
                Game.dependencies.append(dependency)

    @staticmethod
    def initDependencies():
        for dependency in Game.dependencies:
            dependency()

    def start():
        pygame.init()
        pygame.event.set_allowed([KEYDOWN, KEYUP])
        clock = pygame.time.Clock()
        Game.initDependencies()

        Events.dispatch("game.start")
        while Game.active:  
            clock.tick(60)
            Events.dispatch("game.dependency.tick")
            Events.dispatch("game.tick")

            screen.fill(pygame.Color(0, 0, 0));
            Game.level().draw()
            
            pygame.display.flip()

    def addLevel(*levels: AbstractLevel) -> None:
        for level in list(levels):
            level.deactivate()
            Game.levels[level.id] = level
    
    def setLevel(levelId: int) -> None:
        Game.level().deactivate()
        Game.currentLevel = levelId
        if levelId in Game.levels:
            Game.level().make()
            return
        raise LookupError(f"Level '{levelId}' not found.")
    
    def level():
        return Game.levels[Game.currentLevel]