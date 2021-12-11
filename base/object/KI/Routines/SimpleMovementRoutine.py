from pygame import Vector2
from base.core.Dependencies.NodeStorage import NodeStorage
from base.core.Dependencies.NodeVisualizer import NodeVisualizer
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.object.GameObject import GameObject
from base.object.KI.Actions.MovementAction import MovementAction
from base.object.KI.PathFinder import PathFinder
from base.object.KI.Routine import Routine

class SimpleMovementRoutine(Routine):
    def __init__(self, obj: GameObject) -> None:
        super().__init__(obj)
        self.grid = NodeStorage.find(obj)
        self.target = None

        self.gridVisualizer = NodeVisualizer(self.grid).start()
        self.pathVisualizer = NodeVisualizer([])
        
    def createActions(self):
        startNode = PathFinder.nearestNode(self.grid, self.object.pos)
        endNode = PathFinder.nearestNode(self.grid, self.target) 
        paths = PathFinder.find(startNode, endNode, 10)

        if len(paths) == 0:
            return
        path = paths[0]
        self.pathVisualizer.setNodes(path).start()

        actions = []
        for n in path:
            if n.pos is None:
                continue
            lastPos = self.actions[-1].endState if len(self.actions) > 0 else self.object.pos
            actions.append(MovementAction(self.object, lastPos, n.pos)) 
        self.setActions(actions)        
    
    def stop(self):
        Events.unsubscribe(self, "game.tick")
        return self

    def start(self, target: Vector2):
        self.target = target
        self.createActions()
        Events.subscribe(self, "game.tick")

    def receiveEvent(self, event: Event):
        if event.name == "game.tick":
            self.run()