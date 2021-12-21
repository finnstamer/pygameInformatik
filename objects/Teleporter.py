from base.core.Dependencies.CollisionWatcher import CollisionWatcher
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.object.GameObject import GameObject
from pygame import Vector2

class Teleporter():
    def __init__(self, teleporter: GameObject, obj: GameObject, dest: Vector2) -> None:
        self.teleporter = teleporter
        self.obj = obj
        self.dest = dest
        self.collision = ""
    
    def stop(self):
        Events.disconnect(self)
        return self
    
    def start(self):
        Events.subscribe(self, "game.start", self.collision)
        return self

    def receiveEvent(self, event: Event):
        if event.name == "game.start":
            self.collision = CollisionWatcher.watch(self.teleporter, self.obj)
            Events.subscribe(self, self.collision)

        if event.name == self.collision:
            self.obj.updatePos(self.dest)