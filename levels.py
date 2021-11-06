
# LEVEL
#--------------------#--------------------#--------------------
import pygame
from base.core.Level.Level import Level
from base.object.Group import Group
from base.player.Player import Player
from objects.wall import Wall


player = Player()
playerGroup = Group[Player]("player", Player).add(player)

# Level1
#--------------------
wall11 = Wall()
wall12= Wall()

wall11.updatePos(pygame.Vector2(200, 100))
wall12.updatePos(pygame.Vector2(275, 150))
wallGroup1 = Group[Wall]('walls', Wall).add(wall11, wall12)
level1 = Level(1, [playerGroup, wallGroup1])
# Level2
#-------------------
wall21 = Wall()
wall22 = Wall()

wall21.updatePos(pygame.Vector2(150, 100))
wall22.updatePos(pygame.Vector2(275, 150))
wallGroup2 = Group[Wall]('walls', Wall).add(wall21, wall22)
level2 = Level(2, [playerGroup, wallGroup2])
# Level3
#--------------------
global levels
levels = [level1, level2]