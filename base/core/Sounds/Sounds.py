from os import error, stat
from typing import Dict

from base.core.DependencyException import DependencyException
from base.core.Event.Event import Event
from base.core.Event.EventDispatcher import EventDispatcher
import pygame

class Sounds:
    loaded: Dict[str, pygame.mixer.Sound] = {}
    currentlyPlaying: pygame.mixer.Sound = None
    mixer = None

    def __init__(self) -> None:
        # pygame.mixer is only available after pygame.init; therefore add Sounds as dependency
        Sounds.mixer = pygame.mixer
    
    @staticmethod
    def load(id, path):
        if Sounds.mixer is None:
            raise DependencyException(Sounds)
            # raise error(f"Sound '{id}' cannot be loaded before dependency Sound is initialized; Load on 'game.start' Event.")
        Sounds.loaded[id] = Sounds.mixer.Sound(path)
    @staticmethod
    def play(id):
        if id not in Sounds.loaded:
            raise LookupError(f"Sound '{id}' is not loaded.")
        sound = Sounds.loaded[id] 
        if Sounds.currentlyPlaying != sound:
            sound.play()
            Sounds.currentlyPlaying = sound
    
    @staticmethod
    def stop():
        if Sounds.currentlyPlaying is not None:
            Sounds.currentlyPlaying.stop()