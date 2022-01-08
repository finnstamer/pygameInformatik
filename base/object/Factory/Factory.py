from typing import Dict
from base.core.Event.Events import Events

from copy import deepcopy
from inspect import isclass

class Factory():
    objects: Dict[int, object] = {}
    alias: Dict[str, int] = {}
    lastid = 0

    def append(obj: object):
        Factory.lastid += 1
        obj.id = Factory.lastid
        Factory.objects[Factory.lastid] = obj
    
    def setAlias(obj: object, alias: str):
        # if alias in Factory.alias:
            # raise LookupError(f"Factory: Alias {id} already set.")
        Factory.alias[alias] = obj.id
    
    def get(id: int or str):
        if type(id) == int:
            if id not in Factory.objects:
                raise LookupError(f"Factory: ID '{id}' not found.")
            return Factory.objects[id]

        if id not in Factory.alias:
            raise LookupError(f"Factory: Alias '{id}' not found.")
        return Factory.objects[Factory.alias[id]]

    # No Event Subscription Cloning possible due to function only attachment
    def clone(obj: object):
        cloned = deepcopy(obj)
        Factory.append(cloned)
        return cloned

    def removeAlias(obj: object):
        vals = list(Factory.alias.values())
        if obj.id in vals:
            keys = list(Factory.alias.keys())
            alias = keys[list(Factory.alias.values()).index(obj.id)]
            del Factory.alias[alias]
    
    def removeId(obj: object):
        del Factory.objects[obj.id]

    def delete(obj: object):
        # Dependencies can subscribe Events and have no id
        if obj.id is not None:
            Factory.removeAlias(obj)
            Factory.removeId(obj)
        Events.disconnectObject(obj)
        
        subClasses = [getattr(obj, p) for p in dir(obj) if isclass(p) and not p.__name__.startswith("__")]
        for c in subClasses:
            Factory.delete(c)
        del obj