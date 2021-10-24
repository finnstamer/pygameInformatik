from typing import List
import pygame;

class Rectangle():
    def __init__(self) -> None:
        default = pygame.Vector2()
        self.upperLeft = default
        self.upperRight = default
        self.lowerLeft = default
        self.lowerRight = default
        self.topLine = 0
        self.leftLine = 0
        self.center = default
        
        self.corners = []
        self.area = 0
        self.width = 0
        self.height = 0
    

    def byRect(self, rect: pygame.Rect):
        self.upperLeft = pygame.Vector2(rect.topleft) 
        self.upperRight = pygame.Vector2(rect.topright)
        self.lowerLeft = pygame.Vector2(rect.bottomleft)
        self.lowerRight = pygame.Vector2(rect.bottomright)
        self.topLine = self.upperRight.x - self.upperLeft.x
        self.leftLine = self.lowerLeft.y - self.upperLeft.y
        self.center = pygame.Vector2((self.upperLeft.x + self.upperRight.x) / 2, (self.lowerLeft.y + self.upperLeft.y) / 2)

        self.corners = [self.upperLeft, self.upperRight, self.lowerLeft, self.lowerRight]
        self.area = self.topLine * self.leftLine
        self.width = rect.width
        self.height = rect.height
        return self

    def toPyRect(self):
        return pygame.Rect(self.upperLeft.x, self.upperLeft.y, self.width, self.height)

    def onXIntervall(self, x: int):
        return self.upperLeft.x <= x <= self.upperRight.x
    
    def onYIntervall(self, y: int):
        return self.upperLeft.y <= y <= self.lowerLeft.y

    def contains(self, vector: pygame.Vector2):
        return self.onXIntervall(vector.x) and self.onYIntervall(vector.y)