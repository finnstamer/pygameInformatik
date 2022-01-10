from pygame import Vector2
from base.core.Event.Events import Events
from base.core.Level.AbstractLevel import AbstractLevel
from base.core.Level.Level import Level
from base.core.Level.MapBuilder import MapBuilder
from base.objects.Enemy import Enemy
from base.objects.Projectile import Projectile
from base.objects.Weapon import Weapon
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
MapBuilder.allowClickMode(lambda x: f"Ektoplasma().updatePos(Vector2({x})),")

class Level1(AbstractLevel):
    def __init__(self) -> None:
        super().__init__(1)
    def make(self):
        mB = MapBuilder()

        mirrorObjects = [
          Wall(Vector2(10, 10), width=50, height=50),
          Wall(Vector2(10, 200), width=50, height=50),
          Ektoplasma().updatePos(mB.centerVec())
        ]

        
        mB.pointMirror(mB.centerVec(), mirrorObjects)

        # objects = [
        #   Wall(Vector2(), width=5, height=5)
        # ]
        enemy = Enemy(Vector2(300, 300), 50, 50, (250, 0, 0))
        enemy.pathPool = [Vector2(400, 400), Vector2(500, 100), Vector2(200, 500)]
        enemy.setAlias("Enemy")
        
        mB.addObject(Player().updatePos(Vector2(200, 200)), enemy)
        mB.addObject(*mirrorObjects)
        self.objects = mB.objects

        # for i in range(10):
        #     mB.addObject(Wall(Vector2(randrange(0, 500), randrange(0, 500)), 25, 25))

        # player = Player()
        # mB.placeInCenter(player)

        # projectile = Projectile(range=500, damage=10, speed=20, width=5, height=5, relativePosition=Vector2(75, 3))
        # projectile.color = (114, 114, 114)
        # weapon = Weapon(player, Vector2(-10, 10), projectile, cooldown=100, munition=50000)
        # weapon.color = (29, 191, 172)
        # weapon.height = 20
        # weapon.width = 75
        # weapon.setImage("images/pump.png")
        # weapon.setAlias("weapon")

        # mB.addObject(weapon, projectile)

        # ektoplasma = Ektoplasma().setAlias("ekto1")
        # mB.nextTo(player, ektoplasma, 1, 0, marginX=0)

# mB.pointMirror(player.cRect.corners[0], player, ektoplasma)
# mB.axisMirror(-1, player.pos.y, player, ektoplasma)
# level1 = Level(1, *mB.objects)



