from typing import Dict

import pygame
class Fonts():
    fonts: Dict[str, Dict[int, pygame.font.Font]] = {} # {"arial": {25: FONT}}

    def load(font: str, path: str, size):
        if font not in Fonts.fonts or size not in Fonts.fonts[font]:
            pyFont = pygame.font.Font(path, size)
            if font not in Fonts.fonts:
                Fonts.fonts[font] = {}
            Fonts.fonts[font][size] = pyFont
            return pyFont
    
    def remove(font: str, size: int):
        if font in Fonts.fonts and size in Fonts.fonts[font]:
            del Fonts.fonts[font][size]
        
    def get(font: str, size: int):
        if font not in Fonts.fonts or size not in Fonts.fonts[font]:
            raise LookupError(f"Font '{font}' with size '{size} could not be found'")
        return Fonts.fonts[font][size]