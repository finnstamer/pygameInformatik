from typing import List
from copy import deepcopy
from pygame import Vector2, Rect

# Klasse zur genauen Beinhaltung bestimmter Variablen und Methoden.
# Umwandelung in mit pygame kompatiblen Klassen möglich.
class Rectangle():
    def __init__(self) -> None:
        default = Vector2()
        self.y = default
        self.x = default
        self.upperLeft = default
        self.upperRight = default
        self.lowerLeft = default
        self.lowerRight = default
        self.topLine = 0
        self.leftLine = 0
        self.center = default
        
        self.corners: List[Vector2] = []
        self.area = 0
        self.width = 0
        self.height = 0
    
    @staticmethod
    def byRect(rect: Rect):
        return Rectangle.get(Vector2(rect.topleft), Vector2(rect.bottomright))

    @staticmethod
    def get(uL: Vector2, lR: Vector2):
        r = Rectangle()

        r.upperLeft = uL
        r.lowerRight = lR
        r.upperRight = Vector2(lR.x, uL.y)
        r.lowerLeft = Vector2(uL.x, lR.y)
        r.topLine = r.upperRight.x - r.upperLeft.x
        r.leftLine = r.lowerLeft.y - r.upperLeft.y
        r.center = Vector2((r.upperLeft.x + r.upperRight.x) / 2, (r.lowerLeft.y + r.upperLeft.y) / 2)
        r.corners = [r.upperLeft, r.upperRight, r.lowerRight, r.lowerLeft]
        r.area = r.topLine * r.leftLine
        r.width = lR.x - uL.x
        r.height = lR.y - uL.y
        r.y = r.upperLeft.y
        r.x = r.upperLeft.x
        return r

    def toPyRect(self):
        return Rect(self.upperLeft.x, self.upperLeft.y, self.width, self.height)

    @staticmethod
    def byCorner(c: List[Vector2]):
        pyRect = Rect(
            c[0].x, c[0].y, 
            c[1].x - c[0].x,
            c[3].y - c[0].y
        )
        return Rectangle.byRect(pyRect)

    def onXIntervall(self, x: int):
        return self.upperLeft.x < x <= self.upperRight.x
    
    def onYIntervall(self, y: int):
        return self.upperLeft.y <= y <= self.lowerLeft.y
    
    def contains(self, vec: Vector2):
        return self.onXIntervall(vec.x) and self.onYIntervall(vec.y)

    def copy(self):
        return deepcopy(self)