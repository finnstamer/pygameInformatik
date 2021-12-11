from base.object.GameObject import GameObject
from base.object.Group import Group
from base.object.KI.Node import Node
from base.object.KI.PathFinder import PathFinder
from base.core.Game import Game
from settings import screenRes
from Maps.Map1 import level1

game = Game()
game.addLevel(level1)
game.setLevel(1)
game.start()
exit()

def nodeToObject(node: Node, id: int):
    obj = GameObject()
    obj.pos = node.pos
    obj.id = id
    Game.notes[id] = node
    return obj

player = Game.level.getGroup("player").objects[0]

nodes = PathFinder.generateNodes(player)
nodeObjects = []
for n in range(len(nodes)):
    nodeObjects.append(nodeToObject(nodes[n], n))
    nodes[n].id = n
nodeGroup = Group("nodes", Node).add(*nodeObjects)

rootNodeObj: Node = nodeGroup.nearest(player.pos)

rootNode: Node = Game.notes[rootNodeObj.id]
targetNode = rootNode.right

# nList = list(rootNode.neighborsToList().values())

print(rootNode.pos)
print(targetNode.pos)
print("----------------")
print(PathFinder.nodesToIds(rootNode.neighborsToList().values()))
nList = PathFinder.bestNeighbors(rootNode, targetNode)
print(PathFinder.nodesToIds(nList))

# path = PathFinder.find(rootNode, targetNode, 15)

# Tasks:
    # Finn: 
    #   KI > NodeList to Actions => Actions to Routines => Routines to KI
    # Leon: 
    #   Übertragung von Map Concepts ins Game > (Wand-)Klassen für Grundformen erstellen => Sprites entwickeln und implementieren. 
    #   Game Concept weiterentwickeln
    # Aryan: 
    #   Erstellung von Sounds 
    #   Game Concept weiterenwtickeln


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