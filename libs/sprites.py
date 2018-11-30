# TODO: Create enemy and friendly sprites
# TODO: Move jumping and other character rendering stuff into here
# TODO: Try to move controls into here idk

from json import load
settings = load(open("data/settings.json"))

class player:
    def __init__(self, frames, x, y, width, height, speed):
        self.frames = frames
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        #Set non-argument variables
        self.facingRight = False
        self.jumping = False
        self.ducking = False
        self.jumpFrame = 10
        self.attacking = False
        self.attackFrame = 0
    def left(self):
        #if self.x > 0:
        self.facingRight = False
        self.x -= self.speed
    def right(self):
        #if self.x < settings["resolution"]["x"] - self.width:
        self.facingRight = True
        self.x += self.speed
    def duck(self, state):
        if self.y < settings["resolution"]["y"] - self.height:
            # TODO: Replace this with an image asset
            if state and not self.ducking:
                self.ducking = True
                self.y += 5
            elif self.ducking:
                self.ducking = False
                self.y -= 5
    def attack(self, state):
        # TODO: Make attacking
        if state and not self.attacking:
            self.attacking = True
            print("Attacking")
        elif self.attacking:
            self.attacking = False
            print("Attacked")
    #def characterSelection(self):
        #self.character = input("Please select a character")
    def draw(self):
        print()

class friendly:
    oof = "yes"

class enemy:
    oof = "yes"
