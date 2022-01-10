import pygame
from base.objects.CircleBorderObject import CircleOutlineObject

class CircleBorderWall(CircleOutlineObject):
      def __init__(self, radius: int, width: int) -> None:
        super().__init__(radius, width)
        self.solid = True
        self.color = (100, 100, 100)
        self.pos = pygame.math.Vector2(2,8)
        