from time import time_ns
from typing import Callable, Dict, List

from base.core.Event.Events import Events

class Wait():
    queue = [] # [{"name": "sounds.1.stopped", "time:" 124523489, "func": FUNCTION}]

    def callIn(ms: int, function: Callable, name=""):
        callTime = time_ns() + ms * 1000000
        Wait.queue.append((callTime, function, name))

    def onTick(e):
        t = time_ns()
        for time, func, name in Wait.queue:
            if t >= time:
                func()
                Wait.unqueue(time, func, name)
    
    def unqueue(time: int, function: Callable, name):
        entry = (time, function, name)
        if entry in Wait.queue:
            Wait.queue.remove(entry)
    
    def unqueueByName(name: str):
        for t, f, n in Wait.queue:
            if name == n:
                Wait.unqueue(t, f, n)
    
Events.subscribe("game.tick", Wait.onTick, Wait)