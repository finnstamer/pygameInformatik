from base.core.Level.Level import Level
from base.object.Factory.Factory import Factory


class AbstractLevel(Level):
    def __init__(self, id: int) -> None:
        super().__init__(id)
    
    def make(self):
        raise NotImplementedError("Make Function is required in AbstractLevel")
    
    def reset(self):
        for o in self.objects:
            Factory.delete(o)
        self.remove(*self.objects)
        self.make()
