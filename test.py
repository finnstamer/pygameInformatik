from pygame import Vector2
from base.core.Level.Level import Level
from base.object.Group import Group
from objects.wall import Wall

wallObject = Wall()
wallObject.width = 100
wallObject.pos = Vector2(0, 0)


wallObject2 = Wall()
wallObject2.width = 100
wallObject2.pos = Vector2(0, 0)


wallGroup = Group("wall").add(wallObject, wallObject2)

level1 = Level(5, [wallGroup])
