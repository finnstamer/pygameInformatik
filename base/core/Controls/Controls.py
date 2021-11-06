import pygame
from pygame.constants import K_LEFT, K_RIGHT, K_SPACE, K_UP, K_DOWN
class Controls():
    controls = {"left": False, "right": False, "up": False, "down": False, "space": False}

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
            Controls.controls["left"] = True
        if pressed == K_RIGHT:
            Controls.controls["right"] = True
        if pressed == K_UP:
            Controls.controls["up"] = True
        if pressed == K_DOWN:
            Controls.controls["down"] = True
        if pressed == K_SPACE:
            Controls.controls["space"] = True

    @staticmethod
    def updateControlsReleased(released):
        if released == K_LEFT:
            Controls.controls["left"] = False
        if released == K_RIGHT:
            Controls.controls["right"] = False
        if released == K_UP:
            Controls.controls["up"] = False
        if released == K_DOWN:
            Controls.controls["down"] = False
        if released == K_SPACE:
            Controls.controls["space"] = False
