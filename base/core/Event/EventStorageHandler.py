

from typing import Callable
from urllib import request

# Klasse zur Erstellung von Eigenschaften an Objekten zur performanten Erkennung von Events, 
# die an ein Objekt verknüpft sind
class EventStorageHandler():
    prop = "sys_events"
    def store(obj, e: str, func: Callable, request=False):
        if not hasattr(obj, EventStorageHandler.prop):
            setattr(obj, EventStorageHandler.prop, [])
        oldEventProp = getattr(obj, EventStorageHandler.prop)
        oldEventProp.append(EventStorageHandler.toDict(obj, e, func, request))
        setattr(obj, EventStorageHandler.prop, oldEventProp)

    def retrieve(obj):
        if hasattr(obj, EventStorageHandler.prop):
            return list(getattr(obj, EventStorageHandler.prop))
        return []
    
    def toDict(obj, e, func, request):
        return {"event": e, "func": func, "obj": obj, "request": request}
    
    def remove(obj, e: str, func: Callable, request=False):
        if hasattr(obj, EventStorageHandler.prop):
            oldEventProp = getattr(obj, EventStorageHandler.prop)
            oldEventProp.remove(EventStorageHandler.toDict(obj, e, func, request))
            setattr(obj, EventStorageHandler.prop, oldEventProp)
