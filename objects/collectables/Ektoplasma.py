from base.core.Dependencies.CollisionWatcher import CollisionWatcher
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.core.Object.Factory import Factory
from base.core.Object.GameObject import GameObject

class Ektoplasma(GameObject):
    collected = 0 
    def __init__(self) -> None:
        super().__init__(width=25, height=25, color=(3, 173, 63))
        self.collisionEvent = ""
        self.speed = 5
        self.solid = True
        self.health = 50
        # Events.subscribe(self, "game.start", "game.tick")

    def receiveEvent(self, e: Event):
        if e.name == "game.start":
            collisionEvent = CollisionWatcher.watch(self, Factory.get("player"))
            self.collisionEvent = collisionEvent
            Events.subscribe(self, self.collisionEvent)

        if e.name == self.collisionEvent:
            Ektoplasma.collected += 1
            # self.active = False 