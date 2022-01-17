from typing import Dict, List

from base.core.Dependencies.DependencyException import DependencyException
import pygame

from base.core.Dependencies.Sounds.Sound import Sound
from base.core.Dependencies.Wait import Wait
from base.core.Event.Events import Events

# Klasse zum Abspielen von Sounds. 
class SoundsManager:
    registered: Dict[int, Sound] = {}
    playing: List[id] = []

    def register(sound: Sound):
        SoundsManager.registered[sound.id] = sound
    
    def unregister(sound: Sound):
        if sound.id in SoundsManager.registered.keys():
            del SoundsManager.registered[sound.id]

    def play(sound: Sound):
        if sound.id not in SoundsManager.registered.keys():
            raise LookupError(f"Sound '{id}' is not registered.")

        sound = SoundsManager.registered[sound.id]
        if sound.id in SoundsManager.playing:
            SoundsManager.stop() 

        sound.play()
        SoundsManager.playing.append(sound.id)
        Wait.callIn(sound.sound.get_length() * 1000, lambda: SoundsManager.onSoundStop(sound))

    def onSoundStop(sound):
        SoundsManager.stop(sound)
        Events.dispatch(f"sounds.{sound.id}.finished")

    def stop(sound: Sound):
        if sound.id not in SoundsManager.playing:
            raise LookupError(f"Sound '{id}' is not playing.")
        sound.stop()
        SoundsManager.playing.remove(sound.id)

    def isPlaying(sound: Sound):
        return sound.id in SoundsManager.playing

# Events.subscribe("game.tick", SoundsManager.onTick)
