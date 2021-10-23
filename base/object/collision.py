import pygame

from base.object.Rectangle import Rectangle

class Collision():
    def __init__(self) -> None:
        self.collided = False
        self.collisionRect = pygame.Rect(0, 0, 0, 0)
        self.dir = 0 #top clockwise

    def check(self, a: Rectangle, b: Rectangle) -> bool:
        # check for each pixel that shares its coordinates with b
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
            self.collisionRect = pygame.Rect(uL.x, uL.y, uR.x - uL.x, lL.y - uL.y)
            print(uL, uR, lL)
            return True
        return False


