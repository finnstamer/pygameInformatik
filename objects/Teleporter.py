from base.core.Dependencies.CollisionWatcher import CollisionWatcher
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.core.Level.AbstractLevel import AbstractLevel
from base.core.Object.GameObject import GameObject
from pygame import Vector2

class Teleporter():
    def __init__(self, teleporter: GameObject, obj: GameObject, dest: Vector2) -> None:
        self.teleporter = teleporter
        self.obj = obj
        self.dest = dest
        self.colEvent, _ = CollisionWatcher.watch(self.teleporter, self.obj)
        AbstractLevel.bind(self)
        Events.subscribe(self.colEvent, self.onCollision, self)
    
    def stop(self):
        Events.unsubscribe(self.colEvent, self.onCollision, self)
        return self
    
    def onCollision(self, event):
        self.obj.updatePos(self.dest)
