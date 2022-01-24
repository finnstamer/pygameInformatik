from typing import Tuple
from pygame import Vector2
from base.core.Dependencies.Controls import Controls
from base.core.Event.Events import Events
from base.core.Game import Game
from base.core.Object.GameObject import GameObject


class Button2(GameObject):
    def __init__(self, pos: Vector2 = ..., width: int = 0, height: int = 0, color: Tuple = ...) -> None:
        super().__init__(pos=pos, width=width, height=height, color=color)
        Events.subscribe("game.tick", self.onTick)
        self.onClickMethod = lambda: None
        Game.use(Controls)
    
    def onClick(self):
        print("23")
        self.onClickMethod()
        pass

    def onTick(self, event):
        clicked, pos = Controls.clicks["l"]
        if clicked and self.rect.collidepoint(pos):
            self.onClick()