from base.core.Game import Game
from level2 import Level2
from level3 import Level3
from levels import Level1, Start

Game.addLevel(Start(), Level2(), Level1(), Level3())
Game.setLevel(1)
Game.start()