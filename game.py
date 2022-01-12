from base.core.Game import Game
from base.core.Object.Factory import Factory
from level.hub import Hub
from level.level1 import Level1
from level.level2 import Level2
from level.level3 import Level3

Game.addLevel(Hub(), Level1(), Level2(), Level3())
Game.setLevel(0)
Game.start()