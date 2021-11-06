from typing import Tuple
import pygame

class Vec2():
    
    @staticmethod
    def fromTuple(tuple: Tuple[int, int]):
        return pygame.Vector2(tuple)