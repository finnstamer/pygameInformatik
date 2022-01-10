from base.core.Game import Game
from levels import Level1, Start

Game.addLevel(Start(), Level1())
Game.setLevel(0)
Game.start()