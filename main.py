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
    def __init__(self, color, x, y, width, height, velocity):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity
    jumping = False
    ducking = False
    jumpCount = 10
    def left(self):
        if self.x > 0:
            self.x -= self.velocity
    def right(self):
        if self.x < settings["resolution"]["x"] - self.width:
            self.x += self.velocity
    def duck(self, state):
        if self.y < settings["resolution"]["y"] - self.height:
            if state and not self.ducking:
                self.ducking = True
                self.y += self.velocity
                # TODO: Replace this with an image asset
            else:
                self.ducking = False
                self.y -= self.velocity
                # TODO: Replace this with an image asset
    def attack(self):
        print("coming soon ;)")
        # TODO: Make attacking
    def characterSelection(self):
        self.character = input("Please select a character")
        # TODO: Replace this with an image asset

class enemy:
    def __init__(self, color, x, y, width, height, velocity):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity

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
    x = 100,
    y = settings["resolution"]["y"] - 70,
    width = 60,
    height = 60,
    velocity = 5
)

gameActive = True
while gameActive:
    pygame.time.delay(10)
    """Pygame Events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameActive = False
        """Key Events"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                char.duck(True)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                char.duck(False)
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
        if char.jumpCount >= -10:
            if char.jumpCount < 0:
                fall = -1
            else:
                fall = 1
            char.y -= (char.jumpCount ** 2) / 2 * fall
            char.jumpCount -= 1
        else:
            char.jumping = False
            char.jumpCount = 10
    #ATTACK
    if keys[pygame.K_f]: char.attack()
    """Display all of this stuff"""
    screen.fill((0))
    pygame.draw.rect(screen, char.color, (char.x, char.y, char.width, char.height))
    pygame.display.update()

pygame.quit()
quit()
