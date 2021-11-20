from typing import Dict
import pygame
from base.core.Dependencies.Controls import Controls
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.core.Game import Game
from base.object.GameObject import GameObject
from base.object.Group import Group
from base.object.KI.Node import Node
from base.object.KI.PathFinder import PathFinder
from base.object.MovableObject import MovableObject
from settings import screenRes

class Player(MovableObject):
    def __init__(self) -> None:
        MovableObject.__init__(self)

        self.pos = pygame.math.Vector2((50, 50));
        self.color = (50, 50, 50)
        self.solid = True
        self.height = 50
        self.width = 50
        self.speed = 10
        Game.use(Controls)
        Events.subscribe(self, "game.tick", "game.start", "game.dependency.tick")

    def default(self, obj):
        obj.color = (0, 0, 250)
        return obj
    
    def receiveEvent(self, event: Event):
        if event.name == "game.start":
            nodes = PathFinder.optimizeNodes(self, screenRes)

            objNodes = []
            for i in range(len(nodes)):
                node = nodes[i]
                node.id = i
                obj = GameObject()
                obj.id = i
                obj.pos = node.pos
                obj.width = 5
                obj.height = 5
                obj.color = (0, 0, 250)
                Game.notes[i] = node
                objNodes.append(obj)
            
            g = Group("nodes", Node).add(*objNodes)
            print(g.length())
            Game.level.addGroup(g)

        # basically mimicking the defaultValues Dependenccy
        if event.name == "game.dependency.tick":
            Game.level.getGroup("nodes").applyOnEach(self.default)

        if event.name == "game.tick":
            keys = Controls.keys
            self.control(keys)
            if keys["space"]:
                Events.dispatch("game.level.switch", 2 if Game.level.id != 2 else 1)
            if keys["escape"]:
                Events.dispatch("game.stop")
            
            nearest = Game.level.getGroup("nodes").nearest(self.cRect.center)
            node = Game.notes[nearest.id]
            Game.level.getObject(node.down.down.down.right.id).color = (250, 100, 250)
            Game.level.getObject(node.id).color = (50, 250, 50)
            # upperNode = node.higher
            # upperNodeObj = Game.level.getObject(upperNode.id)
            # upperNodeObj.color = (250, 0, 0)
            Game.level.getObject(node.higher.id if node.higher else 0).color = (250, 0, 0)
            Game.level.getObject(node.down.id if node.down else 0).color = (250, 0, 0)
            Game.level.getObject(node.right.id if node.right else 0).color = (250, 0, 0)
            Game.level.getObject(node.left.id if node.left else 0).color = (250, 0, 0)

    def control(self, keys: Dict[str, bool]):
        if keys["left"]:
            self.moveByDelta(-self.speed)
        if keys["right"]:
            self.moveByDelta(self.speed)
        if keys["up"]:
            self.moveByDelta(-self.speed, False)
        if keys["down"]:
            self.moveByDelta(self.speed, False)
