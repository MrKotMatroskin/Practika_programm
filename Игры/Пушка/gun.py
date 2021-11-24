import math
import random
import keyboard
from random import choice
import pygame
import pygame.freetype
from pygame.draw import *

pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.font.init()
pygame.init()
# Ускорение свободного падения
g = 2
# Громкость музыки и выбор музыки (менять не надо)
track = 0
vol = 0.5
# Разброс снарядов (+- по x и +- по y)
razbros = 0
# Количество жизний целей, бота, игрока
livetarget = 3
livebot = 10
livegun = 5
# Задаем ширину и высоту окна
WIDTH = 1500
HEIGHT = 700
# Делаем поверхности
screen = pygame.display.set_mode((WIDTH, HEIGHT))
boomscr = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
# Вывод текста
text2 = pygame.font.Font(None, 36)
text1 = pygame.font.Font(None, 150)
# Различные счетчики
schet = 0  # Счетчик счета
schetcounter = 0  # Счетчик тысяч очков, нужно для призыва нового бота
FPS = 60
clock = pygame.time.Clock()
tickcounter = 0  # Счетчик тиков до перезарядки
tcglobal = 0  # Глобальный счетчик тиков
tcshoot = 0  # Запоминает время предыдущего выстрела игрока
# Массивы
balls = []  # Снаряды
targets = []  # Пассивные цели
kapli = []  # Капли эффекта убийства
booms = []  # Эффект взрыва
# Флаги
Ps = True  # Флаг паузы музыки
Flag = True  # Изменение режима управления, сейчас управление мышкой
finished = False  # Флаг выхода из основного цикла
kt = 2  # Количество пассивных целейd
auto = 0  # Отвечает за включение автоматического режима стрельбы тройным снарядом
# Цвета
RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
# Музыка и звуки
pulemet = pygame.mixer.Sound("Звуки/pulemet.ogg")
pulemet.set_volume(0.1)
fon1 = "Звуки/фон1.ogg"
fon2 = "Звуки/фон2.ogg"
fon3 = "Звуки/фон3.ogg"
fon4 = "Звуки/фон4.ogg"
MUSIC = [fon1, fon2, fon3, fon4]


class Ball:
    def __init__(self, screen: pygame.Surface):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        g - ускорение свободного падения
        """
        self.screen = screen
        self.g = g
        self.x = 40
        self.y = 450
        self.r = random.randint(20, 20)
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна. Слева и сверху стен нет.
        """
        if self.x + self.r <= WIDTH:
            self.x = self.x + self.vx
        else:
            if self.x + self.r >= WIDTH:
                self.x = WIDTH - self.r
            self.vx = self.vx * -1
            self.x = self.x + self.vx

        if self.y + self.r <= HEIGHT:
            self.vy = self.vy + self.g
            self.y = self.y + self.vy - 1
        else:
            if self.y + self.r >= HEIGHT:
                self.y = HEIGHT - self.r
            self.vy = self.vy * -1
            self.vy = self.vy + self.g
            self.y = self.y + self.vy + 1

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
        if ((obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (obj.r + self.r) ** 2) and type(obj) != Gun and type(
                obj) != Ball:
            return True
        else:
            return False


class BallBot(Ball):
    def hittest(self, obj):
        if ((obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (obj.r + self.r) ** 2) and type(obj) != BotKiller and type(
                obj) != BallBot:
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.live = livegun
        self.liveconst = self.live
        self.r = 10
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x = 20
        self.y = 450
        # vx и vy нужны для отправки в BotKiller для расчета упреждения
        self.vx = 0
        self.vy = 0

    def fire2_start(self, k):
        self.f2_on = k

    def fire2_end(self, px, py):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        posx = px
        posy = py
        global balls
        new_ball = Ball(self.screen)
        if posx > self.x:
            self.an = math.atan((-posy + self.y) / (posx - self.x))
        if posx < self.x:
            self.an = math.pi + math.atan((-posy + self.y) / (posx - self.x))
        if posx == self.x:
            self.an = math.pi / 2
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = -self.f2_power * math.sin(self.an)
        new_ball.x = math.cos(self.an) * (self.f2_power + 10) + self.x
        new_ball.y = -(math.sin(self.an) * (self.f2_power + 10)) + self.y
        balls.append(new_ball)

    def fire2_end2(self, px, py):
        """Выстрел тройным мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        posx = px
        posy = py
        global balls
        new_ball1 = Ball(self.screen)
        new_ball2 = Ball(self.screen)
        new_ball3 = Ball(self.screen)
        if posx > self.x:
            self.an = math.atan((-posy + self.y) / (posx - self.x))
        if posx < self.x:
            self.an = math.pi + math.atan((-posy + self.y) / (posx - self.x))
        if posx == self.x:
            self.an = math.pi / 2
        new_ball1.vx = self.f2_power * math.cos(self.an)
        new_ball1.vy = -self.f2_power * math.sin(self.an)
        new_ball2.vx = self.f2_power * math.cos(self.an)
        new_ball2.vy = -self.f2_power * math.sin(self.an)
        new_ball3.vx = self.f2_power * math.cos(self.an)
        new_ball3.vy = -self.f2_power * math.sin(self.an)
        new_ball1.x = math.cos(self.an) * (self.f2_power + 10) + self.x
        new_ball1.y = -(math.sin(self.an) * (self.f2_power + 10)) + self.y
        new_ball2.x = math.cos(self.an) * (self.f2_power + 10) + self.x - (math.cos(self.an + math.pi / 2)) * 40
        new_ball2.y = -(math.sin(self.an) * (self.f2_power + 10)) + self.y + math.sin(self.an + math.pi / 2) * 40
        new_ball3.x = math.cos(self.an) * (self.f2_power + 10) + self.x + (math.cos(self.an + math.pi / 2)) * 40
        new_ball3.y = -(math.sin(self.an) * (self.f2_power + 10)) + self.y - math.sin(self.an + math.pi / 2) * 40
        balls.append(new_ball1)
        balls.append(new_ball2)
        balls.append(new_ball3)
        self.f2_power = 10

    def targetting(self, x, y):
        """Прицеливание. Зависит от положения мыши."""
        xm = x
        ym = y
        if xm > self.x:
            self.an = math.atan((-ym + self.y) / (xm - self.x))
        if xm < self.x:
            self.an = math.pi + math.atan((-ym + self.y) / (xm - self.x))
        if xm == self.x:
            self.an = math.pi / 2

    def draw(self, tickcounter):
        if tickcounter >= FPS:
            tick = FPS
        else:
            tick = tickcounter
        '''Расчет полосочек хп и перезарядки, аналогично и у бота'''
        line(screen, self.color, (self.x, self.y),
             (math.cos(self.an) * (self.f2_power + 10) + self.x, -(math.sin(self.an) * (self.f2_power + 10)) + self.y),
             width=20)
        line(screen, BLUE, (self.x - 20, self.y - 30),
             (self.x - 20 + int(40 * (self.live / self.liveconst)), self.y - 30),
             width=4)
        rect(screen, BLACK, [(self.x - 20, self.y - 32), (41, 6)], width=1)
        line(screen, GREEN, (self.x - 20, self.y - 38), (self.x - 20 + int(40 * (tick / FPS)), self.y - 38), width=4)
        rect(screen, BLACK, [(self.x - 20, self.y - 40), (41, 6)], width=1)
        circle(screen, RED, (self.x, self.y), self.r)

    def power_up(self):
        '''Расчет силы выстрела и рисование прицела. '''
        if self.f2_on == 0:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = (int((100 - self.f2_power) * 2.5), 0, 0)
            for i in range(1, 10):
                circle(screen, RED, (
                    self.x + math.cos(self.an) * (self.f2_power + 10) + math.cos(self.an) * self.f2_power * i,
                    self.y - (math.sin(self.an) * (self.f2_power + 10)) - (
                            math.sin(self.an) * self.f2_power * i - (2 * i ** 2) / 2)), 5)
        elif self.f2_on == 1:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = (int((100 - self.f2_power) * 2.5), 0, 0)
        else:
            self.color = GREY

    def move(self):
        '''Два типа управления.
        Переключаются флагом Flag в начале программы
        '''
        x0 = self.x
        y0 = self.y
        if Flag == False:
            if self.x < WIDTH:
                if keyboard.is_pressed('w'):
                    self.y -= 5
                if keyboard.is_pressed('a'):
                    self.x -= 5
                if keyboard.is_pressed('s'):
                    self.y += 5
                if keyboard.is_pressed('d'):
                    self.x += 5
            else:
                self.x = 40
        else:
            if self.x < WIDTH:
                if keyboard.is_pressed('w'):
                    self.x += math.cos(self.an) * 10
                    self.y += -(math.sin(self.an) * 10)
                if keyboard.is_pressed('a'):
                    self.x += -(math.cos(self.an - math.pi / 2) * 10)
                    self.y += (math.sin(self.an - math.pi / 2) * 10)
                if keyboard.is_pressed('s'):
                    self.x += -(math.cos(self.an) * 10)
                    self.y += math.sin(self.an) * 10
                if keyboard.is_pressed('d'):
                    self.x += math.cos(self.an - math.pi / 2) * 10
                    self.y += -(math.sin(self.an - math.pi / 2) * 10)

            else:
                self.x = 40
        self.vx = self.x - x0
        self.vy = self.y - y0


class BotKiller:
    def __init__(self, screen):
        self.live = livebot
        self.liveconst = self.live
        self.screen = screen
        self.an = 1
        self.an2 = 0
        self.color = GREY
        self.x = WIDTH - 20
        self.y = 400
        self.t = 30  # время полета снаряда в тиках, от него зависит скорость полета снаряда
        self.r = 30
        self.flag = False
        self.xlnach = 0
        self.vx = 0
        self.vy = 0

    def fire(self, obj):
        """Выстрел мячом.

        Происходит при каждые 2 секунды
        Начальные значения компонент скорости мяча vx и vy зависят от положения игрока.
        """
        global balls
        new_ball = BallBot(self.screen)
        new_ball.vx = self.vx + random.randint(-razbros, razbros)  # Разброс
        new_ball.vy = self.vy + random.randint(-razbros, razbros)
        new_ball.x = math.cos(self.an2) * 60 + self.x
        new_ball.y = -(math.sin(self.an2) * 60) + self.y
        balls.append(new_ball)

    def targetting(self, obj):
        """Прицеливание. Зависит от положения игрока.

        Тут также расчитываются скорости снарядов по осям и угол, на который отклоняется сама пушка
        """
        if obj.x > self.x:
            self.an = math.atan((-obj.y + self.y) / (obj.x - self.x))
        if obj.x < self.x:
            self.an = math.pi + math.atan((-obj.y + self.y) / (obj.x - self.x))
        if obj.x == self.x:
            self.an = math.pi / 2
        if self.flag == False:
            self.xlnach = abs(self.x - obj.x)
            self.flag = True
        t = self.t * (abs(self.x - obj.x) / self.xlnach) * 1.1
        if t == 0:
            t = 1
        self.vx = (obj.x + obj.vx * t - (math.cos(self.an2) * 60 + self.x)) / t
        self.vy = (obj.y + obj.vy * t - (-(math.sin(self.an2) * 60) + self.y)) / t - (g * t) / 2

        xobj = self.x + self.vx * 5
        yobj = self.y + self.vy * 5
        if xobj > self.x:
            self.an2 = math.atan((-yobj + self.y) / (xobj - self.x))
        if xobj < self.x:
            self.an2 = math.pi + math.atan((-yobj + self.y) / (xobj - self.x))
        if xobj == self.x:
            self.an2 = math.pi / 2

    def draw(self, tickcounter):
        # Рисование пушки
        tick = tickcounter
        line(screen, self.color, (self.x, self.y),
             (math.cos(self.an2) * 60 + self.x, -(math.sin(self.an2) * 60) + self.y), width=20)
        line(screen, RED, (self.x - 20, self.y - 30),
             (self.x - 20 + int(40 * (self.live / self.liveconst)), self.y - 30), width=4)
        rect(screen, BLACK, [(self.x - 20, self.y - 32), (41, 6)], width=1)
        line(screen, GREEN, (self.x - 20, self.y - 38), (self.x - 20 + int(40 * (tick / (FPS * 2))), self.y - 38),
             width=4)
        rect(screen, BLACK, [(self.x - 20, self.y - 40), (41, 6)], width=1)
        circle(screen, BLUE, (self.x, self.y), 20)

    def move(self):
        self.x += math.cos(self.an) * 1
        self.y -= math.sin(self.an) * 1


class Target:
    def __init__(self):
        self.live = livetarget
        self.rmin = 10
        self.rmax = 50
        self.r = random.randint(self.rmin, self.rmax)
        self.x = random.randint(self.r + 100, WIDTH - self.r - 100)
        self.y = random.randint(self.r + 100, HEIGHT - self.r - 100)
        self.xspeed = random.randint(1, 10)
        self.yspeed = random.randint(1, 10)
        self.color = RED
        self.pr = 0  # Степень прозрачности
        self.zt = int(255 / self.live)  # Убывание прозрачности

    def move(self):
        if (self.x + self.r <= WIDTH) and (self.x - self.r >= 0):
            self.x = self.x + self.xspeed
        else:
            if self.x + self.r >= WIDTH:
                self.x = WIDTH - self.r
            if self.x - self.r <= 0:
                self.x = self.r
            self.xspeed = self.xspeed * -1
            self.x = self.x + self.xspeed

        if (self.y + self.r <= HEIGHT) and (self.y - self.r >= 0):
            self.y = self.y + self.yspeed
        else:
            if self.y + self.r >= HEIGHT:
                self.y = HEIGHT - self.r
            if self.y - self.r <= 0:
                self.y = self.r
            self.yspeed = self.yspeed * -1
            self.y = self.y + self.yspeed

    def draw(self):
        self.pr = self.zt * self.live
        if self.pr < 20:
            self.pr = 0
        circle(boomscr, (255, 0, 0, abs(self.pr)), (self.x, self.y), self.r)
        screen.blit(boomscr, (0, 0))


class KaplyaOfTarget:

    def __init__(self, xx, yy, speed, color, r):
        self.g = 1
        self.x = xx
        self.y = yy
        self.r = int(r / 5)
        self.color = color
        self.xspeed = (random.randint(-3, 3) + speed) * 1.5
        self.yspeed = random.randint(-5, 5)

    def move(self):
        self.yspeed = self.yspeed + self.g
        self.x = int(self.x + self.xspeed)
        self.y = int(self.y + self.yspeed)
        if self.y > HEIGHT + 10:
            self.yspeed = 0

    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)


class Boom:
    def __init__(self, xx, yy, r):
        self.x = xx
        self.y = yy
        self.r = int(r / 2)
        self.dr = 7
        self.liveticks = 8
        self.death = 1
        self.pr = 255
        self.zt = int(self.pr / (self.liveticks / self.death))

    def draw(self):
        self.r += self.dr
        self.pr -= self.zt
        if self.pr < 20:
            self.pr = 0
        self.liveticks -= self.death
        circle(boomscr, (255, 0, 0, self.pr), (self.x, self.y), self.r)
        screen.blit(boomscr, (0, 0))


gun = Gun(screen)
targets.append(gun)
for t in range(kt):
    t = Target()
    targets.append(t)

while not finished:
    clock.tick(FPS)
    tickcounter += 1
    tcglobal += 1
    # Создание нового бота
    if schet // 1000 > schetcounter:
        schetcounter += 1
        bot = BotKiller(screen)
        targets.append(bot)

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            finished = True
        # При нажатии на esс игра заканчивается, при нажатии на пробел меняется флаг автоматической стрельбы
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True
            elif event.key == pygame.K_SPACE:
                auto = 1
            elif event.key == pygame.K_UP:
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
            if event.key == pygame.K_p:
                Ps = not Ps
                if Ps:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                auto = 0
        # Сама автоматическая стрельба
        elif auto == 1:
            gun.fire2_start(1)
            gun.f2_power = 100
            gun.targetting(pos[0], pos[1])
            if tcglobal - tcshoot >= FPS / 10:
                gun.fire2_end2(pos[0], pos[1])
                tcshoot = tcglobal
                pulemet.play()
        elif auto == 0:
            gun.fire2_start(2)
            gun.f2_power = 10
            auto = 2
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                gun.fire2_start(0)
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                if tcglobal - tcshoot >= FPS:
                    gun.fire2_end(pos[0], pos[1])
                    tcshoot = tcglobal
                    gun.fire2_start(2)
                    gun.f2_power = 10
                    pulemet.play()
                else:
                    gun.fire2_start(2)
                    gun.f2_power = 10

        else:
            gun.targetting(pos[0], pos[1])

    # Проверка убитых юнитов, проверка попаданий, запись новых эффектов в массивы, добавление игровых очков
    for b in balls:
        if b.x < -10:
            balls.remove(b)
        else:
            b.draw()
            b.move()
            for t in targets:
                if b.hittest(t) == True:
                    t.live -= 1
                    boom = Boom(b.x, b.y, b.r)
                    booms.append(boom)
                    if b in balls:
                        balls.remove(b)
                    k1 = random.randint(5, 10)
                    if t.live == 0:
                        if type(t) != BotKiller and type(t) != Gun:
                            for i in range(k1):
                                kaplya = KaplyaOfTarget(int(t.x), int(t.y), t.xspeed, t.color, t.r)
                                kapli.append(kaplya)
                            schet += int(100 - ((t.r - t.rmin) / (t.rmax - t.rmin)) * 100)
                        elif type(t) == BotKiller:
                            schet += 500
                        else:
                            finished = not finished
                        boom = Boom(t.x, t.y, t.r)
                        booms.append(boom)
                        targets.remove(t)
                        t = Target()
                        targets.append(t)
    for b1 in balls:
        for b2 in balls:
            if b1.hittest(b2) == True:
                boom = Boom((b1.x + b2.x) / 2, (b1.y + b2.y) / 2, b1.r / 2)
                booms.append(boom)
                balls.remove(b1)
                balls.remove(b2)
    # Отрисовка юнитов, стрельба ботов
    for t in targets:
        t.move()
        if type(t) == BotKiller:
            if tickcounter >= FPS * 2:
                t.fire(gun)
                tickcounter = 0
            else:
                t.targetting(gun)
            t.draw(tickcounter)
        elif type(t) == Gun:
            t.draw(tcglobal - tcshoot)
        else:
            t.draw()
    for k in kapli:
        if k.y > HEIGHT:
            kapli.remove(k)
        else:
            k.draw()
            k.move()
    for boom in booms:
        if boom.liveticks == 0:
            booms.remove(boom)
        else:
            boom.draw()
    gun.power_up()
    schetv = text2.render("score:" + " " + str(schet), True, (180, 0, 0))
    screen.blit(schetv, (10, 50))
    pygame.display.update()
    screen.fill(WHITE)
    boomscr.fill(WHITE)
# Конечная заставка
finished = not finished
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True

    schetv = text1.render("GAME OVER", True, (180, 0, 0))
    screen.blit(schetv, (WIDTH / 2 - 350, HEIGHT / 2 - 50))

    pygame.display.update()
    screen.fill(WHITE)
pygame.quit()
