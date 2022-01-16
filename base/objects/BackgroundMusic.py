from multiprocessing import Event
from typing import List
from base.core.Dependencies.Sounds import Sounds
from base.core.Event.Events import Events
from base.core.Game import Game
from base.core.Level.AbstractLevel import AbstractLevel


class BackgroundMusic():
    isPlaying: List[int] = []
    def __init__(self, id: int, volume: float, restart = True) -> None:
        self.volume = volume
        self.restart = restart
        self.setSound(id)
        Events.subscribe("game.level.delete", self.stopMusic)
        AbstractLevel.bind(self)
    
    def setSound(self, id: int):
        self.soundId = id
        if id not in BackgroundMusic.isPlaying:
            Sounds.play(self.soundId, self.volume)
            BackgroundMusic.isPlaying.append(id)
    
    def stopMusic(self, e: Event):
        if self.restart or e.value != Game.level(): # Stoppe dann wenn restart auf wahr ist oder ein neues Level geladen wird.
            Sounds.stop()
            BackgroundMusic.isPlaying.remove(id)
