from base.core.Level.AbstractLevel import AbstractLevel
from base.objects.Backround import Backround


class Loading(AbstractLevel):
    def __init__(self) -> None:
        super().__init__(999)
    
    def make(self):
        bg = Backround("images/Dschungel.png")
        self.objects.append(bg)
