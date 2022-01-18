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
from objects.Teleporter import Teleporter
from objects.collectables.Ektoplasma import Ektoplasma
from objects.player.Player import Player
from objects.player.Skins import Skins

from objects.wall import Wall

MapBuilder.allowClickMode(lambda x: f"Ektoplasma().hiddenPosUpdate(Vector2({x})),")
class Level3(AbstractLevel):
    def __init__(self) -> None:
        super().__init__(3)
        Events.subscribe("game.tick", self.onTick)
        Events.subscribe("level.loaded", self.onLevelLoad)
        self.highScore = 0
        self.backgroundMusic = Sound("sounds/background.wav", 0.15)
    
    def onLevelLoad(self, e):
        if e.value == self:
            self.startEktoplasma = self.currentEktoplasmaCount()
            Factory.get("Level3.highscore").setText("Highscore:" + str(self.highScore))

    def currentEktoplasmaCount(self):
      return len(list(map(lambda x: isinstance(x, Ektoplasma), self.objects)))

    def onTick(self, e):
        if Game.level() == self:
            collected = self.startEktoplasma - self.currentEktoplasmaCount()
            Factory.get("Level3.counter").setText(str(collected))
            if self.highScore < collected:
                self.highScore = collected
                Factory.get("Level3.highscore").setText("Highscore:" + str(self.highScore))
            if collected >= 516:
                Game.setLevel(4)

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

        Fonts.load("font", "assets/font.ttf", 35)
        Fonts.load("font", "assets/font.ttf", 10)

        text = TextObject(Vector2(810, 5))
        text.color = (3, 173, 63)
        text.setFont("font", 35)
        text.setAlias("Level3.counter")
        text.backgroundColor = (250, 250, 250)
        
        highscore = TextObject(Vector2(925, 5))
        highscore.color = (3, 173, 63)
        highscore.setFont("font", 10)
        highscore.setAlias("Level3.highscore")
        highscore.backgroundColor = (250, 250, 250)

        Skins.apply()
        BackgroundMusic(self.backgroundMusic, False).play()
        self.add(text, highscore)

        paths = [Vector2(530, 40), Vector2(1000, 350), Vector2(530, 650), Vector2(40, 352)]
        for p in paths:
            enemy = Enemy(p, 25, 25)
            enemy.pathPool = paths
            enemy.alertSpeed = 10
            enemy.sleepSpeed = 5
            self.add(enemy)

        ektoplasma = [Ektoplasma().hiddenPosUpdate(Vector2([65, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([80, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([95, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([110, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([125, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([140, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([155, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([170, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([185, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([200, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([215, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([230, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([245, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([260, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([275, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([290, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([305, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([320, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([335, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([350, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([365, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([380, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([395, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([410, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([425, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([440, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([455, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([470, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([485, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([500, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([515, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([530, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([545, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([560, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([575, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([590, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([605, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([620, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([635, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([650, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([665, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([680, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([695, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([710, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([725, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([740, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([755, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([770, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([785, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([800, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([815, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([830, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([845, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([860, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([875, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([890, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([905, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([920, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([935, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([950, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([965, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([980, 65])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 83])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 98])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 113])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 128])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 143])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 158])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 173])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 188])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 203])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 218])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 233])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 248])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 263])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 278])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 293])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 308])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 323])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 338])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 353])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 368])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 383])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 398])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 413])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 428])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 443])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 458])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 473])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 488])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 503])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 518])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 533])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 548])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 563])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 578])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 593])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 608])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 623])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 638])),
Ektoplasma().hiddenPosUpdate(Vector2([67, 653])),
Ektoplasma().hiddenPosUpdate(Vector2([83, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([98, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([113, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([128, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([143, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([158, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([173, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([188, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([203, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([218, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([233, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([248, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([263, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([278, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([293, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([308, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([323, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([338, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([353, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([368, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([383, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([398, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([413, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([428, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([443, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([458, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([473, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([488, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([503, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([518, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([533, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([548, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([563, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([578, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([593, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([608, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([623, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([638, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([653, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([668, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([683, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([698, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([713, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([728, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([743, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([758, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([773, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([788, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([803, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([818, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([833, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([848, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([863, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([878, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([893, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([908, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([923, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([938, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([953, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([968, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([983, 654])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 66])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 81])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 96])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 111])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 126])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 141])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 156])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 171])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 186])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 201])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 216])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 231])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 246])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 261])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 276])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 291])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 306])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 321])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 336])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 351])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 366])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 381])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 396])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 411])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 426])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 441])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 456])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 471])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 486])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 501])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 516])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 531])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 546])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 561])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 576])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 591])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 606])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 621])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 636])),
Ektoplasma().hiddenPosUpdate(Vector2([995, 651])),
Ektoplasma().hiddenPosUpdate(Vector2([105, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([120, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([135, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([150, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([165, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([180, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([195, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([210, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([225, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([240, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([255, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([270, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([285, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([300, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([315, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([330, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([345, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([360, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([375, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([390, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([405, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([420, 236])),
Ektoplasma().hiddenPosUpdate(Vector2([110, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([125, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([140, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([155, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([170, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([185, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([200, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([215, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([230, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([245, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([260, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([275, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([290, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([305, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([320, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([335, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([350, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([365, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([380, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([395, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([410, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([425, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([440, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([455, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([470, 360])),
Ektoplasma().hiddenPosUpdate(Vector2([109, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([139, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([154, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([169, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([184, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([199, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([214, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([229, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([244, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([259, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([274, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([289, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([304, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([319, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([334, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([349, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([364, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([379, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([394, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([409, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([424, 479])),
Ektoplasma().hiddenPosUpdate(Vector2([645, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([675, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([690, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([705, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([720, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([735, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([750, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([765, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([780, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([795, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([810, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([825, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([840, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([855, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([870, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([885, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([900, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([915, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([930, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([945, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([960, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([975, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([594, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([609, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([624, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([639, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([654, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([669, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([684, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([699, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([714, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([729, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([744, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([759, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([774, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([789, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([804, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([819, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([834, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([849, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([864, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([879, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([894, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([909, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([924, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([939, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([954, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([969, 364])),
Ektoplasma().hiddenPosUpdate(Vector2([645, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([675, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([690, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([705, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([720, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([735, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([750, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([765, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([780, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([795, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([810, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([825, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([840, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([855, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([870, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([885, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([900, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([915, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([930, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([945, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([960, 484])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 96])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 111])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 126])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 141])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 156])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 171])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 186])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 201])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 216])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 231])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 246])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 261])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 276])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 291])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 306])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 411])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 426])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 441])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 456])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 471])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 486])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 501])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 516])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 531])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 546])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 561])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 576])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 591])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 606])),
Ektoplasma().hiddenPosUpdate(Vector2([536, 621])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 91])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 106])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 121])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 136])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 151])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 166])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 181])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 196])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 211])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 226])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 241])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 256])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 271])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 286])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 301])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 316])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 331])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 346])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 361])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 376])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 391])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 406])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 421])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 436])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 451])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 466])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 481])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 496])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 511])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 526])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 541])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 556])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 571])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 586])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 601])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 616])),
Ektoplasma().hiddenPosUpdate(Vector2([929, 631])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 99])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 114])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 129])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 144])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 159])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 174])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 189])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 204])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 219])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 234])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 249])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 264])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 279])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 294])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 309])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 324])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 339])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 354])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 369])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 384])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 399])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 414])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 429])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 444])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 459])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 474])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 489])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 504])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 519])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 534])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 549])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 564])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 579])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 594])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 609])),
Ektoplasma().hiddenPosUpdate(Vector2([124, 624])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 93])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 108])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 123])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 138])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 153])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 168])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 183])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 198])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 213])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 228])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 243])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 258])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 273])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 288])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 303])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 318])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 333])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 348])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 363])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 378])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 393])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 408])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 423])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 438])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 453])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 468])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 483])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 498])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 513])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 528])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 543])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 558])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 573])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 588])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 603])),
Ektoplasma().hiddenPosUpdate(Vector2([412, 618])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 103])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 118])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 133])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 148])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 163])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 178])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 193])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 208])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 223])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 238])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 253])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 268])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 283])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 298])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 313])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 328])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 343])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 358])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 373])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 388])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 403])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 418])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 433])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 448])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 463])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 478])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 493])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 508])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 523])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 538])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 553])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 568])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 583])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 598])),
Ektoplasma().hiddenPosUpdate(Vector2([660, 613])),
]
        self.add(*ektoplasma)