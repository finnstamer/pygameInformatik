from typing import Any, Dict, List

from pygame import Vector2
from base.core.Level.AbstractLevel import AbstractLevel

from base.core.Object.Factory import Factory


class Node():
    def __init__(self, pos: Vector2=Vector2(0, 0), higher=None, lower=None, left=None, right=None) -> None:
        self.pos = pos
        self.id = -1
        self.higher: Node = higher
        self.down: Node = lower
        self.left: Node = left
        self.right: Node = right
        self.color = None
        Factory.append(self)
        AbstractLevel.bind(self)
    
    def neighborsToList(self) -> Dict[int, object]:
        return {0: self.higher, 1: self.right, 2: self.down, 3: self.left}
