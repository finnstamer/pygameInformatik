import pygame

from base.core.Object.GameObject import GameObject
from settings import screen
class CircleOutlineObject(GameObject):
    def __init__(self, radius: int, border: int) -> None:
        super().__init__()
        self.radius = radius
        self.border = border
    
    def drawRect(self):
        pygame.draw.circle(screen, self.color, self.pos, self.radius, self.border)
    
    def buildRect(self):
        return pygame.draw.circle(screen, self.color, self.pos, self.radius, self.border)
