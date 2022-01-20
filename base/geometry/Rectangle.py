from turtle import width
from typing import List
from copy import deepcopy
from pygame import Vector2, Rect

class Rectangle():
    def getCorners(rect: Rect):
        return (
            Vector2(rect.x, rect.y), 
            Vector2(rect.x + rect.width, rect.y), 
            Vector2(rect.x + width, rect.y + rect.height), 
            Vector2(rect.x, rect.y + rect.height), 
        )
        