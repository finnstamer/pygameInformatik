from typing import Any, Dict, List

from pygame import Vector2


class Node():
    def __init__(self, pos: Vector2=Vector2(0, 0), higher=None, lower=None, left=None, right=None) -> None:
        self.pos = pos
        self.id = id
        self.higher = higher
        self.lower = lower
        self.left = left
        self.right= right