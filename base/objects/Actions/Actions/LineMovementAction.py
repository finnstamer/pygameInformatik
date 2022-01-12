from pygame import Vector2
from math import sqrt
from base.core.Object.GameObject import GameObject
from base.objects.Actions.Actions.MovementAction import MovementAction

# Action zur Berechnung einer geraden Bewegung in eine Richtung
# Wurde nur Teils getestet und ist !nicht! optimiert.
class LineMovementAction(MovementAction):
    def __init__(self, obj: GameObject, endState: Vector2) -> None:
        super().__init__(obj, endState)
        self.middlewareHandler.on("start", self.onStart)
        self.stepsToDo = 9999
    
    def onStart(self):
        xDiff = self.endState.x - self.object.pos.x 
        yDiff = self.endState.y - self.object.pos.y 
        distance = sqrt(xDiff ** 2 + yDiff ** 2)
        steps = int(distance / self.object.speed)
        if steps == 0:
            self.stepsToDo = 0
            return
        self.xAdjust = int(xDiff / steps)
        self.yAdjust = int(yDiff / steps)
        self.stepsToDo = steps
    
    # Überschreibt onRun von MovementAction
    def onRun(self):
        self.stepsToDo -= 1
        segmentPos = Vector2(self.object.pos.x + self.xAdjust, self.object.pos.y + self.yAdjust)
        segmentPos = self.middlewareHandler.openConnection("segmentPos", segmentPos)
        self.object.updatePos(segmentPos)
    
    def isFinished(self):
        return self.stepsToDo == 0
