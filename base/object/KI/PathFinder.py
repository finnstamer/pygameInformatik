from typing import Dict, List, Tuple
import pygame
from pygame.constants import MULTIGESTURE

from base.core.Game import Game
from base.object.GameObject import GameObject
from base.object.KI.Node import Node

class PathFinder():

    minActions = 5000
    walkedNodes = []
    
    # Optimiert nodes für ein bestimmtes GameObject. Damit werden die Anzahl an Nodes stark reduziert.
    # Merges all nodes which area is the given object to one node
    @staticmethod
    def generateNodes(obj: GameObject, screen: Tuple[int, int]) -> List[Node]:
        nodes: List[Node] = []
        modx = obj.width
        mody = obj.height
        sx = int(screen[0] / modx)
        sy = int(screen[1] / mody)
        for x in range(sx):
            for y in range(sy):
                vec = pygame.Vector2(x * modx, y * mody)
                n = Node(vec)
                
                if y > 0:
                    higherNode = nodes[-1]
                    higherNode.down = n
                    n.higher = higherNode

                if x > 0:
                    leftNode = nodes[-sy]
                    leftNode.right = n
                    n.left = leftNode
                nodes.append(n)
        return nodes

    @staticmethod
    def find(start: Node, dest: Node) -> List[Node]:
        PathFinder.minActions = 750
        paths = PathFinder.findPath(start, dest, maxDepth=5)

        formatted = PathFinder.formatId(paths)
        simplified = PathFinder.simplifyNodePath(formatted)
        sortedPath = sorted(simplified, key=lambda obj: len(obj))

        print("-------------------")
        print(formatted)
        print("-------------------")
        print(sortedPath)


    def findPath(node: Node, dest: Node, recPath=[], depth=0, maxDepth=5, super=False) -> Dict[int, List[Node]]:            
        paths: List[List[Node]] = []
        neighbors = node.neighborsToList()
        PathFinder.walkedNodes.append(node)
        depth += 1
        for i in range(len(neighbors)):
            n = neighbors[i]
            path = recPath + [n]
            if depth > maxDepth or depth > PathFinder.minActions: #or n in PathFinder.walkedNodes:
                return paths

            if n == dest:
                PathFinder.minActions = depth
                paths.append(path)
                return paths

            rec = PathFinder.findPath(n, dest, path, depth, maxDepth)
            if len(rec) > 0:
                paths.append(rec)
        return paths
    
    def formatId(nodeList):
        formatted = []
        for n in nodeList:
            if type(n) is list:
                formatted.append(PathFinder.formatId(n))
            else:
                formatted.append(n.id)
        return formatted

    def simplifyNodePath(nodeList, path=[]) -> List[List[Node]]:
        paths: List[List[Node]] = []
        for i in nodeList:
            allLists = list(filter(lambda x: type(x) is list, i))
            if len(allLists) == 0:
                paths.append(i)
            else:
                paths += (PathFinder.simplifyNodePath(i))
        return paths