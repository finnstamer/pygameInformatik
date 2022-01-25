from tokenize import endpats
from base.core.Action.AbstractAction import AbstractAction
from base.core.Event.Events import Events


class FadeAction(AbstractAction):
    def __init__(self, obj, endState, attr="", speed=0) -> None:
        super().__init__(obj, endState)
        self.attr = attr
        self.speed = speed
        self.eachStep = 0
        self.incrementing = False
        self.middlewareHandler.on("start", lambda: Events.subscribe("game.tick", self.run, self))
        self.middlewareHandler.on("stop", lambda: Events.unsubscribe("game.tick", self.run, self))
        self.middlewareHandler.on("run", self.onRun)
        self.middlewareHandler.on("set", self.onSet)
        self.onSet()

    def onSet(self):
        value = getattr(self.object, self.attr)
        diff = self.endState - value
        self.eachStep = self.speed / diff  
        self.incrementing = self.eachStep > 0
        print(self.eachStep)

    def onRun(self):
        value = getattr(self.object, self.attr)
        setattr(self.object, self.attr, value + self.eachStep)
    
    def isFinished(self) -> bool:
        val = getattr(self.object, self.attr)
        return  val >= self.endState if self.incrementing else val <= self.endState