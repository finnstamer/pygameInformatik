from typing import Dict
import pygame
from base.core.Dependencies.Controls import Controls
from base.core.Dependencies.NodeVisualizer import NodeVisualizer
from base.core.Event.Events import Events
from base.core.Game import Game
from base.core.Object.Factory import Factory
from base.core.Object.GameObject import GameObject

class Player(GameObject):
    def __init__(self) -> None:
        super().__init__()
        Factory.setAlias(self, "player")

        self.pos = pygame.math.Vector2((50, 50));
        self.color = (50, 50, 50)
        self.solid = False
        self.height = 50
        self.width = 50

        self.speed = 5
        self.direction = 1 # Right
        self.allowMovements = True

        self.neighborVisualizer = NodeVisualizer([], (3, 119, 252))
        Game.use(Controls)
        Events.subscribe("game.tick", self.onTick)
        Events.subscribe("game.start", self.onStart)
    
    def onStart(self, event):
        # self.routine = MovementRoutine(Factory.get("ekto1"))
        # self.routine = FollowObjectRoutine(Factory.get("ekto1"), self)
        pass

    def onTick(self, event):
        if self.allowMovements:
            self.control(Controls.keys)
            self.oldMovement()
            # self.move(self.nextPos())

        clicked, pos = Controls.clicks["l"] 
        if clicked:
            Factory.get("weapon").shoot(self.direction)
        
        if Controls.keys["space"]:
            Factory.get("Enemy").alerted = True
        if Controls.keys["escape"]:
            Game.level().reset()
            # Game.level().remove(self)
            # Factory.delete(self)
            # Events.disconnectObject(self)

    def nextPos(self) -> pygame.Vector2:
        return {
            0: pygame.Vector2(self.pos.x, self.pos.y - self.speed),
            1: pygame.Vector2(self.pos.x + self.speed, self.pos.y),
            2: pygame.Vector2(self.pos.x, self.pos.y + self.speed),
            3: pygame.Vector2(self.pos.x - self.speed, self.pos.y)
        }[self.direction]

    def control(self, keys: Dict[str, bool]):
        if keys["w"]:
            self.direction = 0
        if keys["d"]:
            self.direction = 1
        if keys["s"]:
            self.direction = 2
        if keys["a"]:
            self.direction = 3
        
    def oldMovement(self):
        keys = Controls.keys
        if keys["w"]:
            self.move(pygame.Vector2(self.pos.x, self.pos.y - self.speed))
        if keys["d"]:
            self.move(pygame.Vector2(self.pos.x + self.speed, self.pos.y))
        if keys["s"]:
            self.move(pygame.Vector2(self.pos.x, self.pos.y + self.speed))
        if keys["a"]:
            self.move(pygame.Vector2(self.pos.x - self.speed, self.pos.y))
