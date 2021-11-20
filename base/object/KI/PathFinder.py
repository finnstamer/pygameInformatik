from typing import Dict, List, Tuple
import pygame
from pygame.constants import MULTIGESTURE

from base.core.Game import Game
from base.object.GameObject import GameObject
from base.object.KI.Node import Node

class PathFinder():

    minSteps = 5000
    walkedNodes = []
    @staticmethod
    def createNodes(screen: Tuple[int, int], idStart=0, mod=1) -> List[Node]:
        nodes: List[Node] = []
        sx = int(screen[0] / mod)
        sy = int(screen[1] / mod)
        for x in range(sx):
            for y in range(sy):
                vec = pygame.Vector2(x * mod, y * mod)
                nodes.append(Node(idStart, vec, ))
                idStart += 1

        for i in range(len(nodes)):
            node = nodes[i]
            node.neighbors = [
                nodes[i+1] if i < (sx * sy - 1) else None, 
                nodes[i-1] if i > 0 else None, 
                nodes[i + sy] if i < (sx * sy - sy) else None, 
                nodes[i - sy] if i > sy else None
            ] # Down Up Right Left
        return nodes
    
    # Optimiert nodes für ein bestimmtes GameObject. Damit werden die Anzahl an Nodes stark reduziert.
    # Merges all nodes which area is the given object to one node
    @staticmethod
    def optimizeNodes(obj: GameObject, screen: Tuple[int, int]) -> List[Node]:
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

        # for i in range(len(nodes)):
        #     node = nodes[i]
        #     node.neighbors = [
        #         nodes[i+1] if i < (sx * sy - 1) else None, 
        #         nodes[i-1] if i > 0 else None, 
        #         nodes[i + sy] if i < (sx * sy - sy) else None, 
        #         nodes[i - sy] if i > sy else None
        #     ] # Down Up Right Left
        return nodes

    @staticmethod
    def find(start: Node, dest: Node) -> List[Node]:
        PathFinder.minSteps = 750
        paths = PathFinder.walkPath(start, dest, [], 0, 10, super=True)

        formatted = PathFinder.formatId(paths)
        simplePath = PathFinder.breakDown(formatted)


        print("-------------------")
        print(formatted)
        print("-------------------")
        print(simplePath)
        pList = []
        # for p in simplePath:
        #     [pList.append(n.id) for n in p]
        # return pList

    def walkPath(node: Node, dest: Node, recPath=[], steps=0, depth=5, super=False) -> Dict[int, List[Node]]:            
        paths: List[List[Node]] = []
        neighbors = node.neighborsToList()
        PathFinder.walkedNodes.append(node)
        for i in range(len(neighbors)):
            n = neighbors[i]
            path = recPath + [n]
            if steps > depth: #or n in PathFinder.walkedNodes:
                return paths
            steps += 1

            if n == dest:
                print("FOUND")
                paths.append(path)
                return paths

            walked = PathFinder.walkPath(n, dest, path, steps, depth)
            if len(walked) > 0:
                paths.append(walked)
        return paths
    
    def formatId(nodeList):
        formatted = []
        for n in nodeList:
            if type(n) is list:
                formatted.append(PathFinder.formatId(n))
            else:
                formatted.append(n.id)
        return formatted

    def breakDown(nodeList, path=[]) -> List[List[Node]]:
        # [
        #   [0, 14, [25, 2], [25, 3, 5]], 
        # ] 
        # 
        # => [
        #       [0, 14, 25, 2],
        #       [0, 14, 25, 3, 5]
        # ]
        paths: List[List[Node]] = []
        #[14, [28, [29]]
        for i in nodeList:
            allLists = list(filter(lambda x: type(x) is list, i))
            if len(allLists) == 0:
                paths.append(i)
            else:
                paths += (PathFinder.breakDown(i))
        return paths
        # final = []
        # for f in paths:
        #     final.append(path + [f])
        # return final

        # final = []
        # for l in listPath:
        #     final.append(paths + PathFinder.breakDown(l))
        # return final