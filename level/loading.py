from base.core.Level.AbstractLevel import AbstractLevel
from base.objects.Background import Background


class Loading(AbstractLevel):
    def __init__(self) -> None:
        super().__init__(999)
    
    def make(self):
        bg = Background("images/Dschungel.png")
        self.objects.append(bg)
