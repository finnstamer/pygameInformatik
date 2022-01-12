from base.core.Dependencies.CollisionWatcher import CollisionWatcher
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.core.Object.GameObject import GameObject
from pygame import Vector2

class Teleporter():
    def __init__(self, teleporter: GameObject, obj: GameObject, dest: Vector2) -> None:
        self.teleporter = teleporter
        self.obj = obj
        self.dest = dest
        self.colEvent = ""
        self.colEvent = CollisionWatcher.watch(self.teleporter, self.obj)
        Events.subscribe(self.colEvent, self.onCollision)
    
    def stop(self):
        Events.disconnect(self)
        return self
    
    def onCollision(self, event):
        self.obj.updatePos(self.dest)
