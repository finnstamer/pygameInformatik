from base.object.KI.Action import Action
from base.object.MovableObject import MovableObject


class MovementAction(Action):
    def __init__(self, start=MovableObject, end=MovableObject) -> None:
        super().__init__(start=start, end=end)

    def run(self):
        xDiff = abs(self.startState.pos.x) - abs(self.endState.pos.x)
        yDiff = abs(self.endState.pos.y) - abs(self.endState.pos.y)
        xMovement = xDiff > yDiff
        self.startState.moveBySteps(xDiff if xMovement else yDiff, xMovement)

    def isFinished(self) -> bool:
        return self.startState.pos == self.endState.pos
    
