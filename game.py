import re
from base.core.Dependencies.Debugger import Debugger
from base.core.Event.EventRegister import EventRegister
from base.core.Event.Events import Events
from base.core.Game import Game
from base.core.Object.Factory import Factory
from base.core.Object.GameObject import GameObject
from level.hub import Hub
from level.level1 import Level1
from level.level2 import Level2
from level.level3 import Level3
from level.level4 import Level4
from objects.collectables.Ektoplasma import Ektoplasma
import pygame
Debugger.debug = True

# print(re.fullmatch(".\\.moved", "5.moved"))


pygame.init()
Game.addLevel(Hub(), Level1(), Level2(), Level3(), Level4())
Game.setLevel(0)

Game.start()