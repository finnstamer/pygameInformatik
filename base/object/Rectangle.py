from os import stat
from typing import Dict, List
import pygame
from pygame import Rect, Vector2, rect;

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
    

    @staticmethod
    def byRect(rect: pygame.Rect):
        r = Rectangle()

        r.upperLeft = pygame.Vector2(rect.topleft) 
        r.upperRight = pygame.Vector2(rect.topright)
        r.lowerLeft = pygame.Vector2(rect.bottomleft)
        r.lowerRight = pygame.Vector2(rect.bottomright)
        r.topLine = r.upperRight.x - r.upperLeft.x
        r.leftLine = r.lowerLeft.y - r.upperLeft.y
        r.center = pygame.Vector2((r.upperLeft.x + r.upperRight.x) / 2, (r.lowerLeft.y + r.upperLeft.y) / 2)
        r.corners = [r.upperLeft, r.upperRight, r.lowerLeft, r.lowerRight]
        r.area = r.topLine * r.leftLine
        r.width = rect.width
        r.height = rect.height
        return r

    def toPyRect(self):
        return pygame.Rect(self.upperLeft.x, self.upperLeft.y, self.width, self.height)

    @staticmethod
    def byCorner(c: Dict[int, pygame.Vector2]):
        pyRect = pygame.Rect(
            c[0].x, c[0].y, 
            c[1].x - c[0].x,
            c[4].y - c[0].y
        )
        return Rectangle.byRect(pyRect)

    def onXIntervall(self, x: int):
        return self.upperLeft.x <= x <= self.upperRight.x
    
    def onYIntervall(self, y: int):
        return self.upperLeft.y <= y <= self.lowerLeft.y

    def contains(self, vector: pygame.Vector2):
        return self.onXIntervall(vector.x) and self.onYIntervall(vector.y)