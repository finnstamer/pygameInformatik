from typing import Tuple
from pygame import Vector2
from base.core.Dependencies.Controls import Controls
from base.core.Event.Events import Events
from base.object.GameObject import GameObject


class Button(GameObject):
    def __init__(self, pos: Vector2 = ..., width: int = 0, height: int = 0, color: Tuple = ...) -> None:
        super().__init__(pos=pos, width=width, height=height, color=color)
        Events.subscribe("game.tick", self.onTick)
    
    def onClick(pos: Vector2):
        pass

    def onTick(self):
        mousePos = Controls.clicks["l"][1]
        if self.rect.collidepoint(mousePos):
            self.onClick(mousePos)