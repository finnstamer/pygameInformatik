from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.object.AI.Routines.MiddlewareHandler import MiddlewareHandler
from base.object.Factory.Factory import Factory


class Action():
    def __init__(self, obj, endState) -> None:
        self.id = -1
        self.progress = 0
        Factory.append(self)
        self.middlewareHandler = MiddlewareHandler(self)
        self.setStates(obj, endState)
        
    def setStates(self, obj, endState):
        self.stop()
        self.object = obj
        self.endState = endState
        Events.dispatch(f"Action.{self.id}.set", {"action": self})
        return self
    
    def start(self):
        self.progress = 1
        Events.dispatch(f"Action.{self.id}.start", {"action": self})
        return self

    def run(self):
        if self.isFinished():
            self.stop()
            self.progress = 2
            return
        Events.dispatch(f"Action.{self.id}.run", {"action": self})

    def stop(self):
        self.progress = 0
        Events.dispatch(f"Action.{self.id}.stop", {"action": self})
        return self
    
    def isFinished(self):
        raise NotImplementedError(f"'isFinished' Method on {self.__class__.__name__} not implemented.")
    