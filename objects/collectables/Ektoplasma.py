from base.core.Dependencies.CollisionWatcher import CollisionWatcher
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.object.Factory.Factory import Factory
from base.object.GameObject import GameObject
from base.object.KI.Routines.SimpleMovementRoutine import SimpleMovementRoutine
from base.object.MovableObject import MovableObject

class Ektoplasma(MovableObject):
    collected = 0 
    def __init__(self) -> None:
        super().__init__(width=25, height=25, color=(3, 173, 63))
        self.collisionEvent = ""
        self.speed = 5
        Events.subscribe(self, "game.start")

    def receiveEvent(self, e: Event):
        if e.name == "game.start":
            collisionEvent = CollisionWatcher.watch(self, Factory.get("player"))
            self.collisionEvent = collisionEvent
            Events.subscribe(self, self.collisionEvent)

        if e.name == self.collisionEvent:
            Ektoplasma.collected += 1
            # self.active = False 