class Action():
    def __init__(self, state, endState) -> None:
        self.state = state
        self.endState = endState
        self.progress = 0
    
    def onStart(self):
        raise NotImplementedError(f"'onStart' Method on {self.__class__.__name__} not implemented.")

    def onRun(self):
        raise NotImplementedError(f"'_run' Method on {self.__class__.__name__} not implemented.")
    
    def onStop(self):
        raise NotImplementedError(f"'_stop' Method on {self.__class__.__name__} not implemented.")
    
    def isFinished(self):
        raise NotImplementedError(f"'isFinished' Method on {self.__class__.__name__} not implemented.")
    
    def start(self):
        self.progress = 1
        self.onStart()
        return self

    def run(self):
        if self.isFinished():
            self.stop()
            self.progress = 2
            return
        self.onRun()

    def stop(self):
        self.progress = 0
        self.onStop()
        return self