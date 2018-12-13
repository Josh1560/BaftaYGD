# TODO: Create enemy and friendly sprites
# TODO: Move jumping and other character rendering stuff into here
# TODO: Try to move controls into here idk

from json import load
assets = load(open("data/assets.json"))

from pygame import image

class player:
    def __init__(self, path, x, y, speed):
        self.standing = image.load("{}/stand.png".format(path))
        self.crouching = image.load("{}/crouch.png".format(path))
        #self.jumping = image.load("{}/jump.png".format(path))
        self.x = x
        self.y = y
        self.speed = speed
        #Set non-argument variables
        self.facingLeft = False
        self.jumping = False
        self.ducking = False
        self.jumpFrame = 10
        self.attacking = False
        #self.attackFrame = 0
        self.state = self.standing
    def left(self):
        self.facingLeft = True
        self.x -= self.speed
    def right(self):
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
    def __init__(self, name, x, y, speed):
        path = assets["enemySkins"][name]["path"]
        self.green = image.load("{}/aiming_green.png".format(path))
        self.amber = image.load("{}/aiming_amber.png".format(path))
        self.red = image.load("{}/aiming_red.png".format(path))
        #self.crouching = image.load("{}/crouch.png".format(path))
        #self.jumping = image.load("{}/jump.png".format(path))
        self.x = x
        self.y = y
        self.speed = speed
        self.attackTime = assets["enemySkins"][name]["attackTime"]
        #Set non-argument variables
        self.attacking = False
        self.attackFrame = 0
        self.state = self.green
    def attack(self):
        if not self.attacking:
            self.state = self.amber
            self.attacking = True
        #else:
            #print("That kinda shouldnt happen, pls fix")
    def update(self):
        if self.attacking:
            if self.attackFrame >= 30 * self.attackTime:
                self.attacking = False
                self.attackFrame = 0
                self.state = self.green
            elif self.attackFrame >= (30 * self.attackTime) - 20:
                self.state = self.red
            self.attackFrame += 1
