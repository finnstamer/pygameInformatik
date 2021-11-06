from typing import Dict, List
from copy import deepcopy
import pygame

from base.geometry.Vec2 import Vec2

# Eigene Klasse anstatt pygame.Rect, da Rect mir zu wenig wichtige Informationen und Shorthands lieferte.
# Umwandelung in pygame.Rect und andersherum ist möglich. 
class Rectangle():
    def __init__(self) -> None:
        default = pygame.Vector2()
        self.y = default
        self.x = default
        self.upperLeft = default
        self.upperRight = default
        self.lowerLeft = default
        self.lowerRight = default
        self.topLine = 0
        self.leftLine = 0
        self.center = default
        
        self.corners: List[pygame.Vector2] = []
        self.area = 0
        self.width = 0
        self.height = 0
    

    @staticmethod
    def byRect(rect: pygame.Rect):
        return Rectangle.get(Vec2.fromTuple(rect.topleft), Vec2.fromTuple(rect.bottomright))

    @staticmethod
    def get(uL: pygame.Vector2, lR: pygame.Vector2):
        r = Rectangle()

        r.upperLeft = uL
        r.lowerRight = lR
        r.upperRight = pygame.Vector2(lR.x, uL.y)
        r.lowerLeft = pygame.Vector2(uL.x, lR.y)
        r.topLine = r.upperRight.x - r.upperLeft.x
        r.leftLine = r.lowerLeft.y - r.upperLeft.y
        r.center = pygame.Vector2((r.upperLeft.x + r.upperRight.x) / 2, (r.lowerLeft.y + r.upperLeft.y) / 2)
        r.corners = [r.upperLeft, r.upperRight, r.lowerRight, r.lowerLeft]
        r.area = r.topLine * r.leftLine
        r.width = lR.x - uL.x
        r.height = lR.y - uL.y
        r.y = r.upperLeft.y
        r.x = r.upperLeft.x
        return r

    def toPyRect(self):
        return pygame.Rect(self.upperLeft.x, self.upperLeft.y, self.width, self.height)

    @staticmethod
    def byCorner(c: List[pygame.Vector2]):
        pyRect = pygame.Rect(
            c[0].x, c[0].y, 
            c[1].x - c[0].x,
            c[3].y - c[0].y
        )
        return Rectangle.byRect(pyRect)

    def onXIntervall(self, x: int):
        return self.upperLeft.x < x <= self.upperRight.x
    
    def onYIntervall(self, y: int):
        return self.upperLeft.y <= y <= self.lowerLeft.y
    
    def contains(self, vec: pygame.Vector2):
        return self.onXIntervall(vec.x) and self.onYIntervall(vec.y)

    def copy(self):
        return deepcopy(self)