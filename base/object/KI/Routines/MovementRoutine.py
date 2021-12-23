from base.core.Dependencies.NodeStorage import NodeStorage
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.object.GameObject import GameObject
from base.object.KI.Actions.MovementAction2 import MovementAction2
from base.object.KI.PathFinder import PathFinder
from base.object.KI.Routine import Routine


class MovementRoutine(Routine):
    def __init__(self, obj: GameObject) -> None:
        super().__init__()
        self.object = obj
        self.grid = NodeStorage.findGrid(obj)
        self.target = None
    
    def onStart(self):
        Events.subscribe(self, "game.tick")
    
    def onStop(self):
        Events.unsubscribe(self, "game.tick")
        self.stopActions()

    def receiveEvent(self, event: Event):
        self.run()

    def createActions(self):
        self.stopActions()
        startNode = PathFinder.nearestNode(self.grid, self.object.pos)
        endNode = PathFinder.nearestNode(self.grid, self.endState) 
        paths = PathFinder.find(startNode, endNode, 50)

        if len(paths) == 0:
            return
        path = paths[0]

        actions = []
        for n in path:
            if n.pos is None:
                continue
            lastPos = self.actions[-1].endState if len(self.actions) > 0 else self.object.pos
            actions.append(MovementAction2(self.object, lastPos, n.pos)) 
        self.setActions(actions)  
    