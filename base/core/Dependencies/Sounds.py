from typing import Dict

from base.core.Dependencies.DependencyException import DependencyException
import pygame

# Klasse zum Abspielen von Sounds. 
# Muss zur Verwendung über Game.use(Sounds) geladen werden, da
class Sounds:
    loaded: Dict[str, pygame.mixer.Sound] = {}
    currentlyPlaying: pygame.mixer.Sound = None
    mixer = pygame.mixer

    def __init__(self) -> None:
        pass
    @staticmethod
    def load(id, path):
        if Sounds.mixer is None:
            raise DependencyException(Sounds)
        Sounds.loaded[id] = Sounds.mixer.Sound(path)
        
    @staticmethod
    def play(id, vol: float):
        if id not in Sounds.loaded:
            raise LookupError(f"Sound '{id}' is not loaded.")
        sound = Sounds.loaded[id] 
        if Sounds.currentlyPlaying != sound:
            sound.play()
            sound.set_volume(vol)
            Sounds.currentlyPlaying = sound
    
    @staticmethod
    def stop():
        if Sounds.currentlyPlaying is not None:
            Sounds.currentlyPlaying.stop()