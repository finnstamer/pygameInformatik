from pickle import dump, load
from typing import Dict, List

from pygame import Vector2

from base.core.Dependencies.NodeGenerator import NodeGenerator
from base.core.Object.GameObject import GameObject
from base.nodes.Node import Node

# Klasse zur Speicherung und Wiedervewendung von Nodegittern.
class NodeStorage():
    grids: Dict[int, List[Vector2]] = {}

    def add(obj: GameObject, grid: List[Node]):
        NodeStorage.grids[NodeStorage.toDimension(obj)] = grid
    
    def reloadGrid(obj: GameObject) -> List[Node]:
        NodeStorage.removeGrid(obj)
        return NodeStorage.findGrid(obj)

    def toDimension(obj):
        return f"{obj.width}:{obj.height}"

    def findGrid(obj: GameObject) -> List[Node]:
        d = NodeStorage.toDimension(obj)
        keys = list(NodeStorage.grids.keys())
        if d in keys:
            found = NodeStorage.grids[d]
            return found
        grid, skipped = NodeGenerator.semiStaticNodes(obj)
        NodeStorage.add(obj, grid)
        return grid
    
    def removeGrid(obj: GameObject):
        if NodeStorage.toDimension(obj) in NodeStorage.grids:
            del NodeStorage.grids[NodeStorage.toDimension(obj)]