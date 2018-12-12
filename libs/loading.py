import math
from pygame import draw
from random import randint

from json import load
settings = load(open("data/settings.json"))

isLoading = False
loadingTick = int()
loadingTime = int()
rainbow = [(255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (255, 0, 255)]
planets = list()

class planet:
    def __init__(self, screen, point, color):
        self.rect = draw.rect(screen, (0), (settings["resolution"]["x"]//2 - point, settings["resolution"]["y"]//2 - point, point*2, point*2))
        self.color = color
        self.pointX = point
        #Set non-argument variables
        self.pointY = 0
        self.speed = randint(1, 10)/100
        self.cos = math.cos(self.speed)
        self.sin = math.sin(self.speed)
    def update(self, screen):
        x = self.pointX * self.cos - self.pointY * self.sin
        y = self.pointY * self.cos + self.pointX * self.sin
        self.pointX = x
        self.pointY = y
        draw.circle(screen, self.color, (round(self.pointX) + settings["resolution"]["x"]//2, round(self.pointY) + settings["resolution"]["y"]//2), 5)
        angle = math.atan2(self.pointX, self.pointY)
        draw.arc(screen, self.color, self.rect, angle - math.pi/2, angle + math.pi/4, 2)

def initiate(screen, colors, time):
    global isLoading, loadingTime, planets
    isLoading = True
    loadingTime = 30 * time
    planets = list()
    for i in range(len(colors)):
        planets.append(planet(screen, (i + 1) * 25, colors[i]))
