from base.core.Level.AbstractLevel import AbstractLevel
from base.core.Level.MapBuilder import MapBuilder
from pygame import Vector2
from base.core.Object.GameObject import GameObject
from base.objects.Enemy import Enemy
from base.objects.Projectile import Projectile
from base.objects.Weapon import Weapon
from objects.Teleporter import Teleporter
from objects.player.Player import Player

from objects.wall import Wall
class Level3(AbstractLevel):
    def __init__(self) -> None:
        super().__init__(3)
    def make(self):
        player = Player().updatePos(Vector2(520, 300))
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
        # -- X-Axis Down
        tp1 = GameObject(Vector2(1060, 490), 20, 78)
        Teleporter(tp1, player, Vector2(21, 490))
        
        tp2 = GameObject(Vector2(0, 490), 20, 78)
        Teleporter(tp2, player, Vector2(1035, 490))

        # -- X-Axis Up
        tp3 = GameObject(Vector2(1060, 160), 20, 78)
        Teleporter(tp3, player, Vector2(21, 160))
        
        tp4 = GameObject(Vector2(0, 160), 20, 78)
        Teleporter(tp4, player, Vector2(1035, 160))

        # -- Y-Axis Right
        tp5 = GameObject(Vector2(720, 0), 80, 20)
        Teleporter(tp5, player, Vector2(750, 674))

        
        tp7 = GameObject(Vector2(720, 700), 80, 20)
        Teleporter(tp7, player, Vector2(750, 26))

        # -- Y-Axis Left
        tp6 = GameObject(Vector2(280, 0), 80, 20)
        Teleporter(tp6, player, Vector2(310, 674))

        tp8 = GameObject(Vector2(280, 700), 80, 20)
        Teleporter(tp8, player, Vector2(310, 26))

        self.add(tp1, tp2, tp3, tp4, tp5, tp6, tp7, tp8)
        self.add(*objects)

        paths = [Vector2(530, 40), Vector2(1000, 350), Vector2(530, 650), Vector2(40, 352)]
        for p in paths:
            enemy = Enemy(p, 25, 25)
            enemy.pathPool = paths
            self.add(enemy)
