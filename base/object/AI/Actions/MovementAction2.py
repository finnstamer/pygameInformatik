from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.object.GameObject import GameObject
from base.object.AI.Action import Action
from pygame import Vector2

class MovementAction2(Action):
    def __init__(self, obj: GameObject, startState: Vector2, endState: Vector2) -> None:
        super().__init__(startState, endState)
        self.object = obj

    def receiveEvent(self, event: Event):
        self.run()
    
    def onStart(self):
        Events.subscribe(self, "game.tick")
    
    def onRun(self):
        xDiff = self.endState.x - self.object.pos.x 
        yDiff = self.endState.y - self.object.pos.y 
        xMovement = abs(xDiff) > abs(yDiff)
               
        distance = xDiff if xMovement else yDiff
        speed = distance
        if abs(distance) > self.object.speed:
            speed = self.object.speed * distance / abs(distance)
        segmentPos = Vector2(self.object.pos.x + speed if xMovement else self.object.pos.x, self.object.pos.y + speed if not xMovement else self.object.pos.y)
        self.object.updatePos(segmentPos)

    def onStop(self):
        Events.unsubscribe(self, "game.tick")
    
    def isFinished(self):
        return self.object.pos == self.endState