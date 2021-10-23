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
        
        self.corners = []
        self.area = 0
    

    def byRect(self, rect: pygame.Rect):
        self.upperLeft = pygame.Vector2(rect.topleft) 
        self.upperRight = pygame.Vector2(rect.topright)
        self.lowerLeft = pygame.Vector2(rect.bottomleft)
        self.lowerRight = pygame.Vector2(rect.bottomright)
        self.topLine = self.upperRight.x - self.upperLeft.x
        self.leftLine = self.lowerLeft.y - self.upperLeft.y

        self.corners = [self.upperLeft, self.upperRight, self.lowerLeft, self.lowerRight]
        self.area = self.topLine * self.leftLine
        return self

    def onXIntervall(self, x: int):
        return self.upperLeft.x < x < self.upperRight.x
    
    def onYIntervall(self, y: int):
        return self.upperLeft.y < y < self.lowerLeft.y

    def contains(self, vector: pygame.Vector2):
        return self.onXIntervall(vector.x) and self.onYIntervall(vector.y)