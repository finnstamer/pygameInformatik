from pygame import Vector2
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.object.GameObject import GameObject
from base.object.KI.Actions.MovementAction import MovementAction
from base.object.KI.PathFinder import PathFinder
from base.object.KI.Routine import Routine

class SimpleMovementRoutine(Routine):
    def __init__(self, obj: GameObject, target: Vector2) -> None:
        super().__init__(obj)
        self.target = target
        
    def createActions(self):
        self.actions = []
        nodes = PathFinder.generateDynamicNodes(self.object)
        startNode = PathFinder.nearestNode(nodes, self.object.pos)
        endNode = PathFinder.nearestNode(nodes, self.target) 
        paths = PathFinder.find(startNode, endNode)

        if len(paths) == 0:
            return
        path = paths[0]
        
        for n in path:
            print(n.pos)
            if n.pos is None:
                continue
            lastPos = self.actions[-1].endState if len(self.actions) > 0 else self.object.pos
            self.actions.append(MovementAction(self.object, lastPos, n.pos)) 

        self.object.pos = self.actions[0].startState

    def start(self):
        Events.subscribe(self, "game.start", "game.tick")
        self.createActions()

    def receiveEvent(self, event: Event):
        if event.name == "game.tick":
            self.run()