from pygame import Vector2
from base.core.Dependencies.Rendering.Layer import Layer
from base.core.Level.AbstractLevel import AbstractLevel
from base.core.Level.MapBuilder import MapBuilder
from base.objects.Enemy import Enemy
from base.objects.Projectile import Projectile
from base.objects.TextObject import TextObject
from base.objects.Weapon import Weapon
from objects.collectables.Ektoplasma import Ektoplasma
from objects.player.Player import Player
from objects.wall import Wall

class Level1(AbstractLevel):
  def __init__(self) -> None:
    super().__init__(1)

  def make(self):
    mB = MapBuilder()

    mirrorObjects = [
      Wall(Vector2(10, 10), width=50, height=50),
      Wall(Vector2(10, 200), width=50, height=50),
      # Ektoplasma().hiddenPosUpdate(MapBuilder.centerVec())
    ]

    # mB.pointMirror(MapBuilder.centerVec(), mirrorObjects)
    
    player = Player().hiddenPosUpdate(Vector2(200, 200))
    # enemy = Enemy(Vector2(300, 300), 50, 50, (250, 0, 0))
    # enemy.pathPool = [Vector2(400, 400), Vector2(500, 100), Vector2(200, 500)]

    # projectile = Projectile(range=500, damage=10, speed=20, width=5, height=5, relativePosition=Vector2(75, 3))
    # projectile.color = (114, 114, 114)
    # weapon = Weapon(player, Vector2(-10, 10), projectile, cooldown=100, munition=50000)
    # weapon.color = (29, 191, 172)
    # weapon.height = 0
    # weapon.width = 0
    # weapon.setImage("images/pump.png")
    # weapon.setAlias("weapon")

    ektoplasma = Ektoplasma().hiddenPosUpdate(MapBuilder.centerVec())
    
    mB.addObject(player, ektoplasma)
    mB.addObject(*mirrorObjects)
    Layer.addToMultiple(0, 3, [mirrorObjects, [ektoplasma], [player]])
    self.add(*mB.objects)
