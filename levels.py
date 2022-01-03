from pygame import Vector2
from base.core.Event.Events import Events
from base.core.Level.Level import Level
from base.core.Level.MapBuilder import MapBuilder
from base.object.Projectile import Projectile
from base.object.Weapon import Weapon
from objects.collectables.Ektoplasma import Ektoplasma
from objects.player.Player import Player
from objects.wall import Wall
from random import randrange

#### Vorgehensweise mit Beispielen:
# 1. Erstelle einen MapBuilder und deine Objekte. 
#   mB = MapBuilder()
#   wall = Wall(Vector2(x, y), 50, 50)

# 2. Füge sie dem MapBuilder hinzu.
#   mB.addObject(wall, obj2, obj3, ...)

# 3. Füge einem neuen Level deine Objekte hinzu
#   level = Level(1, *mB.objects)

mB = MapBuilder()
for i in range(10):
    mB.addObject(Wall(Vector2(randrange(0, 500), randrange(0, 500)), 25, 25))

player = Player()
mB.placeInCenter(player)

projectile = Projectile(range=150, damage=50, speed=20, width=5, height=5)
projectile.color = (114, 114, 114)
weapon = Weapon(player, Vector2(10, 10), projectile, 100)
weapon.color = (29, 191, 172)
weapon.height = 5
weapon.width = 10
weapon.setAlias("weapon")

mB.addObject(weapon, projectile)

ektoplasma = Ektoplasma().setAlias("ekto1")
mB.nextTo(player, ektoplasma, 1, 0, marginX=0)

# mB.pointMirror(player.cRect.corners[0], player, ektoplasma)
# mB.axisMirror(-1, player.pos.y, player, ektoplasma)
level1 = Level(1, *mB.objects)



