from typing import List

from pygame import Vector2
from base.core.Game import Game
from base.core.Object.GameObject import GameObject
from base.nodes.Node import Node



class NodeVisualizer():
    def __init__(self, nodes: List[Node], color=(250, 0, 250)) -> None:
        self.nodes = nodes
        self.objects = []
        self.nodeObjects = []
        self.color = color

    def setNodes(self, nodes: List[Node]):
        self.nodes = nodes
        return self

    def start(self):
        Game.level().remove(*self.nodeObjects)
        self.nodeObjects = list(map(lambda x: self.toObject(x), self.nodes))
        Game.level().add(*self.nodeObjects)        

    def toObject(self, node: Node) -> GameObject:
        if node is None or node.pos == Vector2(-1, -1):
            return GameObject()
        return GameObject(node.pos, width=5, height=5, color=self.color if node.color is None else node.color)
    
