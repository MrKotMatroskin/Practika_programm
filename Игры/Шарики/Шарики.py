from os import name
import pygame
import json
import pygame.freetype
from pygame.draw import *
from random import randint

pygame.font.init()
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()
zv2 = pygame.mixer.Sound("Звуки/звук_2.ogg")
zv3 = pygame.mixer.Sound("Звуки/звук_3.ogg")
fon1 = "Звуки/фон1.ogg"
fon2 = "Звуки/фон2.ogg"
fon3 = "Звуки/фон3.ogg"
fon4 = "Звуки/фон4.ogg"
MUSIC = [fon1, fon2, fon3, fon4]

# Переменные для циклов
clock = pygame.time.Clock()
finished1 = False
finished2 = False
finished3 = False
finished4 = False

# Громкость музыки и выбор музыки
track = 0
vol = 0.1

# Задание параметров текста
my_font = pygame.freetype.SysFont(None, 35)

# Счетчик времени и тиков
timecounter = 0
tickcounter = 0

# Время игровой сессии
gametime = 120

# Счетчик очков
ochki = 0

# Массивы для объектов
balls = []
kvadrats = []

# Зона смерти квадратов и шаров
killzonek = 10
killzoneb = 20

# Массивы для осколков/ каплей
kapli = []
oskolki = []

# Переменные для координат мышки
x = 0
y = 0

# Флаг для обработки паузы/ запуска фоновой музыки
Ps = False

# Флаг для стартового окна
q = 0

# Размеры экрана
a = 1500
b = 700

# Частота обновления экрана и ширина/ высота
screen = pygame.display.set_mode((a, b))
FPS = 60

# Создание поверхности с выводом очков
screensch = pygame.display.set_mode((a, b))

# Создание объектов вывода текста
text1 = pygame.font.Font(None, 72)
text2 = pygame.font.Font(None, 36)

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

    def __init__(self):  # Создание шара
        self.gx = 0
        self.gy = 0
        self.x = randint(0, a)
        self.y = randint(0, b)
        self.r = randint(20, 30)
        self.color = COLORS[randint(0, 5)]
        self.xspeed = randint(-10, 10)
        self.yspeed = randint(-5, 5)
        self.dx = 10
        self.dy = 10
        self.dxconst = self.dx
        self.dyconst = self.dy

    def motion(self):  # Расчет движения шара

        if (a - self.x - self.r <= self.dx) or (self.x - self.r <=
                                                self.dx):  # Проверка на наличие ускорения на оси х
            if min(a - self.x - self.r, self.x -
                                        self.r) == (a - self.x - self.r):
                self.gx = abs(
                    min(a - self.x - self.r, self.x - self.r) / 100) * -1
            else:
                self.gx = abs(min(a - self.x - self.r, self.x - self.r) / 100)
        else:
            self.gx = 0

        if (b - self.y - self.r <= self.dy) or (self.y - self.r <=
                                                self.dy):  # Проверка на наличие ускорения на оси у
            if min(b - self.y - self.r, self.y -
                                        self.r) == (b - self.y - self.r):
                self.gy = abs(
                    min(b - self.y - self.r, self.y - self.r) / 100) * -1
            else:
                self.gy = abs(min(b - self.y - self.r, self.y - self.r) / 100)
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

    def draw(self):  # Рисование шара

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

        ellipse(screen, self.color, (
            self.x - self.r - self.dx, self.y - self.r - self.dy, 2 * self.r + 2 * self.dx, 2 * self.r + 2 * self.dy))


# Класс объектов "Квадрат"
class Kvadrat:

    def __init__(self):  # Создание квадрата
        self.gx = 0
        self.gy = 0
        self.x = randint(0, a)
        self.y = randint(200, b - 100)
        self.r = randint(20, 30)
        self.color = COLORS[randint(0, 5)]
        self.xspeed = 0  # randint(-5, 5)
        self.yspeed = 0  # randint(-5, 5)

    def motion(self):  # Расчет движения квадрата
        self.gx = randint(-2, 2) / 2
        self.gy = randint(-1, 1) / 2
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

    def draw(self):  # Рисование квадрата
        rect(
            screen,
            self.color,
            (self.x - self.r,
             self.y - self.r,
             2 * self.r,
             2 * self.r))


class Kaplya:

    def __init__(self, xx, yy, speed, color):
        self.g = 1
        self.x = xx
        self.y = yy
        self.r = randint(5, 10)
        self.color = color
        self.xspeed = (randint(-1, 1) + speed) * 2
        self.yspeed = randint(-5, 5)

    def motion(self):
        self.yspeed = self.yspeed + self.g
        self.x = int(self.x + self.xspeed)
        self.y = int(self.y + self.yspeed)
        if self.y > a + 10:
            self.yspeed = 0

    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)


class Oskolok:

    def __init__(self, xx, yy, speed, color):
        self.g = 1
        self.x = xx
        self.y = yy
        self.r = randint(5, 10)
        self.color = color
        self.xspeed = (randint(-1, 1) + speed) * 2
        self.yspeed = randint(-5, 5)

    def motion(self):
        self.yspeed = self.yspeed + self.g
        self.x = int(self.x + self.xspeed)
        self.y = int(self.y + self.yspeed)
        if self.y > a + 10:
            self.yspeed = 0

    def draw(self):
        rect(
            screen,
            self.color,
            (self.x - self.r,
             self.y - self.r,
             2 * self.r,
             2 * self.r))


for i in range(kb):
    ball = Ball()
    balls.append(ball)

for i in range(kk):
    kvadrat = Kvadrat()
    kvadrats.append(kvadrat)
ch = ""
while not finished3:  # Меню игры

    clock.tick(FPS)

    text = text1.render(
        "Тапните мышью в любом месте, чтобы продолжить",
        True,
        BLUE)
    screensch.blit(text, (a / 2 - 700, b / 2))
    text = text1.render(
        "Чтобы изменять музыку, используйте стрелки",
        True,
        BLUE)
    screensch.blit(text, (a / 2 - 700, b / 2 + 70))
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                finished3 = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if vol < 1:
                    vol = vol + 0.1
                else:
                    vol = 1
                pygame.mixer.music.set_volume(vol)
            elif event.key == pygame.K_DOWN:
                if vol > 0:
                    vol = vol - 0.1
                else:
                    vol = 0
                pygame.mixer.music.set_volume(vol)
            elif event.key == pygame.K_RIGHT:
                if track < 3:
                    track = track + 1
                else:
                    track = 3
                pygame.mixer.music.load(MUSIC[track])
                pygame.mixer.music.play(-1)
            elif event.key == pygame.K_LEFT:
                if track > 0:
                    track = track - 1
                else:
                    track = 0
                pygame.mixer.music.load(MUSIC[track])
                pygame.mixer.music.play(-1)
            elif event.key == pygame.K_BACKSPACE:
                ch = ch[:-1]
            elif int(event.key) <= 126 and int(event.key) >= 33:
                ch += pygame.key.name(event.key)
            if event.key == pygame.K_SPACE:
                Ps = not Ps
                if Ps:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
    if ch == "bkz1201":
        killzonek = 700
        killzoneb = killzonek
    pygame.display.update()
    screen.fill(GREY)

while not finished1 and timecounter <= gametime:

    clock.tick(FPS)
    tickcounter = tickcounter + 1
    timecounter = tickcounter // FPS
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished1 = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if vol < 1:
                        vol = vol + 0.1
                    else:
                        vol = 1
                    pygame.mixer.music.set_volume(vol)
                elif event.key == pygame.K_DOWN:
                    if vol > 0:
                        vol = vol - 0.1
                    else:
                        vol = 0
                    pygame.mixer.music.set_volume(vol)
                elif event.key == pygame.K_RIGHT:
                    if track < 3:
                        track = track + 1
                    else:
                        track = 3
                    pygame.mixer.music.load(MUSIC[track])
                    pygame.mixer.music.play(-1)
                elif event.key == pygame.K_LEFT:
                    if track > 0:
                        track = track - 1
                    else:
                        track = 0
                    pygame.mixer.music.load(MUSIC[track])
                    pygame.mixer.music.play(-1)
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
                    if ((ball.x - x) ** 2 + (ball.y - y) **
                        2) ** 0.5 <= ball.r + ball.dxconst + killzoneb:
                        zv2.play()
                        k1 = randint(5, 10)
                        for i in range(k1):
                            kaplya = Kaplya(int(ball.x), int(
                                ball.y), ball.xspeed, ball.color)
                            kapli.append(kaplya)
                        balls.remove(ball)
                        ball = Ball()
                        balls.append(ball)
                        ochki = ochki + 10
                for kvadrat in kvadrats:
                    if (abs(kvadrat.x - x) + abs(kvadrat.y - y)
                    ) <= 2 * kvadrat.r + killzonek:
                        zv3.play()
                        k2 = randint(5, 10)
                        for i in range(k2):
                            oskolok = Oskolok(int(kvadrat.x), int(
                                kvadrat.y), kvadrat.xspeed, kvadrat.color)
                            oskolki.append(oskolok)
                        kvadrats.remove(kvadrat)
                        kvadrat = Kvadrat()
                        kvadrats.append(kvadrat)
                        ochki = ochki + 100

    for kaplya in kapli:
        if kaplya.y > a:
            kapli.remove(kaplya)

    for oskolok in oskolki:
        if oskolok.y > a:
            oskolki.remove(oskolok)

    schetv = text2.render("score:" + " " + str(ochki), True, (180, 0, 0))
    timev = text2.render(str(timecounter) + "/" +
                         str(gametime), True, (180, 0, 0))
    screensch.blit(schetv, (100, 50))
    screensch.blit(timev, (100, 100))
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

pygame.mixer.music.pause()

# Ввод ника
finished2 = False
name = ""
while not finished2:
    screen.fill(GREY)
    my_font.render_to(screen, (100, 100), "Введите ник:", BLUE)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                finished2 = True
            elif event.key == pygame.K_ESCAPE:
                finished2 = True
            elif event.key == pygame.K_BACKSPACE:
                name = name[:-1]
            elif int(event.key) <= 126 and int(event.key) >= 33 or int(event.key) <= 1103 and int(event.key) >= 1040:
                name += pygame.key.name(event.key)
        my_font.render_to(screen, (100, 140), name, BLUE)
        pygame.display.update()

with open(r"r.json") as f:
    data = json.load(f)
data[name] = ochki
h = 200
# Выводим таблицу рекордов
screen.fill(GREY)
rec = []
for k, v in data.items():
    rec.append([v, k])
rec.sort(reverse=True)
for i in rec:
    my_font.render_to(screen, (a / 2 - 50, h),
                      i[1] + ":" + " " + str(i[0]), (255, 255, 255))
    h += 30
pygame.display.update()
finished = False
while not finished:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.key == pygame.K_ESCAPE:
            finished = True
with open(r"r.json", 'w') as f:
    json.dump(data, f)
pygame.quit()
