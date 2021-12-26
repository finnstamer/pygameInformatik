from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.object.GameObject import GameObject
from base.object.AI.Action import Action
from pygame import Vector2

class MovementAction(Action):
    def __init__(self, obj: GameObject, endState: Vector2) -> None:
        super().__init__(obj, endState)
        
        self.middlewareHandler.on("start", lambda: Events.subscribe("game.tick", self.run))
        self.middlewareHandler.on("run", self.onRun)
        self.middlewareHandler.on("stop", lambda: Events.unsubscribe("game.tick", self.run))

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
    
    def isFinished(self):
        return self.object.pos == self.endState