import pygame

from base.core.Object.Factory import Factory
class Sound():
    def __init__(self, path: str, volume: float) -> None:
        self.id = -1
        Factory.append(self)
        self.setPath(path)
        self.setVolume(volume)
    
    def setPath(self, path: str):
        self.path = path
        self.sound = pygame.mixer.Sound(self.path)
    
    def setVolume(self, vol: float):
        self.sound.set_volume(vol)

    def stop(self):
        self.sound.stop()

    def play(self):
        self.sound.play()