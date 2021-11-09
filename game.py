from levels import levels 
from base.core.Game import Game

game = Game()
game.addLevel(*levels)
game.setLevel(1)
game.start()

# while not done:
#     clock.tick(120)
#     done = pygame.key.get_pressed()[K_ESCAPE] 
#     screen.fill(pygame.Color(50, 12, 100));

#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN:
#             keys.updateControlsPressed(event.key)
#         if event.type == pygame.KEYUP:
#             keys.updateControlsReleased(event.key)

#     # Dies macht alle Wände standardmäßig weiß
#     wallGroup.applyOnEach(setWallToWhite)
#     player.control(keys, wallGroup)
#     player.draw()
#     wallGroup.draw()


#     # Nearest Object to player becomes highlighted 
#     #---
#     # nearest = wallGroup.nearest(player.cRect.center) 
#     # nearest.color = (240, 0, 0)

#     # Oject with highest intersection to player becomes highlighted
#     # ---
#     # collided = wallGroup.colliding(player.cRect) 
#     # if len(collided) > 0:
#     #     collided[0].color = (240, 0, 0)

#     # Intersection from player to Walls gets drawn
#     #---
#     for o in wallGroup.objects:
#         intersection = collision.intersection(o.cRect, player.cRect)
#         if collision.isColliding(player.cRect, o.cRect):
#             # Zu Testzwecken, können die die Eckpunkte angezeigt werden
#             # for c in intersection.corners:
#             #     pygame.draw.rect(screen, (0, 100, 250), pygame.Rect(c.x, c.y, 5, 5))
#             pygame.draw.rect(screen, (250, 0, 0), intersection.toPyRect())

#     pygame.display.flip()