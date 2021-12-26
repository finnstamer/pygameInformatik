from base.object.AI.PathFinder import PathFinder
from base.object.AI.Routines.MovementRoutine import MovementRoutine
from base.object.GameObject import GameObject


class FollowObjectRoutine(MovementRoutine):
    def __init__(self, obj: GameObject, target: GameObject) -> None:
        super().__init__(obj)
        self.target = target

        self.middlewareHandler.on("pendingAction.done", self.updateActions)
            
    def updateActions(self, x=False):
        if len(self.actions) > 0:
            targetNode = PathFinder.nearestNode(self.grid, self.target.pos)
            if self.actions[-1].endState != targetNode.pos:
                self.setStates(self.object, self.target.pos)
                self.createActions()
    