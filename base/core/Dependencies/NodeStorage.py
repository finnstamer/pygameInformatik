from typing import Dict, List
from base.core.Dependencies.NodeGenerator import NodeGenerator
from base.object.GameObject import GameObject

from base.object.KI.Node import Node

class NodeStorage():
    grids: Dict[int, List[Node]] = {}

    def add(obj: GameObject, grid: List[Node]):
        NodeStorage.grids[obj.id] = grid
    
    def reloadGrid(obj: GameObject) -> List[Node]:
        NodeStorage.removeGrid(obj)
        return NodeStorage.findGrid(obj)

    def findGrid(obj: GameObject) -> List[Node]:
        if obj.id in NodeStorage.grids:
            return NodeStorage.grids[obj.id]
        # return PathFinder.generateDynamicNodes(obj)
        return NodeGenerator.new_generateDynamicNodes(obj)
    
    def removeGrid(obj: GameObject):
        if obj.id in NodeStorage.grids:
            del NodeStorage.grids[obj.id]