from pygame import Vector2
from base.core.Event.Events import Events
from base.core.Level.AbstractLevel import AbstractLevel
from base.core.Level.Level import Level
from base.core.Level.MapBuilder import MapBuilder
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



class Level1(AbstractLevel):
    def __init__(self) -> None:
        super().__init__(1)
    def make(self):
        mB = MapBuilder()
        objects = [
          # Mittlerer Block
          Wall(Vector2(500,330), width=80, height=70), 
          # Oben rechts und links länglich
          Wall(Vector2(450,90), width=50, height=180), 
          Wall(Vector2(580,90), width=50, height=180), 
          # Unten rechts und links länglich
          Wall(Vector2(450,450), width=50, height=180),
          Wall(Vector2(580,450), width=50, height=180),
          # Mitte links oben und unten
          Wall(Vector2(200,270), width=180, height=50),
          Wall(Vector2(200,400), width=180, height=50),
          # Mitte rechts oben und unten
          Wall(Vector2(700,270), width=180, height=50),
          Wall(Vector2(700,400), width=180, height=50),
          #oben
          Wall(Vector2(360,0), width=360, height=40),
          #unten
          Wall(Vector2(360,680), width=360, height=40),
          #rechts
          Wall(Vector2(0,235), width=40, height=250),
          #links
          Wall(Vector2(1040,235), width=40, height=250),
          # Oben links (groß)
          Wall(Vector2(200,90), width=180, height=120),
          # Oben rechts (groß)
          Wall(Vector2(700,90), width=180, height=120),
          # Unten links (groß)
          Wall(Vector2(200,510), width=180, height=120),
          # Unten rechts (groß)
          Wall(Vector2(700,510), width=180, height=120),
          # Obere rechte Ecke
          Wall(Vector2(0,0), width=280, height=40),
          Wall(Vector2(0,0), width=40, height=155),
          # Untere rechte Ecke
          Wall(Vector2(0,565), width=40, height=155),
          Wall(Vector2(0,680), width=280, height=40),
          # Obere linke Ecke
          Wall(Vector2(800,0), width=280, height=40),
          Wall(Vector2(1040,0), width=40, height=155),
          # Untere linke Ecke
          Wall(Vector2(1040,565), width=40, height=155),
          Wall(Vector2(800,680), width=280, height=40),
          # 
        ]
        mB.addObject(*objects)
        self.objects = mB.objects




























"""
class Level1(AbstractLevel):
    def __init__(self) -> None:
        super().__init__(1)
    def make(self):
        mB = MapBuilder()
        objects = [
          Wall(Vector2(), width=5, height=5)
        ]
        mB.addObject(*objects)
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
"""


