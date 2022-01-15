from base.core.Level.AbstractLevel import AbstractLevel
from base.core.Level.MapBuilder import MapBuilder
from base.objects.Text import TextObject
from pygame import Vector2

class Level4(AbstractLevel):
    def __init__(self) -> None:
        super().__init__(4)
    
    def make(self):
        center = MapBuilder.centerVec()
        text = TextObject(70, Vector2(center.x - 300, center.y - 100))
        text.color = (109, 27, 224)
        text.backgroundColor = (188, 174, 209)
        text.setFontSize(40)
        text.setText("Bravo! Du hast es geschafft!")
        self.add(text)
