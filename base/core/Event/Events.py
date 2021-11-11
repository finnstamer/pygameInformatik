from typing import Any, Callable, Dict, List
from base.core.Event.Event import Event
from base.object.GameObject import GameObject

class Events():
    subscribers: Dict[str, List[GameObject]] = {}
    requests: Dict[str, Callable] = {}

    @staticmethod
    def dispatch(name: str="", value: Any=""):
        if name in Events.subscribers:
            subscribed = Events.subscribers[name]
            for s in subscribed:
                s.receiveEvent(Event(name, value)) 

    @staticmethod
    def subscribe(obj: GameObject, *events: str):
        events = list(events)
        for e in events:
            if e in Events.subscribers:
                subscribed = Events.subscribers[e]
                return subscribed.append(obj)
            Events.subscribers[e] = [obj]

    @staticmethod
    def unsubscribe(obj: GameObject, *events: str):
        events = list(events)
        for e in events:
            if e in Events.subscribers:
                subscribed = Events.subscribers[e]
                Events.subscribers[e] = filter(lambda x: x != obj, subscribed)

    # Unsubscribes object from all events
    @staticmethod
    def disconnect(obj: GameObject):
        for e in Events.subscribers:
            subscribed = Events.subscribers[e]
            Events.subscribers[e] = filter(lambda x: x != obj, subscribed)

    @staticmethod
    def acceptRequest(req: str, func: Callable):
        Events.requests[req] = func
        
    # Während ein Event ausschließlich ausgehend ist, gibt eine Request einen Wert zurück und ist aktiv vom Caller ausgehend.
    @staticmethod
    def request(req: str, *args: Any) -> Any:
        if req in Events.requests:
            return Events.requests[req](*args)
        raise NotImplementedError(f"Request '{req}' is not accepted.")