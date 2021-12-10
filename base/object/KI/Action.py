from base.core.Event.Event import Event
from base.core.Event.Events import Events

from base.object.GameObject import GameObject

class Action():
    def __init__(self, start=None, end=None) -> None:
        self.startState = start
        self.endState = end
        self.state = 0 # 0: Stop; 1: Pending; 2: Finished

    def start(self):
        self.state = 1
        Events.subscribe(self, "game.tick")
        return self
    
    def stop(self):
        Events.unsubscribe(self, "game.tick")
        self.state = 0

    # When run returns a false value
    def run(self) -> bool:
        raise NotImplementedError(f"Run method in {self.__class__.__name__} is missing.")
    
    def receiveEvent(self, event: Event):
        if event.name == "game.tick" and self.state == 1:
            if self.isFinished():
                self.stop()
                self.state = 2
            else:
                self.run()

    def isFinished(self) -> bool:
        raise NotImplementedError(f"isFinished method in {self.__class__.__name__} is missing.")