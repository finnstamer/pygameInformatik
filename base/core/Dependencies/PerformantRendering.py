from multiprocessing import Event
import pygame
from typing import List

from base.core.Event.Events import Events
# TODO
# - Redraw all by rect
class PerformantRendering():
    drawQueue: List[object] = []
    changes: List[pygame.Rect] = []

    def collectChange(e: Event):
        objects = e.value
        if not isinstance(e.value, List):
            objects = [e.value]
        for obj in objects:
            print(f"Collecting change on {e.name}")
            PerformantRendering.changes.append(obj.rect)
            PerformantRendering.drawQueue.append(obj)

    def collectRemove(e: Event):
        PerformantRendering.changes.append(e.value.rect)
        if e.value in PerformantRendering.drawQueue:
            PerformantRendering.drawQueue.remove(e.value)

    def resetChanges():
        PerformantRendering.changes = []
        PerformantRendering.drawQueue = []

    def render():
        pygame.display.update(PerformantRendering.changes)
        for obj in PerformantRendering.drawQueue:
            obj.draw()   
        PerformantRendering.resetChanges()

collectDraw = [
    "*.moved",
    "*.active",
    "level.objects.add"
]
collectErase = [
    "*.inactive",
]
# for e in collectDraw:
#     Events.subscribe(e, PerformantRendering.collectChange, PerformantRendering)
# for e in collectErase:
#     Events.subscribe(e, PerformantRendering.collectRemove, PerformantRendering)
