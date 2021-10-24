import pygame

from base.object.Rectangle import Rectangle

class Collision():
    def __init__(self) -> None:
        self.collided = False
        self.collisionRect = Rectangle()
        self.dir = 0 #top clockwise

    # register each pixel of a that shares its coordinates with b
    def check(self, a: Rectangle, b: Rectangle) -> bool:
        uL = None
        uR = None
        lL = None

        for y in range(int(a.upperLeft.y), int(a.lowerLeft.y)):
            for x in range(int(a.upperLeft.x), int(a.upperRight.x)):
                vec = pygame.Vector2(x, y)
                if b.contains(vec):
                    if uL == None:
                        uL = vec
                    if uL != None and uL.y == y:
                        uR = vec
                    lL = vec
        
        if uL != None:
            self.collided = True
            self.collisionRect = Rectangle().byRect(pygame.Rect(uL.x, uL.y, uR.x - uL.x, lL.y - uL.y))
        return self.collided


