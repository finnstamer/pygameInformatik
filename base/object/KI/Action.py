import pygame
from base.core.Event.Event import Event

from base.object.GameObject import GameObject

class Action():
    def __init__(self, start=GameObject, end=GameObject) -> None:
        self.startState: GameObject = start
        self.endState: GameObject = end
        self.state = 0 # 0: Stop; 1: Pending; 2: Finished

    def start(self):
        self.state = 1
        return self
    
    def stop(self):
        self.state = 0

    # When run returns a false value
    def run(self) -> bool:
        raise NotImplementedError(f"Run method in {self.__class__.__name__} is missing.")
    
    def receiveEvent(self, event: Event):
        if event.name == "game.tick" and self.state == 1:
            self.run()
            self.state == 2 if self.isFinished() else 1

    def isFinished(self) -> bool:
        raise NotImplementedError(f"isFinished method in {self.__class__.__name__} is missing.")


