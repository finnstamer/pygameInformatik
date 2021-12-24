from typing import Dict
import pygame
from base.core.Dependencies.Controls import Controls
from base.core.Dependencies.NodeVisualizer import NodeVisualizer
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.core.Game import Game
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
        Events.subscribe(self, "game.tick", "game.start")

    def default(self, obj):
        obj.color = (0, 250, 250)
        return obj
    
    def receiveEvent(self, event: Event):
        if event.name == "game.start":
            self.routine = MovementRoutine(Factory.get("ekto1"))

        if event.name == "game.tick":
            keys = Controls.keys
            self.control(keys)
            # self.move(self.nextPos())
            self.oldMovement()

            if keys["escape"]:
                self.routine.create(Factory.get("ekto1").pos, self.pos).start()
            
            if keys["space"]:
                root = PathFinder.nearestNode(self.routine.grid, self.pos)
                self.neighborVisualizer.setNodes(list(root.neighborsToList().values())).start()
 
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
