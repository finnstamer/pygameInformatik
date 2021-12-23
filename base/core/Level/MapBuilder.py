from pygame import Vector2
from base.object.Factory.Factory import Factory
from settings import screenRes
from typing import List
from base.object.GameObject import GameObject

class MapBuilder():
    def __init__(self, objects: List[GameObject] = []) -> None:
        self.objects = objects

    def addObject(self, *objects: GameObject):
        for obj in list(objects):
            if obj not in self.objects:
                self.objects.append(obj)
        return self
    
    def centerVec(self):
        return Vector2(screenRes[0] / 2, screenRes[1] / 2)
    
    def placeInCenter(self, obj: GameObject):
        center = self.centerVec()
        obj.updatePos(Vector2(center.x - obj.width, center.y - obj.height))
        self.addObject(obj)
        return self
    
    # Platziert ein Objekt neben ein Referenz-Objekt anhand ihrer sich "berührende" Ecken. Zahl entspricht Ecke im Uhrzeigersinn von oben links mit 0 beginnend
    # Beispiel: Will man ein Objekt exakt rechts neben ein ReferenzObjekt platzieren und sich die obere Rechte mit der oberen Linken berühren soll: nextTo(ref, obj, 1, 0)
    # margin(X/Y) ermöglicht noch einen zusätlichen Abstand
    def nextTo(self, reference: GameObject, obj: GameObject, refC=1, objC=1, marginX: int = 0, marginY: int = 0):
        refCorner = reference.cRect.corners[refC]
        objCorner = obj.cRect.corners[objC]
        diffX = objCorner.x - refCorner.x 
        diffY = objCorner.y - refCorner.y 
        obj.updatePos(Vector2(obj.pos.x - diffX + marginX, obj.pos.y - diffY + marginY))
        self.addObject(obj)
        return self
    
    # Spiegelung von Objekten an der jeweiligen Achse, die nicht -1 ist, und von der jeweiligen Stelle 
    def axisMirror(self, x=-1, y=-1, *objs: GameObject):
        xAxis = x != -1
        for obj in list(objs):
            clonedObj = Factory.clone(obj)
            diff = obj.pos.x - x if xAxis else obj.pos.y - y
            print(diff)
            newPos = Vector2(x - diff - obj.width if xAxis else obj.pos.x, y - diff - obj.height if not xAxis else obj.pos.y)
            print(obj.pos, newPos)
            clonedObj.updatePos(newPos)
            self.addObject(clonedObj)
        return self
    
    # Spieglung von Objekten an einem Punkt
    def pointMirror(self, point: Vector2, *objs: GameObject):
        for obj in list(objs):
            cloned = Factory.clone(obj)
            diffX = obj.pos.x - point.x
            diffY = obj.pos.y - point.y
            newPos = Vector2(point.x - diffX - obj.width, point.y - diffY - obj.height)
            cloned.updatePos(newPos)
            self.addObject(cloned)
        return self
