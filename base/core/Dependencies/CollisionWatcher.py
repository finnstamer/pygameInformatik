from typing import Dict, List
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.object.GameObject import GameObject

# FIXME .unwatch führt zu einer Aufheben des Beobachtens. Zwei Module die auf dieselben Objekte beobachten und eines davon stoppt, unwatched es und macht die Aufgabe des anderen Moduls unmöglich
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

        Events.subscribe(CollisionWatcher, f"{watch.id}.moved", f"{obj.id}.moved")
        return f"CollisionWatcher.collision.{obj.id}.{watch.id}"

    def receiveEvent(event: Event):
        if event.isOfType("moved"):
            movedObj: GameObject = event.value["obj"]
            watchingObjects = CollisionWatcher.watchList[movedObj]

            for obj in watchingObjects:
                if obj.collidesWith(movedObj.rect):
                    Events.dispatch(f"CollisionWatcher.collision.{obj.id}.{movedObj.id}")
                    Events.dispatch(f"CollisionWatcher.collision.{movedObj.id}.{obj.id}")
                
    def unwatch(obj: GameObject, watch: GameObject):
        if watch in CollisionWatcher.watchList:
            CollisionWatcher.watchList[watch].remove(obj)
            if len(CollisionWatcher.watchList[watch]) == 0:
                Events.unsubscribe(CollisionWatcher, f"{watch.id}.moved")

