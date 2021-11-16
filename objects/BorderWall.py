import pygame
from base.object.GameObject import GameObject


class BorderWall (GameObject):
      def __init__(self) -> None:
        super().__init__()
        self.solid = True
        self.color = (100, 100, 100)
        self.pos = pygame.math.Vector2(2,8)
        self.altRect = pygame.draw.rect(100,200,100,2)
        