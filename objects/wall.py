import pygame;
from base.object.GameObject import GameObject
import random;


class Wall(GameObject):
    def __init__(self) -> None:
        super().__init__()
        self.solid = True
        self.color = (240, 240, 240)
        self.pos = pygame.math.Vector2(random.randrange(50, 400), random.randrange(50, 200))
        self.width = 20
        self.height = 20
        self.updateRect()