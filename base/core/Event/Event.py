# Klasse zuer Erhaltung des Namens oder der mitgelieferten Paramter
class Event():
    def __init__(self, name="", value="") -> None:
        self.name: str = name
        self.value = value
    
    def isOfType(self, str):
        return str in self.name.split(".")