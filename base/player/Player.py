import pygame
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
from base.object.GameObject import GameObject

from base.player.Keys import Keys

class Player(GameObject):
    def __init__(self) -> None:
        GameObject.__init__(self)

        self.pos = pygame.math.Vector2((50, 50));
        self.color = (50, 50, 50)
        self.solid = True
        self.height = 50
        self.width = 50
        self.speed = 3

        self.updateRect()

    def move(self, keys: Keys):
        if keys.pressed["left"]:
            self.editPosBy(-self.speed)
        if keys.pressed["right"]:
            self.editPosBy(+self.speed)
        if keys.pressed["up"]:
            self.editPosBy(y=-self.speed)
        if keys.pressed["down"]:
            self.editPosBy(y=self.speed)
        if keys.pressed["space"]:
            self.pos.x += 50
