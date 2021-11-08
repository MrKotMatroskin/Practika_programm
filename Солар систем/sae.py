from os import name
import pygame
import math
import pygame.freetype
from pygame.draw import *
from random import randint

pygame.init()

# Переменные для циклов
clock = pygame.time.Clock()
finished = False


# Счетчик времени и тиков
timecounter = 0
tickcounter = 0

# Время игровой сессии
gametime = 60

# Массивы для объектов
balls = []
kvadrats = []

# Массивы для осколков/ каплей
kapli = []
oskolki = []

# Переменные для координат мышки
x = 0
y = 0

# Размеры экрана
a = 1920
b = 1080

# Частота обновления экрана и ширина/ высота
screen = pygame.display.set_mode((a, b))
FPS = 60

# Количество шаров и кубов
kb = 10
kk = 10

# Цвета
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GREY = (250, 250, 250)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK]

class Planet:
    def __init__(self, mass, x, y, r, speedx, speedy):  # Создание шара
        self.mass = mass
        self.G = 26 #0.001
        self.x = x
        self.y = y
        self.r = r
        self.color = BLACK
        self.xspeed = speedx
        self.yspeed = speedy
        self.F = 0
        self.Fx = 0
        self.Fy = 0
        self.ax = 0
        self.ay = 0
        self.an = 0
    def acssiliration(self, obj):  # Расчет движения шара
        if obj.x > self.x:
            self.an = math.atan((-obj.y + self.y) / (obj.x - self.x))
        if obj.x < self.x:
            self.an = math.pi + math.atan((-obj.y + self.y) / (obj.x - self.x))
        if obj.x == self.x:
            self.an = math.pi / 2
        self.F += self.G*((self.mass*obj.mass)/((self.x-obj.x)**2+(self.y-obj.y)**2))
        self.Fx += self.F*math.cos(self.an)
        self.Fy -= self.F*math.sin(self.an)
        self.ax += self.Fx/self.mass
        self.ay += self.Fy/self.mass

    def motion(self):
        self.xspeed += self.ax
        self.yspeed += self.ay
        self.x += self.xspeed
        self.y += self.yspeed
        self.F = 0
        self.Fx = 0
        self.Fy = 0
        self.ax = 0
        self.ay = 0

    def draw(self):  # Рисование шара
        circle(screen, self.color, (int(self.x), int(self.y)), int(self.r))
        #line(screen, self.color, (int(self.x), int(self.y)), (math.cos(self.an) * self.F + self.x, -(math.sin(self.an) * self.F) + self.y), 2)
        #line(screen, self.color, (int(self.x), int(self.y)), (self.Fx/10 + self.x, self.y), 2)
        #line(screen, self.color, (int(self.x), int(self.y)), (self.x, self.Fy/10 + self.y), 2)
planet1 = Planet(100, 960, 800, 30, 10, 0)
planet2 = Planet(1000, 960, 540, 50, -1, 0)
balls.append(planet1)
balls.append(planet2)
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True
    planet1.acssiliration(planet2)
    planet1.motion()
    planet2.acssiliration(planet1)
    planet2.motion()
    planet1.draw()
    planet2.draw()
    #print(planet1.an)
    #print(planet2.an)
    #print(" ")
    pygame.display.update()
    screen.fill(GREY)
pygame.quit()
