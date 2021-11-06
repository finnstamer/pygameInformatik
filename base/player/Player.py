from typing import Dict
import pygame
from base.core.Event.Event import Event
from base.core.Event.EventDispatcher import EventDispatcher
from base.object.MovableObject import MovableObject

class Player(MovableObject):
    def __init__(self) -> None:
        MovableObject.__init__(self)

        self.pos = pygame.math.Vector2((50, 50));
        self.color = (50, 50, 50)
        self.solid = True
        self.height = 50
        self.width = 50
        self.speed = 3

        self.updateRect()
        EventDispatcher.subscribe(self, "CONTROLS")
    
    def receiveEvent(self, event: Event):
        if event.name == "CONTROLS":
            keys = event.value
            self.control(keys)
            if keys["space"]:
                EventDispatcher.dispatch(Event("G_SWITCH_L", 2))

    def control(self, keys: Dict[str, bool]):
        pos = None
        if keys["left"]:
            pos = self.getPositionChange(-self.speed)
            self.move(pos)
        if keys["right"]:
            pos = self.getPositionChange(self.speed)
            self.move(pos)
        if keys["up"]:
            pos = self.getPositionChange(y=-self.speed)
            self.move(pos)
        if keys["down"]:
            pos = self.getPositionChange(y=self.speed)
            self.move(pos)
        if pos != None:
            self.move(pos)
