from base.core.Dependencies.CollisionWatcher import CollisionWatcher
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.core.Game import Game
from base.core.Object.Factory import Factory
from base.core.Object.GameObject import GameObject

class Ektoplasma(GameObject):
    collected = 0 
    def __init__(self) -> None:
        super().__init__(width=10, height=10, color=(3, 173, 63))
        self.collisionEvent = ""
        self.speed = 5
        self.solid = False
        self.health = 50

        collisionEvent = CollisionWatcher.watch(self, Factory.get("player"))
        self.collisionEvent = collisionEvent
        self.subscribe(self.collisionEvent[0], self.onCollision)

    def onCollision(self, e: Event):
        Ektoplasma.collected += 1
        self.active = False 
        # Game.level().delete(self)
