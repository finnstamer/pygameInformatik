

from typing import Callable

# Klasse zur Erstellung von Eigenschaften an Objekten zur performanten Erkennung von Events, 
# die an ein Objekt verknüpft sind
class EventStorageHandler():
    prop = "sys_events"
    def store(obj, e: str, func: Callable):
        if not hasattr(obj, EventStorageHandler.prop):
            setattr(obj, EventStorageHandler.prop, [])
        oldEventProp = getattr(obj, EventStorageHandler.prop)
        oldEventProp.append(EventStorageHandler.toDict(obj, e, func))
        setattr(obj, EventStorageHandler.prop, oldEventProp)

    def retrieve(obj):
        if hasattr(obj, EventStorageHandler.prop):
            return list(getattr(obj, EventStorageHandler.prop))
        return []
    
    def toDict(obj, e, func):
        return {"event": e, "func": func, "obj": obj}
    
    def remove(obj, e: str, func: Callable):
        if hasattr(obj, EventStorageHandler.prop):
            oldEventProp = getattr(obj, EventStorageHandler.prop)
            oldEventProp.remove(EventStorageHandler.toDict(obj, e, func))
            setattr(obj, EventStorageHandler.prop, oldEventProp)
