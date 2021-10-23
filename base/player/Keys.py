from pygame.constants import K_LEFT, K_RIGHT, K_SPACE, K_UP, K_DOWN;

class Keys():
    def __init__(self) -> None:
        self.pressed = {"left": False, "right": False, "up": False, "down": False, "space": False}

    def updateControlsPressed(self, pressed):
        if pressed == K_LEFT:
            self.pressed["left"] = True
        if pressed == K_RIGHT:
            self.pressed["right"] = True
        if pressed == K_UP:
            self.pressed["up"] = True
        if pressed == K_DOWN:
            self.pressed["down"] = True
        if pressed == K_SPACE:
            self.pressed["space"] = True


    def updateControlsReleased(self, released):
        if released == K_LEFT:
            self.pressed["left"] = False
        if released == K_RIGHT:
            self.pressed["right"] = False
        if released == K_UP:
            self.pressed["up"] = False
        if released == K_DOWN:
            self.pressed["down"] = False
        if released == K_SPACE:
            self.pressed["space"] = False
