from typing import Tuple
from base.core.Object.GameObject import GameObject
import pygame
from settings import screen
class RGBAObject(GameObject):
    def __init__(self, pos: pygame.Vector2 = ..., width: int = 0, height: int = 0, color: Tuple= ...) -> None:
        super().__init__(pos, width, height, color)
        self.alpha = 0
        
    def setAlpha(self, alpha:int):
        self.alpha = alpha
        return self
    
    def drawRect(self):
        surf = pygame.Surface(self.rect.size, pygame.SRCALPHA)
        surf.set_alpha(self.alpha)
        surf.fill(self.color)
        screen.blit(surf, self.rect)
        return self