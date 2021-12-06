import pygame
from pygame.constants import K_ESCAPE, K_LEFT, K_LSHIFT, K_RIGHT, K_SPACE, K_UP, K_DOWN
from base.core.Event.Event import Event

from base.core.Event.Events import Events
class Controls():
    keys = {"left": False, "right": False, "up": False, "down": False, "space": False, "escape": False, "lShift": False}
    pressed = {"left": False, "right": False, "up": False, "down": False, "space": False, "escape": False, "lShift": False}

    def __init__(self) -> None:
        Events.subscribe(self, "game.dependency.tick")

    def receiveEvent(self, event: Event):
        if event.name == "game.dependency.tick":
            Controls.update()
        
    @staticmethod
    def update():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                Controls.updateControlsPressed(event.key)
            if event.type == pygame.KEYUP:
                Controls.updateControlsReleased(event.key)
                    
    @staticmethod
    def updateControlsPressed(pressed):
        if pressed == K_LEFT:
            Controls.keys["left"] = True
        if pressed == K_RIGHT:
            Controls.keys["right"] = True
        if pressed == K_UP:
            Controls.keys["up"] = True
        if pressed == K_DOWN:
            Controls.keys["down"] = True
        if pressed == K_SPACE:
            Controls.keys["space"] = True
        if pressed == K_ESCAPE:
            Controls.keys["escape"] = True
        if pressed == K_LSHIFT:
            Controls.keys["lShift"] = True

    @staticmethod
    def updateControlsReleased(released):
        if released == K_LEFT:
            Controls.keys["left"] = False
        if released == K_RIGHT:
            Controls.keys["right"] = False
        if released == K_UP:
            Controls.keys["up"] = False
        if released == K_DOWN:
            Controls.keys["down"] = False
        if released == K_SPACE:
            Controls.keys["space"] = False
        if released == K_ESCAPE:
            Controls.keys["escape"] = False
        if released == K_LSHIFT:
            Controls.keys["lShift"] = False
