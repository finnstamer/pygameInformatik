from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.core.Action.MovementRoutine import MovementRoutine
from base.core.Object.GameObject import GameObject
from base.nodes.PathFinder import PathFinder

# Klasse zur Verfolgung eines Objektes
class FollowObjectRoutine(MovementRoutine):
    def __init__(self, obj: GameObject, target: GameObject) -> None:
        super().__init__(obj)
        self.target = target

        self.middlewareHandler.on("set", self.onSet, 0)
        self.middlewareHandler.on("pendingAction.done", self.reAdjust)
        self.middlewareHandler.on("finished", lambda: Events.subscribe(f"{self.target.id}.moved", self.restart, self))
        # Wenn Routine von außen gestoppt wird, wird auch das ggf. abonnierte .moved Event des zu verfolgenden Objekt deabonniert
        self.middlewareHandler.on("stop", lambda: Events.unsubscribe(f"{self.target.id}.moved", self.restart, self))
    
    # Damit Routine nicht aufhört, wenn beide Objekte auf derselben Node sind, wird vom verfolgten Objekt
    # das .moved Event abonniert und sobald Micro-Bewegungen benötigt werden und die Bewegung normal abläuft,
    # wieder deabonniert 
    def restart(self, event: Event):
        self.setStates(self.object, self.target)
        self.start()
        if len(self.actions) > 0:    
            Events.unsubscribe("{self.target.id}.moved", self.restart, self)

    # Nach jeder fertigen Micro-Bewegung (also zwischen zwei Nodes) wird überprüft,
    # ob die Zielnode des Paths auch noch mit der nächsten Node des zu verfolgenden Objekt übereinstimmt
    def reAdjust(self):
        targetNode = PathFinder.nearestNode(self.grid, self.target.pos)
        if self.actions[-1].endState != targetNode.pos:
            self.stop()
            self.setStates(self.object, self.target)
            self.start()

    def onSet(self):
        self.endState = self.target.pos