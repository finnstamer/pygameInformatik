import pygame
from typing import List
from base.core.Game import Game
from base.object.GameObject import GameObject

class Movement:        

    # Given a list of solid, blocking objects, check if a position of a given object is allowed.
    def allowPosition(obj: GameObject, pos: pygame.Vector2) -> bool:
        pyRect = obj.cRect.get(pos, pygame.Vector2(pos.x + obj.cRect.width, pos.y + obj.cRect.height)).toPyRect()
        for solid in Game.level.allSolidObjects(): 
            if solid.collidesWith(pyRect):
                return False
        return True

    # Given a list of solid, blocking objects, return the furthest position a given object can move, till it will be blocked
    # Is the object blocked in its original position, it returns None
    def furthestMove(obj: GameObject, pos: pygame.Vector2, startPos: pygame.Vector2 = None) -> pygame.Vector2 or None:
        startPos = obj.pos if startPos is None else startPos
        x = startPos.y == pos.y

        steps = int(pos.x - startPos.x if x else pos.y - startPos.y)
        if steps == 0:
            return pos if Movement.allowPosition(obj, pos) else None
        
        stepsRange = list(range(0, steps + 1 if steps > 0 else steps - 1, 1 if steps > 0 else -1))
        for s in stepsRange:
            i = abs(s)
            pos = pygame.Vector2(startPos.x + s if x else startPos.x, startPos.y + s if not x else startPos.y)
            if Movement.allowPosition(obj, pos) == False:
                if i == 0:
                    return None
                return stepsRange[i - 1]
            stepsRange[i] = pos
        return stepsRange[-1]

    # Given a list of solid, blocking objects, return the first position a given object can move, till it will be blocked
    # Is the object blocked in its original position, it returns None
    def firstMove(obj: GameObject, pos: pygame.Vector2, solidObjects: List[GameObject], startPos: pygame.Vector2 = None) -> pygame.Vector2 or None:
        startPos = obj.pos if startPos is None else startPos
        x = pos.y == startPos.y

        steps = int(pos.x - startPos.x if x else pos.y - startPos.y)
        stepsRange = list(range(0, steps, 1 if steps > 0 else -1))
        for s in stepsRange:
            pos = pygame.Vector2(startPos.x + s if x else startPos.x, startPos.y + s if not x else startPos.y)
            if Movement.allowPosition(obj, pos) == True:
                return pos
        return None