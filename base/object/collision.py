from os import error
from typing import Dict, List
import pygame

from base.object.Rectangle import Rectangle

class Collision():
    
    def __init__(self) -> None:
        self.collided = False
        self.collisionRect = Rectangle()
        self.dir = 0
    
    # Wenn mindestens ein Eckpunkt von a innerhalb b oder andersherum liegt, liegt eine Kollision vor.
    def isColliding(self, a: Rectangle, b: Rectangle):
        return len(Collision.cornerIntersection(a, b)) > 0 or len(Collision.cornerIntersection(b, a)) > 0
    
    # Gibt ein Rechteck der Fläche, die sich a und b teilen zurück
    def intersection(self, a: Rectangle, b: Rectangle) -> Rectangle:
        if self.isColliding(a, b) == False:
            return Rectangle()

        d = pygame.Vector2(0, 0)
        corners = [d, d, d, d]
        for i in range(0, 4):
            for j in range(0, 4):
                bC = b.corners[j]
                if a.contains(bC):
                    corners[j] = bC
                    continue
            
                corners[j] = a.corners[j]
                if a.onXIntervall(bC.x):
                    corners[j] = pygame.Vector2(bC.x, a.corners[j].y)
                if a.onYIntervall(bC.y):
                    corners[j] = pygame.Vector2(a.corners[j].x, bC.y)
                    
        return Rectangle.byCorner(corners)

    # Gibt eine Liste an Eckpunkten von b, die in a liegen zurück
    @staticmethod
    def cornerIntersection(a: Rectangle, b: Rectangle) -> Dict[int, pygame.Vector2]:
        corners: Dict[int, pygame.Vector2] = {}
        for i in range(1, 3):
            for j in range(0, 4):
                bC = b.corners[j]
                if a.contains(bC):
                    corners[j] = bC
        return corners
    
    def check(self, a: Rectangle, b: Rectangle) -> bool:
        self.collided = self.isColliding(a, b)
        if self.collided:
            self.collisionRect = self.intersection(a, b)
        return self.collided
    
    # Gibt ein Rechteck der Fläche, die sich a und b teilen zurück
    # !!! Allerdings durchsucht es jeden Punkt von a, ob dieser sich ein Punkt mit b teilt. Dies hat sehr negative Einflüsse auf die Performance.
    # !!! Für Rechtecke einfach Collision.intersection verwenden
    # !!! Diese Methode braucht bei einem Quadrat mit der Seitenlänge von 50, 2500 Iterationen. Collision.intersection unabhängig der Fläche nur 16 
    def intersection_full(self, a: Rectangle, b: Rectangle) -> Rectangle:
        uL = uR = lL = None

        self.collided = self.check(a, b)
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
        


