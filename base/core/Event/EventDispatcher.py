from typing import Any, Callable, Dict, List
from base.core.Event.Event import Event
from base.core.Game import Game
from base.object.GameObject import GameObject

class EventDispatcher():
    subscribers: Dict[str, List[GameObject]] = {}
    requests: Dict[str, Callable] = {}

    @staticmethod
    def dispatch(event: Event):
        if event.name in EventDispatcher.subscribers:
            subscribed = EventDispatcher.subscribers[event.name]
            for s in subscribed:
                if s.active:
                    s.receiveEvent(event) 

    @staticmethod
    def subscribe(obj: GameObject, *events: str):
        events = list(events)
        for e in events:
            if e in EventDispatcher.subscribers:
                subscribed = EventDispatcher.subscribers[e]
                return subscribed.append(obj)
            EventDispatcher.subscribers[e] = [obj]

    @staticmethod
    def unsubscribe(obj: GameObject, *events: str):
        events = list(events)
        for e in events:
            if e in EventDispatcher.subscribers:
                subscribed = EventDispatcher.subscribers[e]
                EventDispatcher.subscribers[e] = filter(lambda x: x != obj, subscribed)

    # Unsubscribes object from all events
    @staticmethod
    def disconnect(obj: GameObject):
        for e in EventDispatcher.subscribers:
            subscribed = EventDispatcher.subscribers[e]
            EventDispatcher.subscribers[e] = filter(lambda x: x != obj, subscribed)


    @staticmethod
    def acceptRequest(req: str, compute: Callable):
        EventDispatcher.requests[req] = compute
        
    # Während ein Event ausschließlich ausgehend ist, gibt eine Request einen Wert zurück und ist aktiv vom Caller ausgehend.
    @staticmethod
    def request(req: str, *args: Any) -> Any:
        if req in EventDispatcher.requests:
            return EventDispatcher.requests[req](*args)
        raise NotImplementedError(f"Request '{req}' is not accepted.")
