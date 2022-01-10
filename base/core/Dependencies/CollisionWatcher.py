from typing import Dict, List
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.core.Object.GameObject import GameObject

# CollisionWatcher beobachtet die Bewegung zweier Objekte und prüft, ob eine Kollision stattfindet. 
# Sobald die Kollision stattfindet wird ein von der watch Methode zurückgegebenes Event ausgegeben.
class CollisionWatcher():
    watchList: Dict[GameObject, List[GameObject]] = {}

    # Startet die Beobachtung der Objekte in beide Richtung 
    # und gibt ein Eventname zurück, der bei einer Kollision ausgegeben wird.
    def watch(obj: GameObject, watch: GameObject) -> str:
        if watch not in CollisionWatcher.watchList:
            CollisionWatcher.watchList[watch] = []
        
        if obj not in CollisionWatcher.watchList:
            CollisionWatcher.watchList[obj] = []
            
        CollisionWatcher.watchList[watch].append(obj)
        CollisionWatcher.watchList[obj].append(watch)

        Events.subscribe(f"{watch.id}.moved", CollisionWatcher.receiveEvent)
        Events.subscribe(f"{obj.id}.moved", CollisionWatcher.receiveEvent)
        return f"collisionWatcher.collision.{obj.id}.{watch.id}"

    def receiveEvent(event: Event):
        if event.isOfType("moved"):
            movedObj: GameObject = event.value
            watchingObjects = CollisionWatcher.watchList[movedObj]

            for obj in watchingObjects:
                if obj.active and obj.collidesWith(movedObj.rect):
                    Events.dispatch(f"collisionWatcher.collision.{obj.id}.{movedObj.id}")
                    Events.dispatch(f"collisionWatcher.collision.{movedObj.id}.{obj.id}")
    
    # Entfernt die Beobachtung in eine Richtung
    def removeWatcher(obj: GameObject, watch: GameObject):
        if watch in CollisionWatcher.watchList:
            CollisionWatcher.watchList[watch].remove(obj)
            if len(CollisionWatcher.watchList[watch]) == 0:
                Events.unsubscribe(f"{watch.id}.moved", CollisionWatcher.receiveEvent)

    # Entfernt die Beobachtung zweier Objekte in beide Richtungen     
    def unwatch(obj: GameObject, watch: GameObject):
        CollisionWatcher.removeWatcher(obj, watch)
        CollisionWatcher.removeWatcher(watch, obj)