from typing import Dict
from base.core.Event.Events import Events

from copy import deepcopy

class Factory():
    objects: Dict[int, object] = {}
    alias: Dict[str, int] = {}

    def append(obj: object):
        objID = len(Factory.objects)
        obj.id = objID
        Factory.objects[objID] = obj
    
    def setAlias(obj: object, alias: str):
        if alias in Factory.alias:
            raise LookupError(f"Factory: Alias {id} already set.")
        Factory.alias[alias] = obj.id

    def get(id: int or str):
        if type(id) == int:
            if id not in Factory.objects:
                raise LookupError(f"Factory: ID '{id}' not found.")
            return Factory.objects[id]

        if id not in Factory.alias:
            raise LookupError(f"Factory: Alias '{id}' not found.")
        return Factory.objects[Factory.alias[id]]

    # FIXME
    def clone(obj: object, reconnect=False):
        cloned = deepcopy(obj)
        if reconnect:
            Events.subscribe(cloned, *Events.allSubscribedEvents(obj))
        Factory.append(cloned)
        return cloned