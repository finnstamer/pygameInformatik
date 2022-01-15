from typing import List
from base.core.Action.AbstractAction import AbstractAction
from base.core.Event.Events import Events
from base.core.Game import Game
from base.core.Level.AbstractLevel import AbstractLevel
from base.core.Object.Factory import Factory

# Abstrakte Klasse zur Verwaltung mehrerer Aktionen.
# Routine basiert selbst auf einer Aktion. 
# Dadurch wird die Verwaltung von Routinen durch Routinen und damit komplexe Handlungen möglich 
class AbstractRoutine(AbstractAction):
    def __init__(self, obj, endState) -> None:
        super().__init__(obj, endState)
        self.actions: List[AbstractAction] = []
        self.pendingAction = None

        # Aktionen werden nach Beendigugn automatisch entfernt
        self.autoDelete = True

        self.middlewareHandler.on("set", self.createActions)
        self.middlewareHandler.on("run", self.runActions)
        self.middlewareHandler.on("stop", self.stopActions)
    
    # Abstrakte Methode zur Erstellung von Aktionen auf Basis der States
    def createActions(self):
        raise NotImplementedError(f"'createActions' Method on {self.__class__.__name__} not implemented.")
    
    # Ruft nächste Aktion auf, wenn keine gesetzt ist.
    # Ist die Aktion sonst fertig, wird die Aktion auf None gesetzt. 
    def runActions(self):
        if self.pendingAction is None:
            if len(self.actions) == 0:
                return
            self.pendingAction = self.actions[0]
            self.middlewareHandler.dispatch("pendingAction.set", self.pendingAction)
            return self.pendingAction.start()

        if self.pendingAction.progress == 2:
            self.middlewareHandler.dispatch("pendingAction.done", self.pendingAction)
                
            self.actions.pop(0)
            if self.autoDelete:
                Game.level().delete(self.pendingAction)
            self.pendingAction = None

    # Routine ist i.d.R dann fertig, wenn alle darunterliegenden Aktionen beendet sind.
    def isFinished(self):
        return len(self.actions) == 0

    def setActions(self, actions: List[AbstractAction]):
        self.actions = actions
        self.pendingAction = None
    
    # Stoppt alle gesetzten Aktionen
    def stopActions(self):
        for a in self.actions:
            a.stop()
