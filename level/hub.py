from base.core.Game import Game
from base.core.Level.AbstractLevel import AbstractLevel
from base.core.Level.MapBuilder import MapBuilder
from pygame import Vector2

from base.objects.Button import Button

class Hub(AbstractLevel):
  def __init__(self) -> None:
      super().__init__(0)
  
  def make(self):
    mB = MapBuilder()
    button = Button(Vector2(), 200, 200)
    button.onClickMethod = lambda: Game.setLevel(1)
    # button.color = (200, 200, 200)0
    button.setImage("images/start.png")
    mB.placeInCenter(button)
    self.objects = mB.objects