import math
from pygame import draw
from random import randint

from json import load
settings = load(open("data/settings.json"))

isLoading = True
colors = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (255, 0, 255)]
planets = []

class planet:
    def __init__(self, point, screen, color):
        self.pointX = point
        self.pointY = 0
        self.screen = screen
        self.rect = draw.rect(self.screen, (color), (settings["resolution"]["x"]//2 - point, settings["resolution"]["y"]//2 - point, point*2, point*2))
        self.color = color
        #Set non-argument variables
        self.speed = randint(1, 10)/100
        self.cos = math.cos(self.speed)
        self.sin = math.sin(self.speed)
    def update(self):
        x = self.pointX * self.cos - self.pointY * self.sin
        y = self.pointY * self.cos + self.pointX * self.sin
        self.pointX = x
        self.pointY = y
        draw.circle(self.screen, self.color, (round(self.pointX) + settings["resolution"]["x"]//2, round(self.pointY) + settings["resolution"]["y"]//2), 5)
        angle = math.atan2(self.pointX, self.pointY)
        draw.arc(self.screen, self.color, self.rect, angle - math.pi/2, angle + math.pi/4, 2)

def initiate(screen, colors):
    for i in range(len(colors)):
        planets.append(planet((i + 1) * 25, screen, colors[i]))

def update():
    for i in planets:
        i.update()
