class DependencyException(Exception):
    def __init__(self, dependency: object) -> None:
        super().__init__(f"Dependency '{dependency().__class__.__name__}' is used before initialization. Add the dependency via Game.use() and use it after the game.start event is dispatched.")