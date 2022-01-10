from pygame import Vector2, Vector3
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
          Wall(Vector2(505,310), width=25, height=50),Wall(Vector2(460,30), width=100, height=50),
          Wall(Vector2(560,80), width=100, height=50),Wall(Vector2(360,80), width=100, height=50),
          Wall(Vector2(260,130), width=100, height=50),Wall(Vector2(660,130), width=100, height=50),
          Wall(Vector2(760,180), width=100, height=50),Wall(Vector2(860,230), width=225, height=50),
          Wall(Vector2(860,330), width=100, height=50),Wall(Vector2(1016,330), width=60, height=50),
          Wall(Vector2(860,430), width=225, height=50),Wall(Vector2(460,630), width=100, height=50),
          Wall(Vector2(360,580), width=100, height=50),Wall(Vector2(560,580), width=100, height=50),
          Wall(Vector2(660,530), width=100, height=50),Wall(Vector2(760,480), width=100, height=50),
          Wall(Vector2(260,530), width=100, height=50),Wall(Vector2(160,480), width=100, height=50),
          Wall(Vector2(150,330), width=100, height=50),Wall(Vector2(160,180), width=100, height=50),
          Wall(Vector2(0,230), width=160, height=50),Wall(Vector2(0,330), width=100, height=50),
          Wall(Vector2(0,430), width=160, height=50),Wall(Vector2(415,430), width=200, height=25),
          Wall(Vector2(400,230), width=75, height=25),Wall(Vector2(570,230), width=75, height=25),
          Wall(Vector2(440,500), width=150, height=15),Wall(Vector2(440,175), width=150, height=15),
          Wall(Vector2(290,285), width=25, height=150),Wall(Vector2(730,285), width=25, height=150),
          Wall(Vector2(350,310), width=25, height=100),Wall(Vector2(670,310), width=25, height=100),
          Wall(Vector2(790,275), width=25, height=175),Ektoplasma().updatePos(Vector2(20,300)),
          Ektoplasma().updatePos(Vector2(3,300)),Ektoplasma().updatePos(Vector2(40,300)),
          Ektoplasma().updatePos(Vector2(20,300)),Ektoplasma().updatePos(Vector2(60,300)),
          Ektoplasma().updatePos(Vector2(80,300)),Ektoplasma().updatePos(Vector2(100,300)),
          Ektoplasma().updatePos(Vector2(120,300)),Ektoplasma().updatePos(Vector2(140,300)),
         Ektoplasma().updatePos(Vector2(120,320)),Ektoplasma().updatePos(Vector2(120,340)),
          Ektoplasma().updatePos(Vector2(120,360)),Ektoplasma().updatePos(Vector2(120,380)),
          Ektoplasma().updatePos(Vector2(120,400)),Ektoplasma().updatePos(Vector2(100,400)),
          Ektoplasma().updatePos(Vector2(80,400)),Ektoplasma().updatePos(Vector2(60,400)),
          Ektoplasma().updatePos(Vector2(40,400)),Ektoplasma().updatePos(Vector2(20,400)),
          Ektoplasma().updatePos(Vector2(3,400)),Ektoplasma().updatePos(Vector2(140,400)),
          Ektoplasma().updatePos(Vector2(160,400)),Ektoplasma().updatePos(Vector2(180,400)),
          Ektoplasma().updatePos(Vector2(200,400)),Ektoplasma().updatePos(Vector2(220,400)),
          Ektoplasma().updatePos(Vector2(240,400)),Ektoplasma().updatePos(Vector2(260,400)),
          Ektoplasma().updatePos(Vector2(120,200)),
         Ektoplasma().updatePos(Vector2(160,300)),Ektoplasma().updatePos(Vector2(180,300)),
          Ektoplasma().updatePos(Vector2(200,300)),Ektoplasma().updatePos(Vector2(220,300)),
          Ektoplasma().updatePos(Vector2(240,300)),Ektoplasma().updatePos(Vector2(260,300)),
          Ektoplasma().updatePos(Vector2(260,320)),Ektoplasma().updatePos(Vector2(260,340)),
          Ektoplasma().updatePos(Vector2(260,360)),Ektoplasma().updatePos(Vector2(260,380)),
          Ektoplasma().updatePos(Vector2(260,400)),Ektoplasma().updatePos(Vector2(260,420)),
          Ektoplasma().updatePos(Vector2(260,440)),Ektoplasma().updatePos(Vector2(260,460)),
          Ektoplasma().updatePos(Vector2(270,480)),Ektoplasma().updatePos(Vector2(270,500)),
          Ektoplasma().updatePos(Vector2(270,520))

          ]
        
        
        
        
        
        
        
        
        
        
        
        mB.addObject(*objects)
        mB.addObject(Player().updatePos(Vector2(490,370)))
        self.objects = mB.objects

#Ektoplasma().updatePos(mB.centerVec()),
 #         Ektoplasma().updatePos(Vector2(400,300)),