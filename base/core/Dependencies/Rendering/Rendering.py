from multiprocessing import Event
import pygame
from typing import List
from base.core.Dependencies.Rendering.Layer import Layer

from base.core.Event.Events import Events
from settings import screen
# TODO
# - Redraw from lower to higher layer all objects on this changed rect 
    # - Redraw Rect by color and position of corners, so only the changed rect part is redrawn
    # - Redraw image by blit
class Rendering():
    changes: List[pygame.Rect] = []
    
    def addChange(rect: pygame.Rect):
        if rect not in Rendering.changes:
            Rendering.changes.append(rect)
    
    def removeChange(rect: pygame.Rect):
        if rect in Rendering.changes:
            Rendering.changes.remove(rect)

    def reset():
        Rendering.drawQueue = []
        Rendering.changes = []        
    
    def render():
        for rect in Rendering.changes:
            screen.fill((0,0,0), rect)
            for layer in Layer.getAll():
                intersectingObjs = layer.intersectingObjects(rect)
                for obj, r in intersectingObjs:
                    obj.drawSpecific(r)
        
        pygame.display.update(Rendering.changes)
        Rendering.reset()
    
    def collectChange(e):
        if type(e.value) == list:
            Rendering.changes += [obj.rect for obj in e.value]
            return
        Rendering.addChange(e.value.rect)
    
    def collectUpdate(e):
        obj, before = e.value
        Rendering.addChange(pygame.Rect(before.x, before.y, obj.width, obj.height))
        Rendering.addChange(obj.rect)
        
collectchange = [
    "*.active",
    "level.objects.add",
    "*.inactive",
    "level.objects.remove"
]
collectChange = [
    "*.moved"
]
# for e in collectchange:
#     Events.subscribe(e, Rendering.collectChange, Rendering)
# for e in collectChange:
#     Events.subscribe(e, Rendering.collectUpdate, Rendering)
