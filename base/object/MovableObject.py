import pygame
from base.core.Dependencies.Movement import Movement
from base.core.Event.Events import Events
from base.core.Game import Game

from base.object.GameObject import GameObject
 
class MovableObject(GameObject):
    def __init__(self) -> None:
        super().__init__()
        self.speed = 1
    

    # Bewegt das Objekt direkt zu einer Position, wenn es dort nicht blockiert wird.
    def move(self, pos: pygame.Vector2):
        # if Game.level.allowMove(self, pos):
        if Movement.allowPosition(self, pos, Game.level.allSolidObjects()): 
            self.updatePos(pos)
    
    # Bewegt das Objekt bis zu den weitesten Step, der das Objekt mit keinem anderen solidem Objekt kollidieren lässt.
    def moveBySteps(self, steps=0, x=True):
        xDelta = steps if x else 0
        yDelta = steps if not x else 0
        vec = pygame.Vector2(self.pos.x + xDelta, self.pos.y + yDelta)
        pos = Movement.furthestMove(self, vec, Game.level.allSolidObjects())
        self.updatePos(pos)
            
        
    # Überarbietung per Errechnung der Distanz zum nearest solid Object in eine bestimmte Richtung. TODO
    def furthestMove(self, vec: pygame.Vector2, x=True) -> pygame.Vector2 or None:
        steps = int(vec.x - self.pos.x if x else vec.y - self.pos.y)
        if steps == 0:
            return vec if Game.level.allowMove(self, vec) else None
        
        stepsRange = list(range(0, steps, 1 if steps > 0 else -1))
        for s in stepsRange:
            i = abs(s)
            pos = pygame.Vector2(self.pos.x + s if x else self.pos.x, self.pos.y + s if not x else self.pos.y)
            if Game.level.allowMove(self, pos) == False:
                if i == 0:
                    return None
                return stepsRange[i - 1]
            stepsRange[i] = pos
        return stepsRange[-1]

    # Es ist intended, dass das Objekt eventuell in einem soliden Objekt ist.
    def firstMove(self, vec: pygame.Vector2, x=True) -> pygame.Vector2:
        steps = int(vec.x - self.pos.x if x else vec.y - self.pos.y)
        stepsRange = list(range(0, steps, 1 if steps > 0 else -1))
        for s in stepsRange:
            pos = pygame.Vector2(self.pos.x + s if x else self.pos.x, self.pos.y + s if not x else self.pos.y)
            if Game.level.allowMove(self, pos) == True:
                return pos
        return None
    