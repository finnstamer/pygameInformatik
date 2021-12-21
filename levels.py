
# LEVEL
#--------------------#--------------------#--------------------
from random import randrange
import pygame
from base.core.Level.Level import Level
from base.object.Factory.Factory import Factory
from base.object.Group import Group
from objects.collectables.Ektoplasma import Ektoplasma
from objects.player.Player import Player
from objects.Backround import Backround
from objects.wall import Wall
from settings import screenRes
playerGroup = Group(Player())

# Level1
#--------------------
wallGroup1 = Group()
# for w in range(10):
#     wallGroup1.add(Wall().updatePos(pygame.Vector2(randrange(51, screenRes[0]), randrange(51, screenRes[1]))))
wall11 = Wall(pygame.Vector2(217, 205), 50, 75)
wallGroup1.add(wall11)
# wall12= Wall().updatePos(pygame.Vector2(400, 200))
    
ektoplasma = Ektoplasma().updatePos(pygame.Vector2(0, 0))
Factory.setAlias(ektoplasma, "ekto1")

wallGroup1.add(ektoplasma)
level1 = Level(1, [playerGroup, wallGroup1])
# Level2
#-------------------
# wall21 = Wall()
# wall22 = Wall()
# bg = Backround("images/Wasser.png")
# backgroundGroup = Group("bg").add(bg)

# wall21.updatePos(pygame.Vector2(150, 100))
# wall22.updatePos(pygame.Vector2(275, 150))
# wallGroup2 = Group[Wall]('walls').add(wall21, wall22)
# level2 = Level(2, [backgroundGroup, playerGroup, wallGroup2])
# Level3
#--------------------
global levels
levels = [level1]