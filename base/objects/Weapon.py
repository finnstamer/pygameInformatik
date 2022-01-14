from pygame import Vector2
from base.core.Event.Events import Events
from base.core.Object.GameObject import GameObject
from base.objects.Actions.Actions.ShootWeaponAction import ShootWeaponAction
from base.objects.Projectile import Projectile
import time

class Weapon(GameObject):
    
    def __init__(self, owner: GameObject, relativePosition: Vector2, projectile: Projectile, cooldown: float, munition: int = 0) -> None:
        super().__init__()
        self.owner = owner
        self.relativePosition = relativePosition
        self.projectile = projectile
        self.munition = munition
        self.cooldown = cooldown
        self.lastShot = None
        self.subscribe("game.tick", self.onTick)

    def onTick(self, event):
        # Adjust Weapon to Owner
        self.pos = Vector2(self.owner.pos.x + self.relativePosition.x, self.owner.pos.y + self.relativePosition.y)

    def shoot(self, pos):
        if self.munition == 0 or (self.lastShot is not None and (time.time() * 1000 - self.lastShot) <= self.cooldown):
            return
        self.munition = self.munition - 1
        self.lastShot = time.time() * 1000
        self.projectile.pos = Vector2(self.pos.x + self.projectile.relativePosition.x, self.pos.y + self.projectile.relativePosition.y)
        ShootWeaponAction(self, pos).start()

    def shotPosition(self, dir):
        return {
            0: Vector2(self.pos.x, self.pos.y - self.projectile.range),
            1: Vector2(self.pos.x + self.projectile.range, self.pos.y),
            2: Vector2(self.pos.x, self.pos.y + self.projectile.range),
            3: Vector2(self.pos.x - self.projectile.range, self.pos.y)
        }[dir]
