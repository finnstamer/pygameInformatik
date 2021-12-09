
# LEVEL
#--------------------#--------------------#--------------------
import pygame
from base.core.Level.Level import Level
from base.object.CircleOutlineObject import CircleOutlineObject
from base.object.Group import Group
from objects.collectables.Ektoplasma import Ektoplasma
from objects.player.Player import Player
from objects.Backround import Backround
from objects.wall import Wall


player = Player()
playerGroup = Group[Player]("player").add(player)

# Level1
#--------------------
wall11 = Wall()
wall12= Wall()
ektoplasma = Ektoplasma().updatePos(pygame.Vector2(250, 250))

wallGroup1 = Group[Wall]('walls').add(wall11, wall12, ektoplasma)
level1 = Level(1, [playerGroup, wallGroup1])
# Level2
#-------------------
wall21 = Wall()
wall22 = Wall()
bg = Backround("images/Wasser.png")
backgroundGroup = Group("bg").add(bg)

wall21.updatePos(pygame.Vector2(150, 100))
wall22.updatePos(pygame.Vector2(275, 150))
wallGroup2 = Group[Wall]('walls').add(wall21, wall22)
level2 = Level(2, [backgroundGroup, playerGroup, wallGroup2])
# Level3
#--------------------
global levels
levels = [level1, level2]