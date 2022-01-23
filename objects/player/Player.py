from typing import Dict
import pygame
from base.core.Dependencies.Controls import Controls
from base.core.Dependencies.Movement import Movement
from base.core.Dependencies.NodeVisualizer import NodeVisualizer
from base.core.Event.Events import Events
from base.core.Game import Game
from base.core.Object.Factory import Factory
from base.core.Object.GameObject import GameObject

class Player(GameObject):
    def __init__(self) -> None:
        super().__init__()
        Factory.setAlias(self, "player")
        self.pos = pygame.math.Vector2(15, 25);
        self.color = (250, 50, 50)
        self.solid = False
        self.height = 25
        self.width = 25
        
        self.solid = True
        self.fluid = True

        self.setImage("images/player.png")
        self.speed = 300
        self.direction = 1 # Right
        self.allowMovements = True

        Game.use(Controls)
        self.subscribe("game.tick", self.onTick)        

    def onTick(self, event):
        if self.allowMovements:
            self.control(Controls.keys)
            self.oldMovement() # Alte gezielte Bewegungssteuerung

        clicked, pos = Controls.clicks["l"] 
        if clicked:
            # Factory.get("weapon").shoot(pygame.Vector2(pos))
            # print(pos)
            pass
        
        if Controls.released["space"]:
            pass

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
            self.move(pygame.Vector2(self.pos.x, self.pos.y - Movement.sanitizeSpeed(self.speed)))
        if keys["d"]:
            self.move(pygame.Vector2(self.pos.x + Movement.sanitizeSpeed(self.speed), self.pos.y))
        if keys["s"]:
            self.move(pygame.Vector2(self.pos.x, self.pos.y + Movement.sanitizeSpeed(self.speed)))
        if keys["a"]:
            self.move(pygame.Vector2(self.pos.x - Movement.sanitizeSpeed(self.speed), self.pos.y))
