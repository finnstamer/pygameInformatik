import inspect
import pygame
from typing import Any, Dict, List
from base.core.Controls.Controls import Controls
from base.core.Event.Event import Event

from base.core.Event.EventDispatcher import EventDispatcher
from base.core.Level.Level import Level
from base.object.GameObject import GameObject
from settings import screen

class Game():
    dependencies: List[Any] = []
    def __init__(self) -> None:
        self.active = True
        self.notes: Dict[str, Any] = {}
        self.levels: Dict[int, Level] = {}
        self.level = {}
        EventDispatcher.subscribe(self, "game.stop", "game.level.switch", "G_REM", "G_SETN", "G_GETN")
        EventDispatcher.acceptRequest("G_ALLOW_MOVE", self.allowMove)

    def receiveEvent(self, event: Event):
        name = event.name
        if name == "game.stop":
            self.active = False
        if name == "game.level.switch":
            self.setLevel(event.value)
        pass

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
        EventDispatcher.dispatch("game.start")
        while self.active:
            clock.tick(120)
            
            screen.fill(pygame.Color(50, 12, 100));

            Controls.update()
            EventDispatcher.dispatch("G_CONTROLS", Controls.controls)

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
