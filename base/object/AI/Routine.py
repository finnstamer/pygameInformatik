from typing import List
from base.object.AI.Action import Action
from copy import deepcopy

class Routine(Action):
    def __init__(self) -> None:
        super().__init__(False, True)
        self.actions: List[Action] = []
        self.pendingAction = None
        
    def onStart(self):
        raise NotImplementedError(f"'onStart' Method on {self.__class__.__name__} not implemented.")
    
    def onStop(self):
        raise NotImplementedError(f"'onStop' Method on {self.__class__.__name__} not implemented.")
    
    def createActions(self):
        raise NotImplementedError(f"'createActions' Method on {self.__class__.__name__} not implemented.")
    
    def onRun(self):
        if self.progress == 0 or self.progress == 2:
            return
        if self.isFinished():
            self.progress = 2
            return
        
        if self.pendingAction is None:
            self.pendingAction = self.actions[0]
            return self.pendingAction.start()

        if self.pendingAction.progress == 2:
            self.actions.pop(0)
            self.pendingAction = None
            
    def isFinished(self):
        print(len(self.actions))
        return len(self.actions) == 0
    
    def create(self, startState, endState):
        self.stop()
        self.startState = startState
        self.endState = endState
        self.createActions()
        return self

    def setActions(self, actions: List[Action]):
        self.actions = actions
        self.pendingAction = None
    
    def stopActions(self):
        for a in self.actions:
            a.stop()
