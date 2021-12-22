from pygame import Vector2
from base.core.Level.Level import Level
from base.core.Level.MapBuilder import MapBuilder
from objects.collectables.Ektoplasma import Ektoplasma
from objects.player.Player import Player
from objects.wall import Wall

#### Vorgehensweise mit Beispiele:
# 1. Erstelle einen MapBuilder und deine Objekte. 
#   mB = MapBuilder()
#   wall = Wall(Vector2(x, y), 50, 50)

# 2. Füge sie dem MapBuilder hinzu.
#   mB.addObject(wall, obj2, obj3, ...)

# 3. Füge einem neuen Level deine Objekte hinzu
#   level = Level(1, *mB.objects)

mB = MapBuilder()
player = Player()
mB.placeInCenter(player)

ektoplasma = Ektoplasma().setAlias("ekto1")
mB.nextTo(player, ektoplasma, 3, 0)

# mB.pointMirror(player.pos, player, ektoplasma)
# mB.axisMirror(player.pos.x, -1, player, ektoplasma)
level1 = Level(1, *mB.objects)



