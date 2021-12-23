from base.core.Game import Game
from base.object.GameObject import GameObject
from levels import level1

game = Game()
game.addLevel(level1)
game.setLevel(1)
game.start()