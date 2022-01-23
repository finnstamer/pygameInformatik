from base.core.Dependencies.Fonts import Fonts
from base.core.Dependencies.Rendering.Layer import Layer
from base.core.Dependencies.Wait import Wait
from base.core.Event.Events import Events
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
    Fonts.load("start", "assets/font.ttf", 25)
    
    button = Button(Vector2(), 200, 200)
    button.onClickMethod = lambda: Game.setLevel(3)
    # button.color = (200, 200, 200)
    button.setImage("images/start.png")
    mB.placeInCenter(button)
    Layer.get(0).add(button)
    self.add(*mB.objects)