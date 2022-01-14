from base.core.Event.Events import Events
from base.core.Level.Level import Level
from base.core.Object.Factory import Factory

# Abstrakte Klasse zur Erstellung von Level, deren Aufbau durch die .make Methode gespeichert wird
# und somit einen erneuten Aufbau des Levels ermöglicht.
class AbstractLevel(Level):

    # Level gebundene Objekte sind Instanzen, die nicht per .draw Methode gezeichent werden, sondern im Hintergrund agieren
    # und an das Level gebunden sind.
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
        if obj in AbstractLevel.bound:
            AbstractLevel.bound.remove(obj)            
    
    def delete(self, obj):
        Factory.delete(obj)
        if obj in self.objects:
            self.objects.remove(obj)
            return
        if obj in AbstractLevel.bound:
            AbstractLevel.bound.remove(obj)

    # Entfernt alle Objekte aus dem Level
    def deleteAll(self):
        objects = self.objects + AbstractLevel.bound

        for o in objects:
            Factory.delete(o)                

        self.objects = []
        AbstractLevel.bound = []

    # Entfernt alle Objekte aus dem Level und lädt es neu
    def reset(self):
        self.deleteAll()
        self.load()
