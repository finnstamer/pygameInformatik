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
        EventDispatcher.subscribe(self, "G_CONTROLS")

    
    def receiveEvent(self, event: Event):
        if event.name == "G_CONTROLS":
            keys = event.value
            self.control(keys)
            if keys["space"]:
                EventDispatcher.dispatch(Event("G_SWITCH_L", 2))

    def control(self, keys: Dict[str, bool]):
        if keys["left"]:
            self.moveByDelta(-self.speed)
        if keys["right"]:
            self.moveByDelta(self.speed)
        if keys["up"]:
            self.moveByDelta(-self.speed, False)
        if keys["down"]:
            self.moveByDelta(self.speed, False)
