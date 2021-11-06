from typing import Dict, List
from base.core.Event.Event import Event
from base.object.GameObject import GameObject


class EventDispatcher():
    subscribers: Dict[str, List[GameObject]] = {}

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
