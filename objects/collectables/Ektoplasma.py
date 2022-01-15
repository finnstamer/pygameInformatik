from base.core.Dependencies.CollisionWatcher import CollisionWatcher
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.core.Game import Game
from base.core.Object.Factory import Factory
from base.core.Object.GameObject import GameObject

class Ektoplasma(GameObject):
    def __init__(self) -> None:
        super().__init__(width=10, height=10, color=(3, 173, 63))
        self.collisionEvent = ""
        self.solid = False

        collisionEvent = CollisionWatcher.watch(self, Factory.get("player"))
        self.collisionEvent = collisionEvent
        self.subscribe(self.collisionEvent[0], self.onCollision)

    def onCollision(self, e: Event):
        self.active = False 
        Game.level().delete(self)