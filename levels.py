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

<<<<<<< Updated upstream
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
=======

#class Level1(AbstractLevel):
 #   def __init__(self) -> None:
  #      super().__init__(1)
   # def make(self):
    #    mB = MapBuilder()
#
 #       mirrorObjects = [
  #        Wall(Vector2(10, 10), width=50, height=50),
   #       Wall(Vector2(10, 200), width=50, height=50),
    #      Ektoplasma().updatePos(mB.centerVec())
        

        
        #mB.pointMirror(mB.centerVec(), mirrorObjects)

        # objects = [
        #   Wall(Vector2(), width=5, height=5)
        # ]
        # enemy = Enemy(Vector2(300, 300), 50, 50, (250, 0, 0))
        # enemy.pathPool = [Vector2(400, 400), Vector2(500, 100), Vector2(200, 500)]
        # enemy.setAlias("Enemy")
        
        #mB.addObject(Player().updatePos(Vector2(200, 200)))
        #mB.addObject(*mirrorObjects)
        #self.objects = mB.objects

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

MapBuilder.allowClickMode(lambda x: f"Ektoplasma().updatePos(Vector2({x})),")

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
          Wall(Vector2(790,275), width=25, height=175),

          Ektoplasma().updatePos(Vector2((483, 609))),
Ektoplasma().updatePos(Vector2((502, 607))), Ektoplasma().updatePos(Vector2((555, 294))),
Ektoplasma().updatePos(Vector2((582, 287))),
Ektoplasma().updatePos(Vector2((604, 280))),
Ektoplasma().updatePos(Vector2((626, 289))),
Ektoplasma().updatePos(Vector2((634, 302))),
Ektoplasma().updatePos(Vector2((635, 314))),
Ektoplasma().updatePos(Vector2((615, 318))),
Ektoplasma().updatePos(Vector2((603, 317))),
Ektoplasma().updatePos(Vector2((592, 314))),
Ektoplasma().updatePos(Vector2((564, 328))),
Ektoplasma().updatePos(Vector2((562, 346))),
Ektoplasma().updatePos(Vector2((561, 363))),
Ektoplasma().updatePos(Vector2((584, 355))),
Ektoplasma().updatePos(Vector2((614, 345))),
Ektoplasma().updatePos(Vector2((638, 359))),
Ektoplasma().updatePos(Vector2((635, 377))),
Ektoplasma().updatePos(Vector2((621, 389))),
Ektoplasma().updatePos(Vector2((588, 397))),
Ektoplasma().updatePos(Vector2((577, 404))),
Ektoplasma().updatePos(Vector2((590, 398))),
Ektoplasma().updatePos(Vector2((626, 393))),
Ektoplasma().updatePos(Vector2((637, 407))),
Ektoplasma().updatePos(Vector2((640, 415))),
Ektoplasma().updatePos(Vector2((644, 455))),
Ektoplasma().updatePos(Vector2((653, 464))),
Ektoplasma().updatePos(Vector2((670, 449))),
Ektoplasma().updatePos(Vector2((681, 448))),
Ektoplasma().updatePos(Vector2((697, 465))),
Ektoplasma().updatePos(Vector2((470, 554))),
Ektoplasma().updatePos(Vector2((452, 550))),
Ektoplasma().updatePos(Vector2((448, 548))),
Ektoplasma().updatePos(Vector2((430, 547))),
Ektoplasma().updatePos(Vector2((412, 556))),
Ektoplasma().updatePos(Vector2((399, 555))),
Ektoplasma().updatePos(Vector2((379, 550))),
Ektoplasma().updatePos(Vector2((388, 538))),
Ektoplasma().updatePos(Vector2((435, 538))),
Ektoplasma().updatePos(Vector2((442, 538))),
Ektoplasma().updatePos(Vector2((376, 515))),
Ektoplasma().updatePos(Vector2((371, 507))),
Ektoplasma().updatePos(Vector2((356, 496))),
Ektoplasma().updatePos(Vector2((341, 480))),
Ektoplasma().updatePos(Vector2((339, 473))),
Ektoplasma().updatePos(Vector2((316, 470))),
Ektoplasma().updatePos(Vector2((294, 466))),
Ektoplasma().updatePos(Vector2((287, 463))),
Ektoplasma().updatePos(Vector2((262, 461))),
Ektoplasma().updatePos(Vector2((245, 458))),
Ektoplasma().updatePos(Vector2((239, 452))),
Ektoplasma().updatePos(Vector2((246, 416))),
Ektoplasma().updatePos(Vector2((265, 417))),
Ektoplasma().updatePos(Vector2((228, 419))),
Ektoplasma().updatePos(Vector2((218, 417))),
Ektoplasma().updatePos(Vector2((248, 401))),
Ektoplasma().updatePos(Vector2((260, 398))),
Ektoplasma().updatePos(Vector2((263, 394))),
Ektoplasma().updatePos(Vector2((271, 379))),
Ektoplasma().updatePos(Vector2((270, 370))),
Ektoplasma().updatePos(Vector2((272, 361))),
Ektoplasma().updatePos(Vector2((272, 348))),
Ektoplasma().updatePos(Vector2((271, 336))),
Ektoplasma().updatePos(Vector2((269, 329))),
Ektoplasma().updatePos(Vector2((269, 319))),
Ektoplasma().updatePos(Vector2((270, 308))),
Ektoplasma().updatePos(Vector2((271, 302))),
Ektoplasma().updatePos(Vector2((274, 292))),
Ektoplasma().updatePos(Vector2((274, 284))),
Ektoplasma().updatePos(Vector2((273, 259))),
Ektoplasma().updatePos(Vector2((278, 240))),
Ektoplasma().updatePos(Vector2((284, 218))),
Ektoplasma().updatePos(Vector2((292, 219))),
Ektoplasma().updatePos(Vector2((302, 209))),
Ektoplasma().updatePos(Vector2((312, 209))),
Ektoplasma().updatePos(Vector2((322, 221))),
Ektoplasma().updatePos(Vector2((347, 230))),
Ektoplasma().updatePos(Vector2((359, 237))),
Ektoplasma().updatePos(Vector2((378, 165))),
Ektoplasma().updatePos(Vector2((386, 155))),
Ektoplasma().updatePos(Vector2((405, 155))),
Ektoplasma().updatePos(Vector2((421, 157))),
Ektoplasma().updatePos(Vector2((425, 158))),
Ektoplasma().updatePos(Vector2((479, 113))),
Ektoplasma().updatePos(Vector2((484, 107))),
Ektoplasma().updatePos(Vector2((491, 104))),
Ektoplasma().updatePos(Vector2((510, 101))),
Ektoplasma().updatePos(Vector2((521, 101))),
Ektoplasma().updatePos(Vector2((535, 113))),
Ektoplasma().updatePos(Vector2((536, 116))),

Ektoplasma().updatePos(Vector2((530, 611))),
Ektoplasma().updatePos(Vector2((536, 591))),
Ektoplasma().updatePos(Vector2((515, 586))),
Ektoplasma().updatePos(Vector2((484, 579))),
Ektoplasma().updatePos(Vector2((480, 565))),
Ektoplasma().updatePos(Vector2((480, 537))),
Ektoplasma().updatePos(Vector2((485, 534))),
Ektoplasma().updatePos(Vector2((503, 543))),
Ektoplasma().updatePos(Vector2((513, 560))),
Ektoplasma().updatePos(Vector2((521, 545))),
Ektoplasma().updatePos(Vector2((534, 539))),
Ektoplasma().updatePos(Vector2((542, 557))),
Ektoplasma().updatePos(Vector2((562, 540))),
Ektoplasma().updatePos(Vector2((567, 558))),
Ektoplasma().updatePos(Vector2((566, 529))),
Ektoplasma().updatePos(Vector2((578, 553))),
Ektoplasma().updatePos(Vector2((589, 528))),
Ektoplasma().updatePos(Vector2((600, 560))),
Ektoplasma().updatePos(Vector2((619, 539))),
Ektoplasma().updatePos(Vector2((624, 555))),
Ektoplasma().updatePos(Vector2((614, 519))),
Ektoplasma().updatePos(Vector2((611, 505))),
Ektoplasma().updatePos(Vector2((646, 499))),
Ektoplasma().updatePos(Vector2((691, 504))),
Ektoplasma().updatePos(Vector2((735, 495))),
Ektoplasma().updatePos(Vector2((707, 474))),
Ektoplasma().updatePos(Vector2((670, 475))),
Ektoplasma().updatePos(Vector2((644, 479))),
Ektoplasma().updatePos(Vector2((629, 483))),
Ektoplasma().updatePos(Vector2((616, 478))),
Ektoplasma().updatePos(Vector2((587, 473))),
Ektoplasma().updatePos(Vector2((569, 471))),
Ektoplasma().updatePos(Vector2((553, 471))),
Ektoplasma().updatePos(Vector2((535, 471))),
Ektoplasma().updatePos(Vector2((492, 471))),
Ektoplasma().updatePos(Vector2((460, 475))),
Ektoplasma().updatePos(Vector2((439, 478))),
Ektoplasma().updatePos(Vector2((407, 478))),
Ektoplasma().updatePos(Vector2((403, 482))),
Ektoplasma().updatePos(Vector2((403, 504))),
Ektoplasma().updatePos(Vector2((384, 501))),
Ektoplasma().updatePos(Vector2((383, 460))),
Ektoplasma().updatePos(Vector2((369, 470))),
Ektoplasma().updatePos(Vector2((329, 491))),
Ektoplasma().updatePos(Vector2((310, 495))),
Ektoplasma().updatePos(Vector2((294, 495))),
Ektoplasma().updatePos(Vector2((282, 489))),
Ektoplasma().updatePos(Vector2((287, 473))),
Ektoplasma().updatePos(Vector2((308, 466))),
Ektoplasma().updatePos(Vector2((347, 458))),
Ektoplasma().updatePos(Vector2((344, 448))),
Ektoplasma().updatePos(Vector2((340, 436))),
Ektoplasma().updatePos(Vector2((338, 418))),
Ektoplasma().updatePos(Vector2((335, 402))),
Ektoplasma().updatePos(Vector2((335, 397))),
Ektoplasma().updatePos(Vector2((335, 386))),
Ektoplasma().updatePos(Vector2((338, 369))),
Ektoplasma().updatePos(Vector2((340, 342))),
Ektoplasma().updatePos(Vector2((337, 324))),
Ektoplasma().updatePos(Vector2((331, 292))),
Ektoplasma().updatePos(Vector2((329, 264))),
Ektoplasma().updatePos(Vector2((323, 234))),
Ektoplasma().updatePos(Vector2((299, 236))),
Ektoplasma().updatePos(Vector2((291, 242))),
Ektoplasma().updatePos(Vector2((251, 257))),
Ektoplasma().updatePos(Vector2((203, 255))),
Ektoplasma().updatePos(Vector2((189, 251))),
Ektoplasma().updatePos(Vector2((190, 260))),
Ektoplasma().updatePos(Vector2((181, 277))),
Ektoplasma().updatePos(Vector2((187, 291))),
Ektoplasma().updatePos(Vector2((215, 284))),
Ektoplasma().updatePos(Vector2((242, 282))),
Ektoplasma().updatePos(Vector2((239, 296))),
Ektoplasma().updatePos(Vector2((195, 294))),
Ektoplasma().updatePos(Vector2((154, 297))),
Ektoplasma().updatePos(Vector2((125, 300))),
Ektoplasma().updatePos(Vector2((105, 300))),
Ektoplasma().updatePos(Vector2((57, 300))),
Ektoplasma().updatePos(Vector2((37, 302))),
Ektoplasma().updatePos(Vector2((16, 300))),
Ektoplasma().updatePos(Vector2((11, 295))),
Ektoplasma().updatePos(Vector2((45, 286))),
Ektoplasma().updatePos(Vector2((73, 292))),
Ektoplasma().updatePos(Vector2((101, 300))),
Ektoplasma().updatePos(Vector2((130, 307))),
Ektoplasma().updatePos(Vector2((126, 326))),
Ektoplasma().updatePos(Vector2((127, 350))),
Ektoplasma().updatePos(Vector2((126, 362))),
Ektoplasma().updatePos(Vector2((124, 376))),
Ektoplasma().updatePos(Vector2((116, 387))),
Ektoplasma().updatePos(Vector2((35, 402))),
Ektoplasma().updatePos(Vector2((18, 402))),
Ektoplasma().updatePos(Vector2((29, 393))),
Ektoplasma().updatePos(Vector2((59, 389))),
Ektoplasma().updatePos(Vector2((88, 397))),
Ektoplasma().updatePos(Vector2((130, 397))),
Ektoplasma().updatePos(Vector2((158, 397))),
Ektoplasma().updatePos(Vector2((180, 402))),
Ektoplasma().updatePos(Vector2((188, 419))),
Ektoplasma().updatePos(Vector2((182, 441))),
Ektoplasma().updatePos(Vector2((187, 450))),
Ektoplasma().updatePos(Vector2((288, 220))),
Ektoplasma().updatePos(Vector2((299, 214))),
Ektoplasma().updatePos(Vector2((334, 243))),
Ektoplasma().updatePos(Vector2((314, 255))),
Ektoplasma().updatePos(Vector2((306, 238))),
Ektoplasma().updatePos(Vector2((355, 202))),
Ektoplasma().updatePos(Vector2((350, 249))),
Ektoplasma().updatePos(Vector2((338, 276))),
Ektoplasma().updatePos(Vector2((347, 279))),
Ektoplasma().updatePos(Vector2((371, 270))),
Ektoplasma().updatePos(Vector2((401, 293))),
Ektoplasma().updatePos(Vector2((422, 303))),
Ektoplasma().updatePos(Vector2((447, 303))),
Ektoplasma().updatePos(Vector2((484, 282))),
Ektoplasma().updatePos(Vector2((506, 259))),
Ektoplasma().updatePos(Vector2((518, 240))),
Ektoplasma().updatePos(Vector2((503, 208))),
Ektoplasma().updatePos(Vector2((467, 204))),
Ektoplasma().updatePos(Vector2((440, 207))),
Ektoplasma().updatePos(Vector2((409, 208))),
Ektoplasma().updatePos(Vector2((401, 185))),
Ektoplasma().updatePos(Vector2((410, 168))),
Ektoplasma().updatePos(Vector2((436, 150))),
Ektoplasma().updatePos(Vector2((461, 139))),
Ektoplasma().updatePos(Vector2((492, 132))),
Ektoplasma().updatePos(Vector2((505, 116))),
Ektoplasma().updatePos(Vector2((504, 107))),
Ektoplasma().updatePos(Vector2((515, 135))),
Ektoplasma().updatePos(Vector2((552, 147))),
Ektoplasma().updatePos(Vector2((578, 144))),
Ektoplasma().updatePos(Vector2((608, 150))),
Ektoplasma().updatePos(Vector2((621, 158))),
Ektoplasma().updatePos(Vector2((628, 186))),
Ektoplasma().updatePos(Vector2((635, 201))),
Ektoplasma().updatePos(Vector2((662, 210))),
Ektoplasma().updatePos(Vector2((677, 214))),
Ektoplasma().updatePos(Vector2((690, 226))),
Ektoplasma().updatePos(Vector2((692, 249))),
Ektoplasma().updatePos(Vector2((696, 256))),
Ektoplasma().updatePos(Vector2((700, 261))),
Ektoplasma().updatePos(Vector2((707, 274))),
Ektoplasma().updatePos(Vector2((704, 285))),
Ektoplasma().updatePos(Vector2((707, 289))),
Ektoplasma().updatePos(Vector2((712, 297))),
Ektoplasma().updatePos(Vector2((705, 316))),
Ektoplasma().updatePos(Vector2((711, 322))),
Ektoplasma().updatePos(Vector2((712, 327))),
Ektoplasma().updatePos(Vector2((718, 348))),
Ektoplasma().updatePos(Vector2((711, 362))),
Ektoplasma().updatePos(Vector2((716, 376))),
Ektoplasma().updatePos(Vector2((709, 401))),
Ektoplasma().updatePos(Vector2((710, 411))),
Ektoplasma().updatePos(Vector2((708, 424))),
Ektoplasma().updatePos(Vector2((708, 437))),
Ektoplasma().updatePos(Vector2((708, 448))),
Ektoplasma().updatePos(Vector2((724, 453))),
Ektoplasma().updatePos(Vector2((731, 450))),
Ektoplasma().updatePos(Vector2((740, 454))),
Ektoplasma().updatePos(Vector2((746, 449))),
Ektoplasma().updatePos(Vector2((755, 448))),
Ektoplasma().updatePos(Vector2((765, 445))),
Ektoplasma().updatePos(Vector2((765, 436))),
Ektoplasma().updatePos(Vector2((765, 432))),
Ektoplasma().updatePos(Vector2((767, 411))),
Ektoplasma().updatePos(Vector2((770, 409))),
Ektoplasma().updatePos(Vector2((767, 397))),
Ektoplasma().updatePos(Vector2((766, 386))),
Ektoplasma().updatePos(Vector2((765, 379))),
Ektoplasma().updatePos(Vector2((770, 351))),
Ektoplasma().updatePos(Vector2((774, 335))),
Ektoplasma().updatePos(Vector2((775, 331))),
Ektoplasma().updatePos(Vector2((771, 319))),
Ektoplasma().updatePos(Vector2((770, 309))),
Ektoplasma().updatePos(Vector2((772, 302))),
Ektoplasma().updatePos(Vector2((771, 296))),
Ektoplasma().updatePos(Vector2((769, 286))),
Ektoplasma().updatePos(Vector2((769, 267))),
Ektoplasma().updatePos(Vector2((770, 255))),
Ektoplasma().updatePos(Vector2((787, 248))),
Ektoplasma().updatePos(Vector2((815, 247))),
Ektoplasma().updatePos(Vector2((830, 254))),
Ektoplasma().updatePos(Vector2((848, 280))),
Ektoplasma().updatePos(Vector2((854, 303))),
Ektoplasma().updatePos(Vector2((868, 299))),
Ektoplasma().updatePos(Vector2((901, 299))),
Ektoplasma().updatePos(Vector2((953, 300))),
Ektoplasma().updatePos(Vector2((989, 306))),
Ektoplasma().updatePos(Vector2((1000, 306))),
Ektoplasma().updatePos(Vector2((1031, 302))),
Ektoplasma().updatePos(Vector2((1061, 299))),
Ektoplasma().updatePos(Vector2((1062, 299))),
Ektoplasma().updatePos(Vector2((1065, 297))),
Ektoplasma().updatePos(Vector2((977, 324))),
Ektoplasma().updatePos(Vector2((983, 336))),
Ektoplasma().updatePos(Vector2((984, 347))),
Ektoplasma().updatePos(Vector2((985, 365))),
Ektoplasma().updatePos(Vector2((994, 384))),
Ektoplasma().updatePos(Vector2((1012, 396))),
Ektoplasma().updatePos(Vector2((1032, 405))),
Ektoplasma().updatePos(Vector2((1055, 400))),
Ektoplasma().updatePos(Vector2((1062, 396))),
Ektoplasma().updatePos(Vector2((1067, 396))),
Ektoplasma().updatePos(Vector2((968, 407))),
Ektoplasma().updatePos(Vector2((910, 400))),
Ektoplasma().updatePos(Vector2((902, 400))),
Ektoplasma().updatePos(Vector2((867, 399))),
Ektoplasma().updatePos(Vector2((854, 399))),
Ektoplasma().updatePos(Vector2((836, 403))),
Ektoplasma().updatePos(Vector2((837, 420))),
Ektoplasma().updatePos(Vector2((839, 430))),

          ]
        
        
        
        
        
        
        
        
        
        
        
        mB.addObject(*objects)
        mB.addObject(Player().updatePos(Vector2(490,370)))
        self.objects = mB.objects

>>>>>>> Stashed changes
