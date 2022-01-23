from hashlib import algorithms_available
import inspect
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

    def isRegistered(id: int or str):
        if type(id) == int:
            if id in Factory.objects:
                return True
        if id in Factory.alias:
            return True
        return False
        
    # Klont ein Objekt und fügt es der Factory an.
    # Zu beachten ist, dass Event Abonnements nicht kopiert werden
    def clone(obj: object):
        cloned = deepcopy(obj)
        Factory.append(cloned)
        return cloned

    # Entfernt Alias zur ID eines gegeben Objektes
    def removeAlias(obj: object):
        for alias, id in list(Factory.alias.items()):
            if id == obj.id:
                del Factory.alias[alias]

    # Entfernt die ID eines Objektes
    def removeId(obj: object):
        del Factory.objects[obj.id]

    # Isoliert und entfernt ein Objekt vollständig 
    def delete(obj: object):
        if hasattr(obj, "id"):
            Factory.removeAlias(obj)
            Factory.removeId(obj)
        Events.dispatch(f"factory.unbind.{id(obj)}", obj)
        Events.unsubscribeMethodsOnObject(obj)