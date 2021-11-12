import pygame
import sys
from typing import Any, Dict, List
from base.core.Dependencies.Controls import Controls
from base.core.Event.Event import Event

from base.core.Event.Events import Events
from base.core.Level.Level import Level
from base.object.GameObject import GameObject
from settings import screen

class Game():
    tickDelta = 0
    dependencies: List[Any] = []
    level: Level = Level(-1, [])

    def __init__(self) -> None:
        self.active = True
        self.notes: Dict[str, Any] = {}
        self.levels: Dict[int, Level] = {}
        Events.subscribe(self, "game.stop", "game.level.switch")
        # Events.acceptRequest("game.level.movement.allow", lambda o,p: self.level.allowMove(o, p))

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
    def use(dependency: object):
        if dependency not in Game.dependencies:
            Game.dependencies.append(dependency)

    @staticmethod
    def initDependencies():
        for dependency in Game.dependencies:
            dependency()
        
    def draw(self):
        if isinstance(self.level, Level):
            for g in self.level.groups:
                g.draw()

    def start(self):
        pygame.init()
        clock = pygame.time.Clock()
        Game.initDependencies()
        Events.dispatch("game.start")
        while self.active:
            Game.tickDelta = clock.tick(60) / 1000
            Events.dispatch("game.dependency.tick")
            Events.dispatch("game.tick")

            screen.fill(pygame.Color(50, 12, 100));
            self.draw()
            
            pygame.display.flip()

    def addLevel(self, *level: Level):
        for l in list(level):
            l.deactivate()
            self.levels[l.id] = l
    
    def setLevel(self, id: int):
        if isinstance(self.level, Level):
            Game.level.deactivate()

        if id in self.levels:
            Game.level = self.levels[id]
            Game.level.activate()
            return
        raise LookupError(f"Level {id} not found.")
