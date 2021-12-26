from typing import Dict, List
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.object.GameObject import GameObject

# CollisionWatcher beobachtet die Kollision zweier Objekte. Sobald die Kollision stattfindet wird ein von der watch Methode zurückgegebenes Event gefired.
class CollisionWatcher():
    watchList: Dict[GameObject, List[GameObject]] = {}

    def watch(obj: GameObject, watch: GameObject) -> str:
        if watch not in CollisionWatcher.watchList:
            CollisionWatcher.watchList[watch] = []
        
        # Auch wenn das beobachtende Objekt sich bewegt und eine Kollision verursacht soll gefired werden.
        if obj not in CollisionWatcher.watchList:
            CollisionWatcher.watchList[obj] = []
            
        CollisionWatcher.watchList[watch].append(obj)
        CollisionWatcher.watchList[obj].append(watch)

        Events.subscribe(f"{watch.id}.moved", CollisionWatcher.receiveEvent)
        Events.subscribe(f"{obj.id}.moved", CollisionWatcher.receiveEvent)
        return f"collisionWatcher.collision.{obj.id}.{watch.id}"

    def receiveEvent(event: Event):
        if event.isOfType("moved"):
            movedObj: GameObject = event.value["obj"]
            watchingObjects = CollisionWatcher.watchList[movedObj]

            for obj in watchingObjects:
                if obj.active and obj.collidesWith(movedObj.rect):
                    Events.dispatch(f"collisionWatcher.collision.{obj.id}.{movedObj.id}")
                    Events.dispatch(f"collisionWatcher.collision.{movedObj.id}.{obj.id}")
                
    def removeWatcher(obj: GameObject, watch: GameObject):
        if watch in CollisionWatcher.watchList:
            CollisionWatcher.watchList[watch].remove(obj)
            if len(CollisionWatcher.watchList[watch]) == 0:
                Events.unsubscribe(f"{watch.id}.moved", CollisionWatcher.receiveEvent)

                
    def unwatch(obj: GameObject, watch: GameObject):
        CollisionWatcher.removeWatcher(obj, watch)
        CollisionWatcher.removeWatcher(watch, obj)