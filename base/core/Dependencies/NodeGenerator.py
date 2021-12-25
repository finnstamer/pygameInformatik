from math import ceil
from typing import List, Tuple

from pygame import Vector2
from base.core.Dependencies.Movement import Movement
from base.core.Game import Game
from base.object.GameObject import GameObject
from base.object.AI.Node import Node
from settings import screenRes

class NodeGenerator():

    def semiStaticNodes(obj: GameObject) -> Tuple[List[Node], List[List[int]]]:
        nodes: List[Node] = []
        modx = obj.width
        mody = obj.height
        sx = ceil(screenRes[0] / modx)
        sy = ceil(screenRes[1] / mody)
        skipped = []
        for x in range(sx):
            skipped.append([])
            for y in range(sy):
                skipped[x].append(skipped[x][y - 1] if y > 0 else 0)

                vec = Vector2(x * modx, y * mody)
                if not Movement.allowPosition(obj, vec):
                    nodes.append(Node(Vector2(-1, -1)))
                    skipped[x][y] += 1
                    continue
                
                n = Node(vec)
                if y > 0 and skipped[x][y - 1] == skipped[x][y - 2]:
                    higherNode = nodes[-1]
                    higherNode.down = n
                    n.higher = higherNode

                if x > 0:
                    leftNode = nodes[-sy]
                    leftNode.right = n
                    n.left = leftNode
                nodes.append(n)
        return (nodes, skipped)

    def nodeFiller(grid: List[Node], obj) -> List[Node]:
        for node  in grid:
            diffX = node.pos.x % obj.width
            diffY = node.pos.y % obj.height

            x = diffX > 0
            diff = diffX if x else diffY
            if x:
                up = Movement.furthestMove(obj, Vector2(node.pos.x, node.pos.y - diff), node.pos)
                up = Movement.furthestMove(obj, Vector2(node.pos.x, node.pos.y - diff + obj.height), node.pos)
                down = Movement
                pass
            else:
                pass
        return grid

    
    def new_generateDynamicNodes(obj: GameObject):
        solids = Game.level.allSolidObjects()
        semistatic = NodeGenerator.semiStaticNodes(obj)
        nodes = semistatic[0]
        skipped = semistatic[1]

        for solidObject in solids:
            for i, c in enumerate(solidObject.cRect.corners):
                if i < 2: # Top Corners
                    xMovement = Movement.firstMove(obj, Vector2(0, c.y), solids, c)
                    nX = Node(xMovement)
                    # nodes += NodeGenerator.nodeFiller(obj, nX, skipped, False, False)
                else: # Bottom Corners
                    xMovement = Movement.firstMove(obj, Vector2(screenRes[0], c.y), solids, c)
                    nX = Node(xMovement)
                    # nodes += NodeGenerator.nodeFiller(obj, nX, skipped, False, True)

                if i % 2 == 1: # Right Corners
                    yMovement = Movement.firstMove(obj, Vector2(c.x, screenRes[1]), solids, c)
                    nY = Node(yMovement)
                    # nodes += NodeGenerator.nodeFiller(obj, nY, skipped, True, True)
                else: # Left Corners
                    yMovement = Movement.firstMove(obj, Vector2(c.x, 0), solids, c)
                    nY = Node(yMovement)
                    # nodes += NodeGenerator.nodeFiller(obj, nY, skipped, True, False)
                
                if yMovement is not None:
                    nY.color = (235, 78, 16)
                    # nodes.append(nY)
                if xMovement is not None:
                    nX = Node(xMovement)
                    nX.color = (235, 78, 16)
                    # nodes.append(nX)
        nodes = NodeGenerator.nodeFiller(nodes, obj)
        return nodes