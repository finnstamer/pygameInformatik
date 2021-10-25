import pygame
import settings
from pygame.constants import K_ESCAPE, K_LEFT, K_RIGHT
from base.object.Group import Group
from base.object.Rectangle import Rectangle
from base.object.collision import Collision
from base.player.Keys import Keys
from base.player.Player import Player
from objects.wall import Wall


pygame.init()
global screen
screen = pygame.display.set_mode((480, 260))
done = False

hlocation = 50;
vLocation = 50;

clock = pygame.time.Clock()
player = Player()
keys = Keys()

collision = Collision()

wall1 = Wall()
wall1.updatePos(pygame.Vector2(200, 100))
wall2 = Wall()
wall2.updatePos(pygame.Vector2(180, 125))
wall2.color = (240, 0, 240)
wall2.updateRect()
wallGroup = Group[Wall]('walls', Wall).add(wall1)


def setWallToWhite(wall):
    wall.color = (240, 240, 240)
    return wall

while not done:
    clock.tick(60)
    done = pygame.key.get_pressed()[K_ESCAPE] 
    screen.fill(pygame.Color(50, 12, 100));

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keys.updateControlsPressed(event.key)
        if event.type == pygame.KEYUP:
            keys.updateControlsReleased(event.key)

    player.move(keys)
    player.draw()
    
    wallGroup.applyOnEach(setWallToWhite)

    # Nearest Object to player becomes highlighted 
    #---
    # nearest = wallGroup.nearest(player.cRect.center) 
    # nearest.color = (240, 0, 0)

    # Oject with highest intersection to player becomes highlighted
    #---
    # collided = wallGroup.colliding(player.cRect) 
    # if len(collided) > 0:
    #     collided[0].color = (240, 0, 0)

    
    wallGroup.draw()

    # Intersection from player to Walls gets drawn
    #---
    for o in wallGroup.objects:
        if collision.isCollided(player.cRect, o.cRect):
            intersection = collision.getIntersection(o.cRect, player.cRect)
            pygame.draw.rect(screen, (250, 0, 0), intersection.toPyRect())
        

    pygame.display.flip()
