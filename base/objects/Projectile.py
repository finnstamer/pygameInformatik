from pygame import Vector2
from base.core.Object.GameObject import GameObject


class Projectile(GameObject):
    def __init__(self, range: int = 0, damage: int = 0, speed: int = 0, width: int = 0, height: int = 0, relativePosition: Vector2 = Vector2()) -> None:
        super().__init__(width=width, height=height)
        self.speed = speed
        self.damage = damage
        self.range = range
        self.active = False
        self.relativePosition = relativePosition