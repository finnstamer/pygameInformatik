from typing import List
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.core.Game import Game
from base.object.GameObject import GameObject
from base.object.Group import Group

from base.object.KI.Node import Node


class NodeVisualizer():
    def __init__(self, nodes: List[Node], color=(250, 0, 250)) -> None:
        self.nodes = nodes
        self.objects = []
        self.group = Group("nodes")
        self.color = color

    def setNodes(self, nodes: List[Node]):
        self.nodes = nodes
        return self

    def start(self):
        objs = list(map(lambda x: self.toObject(x), self.nodes))
        self.group.clear(objs)
        if Game.level is not None:  
            Game.level.addGroup(self.group)        

    def toObject(self, node: Node) -> GameObject:
        return GameObject(node.pos, width=5, height=5, color=self.color)
    
