print("Starting...")

# TODO: Change resolution to something easier to manage/less lines
# TODO: Add panning to the right when the mouse if on the right of the screen
# TODO: Dont rely on FPS clock for movement AKA stop higher fps means faster movement
# TODO: Add attacking
# TODO: Check if multi-threading exists in Pygame, use it if possible

# CONCEPT: SKIN: Platypus
# CONCEPT: SKIN: Dinosaur
# CONCEPT: SKIN: Doggo
# CONCEPT: SKIN: Kitty cat

import pygame

from json import load
settings = load(open("data/settings.json"))

pygame.init()
screen = pygame.display.set_mode((settings["resolution"]["x"], settings["resolution"]["y"]))
pygame.display.set_caption("BaftaYGD")

class character:
    def __init__(self, color, x, y, width, height, speed):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed
    jumping = False
    ducking = False
    jumpFrame = 10
    attacking = False
    attackFrame = 0
    def left(self):
        #if self.x > 0:
        self.x -= self.speed
    def right(self):
        #if self.x < settings["resolution"]["x"] - self.width:
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
    def characterSelection(self):
        self.character = input("Please select a character")
        # TODO: Replace this with image assets
    def update(self):
        print()

class enemy:
    def __init__(self, color, x, y, width, height, speed):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

class gameResults:
    def victory():
        if remainingWaffles == 0:
            print("Victory")
            # TODO: Replace this with an image asset
    def loss():
        if remainingLives == 0:
            print("Mission Failed (We'll get them next time)")
            # TODO: Replace this with an image asset
    def stalemate():
        if remaininTime == 0:
            print("It's a draw!")


char = character(
    color = (255, 0, 0),
    x = 0,
    y = settings["resolution"]["y"] - 70,
    width = 60,
    height = 60,
    speed = 10
)

render = True
while render:
    pygame.time.delay(10)
    """Pygame Events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            render = False
        """Key Events"""
        # TODO: Try to shorten these lines
        if event.type == pygame.KEYDOWN:
            #DUCK_TRUE
            if event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_LCTRL:
                char.duck(True)
            #ATTACK_TRUE
            if event.key == pygame.K_f: char.attack(True)
        if event.type == pygame.KEYUP:
            #DUCK_FALSE
            if event.key == pygame.K_DOWN or event.key == pygame.K_s or event.key == pygame.K_LCTRL:
                char.duck(False)
            #ATTACK_FALSE
            if event.key == pygame.K_f: char.attack(False)
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: char.attack(True)
        if event.type == pygame.MOUSEBUTTONUP and event.button == 1: char.attack(False)
    """Keypresses"""
    keys = pygame.key.get_pressed()
    #LEFT
    if keys[pygame.K_LEFT]: char.left()
    elif keys[pygame.K_a]: char.left()
    #RIGHT
    if keys[pygame.K_RIGHT]: char.right()
    elif keys[pygame.K_d]: char.right()
    #JUMP
    if not char.jumping:
        if keys[pygame.K_UP]: char.jumping = True
        elif keys[pygame.K_w]: char.jumping = True
        elif keys[pygame.K_SPACE]: char.jumping = True
    else:
        if char.jumpFrame >= -10:
            if char.jumpFrame < 0:
                fall = -1
            else:
                fall = 1
            char.y -= (char.jumpFrame ** 2) / 2 * fall
            char.jumpFrame -= 1
        else:
            char.jumping = False
            char.jumpFrame = 10
    #if char.attacking
    """Mouse Positions"""
    mx, my = pygame.mouse.get_pos()
    #RIGHT
    if mx >= settings["resolution"]["x"] - 128:
        print("Right")
    #LEFT
    elif mx <= 128:
        print("Left")
    """Render screen"""
    screen.fill((0))
    pygame.draw.rect(screen, char.color, (char.x, char.y, char.width, char.height))
    pygame.display.update()

pygame.quit()
quit()
