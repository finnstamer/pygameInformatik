import pygame
from base.core.Event.Events import Events
from base.core.Game import Game

from base.object.GameObject import GameObject
 
class MovableObject(GameObject):
    def __init__(self) -> None:
        super().__init__()
        self.speed = 1
    

    # Bewegt das Objekt direkt zu einer Position, wenn es dort nicht blockiert wird.
    def move(self, pos: pygame.Vector2):
        if Game.level.allowMove(self, pos):
            self.updatePos(pos)
    
    # Bewegt das Objekt bis zu den weitesten Step, der das Objekt mit keinem anderen solidem Objekt kollidieren lässt.
    def moveByDelta(self, steps=0, x=True):
        moves = list(map(lambda s: pygame.Vector2(self.pos.x + s if x else self.pos.x, self.pos.y + s if not x else self.pos.y), range(0, steps, 1 if steps > 0 else -1)))
        for i in range(len(moves)):
            pos = moves[i]
            if Game.level.allowMove(self, pos) == False and i > 0:
                Events.dispatch("player.move", moves[i - 1])
                return self.updatePos(moves[i - 1])
        self.updatePos(moves[-1])
        Events.dispatch("player.move", moves[1])
    