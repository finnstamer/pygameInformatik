from typing import List
from pygame import Vector2
from base.core.Game import Game
from base.core.Object.Factory import Factory
from base.core.Object.GameObject import GameObject


class Spawner():
    def __init__(self, obj: GameObject) -> None:
        self.object = obj

    @staticmethod
    def spawnObject(obj, pos: Vector2) -> GameObject:
        cloned: GameObject = Factory.clone(obj)
        cloned.updatePos(pos)
        Game.level().add(cloned)
        return cloned
    
    def spawnQuantity(self, pos: Vector2, qnty: int):
        for i in range(qnty):
            Spawner.spawnObject(self.object, pos)

    def spawnMultipleObjects(self, positons: List[Vector2]):
        for p in positons:
            Spawner.spawnObject(self.object, p)