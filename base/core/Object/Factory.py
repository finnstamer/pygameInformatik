from typing import Dict
from base.core.Event.Events import Events

from copy import deepcopy
from inspect import isclass

# Klasse zur Indizierung von Objekten zu IDs
class Factory():
    objects: Dict[int, object] = {}
    alias: Dict[str, int] = {}
    lastid = 0

    # Fügt Objekt zur Factory hinzu. ID wird automatisch gesetzt
    def append(obj: object):
        Factory.lastid += 1
        obj.id = Factory.lastid
        Factory.objects[Factory.lastid] = obj
    
    # Ermöglicht die Erstellung eines Alias zur Ids eines gegebenen Objekt
    def setAlias(obj: object, alias: str):
        if alias in Factory.alias:
            raise LookupError(f"Factory: Alias {id} already set.")
        Factory.alias[alias] = obj.id
    
    # Gibt Objekt mit gegebener ID oder Alias zurück
    # LookupError wenn nicht gefunden
    def get(id: int or str):
        if type(id) == int:
            if id not in Factory.objects:
                raise LookupError(f"Factory: ID '{id}' not found.")
            return Factory.objects[id]

        if id not in Factory.alias:
            raise LookupError(f"Factory: Alias '{id}' not found.")
        return Factory.objects[Factory.alias[id]]

    # Klont ein Objekt und fügt es der Factory an.
    # Zu beachten ist, dass Event Abonnements nicht kopiert werden
    def clone(obj: object):
        cloned = deepcopy(obj)
        Factory.append(cloned)
        return cloned

    # Entfernt Alias zur ID eines gegeben Objektes
    def removeAlias(obj: object):
        vals = list(Factory.alias.values())
        if obj.id in vals:
            keys = list(Factory.alias.keys())
            alias = keys[list(Factory.alias.values()).index(obj.id)]
            del Factory.alias[alias]
    
    # Entfernt die ID eines Objektes
    def removeId(obj: object):
        del Factory.objects[obj.id]

    # Isoliert und entfernt ein Objekt vollständig 
    def delete(obj: object):
        if obj.id is not None:
            Factory.removeAlias(obj)
            Factory.removeId(obj)
        Events.disconnectObject(obj)
        
        subClasses = [getattr(obj, p) for p in dir(obj) if isclass(p) and not p.__name__.startswith("__")]
        for c in subClasses:
            Factory.delete(c)
