from typing import List, Tuple
import pygame

from base.core.Game import Game
from base.object.GameObject import GameObject
from base.object.KI.Node import Node

class PathFinder():

    @staticmethod
    def find(a: pygame.Vector2, b: pygame.Vector2):
        nodes: List[Node] = []
        solids = Game.level.allSolidObjects()
        
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

