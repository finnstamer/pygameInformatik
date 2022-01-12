from typing import Tuple
from pygame import Vector2
from base.core.Action.MovementRoutine import MovementRoutine
from base.core.Dependencies.CollisionWatcher import CollisionWatcher
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.core.Game import Game
from base.core.Level.AbstractLevel import AbstractLevel
from base.core.Object.Factory import Factory
from base.core.Object.GameObject import GameObject
from base.objects.Actions.Actions.MovementAction import MovementAction
from random import randrange

from base.objects.Actions.Routines.FollowObjectRoutine import FollowObjectRoutine

class Enemy(GameObject):
    def __init__(self, pos: Vector2 = ..., width: int = 0, height: int = 0, color: Tuple = ...) -> None:
        super().__init__(pos=pos, width=width, height=height, color=(255, 130, 201))
        self.alertedRadius = Vector2(200, 200)
        self.sleepRadius = Vector2(400, 400)
        self.alertedRadiusObject = GameObject(self.pos, self.alertedRadius.x, self.alertedRadius.y)
        self.sleepRadiusObject = GameObject(self.pos, self.sleepRadius.x, self.sleepRadius.y)
        AbstractLevel.bind(self.alertedRadiusObject, self.sleepRadiusObject)
        self.pathPool = [] 
        self.alerted = False

        player = Factory.get("player")
        
        self.solid = True
        self.fluid = True
        self.speed = 3
        self.health = 100

        
        # Events.subscribe("Level.loaded", self.onLoad)
        Events.subscribe(f"{player.id}.moved", self.onMovement)
        Events.subscribe(f"{self.id}.moved", self.onMovement)
        Events.subscribe("game.tick", self.onTick)
        Events.subscribe(f"{self.id}.died", self.onDied)

        self.movement = MovementRoutine(self)
        self.follow = FollowObjectRoutine(self, Factory.get("player"))    

        collisionWithPlayerEvent, _ = CollisionWatcher.watch(self, player)
        Events.subscribe(collisionWithPlayerEvent, self.onPlayerCollision)

        
    def onPlayerCollision(self, e):
        print("H")
        Game.level().reset()

    def onMovement(self, event):
        if Factory.get("player").collidesWith(self.alertedRadiusObject.rect):
            self.alerted = True
        if not Factory.get("player").collidesWith(self.sleepRadiusObject.rect):
            self.alerted = False
            
    def onTick(self, event):
        # Adjust Event Zones
        self.alertedRadiusObject.updatePos(Vector2(self.pos.x - self.alertedRadius.x / 2, self.pos.y - self.alertedRadius.y / 2))
        self.sleepRadiusObject.updatePos(Vector2(self.pos.x - self.sleepRadius.x / 2, self.pos.y - self.sleepRadius.y / 2))
        
        if not self.alerted:
            self.follow.stop()
            if self.movement.progress != 1:
                newPath = self.pathPool[randrange(0, len(self.pathPool))]
                self.movement.setStates(self, newPath)
                self.movement.start()   
                self.color = (255, 130, 201)
        
        if self.alerted and self.follow.progress != 1:
            self.movement.stop()
            # .restart(), weil FollowObject nur beim .setStates(), die Position des zu verfolgenden Obejekt
            # an die darunterliegende MovementRoutine weitergibt (siehe .onSet()). Es werden also keine neuen AKtionen gebildet.
            self.follow.restart(None)
            self.color = (245, 20, 148)
    
    def onDied(self, event):
        self.follow.stop()
        self.movement.stop()