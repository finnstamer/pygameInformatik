from typing import List
from base.core.Event.Events import Events
from base.object.GameObject import GameObject

from base.object.KI.Action import Action


class Routine():
    def __init__(self, obj: GameObject) -> None:
        self.object = obj
        self.actions: List[Action] = []
        self.pendingAction: Action = None
        self.pending = False
    
    def setActions(self, actions: List[Action]):
        self.pendingAction = None
        self.actions = actions
        return self
    
    def run(self):
        self.pending = True
        print(len(self.actions))
        if self.pendingAction is None:
            if len(self.actions) == 0:
                self.pending = False
                return
            self.pendingAction = self.actions[0]
            self.pendingAction.start()
        
        if self.pendingAction.state == 2:
            self.actions.pop(0)
            self.pendingAction = None