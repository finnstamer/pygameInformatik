from base.object.GameObject import GameObject


class Backround(GameObject):
    def __init__(self,image) -> None:
        super().__init__()
        self.height = 260
        self.width = 480
        self.updateRect()
        self.setImage(image)
