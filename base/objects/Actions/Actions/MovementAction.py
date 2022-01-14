from base.core.Action.AbstractAction import AbstractAction
from base.core.Event.Events import Events
from base.core.Object.GameObject import GameObject
from pygame import Vector2

# Aktion zur Bewegung eines Objektes von der ursprünglichen Position zu einer gegebenen.
# Kollisionen werden nicht beachtet.
class MovementAction(AbstractAction):
    def __init__(self, obj: GameObject, endState: Vector2) -> None:
        super().__init__(obj, endState)
        
        # Zum Starten wird die .run() Methode an das "game.tick" Event gebunden.
        # Demnach wird run jeden Tick ausgeführt
        self.middlewareHandler.on("start", lambda: Events.subscribe("game.tick", self.run, self))
        self.middlewareHandler.on("run", self.onRun)
        # Deabonniert .run() Methode beim Stopp
        self.middlewareHandler.on("stop", lambda: Events.unsubscribe("game.tick", self.run, self))

    # Berechnet die nächste Bewegung auf Basis der .speed Eigenschaft des Objektes.
    # ! Kollision werden nicht beachtet !
    # Öffnet eine Connection auf "segmentPos" mit der berechneten Position als Argument
    def onRun(self):
        xDiff = self.endState.x - self.object.pos.x 
        yDiff = self.endState.y - self.object.pos.y 
        xMovement = abs(xDiff) > abs(yDiff)
               
        distance = xDiff if xMovement else yDiff
        speed = distance
        if abs(distance) > self.object.speed:
            speed = self.object.speed * distance / abs(distance)

        segmentPos = Vector2(self.object.pos.x + speed if xMovement else self.object.pos.x, self.object.pos.y + speed if not xMovement else self.object.pos.y)
        segmentPos = self.middlewareHandler.openConnection("segmentPos", segmentPos)
        self.object.updatePos(segmentPos)
    
    # Aktion ist fertig, wenn die Position des Objektes den gegebenen .endState entspricht.
    def isFinished(self):
        return self.object.pos == self.endState