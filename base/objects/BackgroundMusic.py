from multiprocessing import Event
from typing import List
from base.core.Dependencies.Sounds.SoundsManager import SoundsManager
from base.core.Dependencies.Sounds.Sound import Sound
from base.core.Event.Events import Events
from base.core.Game import Game
from base.core.Level.AbstractLevel import AbstractLevel


class BackgroundMusic():
    def __init__(self, music: Sound, restart = True) -> None:
        self.setMusic(music)
        self.restart = restart
        Events.subscribe("game.level.set", self.stopMusic)
        # Events.subscribe("game.tick", self.onTick)
        AbstractLevel.bind(self)
    

    def setMusic(self, sound: Sound):
        self.music = sound
        SoundsManager.register(self.music)

    def play(self):
        if not SoundsManager.isPlaying(self.music):
            SoundsManager.play(self.music)

    def stopMusic(self, e: Event):
        print(SoundsManager.isPlaying(self.music))
        if self.restart or e.value != Game.level(): # Stoppe dann wenn restart auf wahr ist oder ein neues Level geladen wird.
            SoundsManager.stop(self.music)
