from typing import Callable
from base.core.Event.Event import Event
from base.core.Event.Events import Events


class MiddlewareHandler():
    def __init__(self, action) -> None:
        self.action = action
        self.middlewares = {}
    
    def on(self, event: str, func: Callable):
        if event not in self.middlewares:
            self.middlewares[event] = []
            Events.subscribe(self, f"Action.{self.action.id}.{event}")
        self.middlewares[event].append(func)
    
    def receiveEvent(self, event: Event):
        eventName = ".".join(event.name.split(".")[2:])
        if self.middlewares[eventName] is not None: 
            for middleware in self.middlewares[eventName]:
                middleware(False)