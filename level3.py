from base.core.Level.AbstractLevel import AbstractLevel
from base.core.Level.MapBuilder import MapBuilder
from pygame import Vector2
from base.objects.Enemy import Enemy
from base.objects.Projectile import Projectile
from base.objects.Weapon import Weapon
from objects.player.Player import Player

from objects.wall import Wall
class Level3(AbstractLevel):
    def __init__(self) -> None:
        super().__init__(3)
    def make(self):
        mB = MapBuilder()
        player = Player().updatePos(Vector2(100, MapBuilder.centerVec().y - 25))
        projectile = Projectile(range=500, damage=10, speed=20, width=5, height=5, relativePosition=Vector2(75, 3))
        projectile.color = (114, 114, 114)
        weapon = Weapon(player, Vector2(-10, 10), projectile, cooldown=100, munition=50000)
        weapon.color = (29, 191, 172)
        weapon.height = 0
        weapon.width = 0
        weapon.setImage("images/pump.png")
        weapon.setAlias("weapon")

        objects = [
            player, weapon,
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
           
        ]
        mB.addObject(*objects)
        self.objects = mB.objects
        paths = [Vector2(510, 40)]

        for p in paths:
            enemy = Enemy(p, 50, 50)
            enemy.pathPool = paths
            self.objects.append(enemy)
