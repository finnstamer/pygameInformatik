import pygame
from pygame.constants import K_ESCAPE, K_LEFT, K_RIGHT
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
wall = Wall()
keys = Keys()

collision = Collision()
while not done:
    clock.tick(60)
    done = pygame.key.get_pressed()[K_ESCAPE] 

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            keys.updateControlsPressed(event.key)
        if event.type == pygame.KEYUP:
            keys.updateControlsReleased(event.key)

    player.move(keys)
    screen.fill(pygame.Color(50, 12, 100));
    wall.draw(screen)
    player.draw(screen)

    playerRec = Rectangle().byRect(player.rect)
    wallRec = Rectangle().byRect(wall.rect)
    collided = collision.check(wallRec, playerRec)
    if collided:
        # print("Collided")
        pygame.draw.rect(screen, (250, 0, 0), collision.collisionRect)

    pygame.display.flip()
