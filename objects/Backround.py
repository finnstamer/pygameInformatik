from base.object.GameObject import GameObject

from settings import screenRes
class Backround(GameObject):
    def __init__(self,image) -> None:
        super().__init__()
        self.width = screenRes[0]
        self.height = screenRes[1]
        self.updateRect()
        self.setImage(image)
