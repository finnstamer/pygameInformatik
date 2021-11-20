from typing import Any, Dict, List

from pygame import Vector2


class Node():
    def __init__(self, pos: Vector2=Vector2(0, 0), higher=None, lower=None, left=None, right=None) -> None:
        self.pos = pos
        self.id = 0
        self.higher: Node = higher
        self.down: Node = lower
        self.left: Node = left
        self.right: Node = right
    
    def neighborsToList(self) -> List:
        nList = []
        if self.higher is not None:
            nList.append(self.higher)
        if self.right is not None:
            nList.append(self.right)
        if self.down is not None:
            nList.append(self.down)
        if self.left is not None:
            nList.append(self.left)
        return nList
