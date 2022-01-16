

from typing import Callable
from urllib import request

# Klasse zur Erstellung von Eigenschaften an Objekten zur performanten Erkennung von Events, 
# die an ein Objekt verknüpft sind
class EventRegister():
    prop = "sys_events"
    def register(obj, e: str, func: Callable, request=False):
        if not hasattr(obj, EventRegister.prop):
            setattr(obj, EventRegister.prop, [])
        oldEventProp = getattr(obj, EventRegister.prop)
        oldEventProp.append(EventRegister.toDict(obj, e, func, request))
        setattr(obj, EventRegister.prop, oldEventProp)

    def retrieve(obj):
        if hasattr(obj, EventRegister.prop):
            return list(getattr(obj, EventRegister.prop))
        return []
    
    def toDict(obj, e, func, request):
        return {"event": e, "func": func, "obj": obj, "request": request}
    
    def remove(obj, e: str, func: Callable, request=False):
        if hasattr(obj, EventRegister.prop):
            oldEventProp = getattr(obj, EventRegister.prop)
            oldEventProp.remove(EventRegister.toDict(obj, e, func, request))
            setattr(obj, EventRegister.prop, oldEventProp)
