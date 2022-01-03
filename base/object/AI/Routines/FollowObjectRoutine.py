from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.object.AI.PathFinder import PathFinder
from base.object.AI.Routines.MovementRoutine import MovementRoutine
from base.object.GameObject import GameObject


class FollowObjectRoutine(MovementRoutine):
    def __init__(self, obj: GameObject, target: GameObject) -> None:
        super().__init__(obj)
        self.target = target

        self.middlewareHandler.on("set", self.onSet, 0)
        self.middlewareHandler.on("pendingAction.done", self.reAdjust)
        self.middlewareHandler.on("finished", lambda: Events.subscribe(f"{self.target.id}.moved", self.restart))
        self.middlewareHandler.on("stop", lambda: Events.unsubscribe(f"{self.target.id}.moved", self.restart))
    
    def restart(self, event: Event):
        self.setStates(self.object, self.target)
        self.start()
        if len(self.actions) > 0:    
            Events.unsubscribe(event.name, self.restart)

    def reAdjust(self, x=False):
        targetNode = PathFinder.nearestNode(self.grid, self.target.pos)
        if self.actions[-1].endState != targetNode.pos:
            self.stop()
            self.setStates(self.object, self.target)
            self.start()

    def onSet(self):
        self.endState = self.target.pos