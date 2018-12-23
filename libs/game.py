from json import load
#assets = load(open("data/assets.json"))
#players = load(open("data/players.json"))
settings = load(open("data/settings.json"))

import libs.sprites

char = object()
sprites = list()

class game:
    def __init__(self, playerName, playerSkin):
        global char
        self.playerName = playerName
        char = libs.sprites.player(
            name = playerSkin,
            x = 0,
            y = settings["resolution"]["y"] - 74,
            speed = 10
        )
        sprites.append(char)
