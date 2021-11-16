import pygame
from base.object.CircleBorderObject import CircleBorderObject
from base.object.CircleObject import CircleObject
from base.object.GameObject import GameObject


class CircleWall(CircleObject):
      def __init__(self, radius: int) -> None:
        super().__init__(radius)
        self.solid = True
        self.color = (100, 100, 100)
        self.pos = pygame.math.Vector2(2,8)


