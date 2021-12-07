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
        self.solid = False
        self.height = 50
        self.width = 50
        self.speed = 10
        Game.use(Controls)
        Events.subscribe(self, "game.tick", "game.start", "game.dependency.tick")

    def default(self, obj):
        obj.color = (0, 250, 250)
        return obj
    
    def receiveEvent(self, event: Event):
        if event.name == "game.tick":
            keys = Controls.keys
            self.control(keys)
            if keys["escape"]:
                Events.dispatch("game.stop")
        

    def control(self, keys: Dict[str, bool]):
        if keys["left"]:
            self.moveBySteps(-self.speed)
        if keys["right"]:
            self.moveBySteps(self.speed)
        if keys["up"]:
            self.moveBySteps(-self.speed, False)
        if keys["down"]:
            self.moveBySteps(self.speed, False)