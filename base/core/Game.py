from this import d
import pygame
from typing import Any, Dict, List

from pygame.constants import KEYDOWN, KEYUP, MOUSEBUTTONUP
from base.core.Dependencies.Debugger import Debugger
from base.core.Dependencies.Rendering.Rendering import Rendering

from base.core.Event.Events import Events
from base.core.Level.AbstractLevel import AbstractLevel
from base.core.Level.Level import Level
from settings import screen

class Game():
    active = True
    isStarted = False
    dependencies: List[Any] = []
    currentLevel: int = -1
    levels: Dict[int, AbstractLevel] = {0: Level(0)}
    deltaTime = 0
    frameRate = 60

    # Funktion zur 
    def use(*dependencies: object):
        for dependency in list(dependencies):
            if dependency not in Game.dependencies:
                # Ist Spiel bereits gestartet, würde die Initalisierung nicht mehr aufgerufen werden
                if Game.isStarted:
                    dependency()
                Game.dependencies.append(dependency)

    # Dependencies werden initialisiert
    def initDependencies():
        for dependency in Game.dependencies:
            dependency()

    # Game Loop wird gestartet und Events ausgegeben
    def start():
        # pygame.init()
        pygame.event.set_allowed([KEYDOWN, KEYUP, MOUSEBUTTONUP])
        clock = pygame.time.Clock()
        Game.initDependencies()

        Events.dispatch("game.start")
        Game.isStarted = True
        while Game.active:  
            Game.deltaTime = clock.tick(Game.frameRate)
            # Rendering.render()
            
            Events.dispatch("game.dependency.tick")
            Events.dispatch("game.tick")
            screen.fill(pygame.Color(0, 0, 0));
            Game.level().draw()
            
            pygame.display.flip()

    def addLevel(*levels: AbstractLevel) -> None:
        for level in list(levels):
            level.deactivate()
            Game.levels[level.id] = level
    
    # Setze aktuelles Level zum Level mit gegebener Id
    # Aktuelles Level wird deaktiviert (Level.deactivate)
    def setLevel(levelId: int) -> None:
        if levelId not in Game.levels:
            raise LookupError(f"Level '{levelId}' not found.")

        Events.dispatch("game.level.set", Game.levels[levelId])
        if Game.currentLevel >= 0: # Default unset Level is -1
            Debugger.log(f"Game: Deleting {Game.currentLevel}...")
            Game.level().deactivate()
            Game.level().deleteAll()
            Debugger.log(f"Game: Finished Deleting {Game.currentLevel}")
        Game.currentLevel = levelId
        Debugger.log(f"Game: Loading {levelId}...")
        Game.level().load()
        Debugger.log(f"Game: Finished Loading {levelId}")

    def level():
        return Game.levels[Game.currentLevel]