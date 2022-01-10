from typing import List

from pygame import Vector2
from base.core.Dependencies.Movement import Movement
from base.core.Game import Game
from base.objects.Actions.Actions.MovementAction import MovementAction
from base.objects.Actions.Actions.ShootAction import ShootAction
from base.core.Object.GameObject import GameObject


class Projectile(GameObject):
    def __init__(self, range: int = 0, damage: int = 0, speed: int = 0, width: int = 0, height: int = 0, relativePosition: Vector2 = Vector2()) -> None:
        super().__init__(width=width, height=height)
        self.speed = speed
        self.damage = damage
        self.range = range
        self.active = False
        self.relativePosition = relativePosition
    
    def prepare(self):
        self.action = ShootAction(self, self.pos)
        self.action.middlewareHandler.on("shot.hit", self.onHit)
    
    def onHit(self):
        for obj in self.action.hitObjects:
            obj.damage(self.damage)
        self.action.stop()