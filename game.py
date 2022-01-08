from base.core.Game import Game
from levels import Level1

Game.addLevel(Level1(1))
Game.setLevel(1)
Game.start()