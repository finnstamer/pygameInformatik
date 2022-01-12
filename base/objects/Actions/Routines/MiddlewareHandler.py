from typing import Any, Callable
from base.core.Event.Event import Event
from base.core.Event.Events import Events

# Klasse zum Verwalten Aktion-bedingter Events, was äußeren Eingriff in komplexe Handlungen via einem spezifizierten Events (Events.py) basiertem System ermöglicht
# ! Ist nur auf ~Aktionen ausgelegt. !
class MiddlewareHandler():
    def __init__(self, action) -> None:
        self.action = action
        self.middlewares = {}
    
    # Shorthand zum Ausgeben eines Events, das an die Aktion gebunden ist
    def dispatch(self, event: str, value: Any = ""):
        Events.dispatch(f"Action.{self.action.id}.{event}", (self.action, value))
    
    # Abonniert eine Funktion an ein Event
    # Das Event wird intern an .receiveEvent() abonniert 
    # und darüber an die Middlewares in der Reihenfolge der Liste weitergegeben
    def on(self, event: str, func: Callable, forcePos=-1):
        if event not in self.middlewares:
            self.middlewares[event] = []
            Events.subscribe(f"Action.{self.action.id}.{event}", self.receiveEvent)
        
        if forcePos != -1:
            self.middlewares[event][forcePos:forcePos] = [func]
            return
        self.middlewares[event].append(func)
    
    # Gibt abonniertes Event an Middlewares weiter
    def receiveEvent(self, event: Event):
        eventName = ".".join(event.name.split(".")[2:])
        if self.middlewares[eventName] is not None: 
            for middleware in self.middlewares[eventName]:
                middleware()

    # Erstellt einen Verbindungspunkt zu einer dritten Funktion
    # Intern wird Events.request() aufgerufen und der Rückgabewert der verbundenen Funktion zurückgegeben.  
    def openConnection(self, name="", value=""):
        return Events.request(f"Action.{self.action.id}.{name}", value)
    
    # Verbindet eine Funktion an ein Event
    def connect(self, name, func: Callable):
        Events.acceptRequest(f"Action.{self.action.id}.{name}", func)
