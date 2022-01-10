from pygame import Vector2
from base.core.Dependencies.Movement import Movement
from base.core.Dependencies.Spawner import Spawner
from base.core.Game import Game
from base.objects.Actions.Actions.MovementAction import MovementAction
from base.core.Object.GameObject import GameObject

# Aktion zum Schuss eines duplizierten Projektils auf Basis der MovementAction
class ShootWeaponAction(MovementAction):
    def __init__(self, weapon: GameObject, endState: Vector2) -> None:
        super().__init__(weapon, endState)
        self.hitObjects = []
        self.weapon = weapon
        self.middlewareHandler.on("start", self.spawnProjectile)
        self.middlewareHandler.on("run", self.resetHitObjects)
        self.middlewareHandler.connect("segmentPos", self.evaluateNextPos)
        self.middlewareHandler.on("shot.hit", self.onHit)
        self.middlewareHandler.on("finished", self.removeProjectile)

    def spawnProjectile(self):
        self.object = Spawner.spawnObject(self.weapon.projectile, self.weapon.projectile.pos)
        self.object.active = True
    
    # Setzt die Liste der getroffenen Objekte bei jedem Tick zurück
    def resetHitObjects(self):
        self.hitObjects = []

    # Verbinde mit der nach jedem Tick berechneten Position
    # Ist der reguläre Weg von einem Objekt behindert, wird "shot.hit" Event ausgegeben, 
    # die Aktion beendet und das Objekt entfernt
    def evaluateNextPos(self, pos) -> Vector2:
        furthestMove, objects = Movement.furthestMove_collider(self.object, pos, self.object.pos)
        if furthestMove == self.object.pos or furthestMove is None:
            self.hitObjects = objects
            self.middlewareHandler.dispatch("shot.hit")
            self.stop()
            self.removeProjectile()
            return self.object.pos
        return furthestMove

    def onHit(self):
        for obj in self.hitObjects:
            obj.damage(self.weapon.projectile.damage)
            
    def removeProjectile(self):
        self.object.active = False
        Game.level().remove(self.object)
    