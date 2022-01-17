from base.core.Dependencies.Fonts import Fonts
from base.core.Dependencies.Sounds.Sound import Sound
from base.core.Event.Events import Events
from base.core.Game import Game
from base.core.Level.AbstractLevel import AbstractLevel
from base.core.Level.MapBuilder import MapBuilder
from pygame import Vector2
from base.core.Object.Factory import Factory
from base.core.Object.GameObject import GameObject
from base.objects.BackgroundMusic import BackgroundMusic
from base.objects.Enemy import Enemy
from base.objects.Projectile import Projectile
from base.objects.TextObject import TextObject
from base.objects.Weapon import Weapon
from base.objects.Backround import Backround
from objects.Teleporter import Teleporter
from objects.collectables.Ektoplasma import Ektoplasma
from objects.player.Player import Player
from objects.player.Skins import Skins
from objects.wall import Wall
class Level2(AbstractLevel):
    def __init__(self) -> None:
        super().__init__(2)
        Events.subscribe("game.tick", self.onTick)
        Events.subscribe("Level.loaded", self.onLevelLoad)
        self.startEktoplasma = -1
        self.highScore = 0
        self.backgroundSound = Sound("sounds/backgroun2.wav", 0.15)

    
    def currentEktoplasmaCount(self):
      return len(list(map(lambda x: isinstance(x, Ektoplasma), self.objects)))

    def onLevelLoad(self, e):
      if e.value == self:
        self.startEktoplasma = self.currentEktoplasmaCount()
        Factory.get("Level2.highscore").setText("Highscore:" + str(self.highScore))

    def onTick(self, e):
      if Game.level() == self:
        collected = self.startEktoplasma - self.currentEktoplasmaCount()
        Factory.get("Level2.counter").setText(str(collected))
        if self.highScore < collected:
          self.highScore = collected
          Factory.get("Level2.highscore").setText("Highscore:" + str(self.highScore))
        if collected == 346:
          Game.setLevel(4)

    def make(self):
        mB = MapBuilder()
        player = Player().hiddenPosUpdate(Vector2(500, 600))
        projectile = Projectile(range=500, damage=10, speed=20, width=5, height=5, relativePosition=Vector2(75, 3))
        projectile.color = (114, 114, 114)
        weapon = Weapon(player, Vector2(-10, 10), projectile, cooldown=100, munition=50000)
        weapon.color = (29, 191, 172)
        weapon.height = 0
        weapon.width = 0
        weapon.setImage("images/weapon.png")
        weapon.setAlias("weapon")

        enemy = Enemy(Vector2(472, 197), 20, 20, (250, 0, 0))
        enemy.pathPool = [Vector2(130, 411), Vector2(511, 128), Vector2(418, 408)]
        enemy.setAlias("Enemy")

        enemy2 = Enemy(Vector2(472, 264), 20, 20, (250, 0, 0))
        enemy2.pathPool = [Vector2(539, 137), Vector2(889, 392), Vector2(591, 409)]

        teleport1 = GameObject(Vector2(0, 280), 35, 50)
        Teleporter(teleport1, player, Vector2(1027, 287))

        teleport2 = GameObject(Vector2(1053, 280), 35, 50)
        Teleporter(teleport2, player, Vector2(37, 280))
        
        teleport1 = GameObject(Vector2(0, 381), 35, 50)
        Teleporter(teleport1, player, Vector2(1027, 381))

        teleport2 = GameObject(Vector2(1053, 381), 35, 50)
        Teleporter(teleport2, player, Vector2(37, 381))

        Fonts.load("font", "assets/font.ttf", 35)
        Fonts.load("font", "assets/font.ttf", 15)

        BackgroundMusic(self.backgroundSound, False).play()

        text = TextObject(Vector2(700, 0))
        text.color = (3, 173, 63)
        text.setFont("font", 35)
        text.setAlias("Level2.counter")
        
        highscore = TextObject(Vector2(800, 0))
        highscore.color = (3, 173, 63)
        highscore.setFont("font", 15)
        highscore.setAlias("Level2.highscore")

        bg = Backround("images/background.gif")

        Skins.setCurrentSkin(1)
        Skins.apply()

        objects = [
          bg,
        player, enemy, enemy2, text, highscore, weapon, teleport1, teleport2,
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
          Wall(Vector2(790,275), width=25, height=175),

           Ektoplasma().hiddenPosUpdate(Vector2([270, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 214])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 229])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 244])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 259])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 274])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 289])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 304])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 319])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 334])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 349])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 379])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 394])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 409])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 424])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 439])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 454])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 469])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 499])),
Ektoplasma().hiddenPosUpdate(Vector2([34, 301])),
Ektoplasma().hiddenPosUpdate(Vector2([49, 301])),
Ektoplasma().hiddenPosUpdate(Vector2([64, 301])),
Ektoplasma().hiddenPosUpdate(Vector2([79, 301])),
Ektoplasma().hiddenPosUpdate(Vector2([94, 301])),
Ektoplasma().hiddenPosUpdate(Vector2([109, 301])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 301])),
Ektoplasma().hiddenPosUpdate(Vector2([139, 301])),
Ektoplasma().hiddenPosUpdate(Vector2([154, 301])),
Ektoplasma().hiddenPosUpdate(Vector2([169, 301])),
Ektoplasma().hiddenPosUpdate(Vector2([184, 301])),
Ektoplasma().hiddenPosUpdate(Vector2([199, 301])),
Ektoplasma().hiddenPosUpdate(Vector2([214, 301])),
Ektoplasma().hiddenPosUpdate(Vector2([229, 301])),
Ektoplasma().hiddenPosUpdate(Vector2([244, 301])),
Ektoplasma().hiddenPosUpdate(Vector2([166, 253])),
Ektoplasma().hiddenPosUpdate(Vector2([181, 253])),
Ektoplasma().hiddenPosUpdate(Vector2([196, 253])),
Ektoplasma().hiddenPosUpdate(Vector2([211, 253])),
Ektoplasma().hiddenPosUpdate(Vector2([226, 253])),
Ektoplasma().hiddenPosUpdate(Vector2([241, 253])),
Ektoplasma().hiddenPosUpdate(Vector2([200, 268])),
Ektoplasma().hiddenPosUpdate(Vector2([200, 283])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 329])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 344])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 359])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 374])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 389])),
Ektoplasma().hiddenPosUpdate(Vector2([35, 405])),
Ektoplasma().hiddenPosUpdate(Vector2([50, 405])),
Ektoplasma().hiddenPosUpdate(Vector2([65, 405])),
Ektoplasma().hiddenPosUpdate(Vector2([80, 405])),
Ektoplasma().hiddenPosUpdate(Vector2([95, 405])),
Ektoplasma().hiddenPosUpdate(Vector2([110, 405])),
Ektoplasma().hiddenPosUpdate(Vector2([125, 405])),
Ektoplasma().hiddenPosUpdate(Vector2([140, 405])),
Ektoplasma().hiddenPosUpdate(Vector2([155, 405])),
Ektoplasma().hiddenPosUpdate(Vector2([170, 405])),
Ektoplasma().hiddenPosUpdate(Vector2([185, 405])),
Ektoplasma().hiddenPosUpdate(Vector2([200, 405])),
Ektoplasma().hiddenPosUpdate(Vector2([215, 405])),
Ektoplasma().hiddenPosUpdate(Vector2([230, 405])),
Ektoplasma().hiddenPosUpdate(Vector2([245, 405])),
Ektoplasma().hiddenPosUpdate(Vector2([203, 422])),
Ektoplasma().hiddenPosUpdate(Vector2([203, 437])),
Ektoplasma().hiddenPosUpdate(Vector2([167, 455])),
Ektoplasma().hiddenPosUpdate(Vector2([182, 455])),
Ektoplasma().hiddenPosUpdate(Vector2([197, 455])),
Ektoplasma().hiddenPosUpdate(Vector2([212, 455])),
Ektoplasma().hiddenPosUpdate(Vector2([227, 455])),
Ektoplasma().hiddenPosUpdate(Vector2([242, 455])),
 Ektoplasma().hiddenPosUpdate(Vector2([271, 514])),
Ektoplasma().hiddenPosUpdate(Vector2([284, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([299, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([314, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([329, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([344, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([359, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([374, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([389, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([404, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([419, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([434, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([449, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([464, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([479, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([494, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([509, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([524, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([539, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([554, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([569, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([584, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([599, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([614, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([629, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([644, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([286, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([301, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([316, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([331, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([346, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([361, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([376, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([391, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([406, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([421, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([436, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([451, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([466, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([481, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([496, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([511, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([526, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([541, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([556, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([571, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([586, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([601, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([616, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([631, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([646, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([661, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([676, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([691, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([706, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([721, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([736, 199])),
Ektoplasma().hiddenPosUpdate(Vector2([382, 152])),
Ektoplasma().hiddenPosUpdate(Vector2([397, 152])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 152])),
Ektoplasma().hiddenPosUpdate(Vector2([427, 152])),
Ektoplasma().hiddenPosUpdate(Vector2([442, 152])),
Ektoplasma().hiddenPosUpdate(Vector2([457, 152])),
Ektoplasma().hiddenPosUpdate(Vector2([472, 152])),
Ektoplasma().hiddenPosUpdate(Vector2([487, 152])),
Ektoplasma().hiddenPosUpdate(Vector2([502, 152])),
Ektoplasma().hiddenPosUpdate(Vector2([517, 152])),
Ektoplasma().hiddenPosUpdate(Vector2([658, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([673, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([688, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([703, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([718, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([733, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([748, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 210])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 225])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 240])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 255])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 270])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 285])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 300])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 315])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 330])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 345])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 375])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 390])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 405])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 420])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 435])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 450])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 465])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 480])),
Ektoplasma().hiddenPosUpdate(Vector2([709, 495])),
Ektoplasma().hiddenPosUpdate(Vector2([384, 164])),
Ektoplasma().hiddenPosUpdate(Vector2([384, 179])),
Ektoplasma().hiddenPosUpdate(Vector2([531, 153])),
Ektoplasma().hiddenPosUpdate(Vector2([546, 153])),
Ektoplasma().hiddenPosUpdate(Vector2([561, 153])),
Ektoplasma().hiddenPosUpdate(Vector2([576, 153])),
Ektoplasma().hiddenPosUpdate(Vector2([591, 153])),
Ektoplasma().hiddenPosUpdate(Vector2([606, 153])),
Ektoplasma().hiddenPosUpdate(Vector2([621, 153])),
Ektoplasma().hiddenPosUpdate(Vector2([636, 153])),
Ektoplasma().hiddenPosUpdate(Vector2([638, 165])),
Ektoplasma().hiddenPosUpdate(Vector2([638, 180])),
Ektoplasma().hiddenPosUpdate(Vector2([504, 139])),
Ektoplasma().hiddenPosUpdate(Vector2([504, 124])),
Ektoplasma().hiddenPosUpdate(Vector2([468, 97])),
Ektoplasma().hiddenPosUpdate(Vector2([483, 97])),
Ektoplasma().hiddenPosUpdate(Vector2([498, 97])),
Ektoplasma().hiddenPosUpdate(Vector2([513, 97])),
Ektoplasma().hiddenPosUpdate(Vector2([528, 97])),
Ektoplasma().hiddenPosUpdate(Vector2([543, 97])),
Ektoplasma().hiddenPosUpdate(Vector2([408, 530])),
Ektoplasma().hiddenPosUpdate(Vector2([408, 545])),
Ektoplasma().hiddenPosUpdate(Vector2([423, 548])),
Ektoplasma().hiddenPosUpdate(Vector2([438, 548])),
Ektoplasma().hiddenPosUpdate(Vector2([453, 548])),
Ektoplasma().hiddenPosUpdate(Vector2([468, 548])),
Ektoplasma().hiddenPosUpdate(Vector2([483, 548])),
Ektoplasma().hiddenPosUpdate(Vector2([498, 548])),
Ektoplasma().hiddenPosUpdate(Vector2([513, 548])),
Ektoplasma().hiddenPosUpdate(Vector2([528, 548])),
Ektoplasma().hiddenPosUpdate(Vector2([543, 548])),
Ektoplasma().hiddenPosUpdate(Vector2([558, 548])),
Ektoplasma().hiddenPosUpdate(Vector2([573, 548])),
Ektoplasma().hiddenPosUpdate(Vector2([588, 548])),
Ektoplasma().hiddenPosUpdate(Vector2([595, 529])),
Ektoplasma().hiddenPosUpdate(Vector2([507, 563])),
Ektoplasma().hiddenPosUpdate(Vector2([507, 578])),
Ektoplasma().hiddenPosUpdate(Vector2([507, 593])),
Ektoplasma().hiddenPosUpdate(Vector2([507, 608])),
Ektoplasma().hiddenPosUpdate(Vector2([729, 252])),
Ektoplasma().hiddenPosUpdate(Vector2([744, 252])),
Ektoplasma().hiddenPosUpdate(Vector2([759, 252])),
Ektoplasma().hiddenPosUpdate(Vector2([774, 252])),
Ektoplasma().hiddenPosUpdate(Vector2([789, 252])),
Ektoplasma().hiddenPosUpdate(Vector2([804, 252])),
Ektoplasma().hiddenPosUpdate(Vector2([819, 252])),
Ektoplasma().hiddenPosUpdate(Vector2([834, 252])),
Ektoplasma().hiddenPosUpdate(Vector2([769, 266])),
Ektoplasma().hiddenPosUpdate(Vector2([769, 281])),
Ektoplasma().hiddenPosUpdate(Vector2([769, 296])),
Ektoplasma().hiddenPosUpdate(Vector2([769, 311])),
Ektoplasma().hiddenPosUpdate(Vector2([769, 326])),
Ektoplasma().hiddenPosUpdate(Vector2([769, 341])),
Ektoplasma().hiddenPosUpdate(Vector2([769, 356])),
Ektoplasma().hiddenPosUpdate(Vector2([769, 371])),
Ektoplasma().hiddenPosUpdate(Vector2([769, 386])),
Ektoplasma().hiddenPosUpdate(Vector2([769, 401])),
Ektoplasma().hiddenPosUpdate(Vector2([769, 416])),
Ektoplasma().hiddenPosUpdate(Vector2([769, 431])),
Ektoplasma().hiddenPosUpdate(Vector2([720, 459])),
Ektoplasma().hiddenPosUpdate(Vector2([735, 459])),
Ektoplasma().hiddenPosUpdate(Vector2([750, 459])),
Ektoplasma().hiddenPosUpdate(Vector2([765, 459])),
Ektoplasma().hiddenPosUpdate(Vector2([780, 459])),
Ektoplasma().hiddenPosUpdate(Vector2([795, 459])),
Ektoplasma().hiddenPosUpdate(Vector2([810, 459])),
Ektoplasma().hiddenPosUpdate(Vector2([825, 459])),
Ektoplasma().hiddenPosUpdate(Vector2([840, 459])),
Ektoplasma().hiddenPosUpdate(Vector2([837, 275])),
Ektoplasma().hiddenPosUpdate(Vector2([837, 290])),
Ektoplasma().hiddenPosUpdate(Vector2([837, 305])),
Ektoplasma().hiddenPosUpdate(Vector2([837, 320])),
Ektoplasma().hiddenPosUpdate(Vector2([837, 335])),
Ektoplasma().hiddenPosUpdate(Vector2([837, 350])),
Ektoplasma().hiddenPosUpdate(Vector2([837, 365])),
Ektoplasma().hiddenPosUpdate(Vector2([837, 380])),
Ektoplasma().hiddenPosUpdate(Vector2([837, 395])),
Ektoplasma().hiddenPosUpdate(Vector2([837, 410])),
Ektoplasma().hiddenPosUpdate(Vector2([837, 425])),
Ektoplasma().hiddenPosUpdate(Vector2([860, 299])),
Ektoplasma().hiddenPosUpdate(Vector2([875, 299])),
Ektoplasma().hiddenPosUpdate(Vector2([890, 299])),
Ektoplasma().hiddenPosUpdate(Vector2([905, 299])),
Ektoplasma().hiddenPosUpdate(Vector2([920, 299])),
Ektoplasma().hiddenPosUpdate(Vector2([935, 299])),
Ektoplasma().hiddenPosUpdate(Vector2([950, 299])),
Ektoplasma().hiddenPosUpdate(Vector2([965, 299])),
Ektoplasma().hiddenPosUpdate(Vector2([980, 299])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 299])),
Ektoplasma().hiddenPosUpdate(Vector2([1010, 299])),
Ektoplasma().hiddenPosUpdate(Vector2([1025, 299])),
Ektoplasma().hiddenPosUpdate(Vector2([1040, 299])),
Ektoplasma().hiddenPosUpdate(Vector2([863, 402])),
Ektoplasma().hiddenPosUpdate(Vector2([878, 402])),
Ektoplasma().hiddenPosUpdate(Vector2([893, 402])),
Ektoplasma().hiddenPosUpdate(Vector2([908, 402])),
Ektoplasma().hiddenPosUpdate(Vector2([923, 402])),
Ektoplasma().hiddenPosUpdate(Vector2([938, 402])),
Ektoplasma().hiddenPosUpdate(Vector2([953, 402])),
Ektoplasma().hiddenPosUpdate(Vector2([968, 402])),
Ektoplasma().hiddenPosUpdate(Vector2([983, 402])),
Ektoplasma().hiddenPosUpdate(Vector2([998, 402])),
Ektoplasma().hiddenPosUpdate(Vector2([1013, 402])),
Ektoplasma().hiddenPosUpdate(Vector2([1028, 402])),
Ektoplasma().hiddenPosUpdate(Vector2([1043, 402])),
Ektoplasma().hiddenPosUpdate(Vector2([984, 326])),
Ektoplasma().hiddenPosUpdate(Vector2([984, 341])),
Ektoplasma().hiddenPosUpdate(Vector2([984, 356])),
Ektoplasma().hiddenPosUpdate(Vector2([984, 371])),
Ektoplasma().hiddenPosUpdate(Vector2([486, 240])),
Ektoplasma().hiddenPosUpdate(Vector2([501, 240])),
Ektoplasma().hiddenPosUpdate(Vector2([516, 240])),
Ektoplasma().hiddenPosUpdate(Vector2([531, 240])),
Ektoplasma().hiddenPosUpdate(Vector2([546, 240])),
Ektoplasma().hiddenPosUpdate(Vector2([657, 240])),
Ektoplasma().hiddenPosUpdate(Vector2([672, 240])),
Ektoplasma().hiddenPosUpdate(Vector2([687, 240])),
Ektoplasma().hiddenPosUpdate(Vector2([676, 256])),
Ektoplasma().hiddenPosUpdate(Vector2([676, 271])),
Ektoplasma().hiddenPosUpdate(Vector2([676, 286])),
Ektoplasma().hiddenPosUpdate(Vector2([681, 420])),
Ektoplasma().hiddenPosUpdate(Vector2([681, 435])),
Ektoplasma().hiddenPosUpdate(Vector2([681, 450])),
Ektoplasma().hiddenPosUpdate(Vector2([681, 465])),
Ektoplasma().hiddenPosUpdate(Vector2([681, 480])),
Ektoplasma().hiddenPosUpdate(Vector2([686, 498])),
Ektoplasma().hiddenPosUpdate(Vector2([671, 498])),
Ektoplasma().hiddenPosUpdate(Vector2([656, 498])),
Ektoplasma().hiddenPosUpdate(Vector2([641, 498])),
Ektoplasma().hiddenPosUpdate(Vector2([626, 498])),
Ektoplasma().hiddenPosUpdate(Vector2([611, 498])),
Ektoplasma().hiddenPosUpdate(Vector2([390, 240])),
Ektoplasma().hiddenPosUpdate(Vector2([375, 240])),
Ektoplasma().hiddenPosUpdate(Vector2([360, 242])),
Ektoplasma().hiddenPosUpdate(Vector2([360, 257])),
Ektoplasma().hiddenPosUpdate(Vector2([360, 272])),
Ektoplasma().hiddenPosUpdate(Vector2([360, 287])),
Ektoplasma().hiddenPosUpdate(Vector2([360, 415])),
Ektoplasma().hiddenPosUpdate(Vector2([360, 430])),
Ektoplasma().hiddenPosUpdate(Vector2([362, 445])),
Ektoplasma().hiddenPosUpdate(Vector2([362, 460])),
Ektoplasma().hiddenPosUpdate(Vector2([362, 475])),
Ektoplasma().hiddenPosUpdate(Vector2([362, 490])),
Ektoplasma().hiddenPosUpdate(Vector2([431, 504])),
Ektoplasma().hiddenPosUpdate(Vector2([416, 504])),
Ektoplasma().hiddenPosUpdate(Vector2([401, 504])),
Ektoplasma().hiddenPosUpdate(Vector2([386, 504])),
Ektoplasma().hiddenPosUpdate(Vector2([371, 504])),
Ektoplasma().hiddenPosUpdate(Vector2([402, 286])),
Ektoplasma().hiddenPosUpdate(Vector2([417, 286])),
Ektoplasma().hiddenPosUpdate(Vector2([432, 286])),
Ektoplasma().hiddenPosUpdate(Vector2([403, 302])),
Ektoplasma().hiddenPosUpdate(Vector2([418, 302])),
Ektoplasma().hiddenPosUpdate(Vector2([433, 302])),
Ektoplasma().hiddenPosUpdate(Vector2([403, 320])),
Ektoplasma().hiddenPosUpdate(Vector2([418, 320])),
Ektoplasma().hiddenPosUpdate(Vector2([433, 320])),
Ektoplasma().hiddenPosUpdate(Vector2([576, 291])),
Ektoplasma().hiddenPosUpdate(Vector2([591, 291])),
Ektoplasma().hiddenPosUpdate(Vector2([606, 291])),
Ektoplasma().hiddenPosUpdate(Vector2([578, 311])),
Ektoplasma().hiddenPosUpdate(Vector2([593, 311])),
Ektoplasma().hiddenPosUpdate(Vector2([608, 311])),Ektoplasma().hiddenPosUpdate(Vector2([578, 327])),
Ektoplasma().hiddenPosUpdate(Vector2([593, 327])),
Ektoplasma().hiddenPosUpdate(Vector2([608, 327])),
Ektoplasma().hiddenPosUpdate(Vector2([420, 346])),
Ektoplasma().hiddenPosUpdate(Vector2([420, 361])),
Ektoplasma().hiddenPosUpdate(Vector2([420, 376])),
Ektoplasma().hiddenPosUpdate(Vector2([420, 391])),
Ektoplasma().hiddenPosUpdate(Vector2([436, 390])),
Ektoplasma().hiddenPosUpdate(Vector2([451, 390])),
Ektoplasma().hiddenPosUpdate(Vector2([466, 390])),
Ektoplasma().hiddenPosUpdate(Vector2([597, 344])),
Ektoplasma().hiddenPosUpdate(Vector2([597, 359])),
Ektoplasma().hiddenPosUpdate(Vector2([597, 374])),
Ektoplasma().hiddenPosUpdate(Vector2([597, 389])),
Ektoplasma().hiddenPosUpdate(Vector2([587, 391])),
Ektoplasma().hiddenPosUpdate(Vector2([572, 391])),
Ektoplasma().hiddenPosUpdate(Vector2([557, 391])),




          ]
        
        
        
        
        
        
        
        
        
        
        
        mB.addObject(*objects)
        self.set(*mB.objects)