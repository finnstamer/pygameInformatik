from gc import callbacks
import inspect
import optparse
from typing import Any, Callable, Dict, List
from base.core.Event.Event import Event
from base.core.Event.EventRegister import EventRegister

# Klasse zur ausgeben und abonnieren von Events, sowie zur Errichtung von Requests
class Events():
    subscribers: Dict[str, List[Callable]] = {}
    requests: Dict[str, Callable] = {}

    # Gibt ein Event an alle abonnierten Funktionen
    def dispatch(name: str="", value: Any=""):
        if name in Events.subscribers:
            subscribed = Events.subscribers[name]
            for s in subscribed:
                s(Event(name, value)) 
    
    # Abonniert ein Event an eine Funktion
    def subscribe(event: str, func: Callable, obj = None):
        if event not in Events.subscribers:
            Events.subscribers[event] = [func]
        if func not in Events.subscribers[event]:
            Events.subscribers[event].append(func)
        if obj is not None:
            EventRegister.register(obj, event, func)

    # Deabonniert ein bestimmtes Event von einer Funktion
    def unsubscribe(event, func: Callable, obj=None):
        if event in Events.subscribers.keys() and func in Events.subscribers[event]:
            Events.subscribers[event].remove(func)
            EventRegister.remove(obj, event, func)

    # Deabonniert alle Events von einer Funktion
    def unsubscribeAll(func: Callable):
        for event in Events.subscribers:
            Events.unsubscribe(event, func)

    # Deabonniert alle Events von allen Funktionen eines Objektes
    def unsubscribeMethodsOnObject(obj: object):
        events = EventRegister.retrieve(obj)
        for i in range(len(events)):
            e = events[i]
            event, func, isRequest = (e["event"], e["func"], e["request"])
            if isRequest:
                Events.rejectRequest(event, func, obj)
                continue
            Events.unsubscribe(event, func, obj)
            
    # Eröffnet die Verbindungsstelle einer bestimmten Request an eine Funktion
    # Nur eine Funktion ist an eine Request gebunden. Wird hiermit ggf. überschrieben. 
    def acceptRequest(req: str, func: Callable, obj=None):
        Events.requests[req] = func
        EventRegister.register(obj, req, func, True)
    
    def rejectRequest(req: str, func: callbacks, obj=None):
        if req in Events.requests:
            del Events.request[req]
            EventRegister.remove(obj, req, func, True)
        
    # Gibt argumente an mit dieser Request verbundene Funktion weiter und gibt diese zurück.
    # Ist keine Funktion angegeben, werden die Argumente wieder zurückgegeben.
    def request(req: str, arg: Any) -> Any:
        if req in Events.requests:
            return Events.requests[req](arg)
        return arg

    # Gibt alle Events zurück, die eine bestimmte Funktion abonniert hat.
    def allSubscribedEvents(func: Callable):
        events = []
        for e in Events.subscribers.items():
            if func in e[1]:
                events.append(e[0])                
        return events