import pygame;
from base.object.GameObject import GameObject
import random;


class Wall(GameObject):
    def __init__(self) -> None:
        super().__init__(
            color=(240, 240, 240), 
            pos=pygame.math.Vector2(random.randrange(50, 400), 
            random.randrange(50, 200)),
            width=50,
            height=50
        )
        self.solid = True
