from typing import Dict, List
from base.core.Event.Event import Event
from base.core.Event.Events import Events
from base.object.GameObject import GameObject


class CollisionWatcher():
    watchList: Dict[GameObject, List[GameObject]] = {}

    def watch(obj: GameObject, watch: GameObject) -> str:
        if watch not in CollisionWatcher.watchList:
            CollisionWatcher.watchList[watch] = []
        CollisionWatcher.watchList[watch].append(obj)
        
            
        Events.subscribe(CollisionWatcher, f"{watch.id}.moved")
        return f"CollisionWatcher.collision.{obj.id}.{watch.id}"

    def receiveEvent(event: Event):
        if event.isOfType("moved"):
            movedObj: GameObject = event.value["obj"]
            watchingObjects = CollisionWatcher.watchList[movedObj]

            for obj in watchingObjects:
                if obj.collidesWith(movedObj.rect):
                    Events.dispatch(f"CollisionWatcher.collision.{obj.id}.{movedObj.id}")
                
    def unwatch(obj: GameObject, watch: GameObject):
        if watch in CollisionWatcher.watchList:
            CollisionWatcher.watchList[watch].remove(obj)
            if len(CollisionWatcher.watchList[watch]) == 0:
                Events.unsubscribe(CollisionWatcher, f"{watch.id}.moved")

