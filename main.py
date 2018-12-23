# TODO: Add camera classes
# TODO: Add attacking
# TODO: Get some graphics sorted
# TODO: Sort out animations

print("Starting...")

from json import load
assets = load(open("data/assets.json"))
players = load(open("data/players.json"))
settings = load(open("data/settings.json"))

import pygame
pygame.init()
screen = pygame.display.set_mode((settings["resolution"]["x"], settings["resolution"]["y"]))
pygame.display.set_caption("BaftaYGD")
clock = pygame.time.Clock()

"""Initialise Loading Screen""" # TODO: Move this into the game lib
import libs.loading
libs.loading.initiate(screen, libs.loading.rainbow[1:], 3)

"""Initialise Game"""
import libs.game
libs.game.game("playerName", "green_guy")

"""Initialise Sprites""" # TODO: Move this into the game lib
enemy = libs.sprites.enemy(
    name = "sgt_waffles",
    x = settings["resolution"]["x"] - 150,
    y = settings["resolution"]["y"] - 74,
    speed = 10
)
libs.game.sprites.append(enemy)

"""class gameResults:
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
            print("It's a draw!")"""

render = True
while render:
    clock.tick(30)
    """Event Handling"""
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            render = False
        """Key Events"""
        if not libs.loading.isLoading:
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_ESCAPE: render = False # TODO: Change this to an esc menu
                #DUCK_TRUE
                if i.key in [pygame.K_DOWN, pygame.K_s, pygame.K_LCTRL]: libs.game.char.duck(True)
                #ATTACK_TRUE
                if i.key == pygame.K_f:
                    libs.game.char.attack(True)
                    enemy.attack()
            if i.type == pygame.KEYUP:
                #DUCK_FALSE
                if i.key in [pygame.K_DOWN, pygame.K_s, pygame.K_LCTRL]: libs.game.char.duck(False)
                #ATTACK_FALSE
                if i.key == pygame.K_f: libs.game.char.attack(False)
            if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1: libs.game.char.attack(True)
            if i.type == pygame.MOUSEBUTTONUP and i.button == 1: libs.game.char.attack(False)
    screen.fill((255, 255, 255))
    # TODO: Make this an actual background
    if libs.loading.isLoading:
        if libs.loading.loadingFrame >= libs.loading.loadingTime:
            libs.loading.isLoading = False
            libs.loading.loadingFrame = 0
        pygame.draw.circle(screen, libs.loading.rainbow[0], (settings["resolution"]["x"]//2, settings["resolution"]["y"]//2), 5)
        for i in libs.loading.planets:
            i.update(screen)
        libs.loading.loadingFrame += 1
    else:
        """Keypresses"""
        keys = pygame.key.get_pressed()
        #LEFT
        if keys[pygame.K_LEFT]: libs.game.char.left()
        elif keys[pygame.K_a]: libs.game.char.left()
        #RIGHT
        if keys[pygame.K_RIGHT]: libs.game.char.right()
        elif keys[pygame.K_d]: libs.game.char.right()
        #JUMP
        if not libs.game.char.jumping:
            for i in [pygame.K_UP, pygame.K_w, pygame.K_SPACE]:
                if keys[i]:
                    libs.game.char.jumping = True
        else:
            if libs.game.char.jumpFrame >= -10:
                if libs.game.char.jumpFrame < 0:
                    fall = -1
                else:
                    fall = 1
                libs.game.char.y -= (libs.game.char.jumpFrame ** 2) / 2 * fall
                libs.game.char.jumpFrame -= 1
            else:
                libs.game.char.jumping = False
                libs.game.char.jumpFrame = 10
        #if libs.game.char.attacking
        """Mouse Positions"""
        mx, my = pygame.mouse.get_pos()
        #LEFT
        if mx <= 128:
            print("Left")
        #RIGHT
        elif mx >= settings["resolution"]["x"] - 128:
            print("Right")
        """Draw Sprites"""
        enemy.update()
        for i in libs.game.sprites:
            screen.blit(pygame.transform.flip(i.state, i.facingLeft, False), (i.x, i.y))
    pygame.display.update()

pygame.quit()
quit()
