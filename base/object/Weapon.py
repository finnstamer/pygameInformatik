from pygame import Vector2, color
from base.core.Dependencies.Spawner import Spawner
from base.core.Event.Events import Events
from base.object.AI.Actions.MovementAction import MovementAction
from base.object.GameObject import GameObject
from base.object.Projectile import Projectile
import time

class Weapon(GameObject):
    
    def __init__(self, owner: GameObject, relativePosition: Vector2, projectile: Projectile, cooldown: float) -> None:
        super().__init__()
        self.owner = owner
        self.relativePosition = relativePosition
        self.projectile = projectile
        self.cooldown = cooldown
        self.lastShot = None
        Events.subscribe("game.tick", self.onTick)

    def onTick(self, event):
        self.pos = Vector2(self.owner.pos.x + self.relativePosition.x, self.owner.pos.y + self.relativePosition.y)

    def shoot(self, dir: int):
        if self.lastShot is None or (time.time() * 1000 - self.lastShot) > self.cooldown:
            self.lastShot = time.time() * 1000
        else:
            return        
        projectile: Projectile = Spawner.spawnObject(self.projectile, self.pos)
        projectile.prepare()
        projectile.movementAction.setStates(projectile, self.shotPosition(dir))
        projectile.movementAction.start()

    def shotPosition(self, dir):
        return {
            0: Vector2(self.pos.x, self.pos.y - self.projectile.range),
            1: Vector2(self.pos.x + self.projectile.range, self.pos.y),
            2: Vector2(self.pos.x, self.pos.y + self.projectile.range),
            3: Vector2(self.pos.x - self.projectile.range, self.pos.y)
        }[dir]
