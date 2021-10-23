import pygame;
from base.object.GameObject import GameObject


class Wall(GameObject):
    def __init__(self) -> None:
        super().__init__()
        self.solid = True
        self.color = (240, 240, 240)
        self.pos = pygame.math.Vector2(100, 100)
        self.width = 20
        self.height = 20
        self.updateRect()