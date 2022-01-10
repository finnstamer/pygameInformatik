from pygame import Vector2
from base.core.Dependencies.Movement import Movement
from base.core.Game import Game
from base.objects.Actions.Actions.MovementAction import MovementAction
from base.core.Object.GameObject import GameObject


class ShootAction(MovementAction):
    def __init__(self, projectile: GameObject, endState: Vector2) -> None:
        super().__init__(projectile, endState)
        self.middlewareHandler.on("start", self.setActive)
        self.middlewareHandler.on("run", self.resetHitObjects)
        self.middlewareHandler.on("finished", self.deactivateProjectile)
        self.middlewareHandler.connect("segmentPos", self.evaluateNextPos)

    def resetHitObjects(self):
        self.hitObjects = []

    def setActive(self):
        self.object.active = True
    
    def evaluateNextPos(self, pos):
        furthestMove, objects = Movement.furthestMove_collider(self.object, pos, self.object.pos)
        if furthestMove == self.object.pos or furthestMove is None:
            self.hitObjects = objects
            self.middlewareHandler.dispatch("shot.hit")
            self.stop()
            self.deactivateProjectile()
            return self.object.pos
        return furthestMove

    def deactivateProjectile(self):
        self.object.active = False
        Game.level().remove(self.object)