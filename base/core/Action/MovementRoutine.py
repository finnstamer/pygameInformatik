from base.core.Action.AbstractRoutine import AbstractRoutine
from base.core.Dependencies.NodeStorage import NodeStorage
from base.core.Dependencies.NodeVisualizer import NodeVisualizer
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.nodes.PathFinder import PathFinder
from base.objects.Actions.Actions.LineMovementAction import LineMovementAction
from base.objects.Actions.Actions.MovementAction import MovementAction
from base.core.Object.GameObject import GameObject

# Klasse zur Erzeugung einer komplexen Bewegung auf Basis der Wegfindung
class MovementRoutine(AbstractRoutine):
    def __init__(self, obj: GameObject) -> None:
        super().__init__(obj, True)
        self.grid = NodeStorage.findGrid(self.object)
        self.pathVisualizer = NodeVisualizer([])
        self.gridVisualizer = NodeVisualizer([], (50, 50, 50))
        self.gridVisualizer.setNodes(self.grid)
        
        self.middlewareHandler.on("start", lambda: Events.subscribe("game.tick", self.run, self))
        self.middlewareHandler.on("stop", lambda: Events.unsubscribe("game.tick", self.run, self))

    def createActions(self):
        self.pendingAction = None
        self.stopActions()
        startNode = PathFinder.nearestNode(self.grid, self.object.pos)
        endNode = PathFinder.nearestNode(self.grid, self.endState) 
        paths = PathFinder.find(startNode, endNode, 100)

        if len(paths) == 0:
            return
        path = paths[0]

        actions = []
        for n in path:
            if n.pos is None:
                continue
            lastPos = self.actions[-1].endState if len(self.actions) > 0 else self.object.pos
            actions.append(MovementAction(self.object, n.pos)) 
        self.setActions(actions)  
        self.pathVisualizer.setNodes(path)