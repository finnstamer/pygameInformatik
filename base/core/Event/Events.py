from typing import Any, Callable, Dict, List
from base.core.Event.Event import Event
from inspect import getargspec

class Events():
    # subscribers: Dict[str, List[object]] = {}
    subscribers: Dict[str, List[Callable]] = {}
    requests: Dict[str, Callable] = {}

    @staticmethod
    def dispatch(name: str="", value: Any=""):
        if name in Events.subscribers:
            subscribed = Events.subscribers[name]
            for s in subscribed:
                s(Event(name, value)) 
    
    @staticmethod
    def subscribe(event: str, func: Callable):
        if event not in Events.subscribers:
            Events.subscribers[event] = [func]
        if func not in Events.subscribers[event]:
            Events.subscribers[event].append(func)

    @staticmethod
    def unsubscribe(event, func: Callable):
        if event in Events.subscribers:
            subscribed = Events.subscribers[event]
            Events.subscribers[event] = list(filter(lambda x: x != func, subscribed))

    # Unsubscribes func from all subscribed Events
    @staticmethod
    def disconnect(func: Callable):
        for e in Events.subscribers:
            subscribed = Events.subscribers[e]
            Events.subscribers[e] = list(filter(lambda x: x != func, subscribed))

    def disconnectObject(obj: object):
        funcs = [getattr(obj, f) for f in dir(obj) if not f.startswith("__") and callable(getattr(obj, f))]
        print(funcs)
        for f in funcs:
            print(f)
            Events.disconnect(f)

    @staticmethod
    def acceptRequest(req: str, func: Callable):
        Events.requests[req] = func
        
    # Objekte die eine Request ausgeben, erwarten eine Antwort 
    @staticmethod
    def request(req: str, arg: Any) -> Any:
        if req in Events.requests:
            return Events.requests[req](arg)
        return arg
        # raise NotImplementedError(f"Request '{req}' is not accepted.")

    def allSubscribedEvents(func: Callable):
        events = []
        for e in Events.subscribers.items():
            if func in e[1]:
                events.append(e[0])                
        return events