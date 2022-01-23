import pygame
from base.core.Dependencies.Debugger import Debugger
from base.core.Game import Game
from level.hub import Hub
from level.level1 import Level1
from level.level2 import Level2
from level.level3 import Level3
from level.level4 import Level4

Debugger.debug = True

pygame.init()
Game.addLevel(Hub(), Level1(), Level2(), Level3(), Level4())
Game.setLevel(0)

Game.start()