from typing import Dict
from base.object.KI.Routine import Routine
from base.object.MovableObject import MovableObject


class KIObject(MovableObject):
    
    def  __init__(self) -> None:
        super().__init__()
        self.routines: Dict[int, Routine] = {}
        self.routine = None
        