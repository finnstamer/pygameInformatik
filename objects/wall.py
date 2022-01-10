import pygame
from pygame.math import Vector2;
from base.core.Object.GameObject import GameObject
import random;


class Wall(GameObject):
    def __init__(self, pos: Vector2=Vector2(0, 0), width: int=1, height: int=1) -> None:
        super().__init__(
            color=(240, 240, 240), 
            pos=pos,
            width=width,
            height=height
        )
        self.solid = True
