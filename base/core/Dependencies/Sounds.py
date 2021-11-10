from typing import Dict

from base.core.Dependencies.DependencyException import DependencyException
import pygame

# pygame.mixer is only available after pygame.init; therefore add Sounds as dependency
class Sounds:
    loaded: Dict[str, pygame.mixer.Sound] = {}
    currentlyPlaying: pygame.mixer.Sound = None
    mixer = None

    def __init__(self) -> None:
        Sounds.mixer = pygame.mixer
    
    @staticmethod
    def load(id, path):
        if Sounds.mixer is None:
            raise DependencyException(Sounds)
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