from pygame import Vector2
from base.object.GameObject import GameObject
from base.object.AI.Action import Action
from base.object.MovableObject import MovableObject


class MovementAction(Action):
    def __init__(self, obj: MovableObject, start:Vector2, end:Vector2) -> None:
        super().__init__()
        self.object: MovableObject = obj
        self.startState: Vector2 = start
        self.endState: Vector2 = end

    def run(self):
        xDiff = self.endState.x - self.object.pos.x 
        yDiff = self.endState.y - self.object.pos.y 
        xMovement = abs(xDiff) > abs(yDiff)
               
        distance = xDiff if xMovement else yDiff
        speed = distance
        if abs(distance) > self.object.speed:
            speed = self.object.speed * distance / abs(distance)
        segmentPos = Vector2(self.object.pos.x + speed if xMovement else self.object.pos.x, self.object.pos.y + speed if not xMovement else self.object.pos.y)
        self.object.updatePos(segmentPos) 

    def isFinished(self) -> bool:
        return self.object.pos == self.endState
    
