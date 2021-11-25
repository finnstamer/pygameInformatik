import pygame
from typing import Dict, List
from base.core.Dependencies.DependencyException import DependencyException
from base.core.Event.Event import Event
from base.core.Game import Game
from base.object.GameObject import GameObject
from base.object.KI.Node import Node
from base.object.MovableObject import MovableObject
from settings import screenRes

class PathFinder():
    minActions = 5000
    walkedNodes = []
    
    # Optimiert nodes für ein bestimmtes GameObject. Damit werden die Anzahl an Nodes stark reduziert.
    # Merges all nodes which area is the given object to one node    
    @staticmethod
    def generateStaticNodes(obj: GameObject) -> List[Node]:
        nodes: List[Node] = []
        modx = obj.width
        mody = obj.height
        sx = int(screenRes[0] / modx)
        sy = int(screenRes[1] / mody)
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
    
    # TODO
    def generateDynamicNodes(obj: GameObject):
        if Game.level is None:
            raise DependencyException(PathFinder)
        
        nodes: List[Node] = []
        modx = obj.width
        mody = obj.height
        sx = int(screenRes[0] / modx)
        sy = int(screenRes[1] / mody)

        testObj = MovableObject()
        testObj.rect = obj.cRect.get(obj.pos, obj.cRect.lowerRight)
        testObj.speed = 1
        for x in range(sx):
            for y in range(sy):
                if y > 0:
                    vec = pygame.Vector2(x * modx, y * mody)
                    vec = testObj.furthestMove(vec, x=False)
                    n = Node(vec)
                    higherNode = nodes[-1]
                    higherNode.down = n
                    n.higher = higherNode
                    # if Game.level.allowMove(testObj, vec):
                    #     higherNode.down = n
                    #     n.higher = higherNode
                    # else:


                if x > 0:
                    leftNode = nodes[-sy]
                    leftNode.right = n
                    n.left = leftNode
                
                nodes.append(n)

                testRec = obj.cRect.get(vec, (vec.x + obj.width, vec.y + obj.height))
                testObj.rect = testRec
        return nodes

    @staticmethod
    def find(start: Node, dest: Node, depth: int=5) -> List[Node]:
        PathFinder.minActions = 750
        paths = PathFinder.findPaths(start, dest, depth=-1, maxDepth=depth, recPath=[start])

        # paths = PathFinder.nodesToIds(paths) # For testing
        sortedPath = sorted(paths, key=lambda obj: len(obj))

        print("------------------- ------------------ -------------------")
        print("------------------- PATH FINDER RESULT -------------------")
        print(f"------------------- root: {start.id} - dest: {dest.id} -------------------")
        print(sortedPath)
        print("------------------- ------------------ -------------------")
        return sortedPath


    def findPaths(node: Node, dest: Node, recPath=[], depth=0, maxDepth=5) -> List[List[Node]]:            
        paths: List[List[Node]] = []
        neighbors = PathFinder.bestNeighbors(node, dest)
        PathFinder.walkedNodes.append(node)
        depth += 1
        for i in range(len(neighbors)):
            n = neighbors[i]
            print(n)
            if n == None:
                continue
        
            path = recPath + [n]
            if depth > maxDepth or depth > PathFinder.minActions: #or n in PathFinder.walkedNodes:
                return paths

            if n == dest:
                PathFinder.minActions = 0
                paths.append(path)
                return paths

            rec = PathFinder.findPaths(n, dest, path, depth, maxDepth)
            if len(rec) > 0:
                paths += rec
        return paths
    
    def nodesToIds(nodeList):
        formatted = []
        for n in nodeList:
            if type(n) is list:
                formatted.append(PathFinder.nodesToIds(n))
            else:
                formatted.append(n.id)
        return formatted

    # Optimiert die Nachbarliste an Nodes einer root Node so, dass relativ zur Position, die nächsten Nodes in Richtung Ziel als als erstes in der Liste stehen.
    def bestNeighbors(node: Node, dest: Node) -> List[Node]:
        nList = node.neighborsToList()

        mapped = [
            [node.pos.y - dest.pos.y, nList[0]], 
            [dest.pos.x - node.pos.x, nList[1]],
            [dest.pos.y - node.pos.y, nList[2]],
            [node.pos.x - dest.pos.x, nList[3]]
        ]
        order = sorted(mapped, key=lambda y: y[0], reverse=True)
        return [v[1] for v in order]