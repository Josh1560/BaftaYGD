print("Starting...")

import pygame

from json import load
settings = load(open("data/settings.json"))

pygame.init()
screen = pygame.display.set_mode((settings["resolution"]["x"], settings["resolution"]["y"]))
pygame.display.set_caption("BaftaYGD")

class character:
    def __init__(self, x, y, width, height, velocity):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.velocity = velocity

char = character(
    x = 100,
    y = 50,
    width = 60,
    height = 60,
    velocity = 5
)

active = True
while active:
    pygame.time.delay(10)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            active = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        char.x -= char.velocity
    if keys[pygame.K_RIGHT]:
        char.x += char.velocity
    if keys[pygame.K_UP]:
        char.y -= char.velocity
    if keys[pygame.K_DOWN]:
        char.y += char.velocity
    pygame.draw.rect(screen, (255, 0, 0), (char.x, char.y, char.width, char.height))
    pygame.display.update()

pygame.quit()
