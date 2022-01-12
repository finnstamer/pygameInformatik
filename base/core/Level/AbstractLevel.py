from base.core.Event.Events import Events
from base.core.Level.Level import Level
from base.core.Object.Factory import Factory

# Abstrakte Klasse zur Erstellung von Level, deren Aufbau durch die .make Methode gespeichert wird
# und somit einen erneuten Aufbau des Levels ermöglicht.
class AbstractLevel(Level):
    bound = []
    def __init__(self, id: int) -> None:
        super().__init__(id)
    
    # Aufbau des Leves und Zuweisung aller Objekte zu .objects benötigt
    def make(self):
        raise NotImplementedError("Make Function is required in AbstractLevel")
    
    def load(self):
        self.make()
        Events.dispatch(f"Level.loaded", self)
    
    # Bindet ein Nicht-GameObject an das aktive Level. Und wird regulär wie .objects beim Levelwechsel/-restart entfernt 
    def bind(*objs):
        AbstractLevel.bound += (list(objs))

    def unbind(obj):
        AbstractLevel.bound.remove(obj)
    
    # Entfernt alle Objekte aus dem Level
    def delete(self):
        objects = self.objects + AbstractLevel.bound
        uniqueObjects = list(set(objects))

        for o in uniqueObjects:
            Factory.delete(o)                

        self.objects = []
        AbstractLevel.bound = []

    # Entfernt alle Objekte aus dem Level und lädt es neu
    def reset(self):
        self.delete()
        self.load()
