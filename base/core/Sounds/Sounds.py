from typing import Dict
from base.core.Event.Event import Event
from base.core.Event.EventDispatcher import EventDispatcher
import pygame

# Sounds dürfen frühstens nach dem G_START Event von der Game-Klasse geladen werden.
class Sounds:
    loaded: Dict[str, pygame.mixer.Sound] = {}
    currentlyPlaying: pygame.mixer.Sound = None
    def __init__(self) -> None:
        EventDispatcher.subscribe(self, "S_LOAD", "S_PLAY", "S_STOP")
    
    def receiveEvent(self, event: Event):
        if event.name == "S_LOAD":
            Sounds.loaded[event.value[0]] = pygame.mixer.Sound(event.value[1])
        if event.name == "S_PLAY":
            print(Sounds.loaded)
            if event.value not in Sounds.loaded:
                raise LookupError(f"Sound '{event.value}' is not loaded.")
            sound = Sounds.loaded[event.value] 
            if Sounds.currentlyPlaying != sound:
                sound.play()
                Sounds.currentlyPlaying = sound
        if event.name == "S_STOP":
            if Sounds.currentlyPlaying is not None:
                Sounds.currentlyPlaying.stop()

    @staticmethod
    def start():
        return Sounds()