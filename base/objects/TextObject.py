from typing import Tuple
from base.core.Dependencies.Fonts import Fonts
from base.core.Event.Events import Events
from base.core.Object.GameObject import GameObject
from pygame import Vector2
import pygame
from settings import screen 


class TextObject(GameObject):
    def __init__(self, pos: Vector2 = Vector2(0, 0), width: int = 0, height: int = 0, color: Tuple = (0, 0, 0)) -> None:
        super().__init__(pos, width, height, color)
        self.height = 50
        self.width = 50
        self.font = None
        self.text = ""
        self.backgroundColor = (0, 0, 0)
        self.renderFont = None
        self.updateRect()

    def setFont(self, font: str, size: int=0):
        self.font = Fonts.get(font, size)
    
    def setText(self, text: str):
        if self.font is None:
            raise LookupError("Font has to be set!")
        self.text = text
        self.renderFont = self.font.render(self.text, 1, self.color, self.backgroundColor)

    def drawRect(self):
        if self.renderFont:
            screen.blit(self.renderFont, self.rect)
    