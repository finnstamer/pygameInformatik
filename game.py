from base.core.Game import Game
from levels import levels
game = Game()
game.addLevel(*levels)
game.setLevel(1)
game.start()