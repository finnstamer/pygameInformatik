import pygame

from base.object.GameObject import GameObject
from settings import screen
class CircleObject(GameObject):
    def __init__(self, radius: int) -> None:
        super().__init__()
        self.radius = radius
    
    def buildRect(self):
        return pygame.draw.circle(screen, self.color, self.pos, self.radius)

    def drawRect(self):
        pygame.draw.circle(screen, self.color, self.pos, self.radius)

