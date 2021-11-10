from typing import Dict
import pygame
from base.core.Dependencies.Controls import Controls
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.core.Game import Game
from base.object.MovableObject import MovableObject

class Player(MovableObject):
    def __init__(self) -> None:
        MovableObject.__init__(self)

        self.pos = pygame.math.Vector2((50, 50));
        self.color = (50, 50, 50)
        self.solid = True
        self.height = 50
        self.width = 50
        self.speed = 3
        Game.use(Controls)
        Events.subscribe(self, "game.tick")

    def receiveEvent(self, event: Event):
        if event.name == "game.tick":
            keys = Controls.keys
            self.control(keys)
            if keys["space"]:
                Events.dispatch("game.level.switch", 2)

    def control(self, keys: Dict[str, bool]):
        if keys["left"]:
            self.moveByDelta(-self.speed)
        if keys["right"]:
            self.moveByDelta(self.speed)
        if keys["up"]:
            self.moveByDelta(-self.speed, False)
        if keys["down"]:
            self.moveByDelta(self.speed, False)
