from typing import Dict
import pygame
from base.core.Dependencies.Controls import Controls
from base.core.Dependencies.NodeVisualizer import NodeVisualizer
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.core.Game import Game
from base.object.AI.Routines.FollowObjectRoutine import FollowObjectRoutine
from base.object.Factory.Factory import Factory
from base.object.AI.PathFinder import PathFinder
from base.object.AI.Routines.MovementRoutine import MovementRoutine
from base.object.GameObject import GameObject

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

        self.neighborVisualizer = NodeVisualizer([], (3, 119, 252))
        Game.use(Controls)
        Events.subscribe("game.tick", self.onTick)
        Events.subscribe("game.start", self.onStart)
    
    def onStart(self, event):
        # self.routine = MovementRoutine(Factory.get("ekto1"))
        self.routine = FollowObjectRoutine(Factory.get("ekto1"), self)

    def onTick(self, event):
        # print(self.routine.progress)
        self.control(Controls.keys)
        # self.move(self.nextPos())
        self.oldMovement()

        if Controls.keys["space"]:
            # self.routine.setStates(Factory.get("ekto1"), self).start()
            Factory.get("weapon").shoot(self.direction)
        if Controls.keys["escape"]:
            self.routine.stop()

    def nextPos(self) -> pygame.Vector2:
        return {
            0: pygame.Vector2(self.pos.x, self.pos.y - self.speed),
            1: pygame.Vector2(self.pos.x + self.speed, self.pos.y),
            2: pygame.Vector2(self.pos.x, self.pos.y + self.speed),
            3: pygame.Vector2(self.pos.x - self.speed, self.pos.y)
        }[self.direction]

    def control(self, keys: Dict[str, bool]):
        if keys["up"]:
            self.direction = 0
        if keys["right"]:
            self.direction = 1
        if keys["down"]:
            self.direction = 2
        if keys["left"]:
            self.direction = 3
        
    def oldMovement(self):
        keys = Controls.keys
        if keys["up"]:
            self.move(pygame.Vector2(self.pos.x, self.pos.y - self.speed))
        if keys["right"]:
            self.move(pygame.Vector2(self.pos.x + self.speed, self.pos.y))
        if keys["down"]:
            self.move(pygame.Vector2(self.pos.x, self.pos.y + self.speed))
        if keys["left"]:
            self.move(pygame.Vector2(self.pos.x - self.speed, self.pos.y))
