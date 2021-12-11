from pygame import Vector2
from base.core.Level.Level import Level
from base.object.Group import Group
from objects.wall import Wall

wall = Wall()
wallGroup = Group("wall").add(wall)


level1 = Level(1, [wallGroup])

wallobject = Wall()
wallobject.width = 100
wallobject.pos = Vector2(2,2)

