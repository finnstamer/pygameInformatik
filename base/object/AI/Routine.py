from typing import List
from base.core.Event.Events import Events
from base.object.AI.Action import Action

class Routine(Action):
    def __init__(self, obj, endState) -> None:
        super().__init__(obj, endState)
        self.actions: List[Action] = []
        self.pendingAction = None

        self.middlewareHandler.on("stop", self.stopActions)
        self.middlewareHandler.on("set", self.createActions)
        self.middlewareHandler.on("run", self.runActions)
    
    def createActions(self):
        raise NotImplementedError(f"'createActions' Method on {self.__class__.__name__} not implemented.")
    
    def runActions(self):
        if self.progress == 0 or self.progress == 2:
            return
        if self.isFinished():
            self.progress = 2
            return
        
        if self.pendingAction is None:
            if len(self.actions) == 0:
                return
            self.pendingAction = self.actions[0]
            Events.dispatch(f"Action.{self.id}.pendingAction.set", {"action": self, "done": self.pendingAction})
            return self.pendingAction.start()

        if self.pendingAction.progress == 2:
            Events.dispatch(f"Action.{self.id}.pendingAction.done", {"action": self, "done": self.pendingAction})
            self.actions.pop(0)
            self.pendingAction = None

    def isFinished(self):
        return len(self.actions) == 0

    def setActions(self, actions: List[Action]):
        self.actions = actions
        self.pendingAction = None
    
    def stopActions(self):
        for a in self.actions:
            a.stop()
