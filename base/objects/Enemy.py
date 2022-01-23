from typing import Tuple
from pygame import Vector2
from base.core.Action.MovementRoutine import MovementRoutine
from base.core.Dependencies.CollisionWatcher import CollisionWatcher
from base.core.Dependencies.Rendering.Layer import Layer
from base.core.Game import Game
from base.core.Level.AbstractLevel import AbstractLevel
from base.core.Object.Factory import Factory
from base.core.Object.GameObject import GameObject
from random import randrange
from pygame import Rect

from base.objects.Actions.Routines.FollowObjectRoutine import FollowObjectRoutine

class Enemy(GameObject):
    def __init__(self, pos: Vector2 = ..., width: int = 0, height: int = 0, color: Tuple = ...) -> None:
        super().__init__(pos=pos, width=width, height=height, color=(255, 153, 211))
        self.alertedRadius = Vector2(300, 300)
        self.sleepRadius = Vector2(450, 450)
        
        self.alertedRadiusRect = Rect(self.pos.x, self.pos.y, self.alertedRadius.x, self.alertedRadius.y)
        self.sleepRadiusRect = Rect(self.pos.x, self.pos.y, self.sleepRadius.x, self.sleepRadius.y)
        
        self.pathPool = [] 
        self.alerted = False

        player = Factory.get("player")
        
        self.solid = True
        self.fluid = True
        self.sleepSpeed = 200
        self.alertSpeed = 275
        self.speed = 0
        self.health = 100

        
        self.subscribe("level.loaded", self.onLoad)
        self.subscribe(f"{player.id}.moved", self.onMovement)
        self.subscribe(f"{self.id}.moved", self.onMovement)
        self.subscribe("game.tick", self.onTick)
        self.subscribe(f"{self.id}.died", self.onDied)       

        collisionWithPlayerEvent, _ = CollisionWatcher.watch(self, player)
        self.subscribe(collisionWithPlayerEvent, self.onPlayerCollision)

    # Lade Routinen, wenn alle nonFluidSolids geladen sind
    def onLoad(self, e):        
        self.movement = MovementRoutine(self)
        self.follow = FollowObjectRoutine(self, Factory.get("player"))  
        
    def onPlayerCollision(self, e):
        Game.setLevel(Game.currentLevel)
        pass


    def onMovement(self, event):
        if Factory.get("player").collidesWith(self.alertedRadiusRect):
            self.alerted = True
        if not Factory.get("player").collidesWith(self.sleepRadiusRect):
            self.alerted = False
            
    def onTick(self, event):
        # Adjust Event Zones
        self.alertedRadiusRect.update(self.pos.x - self.alertedRadius.x / 2, self.pos.y - self.alertedRadius.y / 2, self.alertedRadius.x, self.alertedRadius.y)
        self.sleepRadiusRect.update(self.pos.x - self.sleepRadius.x / 2, self.pos.y - self.sleepRadius.y / 2, self.sleepRadius.x, self.sleepRadius.y)
        # self.sleepRadiusRect.move_ip(Vector2(self.pos.x - self.sleepRadius.x / 2, self.pos.y - self.sleepRadius.y / 2))

        # Über die Movements wird überprüft ob das nächste Movement in einer Aktion zu einer Kollision führt
        if self.health == 0:
            return         
        if not self.alerted:
            self.speed = self.sleepSpeed
            self.follow.stop()
            if self.movement.progress != 1:
                newPath = self.pathPool[randrange(0, len(self.pathPool))]
                self.movement.setStates(self, newPath)
                self.movement.start()   
                self.color = (255, 153, 211)
        
        if self.alerted and self.follow.progress != 1:
            self.speed = self.alertSpeed
            self.movement.stop()
            # .restart(), weil FollowObject nur beim .setStates(), die Position des zu verfolgenden Obejekt
            # an die darunterliegende MovementRoutine weitergibt (siehe .onSet()). Es werden also keine neuen AKtionen gebildet.
            self.follow.restart(None)
            self.color = (191, 6, 0)
    
    def onDied(self, event):
        self.follow.stop()
        self.movement.stop()