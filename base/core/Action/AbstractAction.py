from base.core.Level.AbstractLevel import AbstractLevel
from base.objects.Actions.Routines.MiddlewareHandler import MiddlewareHandler
from base.core.Object.Factory import Factory

# Abstrakte Klasse zum State Management einer beliebiegen Aktion
# Dient zum Grundaufbau vieler Aktionen / Routinen
class AbstractAction():
    def __init__(self, obj, endState) -> None:
        self.id = -1
        self.progress = 0
        Factory.append(self)
        AbstractLevel.bind(self)
        # Ermöglich den Eingriff eine Aktion und seinen äußeren Komponente von diesen oder Dritten
        self.middlewareHandler = MiddlewareHandler(self)
        self.setStates(obj, endState)
    
    # Bindet standardmäßig Aktion an Level.
    # Ermöglicht das Löschen einer Aktion nach dem Beendigung des Levels, damit es zu keinen Event und Objekt Konflikten kommt.
    # Stoppt die Aktion und setzt die aktuellen States
    def setStates(self, obj, endState):
        self.stop()
        self.object = obj
        self.endState = endState
        self.middlewareHandler.dispatch("set")
        return self
    
    # Startet die Aktion
    def start(self):
        self.progress = 1
        self.middlewareHandler.dispatch("start")
        return self
    
    # Ist .isFinished() wahr, wird die Aktion gestoppt und "finished" Event ausgegeben
    # Sonst wird "run" Event ausgegeben.
    def run(self, event):
        print(self.isFinished())
        if self.isFinished():
            self.stop()
            self.progress = 2
            self.middlewareHandler.dispatch("finished")
            return
        self.middlewareHandler.dispatch("run")

    # Stoppt die Aktion
    def stop(self):
        self.progress = 0
        self.middlewareHandler.dispatch("stop")
        return self

    def isFinished(self) -> bool:
        raise NotImplementedError(f"'isFinished' Method on {self.__class__.__name__} not implemented.")
    