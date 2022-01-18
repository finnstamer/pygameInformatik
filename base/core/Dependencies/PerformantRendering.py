import pygame
from typing import List
from base.core.Event.Events import Events

class PerformantRendering():
    changes: List[object] = []

    def collectChange(obj: object):
        PerformantRendering.changes.append(obj.rect)
    
    def resetChanges():
        PerformantRendering.changes = []

    def onTick(e):
        print(f"A: {e.name}")
        PerformantRendering.resetChanges()
    
    def render():
        pygame.display.update(PerformantRendering.changes)        
    

# Events.subscribe("game.*tick", PerformantRendering.onTick, PerformantRendering)
