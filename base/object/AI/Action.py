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
        self.middlewareHandler.dispatch("set")
        return self
    
    def start(self):
        self.progress = 1
        self.middlewareHandler.dispatch("start")
        return self
        

    def run(self, event):
        if self.isFinished():
            self.stop()
            self.progress = 2
            self.middlewareHandler.dispatch("finished")
            return
        self.middlewareHandler.dispatch("run")

    def stop(self):
        self.progress = 0
        self.middlewareHandler.dispatch("stop")
        return self
    
    def isFinished(self):
        raise NotImplementedError(f"'isFinished' Method on {self.__class__.__name__} not implemented.")
    