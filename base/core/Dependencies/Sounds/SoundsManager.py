from typing import Dict, List

from base.core.Dependencies.DependencyException import DependencyException
import pygame

from base.core.Dependencies.Sounds.Sound import Sound

# Klasse zum Abspielen von Sounds. 
class SoundsManager:
    registered: Dict[int, Sound] = {}
    playing: Dict[int, Sound] = {}

    def register(sound: Sound):
        SoundsManager.registered[sound.id] = sound
    
    def unregister(sound: Sound):
        if sound.id in SoundsManager.registered.keys():
            del SoundsManager.registered[sound.id]

    def play(sound: Sound):
        if sound.id not in SoundsManager.registered.keys():
            raise LookupError(f"Sound '{id}' is not registered.")

        sound = SoundsManager.registered[sound.id]
        if sound in SoundsManager.playing:
            SoundsManager.stop() 

        sound.play()
        SoundsManager.playing[sound.id] = sound

    def stop(sound: Sound):
        if sound.id not in SoundsManager.playing.keys():
            raise LookupError(f"Sound '{id}' is not playing.")
        sound.stop()
        del SoundsManager.playing[sound.id]

    def isPlaying(sound: Sound):
        return sound.id in SoundsManager.playing.keys()
