
# LEVEL
#--------------------#--------------------#--------------------
from random import randrange
from pygame import Vector2
from base.core.Level.Level import Level
from base.object.Factory.Factory import Factory
from objects.collectables.Ektoplasma import Ektoplasma
from objects.player.Player import Player
from objects.wall import Wall

# for w in range(10):
#     wallGroup1.add(Wall().updatePos(pygame.Vector2(randrange(51, screenRes[0]), randrange(51, screenRes[1]))))
# wall12= Wall().updatePos(pygame.Vector2(400, 200))
    
level1 = Level(1,
    Player(),
    Wall(Vector2(217, 205), 50, 75),
    Ektoplasma().updatePos(Vector2(0, 0)).setAlias("ekto1")
)

levels = [level1]