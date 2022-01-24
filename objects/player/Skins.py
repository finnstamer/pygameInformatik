from base.core.Object.Factory import Factory


class Skins():
    skins = {0: "images/player/skin1.png", 1: "images/player/skin2.png"}
    currentSkin = 1

    def apply():
        if Factory.isRegistered("player"):
            Factory.get("player").setImage(Skins.skins[Skins.currentSkin])
        
    def setCurrentSkin(skin: int):
        Skins.currentSkin = skin
        Skins.apply()