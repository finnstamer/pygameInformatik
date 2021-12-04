from typing import List

import pygame
from base.object.GameObject import GameObject
from settings import screen
class Movement:        

    # Given a list of solid, blocking objects, check if a position of a given object is allowed.
    def allowPosition(obj: GameObject, pos: pygame.Vector2, solidObjects: List[GameObject]) -> bool:
        pyRect = obj.cRect.get(pos, pygame.Vector2(pos.x + obj.cRect.width, pos.y + obj.cRect.height)).toPyRect()
        for solid in solidObjects: 
            if solid.collidesWith(pyRect):
                return False
        return True

    # Given a list of solid, blocking objects, return the furthest position a given object can move, till it will be blocked
    # Is the object blocked in its original position, it returns None
    def furthestMove(obj: GameObject, pos: pygame.Vector2, solidObjects: List[GameObject], startPos: pygame.Vector2 = None) -> pygame.Vector2 or None:
        startPos = startPos if startPos is not None else obj.pos
        xMovement = pos.y == startPos.y
        steps = int(pos.x - startPos.x if xMovement else pos.y - startPos.y)
        if steps == 0:
            return pos if Movement.allowPosition(obj, startPos, solidObjects) else None
        
        stepsRange = list(range(0, steps + 1, 1 if steps > 0 else -1))
        for s in stepsRange:
            i = abs(s)
            pos = pygame.Vector2(
                startPos.x + s if xMovement else startPos.x,
                startPos.y + s if not xMovement else startPos.y
            )
            if Movement.allowPosition(obj, pos, solidObjects) == False:
                if i == 0:
                    return None
                return stepsRange[i - 1]
            stepsRange[i] = pos
        return stepsRange[-1]

    # Given a list of solid, blocking objects, return the first position a given object can move, till it will be blocked
    # Is the object blocked in its original position, it returns None
    def firstMove(obj: GameObject, pos: pygame.Vector2, solidObjects: List[GameObject], startPos: pygame.Vector2 = None) -> pygame.Vector2 or None:
        startPos = startPos if startPos is not None else obj.pos
        xMovement = pos.y == startPos.y

        steps = int(pos.x - startPos.x if xMovement else pos.y - startPos.y)
        stepsRange = list(range(0, steps + 1, 1 if steps > 0 else -1))

        for s in stepsRange:
            pos = pygame.Vector2(startPos.x + s if xMovement else startPos.x, startPos.y + s if not xMovement else startPos.y)
            if Movement.allowPosition(obj, pos, solidObjects):
                return pos
        return None
    