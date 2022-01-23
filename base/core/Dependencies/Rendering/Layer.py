from __future__ import annotations
from typing import Dict, List, Tuple
from base.core.Event.Events import Events
from base.core.Level.AbstractLevel import AbstractLevel
from pygame import Rect

# Dient zur Speicherung der Ebene der GameObjects
class Layer():
    layers: Dict[int, Layer] = {}
    def __init__(self, layer: int, objects: List[object] = []) -> None:
        self.objects = objects
        self.layer = layer
        
        AbstractLevel.bind(self)
        Layer.layers[self.layer] = self
        Events.subscribe(f"factory.delete.{id(self)}", self.removeSelf)
    
    # Fügt Objekte zu einem Layer hinzu
    def add(self, *objects) -> Layer:
        self.objects += list(objects)
        return self 

    def removeSelf(self, e):
        Layer.layers.remove(self)
    
    def addToMultiple(start: int, end: int, objects: List[List[object]]):
        for i in range(start, end):
            _objects = objects[i] if len(objects) - 1 >= i else []
            Layer.get(i).add(*_objects)
        
    def get(layer) -> Layer:
        if layer in Layer.layers:
            return Layer.layers[layer]
        return Layer(layer)

    def getAll() -> List[Layer]:
        return list(Layer.layers.values())
    
    # Gibt alle Objekte zurück, die das gegebene Rechteck schneiden.
    def intersectingObjects(self, rect: Rect) -> List[Tuple[object, Rect]]:
        intersections = []
        for obj in self.objects:
            intersectingRect = obj.rect.clip(rect)
            w, h = intersectingRect.size
            if w != 0 and h != 0:
                intersections.append((obj, intersectingRect))
        return intersections
     
    def getLayerByObject(obj) -> Layer:
        for l in Layer.getAll():
            if obj in l.objects:
                return l
        raise LookupError(f"Object {obj.id} not registered in Layer at Rendering time")