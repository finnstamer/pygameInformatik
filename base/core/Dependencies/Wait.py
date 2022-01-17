from time import time_ns
from typing import Callable, Dict, List

from base.core.Event.Events import Events

class Wait():
    queue: Dict[int, List[Callable]] = {}

    def callIn(ms: int, function: Callable):
        callTime = time_ns() + ms * 1000000
        if callTime not in Wait.queue.keys():
            Wait.queue[callTime] = []
        Wait.queue[callTime].append(function)

    def onTick(e):
        t = time_ns()
        for time, functions in list(Wait.queue.items()):
            if t >= time:
                for f in functions:
                    f()
                    Wait.remove(time, f)
    
    def remove(time: int, function: Callable):
        if time in Wait.queue.keys():
            Wait.queue[time].remove(function)
    
    def removeTime(time: int):
        if time in Wait.queue.keys():
            del Wait.queue[time]

Events.subscribe("game.tick", Wait.onTick, Wait)