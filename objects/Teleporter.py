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
        Events.subscribe(self, "game.start")
    
    def receiveEvent(self, event: Event):
        if event.name == "game.start":
            self.collision = CollisionWatcher.watch(self.teleporter, self.obj)

        if event.name == self.collision:
            self.obj.updatePos(self.dest)