# TODO: Create enemy and friendly sprites
# TODO: Move jumping and other character rendering stuff into here
# TODO: Try to move controls into here idk

from pygame import image

class player:
    def __init__(self, path, x, y, width, height, speed):
        self.standing = image.load("{}/stand.png".format(path))
        self.crouching = image.load("{}/crouch.png".format(path))
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
        #Set non-argument variables
        self.facingLeft = False
        self.jumping = False
        self.ducking = False
        self.jumpFrame = 10
        self.attacking = False
        self.attackFrame = 0
        self.state = self.standing
    def left(self):
        #if self.x > 0:
        self.facingLeft = True
        self.x -= self.speed
    def right(self):
        #if self.x < settings["resolution"]["x"] - self.width:
        self.facingLeft = False
        self.x += self.speed
    def duck(self, state):
        if state and not self.ducking:
            self.ducking = True
            self.state = self.crouching
        elif self.ducking:
            self.ducking = False
            self.state = self.standing
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
    #def draw(self):
        #screen.blit(pygame.transform.flip(self.state, self.facingLeft, False), (self.x, self.y))

class friendly:
    oof = "yes"

class enemy:
    oof = "yes"
