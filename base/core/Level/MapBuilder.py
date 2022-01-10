from pygame import Vector2
from base.core.Dependencies.Controls import Controls
from base.core.Event.Events import Events
from base.core.Game import Game
from base.core.Object.Factory import Factory
from objects.collectables.Ektoplasma import Ektoplasma
from settings import screenRes
from typing import List
from base.core.Object.GameObject import GameObject

# Helper Klasse zur Erstellung von Level
# Objekte, deren argumentname nicht referenz ist, werden ggf. geklont und automatisch hinzugefügt und 
class MapBuilder():
    clickMode = False
    start = None
    clicks = []
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
    def nextTo(self, reference: GameObject, obj: GameObject, refC=0, objC=0, marginX: int = 0, marginY: int = 0):
        refCorner = reference.cRect.corners[refC]
        objCorner = obj.cRect.corners[objC]
        diffX = objCorner.x - refCorner.x 
        diffY = objCorner.y - refCorner.y 
        obj.updatePos(Vector2(obj.pos.x - diffX + marginX, obj.pos.y - diffY + marginY))
        self.addObject(obj)
        return self
    
    # Spiegelung von Objekten an der jeweiligen Achse, die nicht -1 ist, und von der jeweiligen Stelle 
    def axisMirror(self, x=-1, y=-1, objs: List[GameObject]=[]):
        xAxis = x != -1
        for obj in list(objs):
            clonedObj = Factory.clone(obj)
            diff = obj.pos.x - x if xAxis else obj.pos.y - y
            newPos = Vector2(x - diff - obj.width if xAxis else obj.pos.x, y - diff - obj.height if not xAxis else obj.pos.y)
            clonedObj.updatePos(newPos)
            self.addObject(clonedObj)
        return self
    
    # Spieglung von Objekten an einem Punkt
    def pointMirror(self, point: Vector2, objs: GameObject):
        for obj in list(objs):
            cloned = Factory.clone(obj)
            diffX = obj.pos.x - point.x
            diffY = obj.pos.y - point.y
            newPos = Vector2(point.x - diffX - obj.width, point.y - diffY - obj.height)
            cloned.updatePos(newPos)
            self.addObject(cloned)
        return self
    
    def allowClickMode(method):
        MapBuilder.clickMethod = method
        Events.subscribe("game.tick", MapBuilder.onTick)
    
    def onTick(event):
        if Controls.released["space"]:
            if MapBuilder.clickMode:
                MapBuilder.clickMode = False
                f = open("clickMode.txt", "w")
                for i in MapBuilder.clicks:
                    f.write(MapBuilder.clickMethod(i) + "\n")
                f.close()
            MapBuilder.clickMode = not MapBuilder.clickMode
        
        isClicked, pos = Controls.clicks["l"]
        pos = Vector2(pos)
        if MapBuilder.clickMode and isClicked:
            if MapBuilder.start is None:
                MapBuilder.start = Vector2(pos)
            else:
                diffVec = Vector2(pos.x - MapBuilder.start.x, pos.y - MapBuilder.start.y)
                xVec = abs(diffVec.x) > abs(diffVec.y)
                objNum = diffVec.x / 15 if xVec else diffVec.y / 15
                signum = diffVec.x / abs(diffVec.x) if xVec else diffVec.y / abs(diffVec.y) 
                print(signum)
                rng = range(int(MapBuilder.start.x) if xVec else int(MapBuilder.start.y), int(pos.x) if xVec else int(pos.y), int(signum * 15))
                for i in rng:
                    print(i)
                    newPos = Vector2(i if xVec else MapBuilder.start.x, i if not xVec else MapBuilder.start.y)
                    MapBuilder.clicks.append(newPos)
                    Game.level().add(Ektoplasma().updatePos(newPos))
                MapBuilder.start = None