from os import error
from typing import Dict
import pygame

from base.object.Rectangle import Rectangle

class Collision():
    def __init__(self) -> None:
        self.collided = False
        self.collisionRect = Rectangle()
        self.dir = 0 #top clockwise

    def isCollided(self, a: Rectangle, b: Rectangle) -> bool:
        for i in range(1, 5):
            aC = a.corners[i - 1]
            aOC = a.corners[i % 4]
            for j in range(1, 5):
                bC = b.corners[j - 1]
                if (aC.x >= bC.x >= aOC.x) and (aC.y <= bC.y <= aOC.y):
                    return True
        return False

    def getIntersection_performance(self, a: Rectangle, b: Rectangle) -> Rectangle:
        corners: Dict[int, pygame.Vector2] = {}
        for i in range(1, 5):
            aC = a.corners[i - 1]
            aOC = a.corners[i % 4]
            for j in range(1, 5):
                bC = b.corners[j - 1]
                if (aC.x >= bC.x >= aOC.x) and (aC.y <= bC.y <= aOC.y):
                    corners[j - 1] = bC

        return Rectangle.byCorner(corners)
    
    # register each pixel of a that shares its coordinates with b
    def getIntersection(self, a: Rectangle, b: Rectangle) -> Rectangle:
        uL = uR = lL = None

        self.collided = self.isCollided(a, b)
        if self.collided:
            for y in range(int(a.upperLeft.y), int(a.lowerLeft.y) + 1):
                for x in range(int(a.upperLeft.x), int(a.upperRight.x) + 1):
                    vec = pygame.Vector2(x, y)
                    if b.contains(vec):
                        if uL == None:
                            uL = vec
                        if uL != None and uL.y == y:
                            uR = vec
                        lL = vec
            return Rectangle().byRect(pygame.Rect(uL.x, uL.y, uR.x - uL.x, lL.y - uL.y))
        raise error("No Collision Found.")
        


