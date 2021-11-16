import pygame

from base.object.GameObject import GameObject
from settings import screen
class CircleObject(GameObject):
    def __init__(self, radius: int, width: int) -> None:
        super().__init__()
        self.radius = radius
        self.width = width
    
    def buildRect(self):
        return pygame.draw.circle(screen, self.color, self.pos, self.radius, self.width)
