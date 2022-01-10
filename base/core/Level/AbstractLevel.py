from base.core.Level.Level import Level
from base.core.Object.Factory import Factory

# Abstrakte Klasse zur Erstellung von Level, deren Aufbau durch die .make Methode gespeichert wird
# und somit einen erneuten Aufbau des Levels ermöglicht.
class AbstractLevel(Level):
    def __init__(self, id: int) -> None:
        super().__init__(id)
    
    # Aufbau des Leves und Zuweisung aller Objekte zu .objects benötigt
    def make(self):
        raise NotImplementedError("Make Function is required in AbstractLevel")
    
    # Entfernt alle Objekte aus dem Level
    def delete(self):
        for o in self.objects:
            Factory.delete(o)
        self.remove(*self.objects)

    # Entfernt alle Objekte aus dem Level und lädt es neu
    def reset(self):
        self.delete()
        self.make()
