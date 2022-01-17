from base.core.Dependencies.Fonts import Fonts
from base.core.Level.AbstractLevel import AbstractLevel
from base.core.Level.MapBuilder import MapBuilder
from base.objects.TextObject import TextObject
from pygame import Vector2

class Level4(AbstractLevel):
    def __init__(self) -> None:
        super().__init__(4)
    
    def make(self):
        center = MapBuilder.centerVec()
        Fonts.load("font", "assets/font.ttf", 22)
        text = TextObject(Vector2(center.x - 300, center.y - 100))
        text.setFont("font", 22)
        text.color = (109, 27, 224)
        text.backgroundColor = (0, 0, 0)
        text.setText("Bravo! Du hast es geschafft!")
        self.add(text)
