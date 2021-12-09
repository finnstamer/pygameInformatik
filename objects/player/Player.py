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
        self.direction = 1 # Right

        Game.use(Controls)
        Events.subscribe(self, "game.tick", "game.start", "game.dependency.tick")

    def default(self, obj):
        obj.color = (0, 250, 250)
        return obj
    
    def receiveEvent(self, event: Event):
        if event.name == "game.tick":
            keys = Controls.keys
            self.control(keys)
            self.move(self.nextPos())

            if keys["escape"]:
                Events.dispatch("game.stop")
 
    def nextPos(self) -> pygame.Vector2:
        return {
            0: lambda: pygame.Vector2(self.pos.x, self.pos.y - self.speed),
            1: lambda: pygame.Vector2(self.pos.x + self.speed, self.pos.y),
            2: lambda: pygame.Vector2(self.pos.x, self.pos.y + self.speed),
            3: lambda: pygame.Vector2(self.pos.x - self.speed, self.pos.y)
        }[self.direction]()

    def control(self, keys: Dict[str, bool]):
        if keys["up"]:
            self.direction = 0
        if keys["right"]:
            self.direction = 1
        if keys["down"]:
            self.direction = 2
        if keys["left"]:
            self.direction = 3