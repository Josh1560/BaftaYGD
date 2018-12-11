print("Starting...")

# TODO: Add camera classes
# TODO: Add attacking
# TODO: Get some graphics sorted
# TODO: Sort out animations

# CONCEPT: SKIN: Platypus
# CONCEPT: SKIN: Dinosaur
# CONCEPT: SKIN: Doggo
# CONCEPT: SKIN: Kitty cat

import pygame

from json import load
settings = load(open("data/settings.json"))
assets = load(open("data/assets.json"))

pygame.init()
screen = pygame.display.set_mode((settings["resolution"]["x"], settings["resolution"]["y"]))
pygame.display.set_caption("BaftaYGD")
clock = pygame.time.Clock()

import libs.loading
libs.loading.initiate(screen, (libs.loading.colors[1:]))

import libs.sprites
char = libs.sprites.player(
    path = assets["playerSkins"]["green_guy"]["path"],
    x = 0,
    y = settings["resolution"]["y"] - 74,
    width = 64,
    height = 64,
    speed = 10
)

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

render = True
while render:
    clock.tick(30)
    """Pygame Events"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            render = False
        """Key Events"""
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: render = False
            #DUCK_TRUE
            if event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_LCTRL]: char.duck(True)
            #ATTACK_TRUE
            if event.key == pygame.K_f: char.attack(True)
        if event.type == pygame.KEYUP:
            #DUCK_FALSE
            if event.key in [pygame.K_DOWN, pygame.K_s, pygame.K_LCTRL]: char.duck(False)
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
        for i in [pygame.K_UP, pygame.K_w, pygame.K_SPACE]:
            if keys[i]:
                char.jumping = True
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
    #LEFT
    if mx <= 128:
        print("Left")
    #RIGHT
    elif mx >= settings["resolution"]["x"] - 128:
        print("Right")
    """Render screen"""
    screen.fill((255, 255, 255))
    """Loading"""
    if libs.loading.isLoading:
        libs.loading.update()
        pygame.draw.circle(screen, libs.loading.colors[0], (settings["resolution"]["x"]//2, settings["resolution"]["y"]//2), 5)
    screen.blit(pygame.transform.flip(char.state, char.facingLeft, False), (char.x, char.y))
    pygame.display.update()

pygame.quit()
quit()
