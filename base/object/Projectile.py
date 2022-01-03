from base.core.Dependencies.Movement import Movement
from base.core.Game import Game
from base.object.AI.Actions.MovementAction import MovementAction
from base.object.GameObject import GameObject


class Projectile(GameObject):
    def __init__(self, range: int = 0, damage: int = 0, speed: int = 0, width: int = 0, height: int = 0) -> None:
        super().__init__(width=width, height=height)
        self.speed = speed
        self.damage = damage
        self.range = range
        self.active = False
    
    def prepare(self):
        self.movementAction = MovementAction(self, self.pos)
        self.movementAction.middlewareHandler.on("finished", self.onFinished)
        self.movementAction.middlewareHandler.on("finished", self.fadeOut)
        self.movementAction.middlewareHandler.connect("segmentPos", self.evaluateNextPos)
        self.active = True
    
    def evaluateNextPos(self, pos):
        furthestMove, objects = Movement.furthestMove_collider(self, pos, self.pos)
        if furthestMove == self.pos or furthestMove is None:
            self.movementAction.stop()
            self.onFinished() 
            self.hit(objects)
            return self.pos
        if furthestMove != pos:
            return furthestMove
        return pos
    
    def hit(self, objects):
        print(objects)
        pass

    def fadeOut(self):
        pass

    def onFinished(self):
        self.hit([])
        self.active = False
        Game.level.remove(self)
