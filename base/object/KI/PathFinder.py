import pygame
from typing import List

from math import ceil as ceil
from base.core.Dependencies.DependencyException import DependencyException
from base.core.Dependencies.Movement import Movement
from base.core.Game import Game
from base.object.GameObject import GameObject
from base.object.KI.Node import Node
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
        sx = ceil(screenRes[0] / modx)
        sy = ceil(screenRes[1] / mody)
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


    def semiStaticNodes(obj: GameObject, solids: List[GameObject]):
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

                vec = pygame.Vector2(x * modx, y * mody)
                if not Movement.allowPosition(obj, vec, solids):
                    nodes.append(Node(pygame.Vector2(-1, -1)))
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
        print(skipped)
        return nodes
    
    def new_generateDynamicNodes(obj: GameObject):
        solids = Game.level.allSolidObjects()
        nodes = PathFinder.semiStaticNodes(obj, solids)

        for obj in solids:
            for i, c in enumerate(obj.cRect.corners):
                if i < 2: # Top Corners
                    xMovement = Movement.firstMove(obj, pygame.Vector2(0, c.y), solids, c)
                else: # Bottom Corners
                    xMovement = Movement.firstMove(obj, pygame.Vector2(screenRes[0], c.y), solids, c)
                if i % 2 == 1: # Right Corners
                    yMovement = Movement.firstMove(obj, pygame.Vector2(c.x, 0), solids, c)
                else: # Left Corners
                    yMovement = Movement.firstMove(obj, pygame.Vector2(c.x, screenRes[1]), solids, c)
                
                nX = Node(xMovement)
                nY = Node(yMovement)
                # nodes.append(nX)
                # nodes.append(nY)
        return nodes
    # TODO
    # Dynamische Nodes passen sich im Gegensatz zu statischen an ihre Umgebung an. Also berücksichtigen solide NPOs
    # Berechnet Nodes danach, ob zwischen der vorherigen Position und der "estimated Position" der jetzigen Iteration kein solides Objektes liegt
    def generateDynamicNodes(obj: GameObject, mod=1):
        if Game.level is None:
            raise DependencyException(PathFinder)
        
        nodes: List[Node] = []
        sx = ceil(screenRes[0] / obj.width * mod)
        sy = ceil(screenRes[1] / obj.height * mod)
        
        solidObjects = list(filter(lambda x: x is not obj, Game.level.allSolidObjects()))
        skipped = []
        for x in range(sx):
            pos = pygame.Vector2(x * obj.width / mod, 0)
            skipped.append([])
            for y in range(sy):
                skipped[x].append(skipped[x][y - 1] if y > 0 else 0)
                # Estimated Node Position
                estPos = pygame.Vector2(x * obj.width / mod, y * obj.height / mod)
                
                # Von vorheriger Node zur estPos
                furthestDown = Movement.furthestMove(obj, estPos, solidObjects, pos)
                # Wenn unsere Startposition (pos) bereits kollidiert, frage nach der erst-möglichen Position und setzte sie als neue Node
                if furthestDown is None:
                    firstDownPos = Movement.firstMove(obj, pygame.Vector2(pos.x, screenRes[1]), solidObjects, pos)
                    downNode = Node(firstDownPos)
                    pos = downNode.pos
                else:
                    downNode = Node(furthestDown)
                    if y != 0:
                        if nodes[-1].pos == downNode.pos:
                            # Um später von rechts nach links nachvollziehen zu können, ob Nodes geskipped worden, und ab welchen y-Value wird das in skipped festgehalten.
                            skipped[x][y] += 1
                            pos = estPos
                            continue
                        nodes[-1].down = downNode
                        downNode.higher = nodes[-1]
                    if x != 0:
                        # Die Anzahl der geskippten Nodes der gesamten letzen Col  -  die Nodes in der letzten Col, die noch vorher geskippt worden   +    die geskippten der aktuellen Col
                        skippedFromLastCol = skipped[x - 1][-1] - skipped[x - 1][y] + skipped[x][y]
                        nodes[-sy + skippedFromLastCol].right = downNode
                        downNode.left = nodes[-sy + skippedFromLastCol] # Problem: Skipped Values of the last col are only correct if the skip is in the the section of nodes to the left side
                    pos = estPos
                nodes.append(downNode)
        print(skipped)
        # # TESTING: FIXME
        # Game.notes["skipped"] = skipped
        return nodes

    # TODO Add "diagonal Node block" => Add nodes in a triangle "block" to allow diagonal movement in a collision checked space 

    @staticmethod
    def find(start: Node, dest: Node, depth: int=5) -> List[List[Node]]:
        if start == dest:
            return []
        PathFinder.minActions = 750
        paths = PathFinder.findPaths(start, dest, depth=-1, maxDepth=depth, recPath=[start])

        # paths = PathFinder.nodesToIds(paths) # For testing
        sortedPaths = sorted(paths, key=lambda obj: len(obj))

        # print("------------------- ------------------ -------------------")
        # print("------------------- PATH FINDER RESULT -------------------")
        # print(f"------------------- root: {start.id} - dest: {dest.id} -------------------")
        # print(sortedPath)
        # print("------------------- ------------------ -------------------")
        return sortedPaths


    def findPaths(node: Node, dest: Node, recPath=[], depth=0, maxDepth=5) -> List[List[Node]]:            
        paths: List[List[Node]] = []
        neighbors = PathFinder.bestNeighbors(node, dest)
        PathFinder.walkedNodes.append(node)
        depth += 1
        for i in range(len(neighbors)):
            n = neighbors[i]
            if n == None or n in recPath: # Dont search double on paths, already gone by the other "instances"
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
    
    #TODO
    def nearestNode(nodes: List[Node], pos: pygame.Vector2) -> Node:
        mapped = map(lambda x: (x.pos.distance_to(pos), x), nodes)
        return sorted(mapped, key=lambda x:x[0])[0][1]
