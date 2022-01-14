from pygame import Vector2
from base.core.Dependencies.Movement import Movement
from base.core.Dependencies.Spawner import Spawner
from base.core.Game import Game
from base.core.Object.Factory import Factory
from base.objects.Actions.Actions.LineMovementAction import LineMovementAction
from base.objects.Actions.Actions.MovementAction import MovementAction
from base.core.Object.GameObject import GameObject

# Aktion zum Schuss eines duplizierten Projektils auf Basis der MovementAction
class ShootWeaponAction(LineMovementAction):
    def __init__(self, weapon: GameObject, endState: Vector2) -> None:
        super().__init__(weapon, endState)
        self.hitObjects = []
        self.weapon = weapon
        self.middlewareHandler.on("start", self.spawnProjectile, -2)
        self.middlewareHandler.on("start", self.setSteps)
        self.middlewareHandler.on("run", self.resetHitObjects)
        self.middlewareHandler.connect("segmentPos", self.evaluateNextPos)
        self.middlewareHandler.on("shot.hit", self.onHit)
        self.middlewareHandler.on("finished", self.removeProjectile)

    def spawnProjectile(self):
        self.object = Spawner.spawnObject(self.weapon.projectile, self.weapon.projectile.pos)
        self.object.active = True
    
    # Setze die max Anzahl an Steps für die LIneMovementAction in Abhängigkeit der range, anstatt der geklickten Position 
    def setSteps(self):
        if self.stepsToDo != 0:
            self.stepsToDo = int(self.weapon.projectile.range / self.weapon.projectile.speed) 
            
    
    # Setzt die Liste der getroffenen Objekte bei jedem Tick zurück
    def resetHitObjects(self):
        self.hitObjects = []

    # Verbinde mit der nach jedem Tick berechneten Position
    # Ist der reguläre Weg von einem Objekt behindert, wird "shot.hit" Event ausgegeben, 
    # die Aktion beendet und das Objekt entfernt
    def evaluateNextPos(self, pos) -> Vector2:
        furthestMove, objects = Movement.furthestLineMovement(self.object, pos)
        if len(objects) > 0:
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
        Game.level().delete(self.object)