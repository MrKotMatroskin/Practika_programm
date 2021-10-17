import pygame
from pygame.draw import *
from random import randint
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
zv1 = pygame.mixer.Sound("Звуки/звук_1.ogg")
zv2 = pygame.mixer.Sound("Звуки/звук_2.ogg")
zv3 = pygame.mixer.Sound("Звуки/звук_3.ogg")
pygame.mixer.music.load("Звуки/фон.ogg")
pygame.mixer.music.play(-1)

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
GREY = (150, 150, 250)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN, BLACK]

# Класс объектов "Шар"
class Ball:

    def __init__(self): # Создание шара
        self.gx = 0
        self.gy = 0
        self.x = randint(0, a)
        self.y = randint(0, b)
        self.r = randint(20, 30)
        self.color = COLORS[randint(0, 5)]
        self.xspeed = randint(-5, 5)
        self.yspeed = randint(-5, 5)
        self.dx = 10
        self.dy = 10
        self.dxconst = self.dx
        self.dyconst = self.dy

    def motion(self): # Расчет движения шара

        if (a - self.x - self.r <= self.dx) or (self.x - self.r <= self.dx): # Проверка на наличие ускорения на оси х
            if min(a - self.x - self.r, self.x - self.r) == (a - self.x - self.r):
                self.gx = abs(min(a - self.x - self.r, self.x - self.r) / 1000) * -1
            else:
                self.gx = abs(min(a - self.x - self.r, self.x - self.r) / 1000)
        else:
            self.gx = 0

        if (b - self.y - self.r <= self.dy) or (self.y - self.r <= self.dy): # Проверка на наличие ускорения на оси у
            if min(b - self.y - self.r, self.y - self.r) == (b - self.y - self.r):
                self.gy = abs(min(b - self.y - self.r, self.y - self.r) / 1000) * -1
            else:
                self.gy = abs(min(b - self.y - self.r, self.y - self.r) / 1000)
        else:
            self.gy = 0

        if (self.x + self.r <= a) and (self.x - self.r >= 0):
            self.xspeed = self.xspeed + self.gx
            self.x = self.x + self.xspeed
        else:
            if self.x + self.r >= a:
                self.x = a - self.r
            if self.x - self.r <= 0:
                self.x = self.r
            self.xspeed = self.xspeed * -1
            self.xspeed = self.xspeed + self.gx
            self.x = self.x + self.xspeed

        if (self.y + self.r <= b) and (self.y - self.r >= 0):
            self.yspeed = self.yspeed + self.gy
            self.y = self.y + self.yspeed
        else:
            if self.y + self.r >= b:
                self.y = b - self.r
            if self.y - self.r <= 0:
                self.y = self.r
            self.yspeed = self.yspeed * -1
            self.yspeed = self.yspeed + self.gy
            self.y = self.y + self.yspeed

    def draw(self): # Рисование шара

        if (self.x + self.r + self.dx <= a) and (self.x - self.r - self.dx >= 0):
            self.dx = self.dxconst
        else:
            if self.x + self.r + self.dx >= a:
                self.dx = a - self.x - self.r
            if self.x - self.r - self.dx <= 0:
                self.dx = self.x - self.r

        if (self.y + self.r + self.dy <= b) and (self.y - self.r - self.dy >= 0):
            self.dy = self.dyconst
        else:
            if self.y + self.r + self.dy >= b:
                self.dy = b - self.y - self.r
            if self.y - self.r - self.dy <= 0:
                self.dy = self.y - self.r

        ellipse(screen, self.color, (self.x - self.r - self.dx, self.y - self.r - self.dy, 2*self.r + 2*self.dx, 2*self.r + 2*self.dy))

# Класс объектов "Квадрат"
class Kvadrat:

    def __init__(self): # Создание квадрата
        self.gx = 0
        self.gy = 0
        self.x = randint(0, a)
        self.y = randint(200, b-100)
        self.r = randint(20, 30)
        self.color = COLORS[randint(0, 5)]
        self.xspeed = 0 #randint(-5, 5)
        self.yspeed = 0 #randint(-5, 5)

    def motion(self): # Расчет движения квадрата
        self.gx = randint(-2, 2)/2
        self.gy = randint(-1, 1)/2
        if (self.x + self.r <= a) and (self.x - self.r >= 0):
            self.xspeed = self.xspeed + self.gx
            self.x = self.x + self.xspeed
        else:
            if self.x + self.r >= a:
                self.x = a - self.r
            if self.x - self.r <= 0:
                self.x = self.r
            self.xspeed = self.xspeed * -0.6
            self.xspeed = self.xspeed + self.gx
            self.x = self.x + self.xspeed

        if (self.y + self.r <= b) and (self.y - self.r >= 0):
            self.yspeed = self.yspeed + self.gy
            self.y = self.y + self.yspeed
        else:
            if self.y + self.r >= b:
                self.y = b - self.r
            if self.y - self.r <= 0:
                self.y = self.r
            self.yspeed = self.yspeed * -0.6
            self.yspeed = self.yspeed + self.gy
            self.y = self.y + self.yspeed

    def draw(self): # Рисование квадрата
        rect(screen, self.color, (self.x - self.r, self.y - self.r, 2*self.r, 2*self.r))

class Kaplya:

    def __init__(self, xx, yy, color):
        self.g = 1
        self.x = xx
        self.y = yy
        self.r = randint(5, 10)
        self.color = color
        self.xspeed = randint(-10, 10)
        self.yspeed = randint(-5, 5)

    def motion(self):
        self.yspeed = self.yspeed + self.g
        self.x = self.x + self.xspeed
        self.y = self.y + self.yspeed
    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)

class Oskolok:

    def __init__(self, xx, yy, color):
        self.g = 1
        self.x = xx
        self.y = yy
        self.r = randint(5, 10)
        self.color = color
        self.xspeed = randint(-10, 10)
        self.yspeed = randint(-5, 5)

    def motion(self):
        self.yspeed = self.yspeed + self.g
        self.x = self.x + self.xspeed
        self.y = self.y + self.yspeed
    def draw(self):
        rect(screen, self.color, (self.x - self.r, self.y - self.r, 2*self.r, 2*self.r))

balls = []
kvadrats = []

for i in range(kb):
    ball = Ball()
    balls.append(ball)

for i in range(kk):
    kvadrat = Kvadrat()
    kvadrats.append(kvadrat)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

x = 0
y = 0
kapli = []
oskolki = []
Ps = False

q = 0

while q == 0: # Меню игры

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                q=1
            else:
                q=0

    pygame.display.update()
    screen.fill(GREY)


while not finished:

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Ps = not Ps
                if Ps:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x, y = event.pos
                for ball in balls:
                    if ((ball.x-x)**2+(ball.y-y)**2)**0.5 <= ball.r:
                        zv2.play()
                        k1 = randint(5, 20)
                        for i in range(k1):
                            kaplya = Kaplya(ball.x, ball.y, ball.color)
                            kapli.append(kaplya)
                        balls.remove(ball)
                        ball = Ball()
                        balls.append(ball)
                for kvadrat in kvadrats:
                    if (abs(kvadrat.x - x) + abs(kvadrat.y - y)) <= 2 * kvadrat.r:
                        zv3.play()
                        k2 = randint(5, 20)
                        for i in range (k2):
                            oskolok = Oskolok(kvadrat.x, kvadrat.y, kvadrat.color)
                            oskolki.append(oskolok)
                        kvadrats.remove(kvadrat)
                        kvadrat = Kvadrat()
                        kvadrats.append(kvadrat)
    for ball in balls:
        ball.motion()
        ball.draw()

    for kaplya in kapli:
        kaplya.motion()
        kaplya.draw()

    for kvadrat in kvadrats:
        kvadrat.motion()
        kvadrat.draw()

    for oskolok in oskolki:
        oskolok.motion()
        oskolok.draw()

    pygame.display.update()
    screen.fill(GREY)

pygame.quit()
