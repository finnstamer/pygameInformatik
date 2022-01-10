import pygame
from pygame.constants import K_ESCAPE, K_LEFT, K_LSHIFT, K_RIGHT, K_SPACE, K_UP, K_DOWN, KSCAN_A, KSCAN_D, KSCAN_S, KSCAN_W, K_a, K_d, K_s, K_w
from base.core.Event.Event import Event

from base.core.Event.Events import Events
class Controls():
    keys = {"w": False, "s": False, "a": False, "d": False, "left": False, "right": False, "up": False, "down": False, "space": False, "escape": False, "lShift": False}
    pressed = {}
    released = {}
    clicks = {"l": (False, pygame.Vector2(0, 0))}
    
    def __init__(self) -> None:
        Events.subscribe("game.dependency.tick", Controls.update)
        
    @staticmethod
    def update(event):
        Controls.released = {"left": False, "right": False, "up": False, "down": False, "space": False, "escape": False, "lShift": False}
        Controls.pressed = {"left": False, "right": False, "up": False, "down": False, "space": False, "escape": False, "lShift": False}
        Controls.clicks["l"] = (False, pygame.Vector2())
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                Controls.updateControlsPressed(event.key)
            if event.type == pygame.KEYUP:
                Controls.updateControlsReleased(event.key)
            if event.type == pygame.MOUSEBUTTONUP:
                Controls.updateClicks()
            
    def updateClicks():
        Controls.clicks["l"] = (True, pygame.mouse.get_pos())
                
    @staticmethod
    def updateControlsPressed(k):
        if k == K_SPACE:
            Controls.keys["space"] = True
            Controls.pressed["space"] = True
        if k == K_ESCAPE:
            Controls.keys["escape"] = True
            Controls.pressed["escape"] = True
        if k == K_LSHIFT:
            Controls.keys["lShift"] = True
            Controls.pressed["lShift"] = True
        
        if k == K_w:
            Controls.keys["w"] = True
            Controls.pressed["w"] = True
        if k == K_d:
            Controls.keys["d"] = True
            Controls.pressed["d"] = True
        if k == K_s:
            Controls.keys["s"] = True
            Controls.pressed["s"] = True
        if k == K_a:
            Controls.keys["a"] = True
            Controls.pressed["a"] = True

    @staticmethod
    def updateControlsReleased(k):
        Controls.released["space"] = False
        if k == K_LEFT:
            Controls.keys["left"] = False
        if k == K_RIGHT:
            Controls.keys["right"] = False
        if k == K_UP:
            Controls.keys["up"] = False
        if k == K_DOWN:
            Controls.keys["down"] = False
        if k == K_SPACE:
            Controls.keys["space"] = True
        if k == K_ESCAPE:
            Controls.keys["escape"] = False
        if k == K_LSHIFT:
            Controls.keys["lShift"] = False
        if k == K_w:
            Controls.keys["w"] = False   
        if k == K_d:
            Controls.keys["d"] = False   
        if k == K_s:
            Controls.keys["s"] = False   
        if k == K_a:
            Controls.keys["a"] = False   