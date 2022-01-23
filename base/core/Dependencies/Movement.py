from math import sqrt
import pygame
from typing import List, Tuple
from base.core.Game import Game

# Klasse zur Verarbeitung von Positionen und Berechnungen von Bewegungen
class Movement: 
    
    def sanitizeSpeed(speed: int):
        return speed * (Game.deltaTime / 1000)
    
    # Given a list of solid, blocking objects, check if a position of a given object is allowed.
    def allowPosition(obj: object, pos: pygame.Vector2, objs: List = None) -> bool:
        pyRect = pygame.Rect(pos.x, pos.y, obj.width, obj.height)
        objects = Game.level().solids if objs is None else objs
        for solid in objects: 
            if solid != obj and solid.collidesWith(pyRect):
                return False
        return True
    
    def collidingObjects(obj: object, pos: pygame.Vector2, objs=None) -> List[object]:
        objects = []
        pyRect = pygame.Rect(pos.x, pos.y, obj.width, obj.height)
        solids = Game.level().solids if objs is None else objs

        for solid in solids:
            if solid.collidesWith(pyRect):
                objects.append(solid)
        return objects

    # Given a list of solid, blocking objects, return the furthest position a given object can move, till it will be blocked
    # Is the object blocked in its original position, it returns None
    def furthestMove(obj: object, pos: pygame.Vector2, startPos: pygame.Vector2 = None, objs = None) -> pygame.Vector2 or None:
        startPos = obj.pos if startPos is None else startPos
        x = startPos.y == pos.y

        steps = int(pos.x - startPos.x if x else pos.y - startPos.y)
        if steps == 0:
            return pos if Movement.allowPosition(obj, pos, objs) else None
        
        stepsRange = list(range(0, steps + 1 if steps > 0 else steps - 1, 1 if steps > 0 else -1))
        for s in stepsRange:
            i = abs(s)
            pos = pygame.Vector2(startPos.x + s if x else startPos.x, startPos.y + s if not x else startPos.y)
            if Movement.allowPosition(obj, pos, objs) == False:
                if i == 0:
                    return None
                return stepsRange[i - 1]
            stepsRange[i] = pos
        return stepsRange[-1]
    
    # Selbes Prinzip wie bei .furthestMove(), es werden dagegen noch die kolliderienden Objekte zurückgegeben
    def furthestMove_collider(obj: object, pos: pygame.Vector2, startPos: pygame.Vector2 = None, objs =None) -> Tuple[pygame.Vector2 or None, List[object]]:
        startPos = obj.pos if startPos is None else startPos
        x = startPos.y == pos.y

        steps = int(pos.x - startPos.x if x else pos.y - startPos.y)
        if steps == 0:
            return pos if Movement.allowPosition(obj, pos, objs) else None
        
        stepsRange = list(range(0, steps + 1 if steps > 0 else steps - 1, 1 if steps > 0 else -1))
        for s in stepsRange:
            i = abs(s)
            pos = pygame.Vector2(startPos.x + s if x else startPos.x, startPos.y + s if not x else startPos.y)
            collidingObjects = Movement.collidingObjects(obj, pos, objs)
            if len(collidingObjects) > 0:
                if i == 0:
                    return (None, collidingObjects)
                return (stepsRange[i - 1], collidingObjects)
            stepsRange[i] = pos
        return (stepsRange[-1], [])

    # Given a list of solid, blocking objects, return the first position a given object can move, till it will be blocked
    # Is the object blocked in its original position, it returns None
    def firstMove(obj: object, pos: pygame.Vector2, solidObjects: List[object], startPos: pygame.Vector2 = None, objs = None) -> pygame.Vector2 or None:
        startPos = obj.pos if startPos is None else startPos
        x = pos.y == startPos.y

        steps = int(pos.x - startPos.x if x else pos.y - startPos.y)
        stepsRange = list(range(0, steps, 1 if steps > 0 else -1))
        for s in stepsRange:
            pos = pygame.Vector2(startPos.x + s if x else startPos.x, startPos.y + s if not x else startPos.y)
            if Movement.allowPosition(obj, pos, objs) == True:
                return pos
        return None
    
    def furthestLineMovement(obj: object, pos: pygame.Vector2, objs=None):
        xDiff = pos.x - obj.pos.x 
        yDiff = pos.y - obj.pos.y
        distance = sqrt(xDiff ** 2 + yDiff ** 2)
        xAdjust = xDiff / distance
        yAdjust = yDiff / distance
        lastPos = pos
        for i in range(int(distance)):
            _pos = pygame.Vector2(int(obj.pos.x + i * xAdjust), int(obj.pos.y + i* yAdjust))
            if Movement.allowPosition(obj, _pos, objs) is False:
                return (lastPos, Movement.collidingObjects(obj, lastPos, objs))
            lastPos = pos
        return (pos, [])