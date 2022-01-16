import pygame
from typing import List

from math import ceil as ceil
from base.core.Dependencies.DependencyException import DependencyException
from base.core.Dependencies.Movement import Movement
from base.core.Game import Game
from base.core.Object.GameObject import GameObject
from base.nodes.Node import Node
from settings import screenRes

# Klasse zur algorithmischen Wegfindung
class PathFinder():
    minActions = 5000
    walkedNodes = []
    
    @staticmethod
    def find(start: Node, dest: Node, depth: int=5) -> List[List[Node]]:
        if start == dest:
            return []
        
        PathFinder.minActions = 750
        paths = PathFinder.findPaths(start, dest, depth=-1, maxDepth=depth, recPath=[start])
        sortedPaths = sorted(paths, key=lambda obj: len(obj))

        return sortedPaths

    def findPaths(node: Node, dest: Node, recPath=[], depth=0, maxDepth=5) -> List[List[Node]]:            
        paths: List[List[Node]] = []
        neighbors = PathFinder.bestNeighbors(node, dest)
        PathFinder.walkedNodes.append(node)
        depth += 1
        for i in range(len(neighbors)):
            n = neighbors[i]
            if n == None or n in recPath: # Verhindere doppelte Suche
                continue
        
            path = recPath + [n]
            if depth > maxDepth:
                PathFinder.minActions = 0

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
    
    def nearestNode(nodes: List[Node], pos: pygame.Vector2) -> Node:
        mapped = map(lambda x: (x.pos.distance_to(pos), x), nodes)
        return sorted(mapped, key=lambda x:x[0])[0][1]
