from typing import Tuple
import pygame
from base.core.Dependencies.Movement import Movement
from base.core.Game import Game

from base.object.GameObject import GameObject
 
class MovableObject(GameObject):
    def __init__(self, pos: pygame.Vector2 = pygame.math.Vector2(0, 0), width: int = 0, height: int = 0, color: Tuple = (0, 0, 0)) -> None:
        super().__init__(pos=pos, width=width, height=height, color=color)
        self.speed = 1
        self.allowMovement = True
    
    # Bewegt das Objekt zur weitest möglichen Position in Richtung pos
    def move(self, pos: pygame.Vector2):
        # if Game.level.allowMove(self, pos):
        xMov = self.pos.y == pos.y
        furthestPos = Movement.furthestMove(self, pos)
        if furthestPos is not None:
            self.updatePos(furthestPos)            
        
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
    