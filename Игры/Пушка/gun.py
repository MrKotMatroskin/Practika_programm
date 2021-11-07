import math
import random
import keyboard
import mouse
from random import choice
import pygame
import pygame.freetype
from pygame.draw import *

pygame.font.init()
pygame.init()
WIDTH = 1920
HEIGHT = 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
boomscr = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
text2 = pygame.font.Font(None, 36)
schet = 0
FPS = 60
tickcounter = FPS
balls = []
targets = []
kapli = []
booms =[]
clock = pygame.time.Clock()
auto = False
finished = False
kt = 1

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

class Ball:
    def __init__(self, screen: pygame.Surface):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.g = 2
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
        и стен по краям окна (размер окна 800х600).
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
            self.y = self.y + self.vy
        else:
            if self.y + self.r >= HEIGHT:
                self.y = HEIGHT - self.r
            self.vy = self.vy * -1
            self.vy = self.vy + self.g
            self.y = self.y + self.vy 
        

    def draw(self):
        pygame.draw.circle(self.screen, self.color, (self.x, self.y), self.r)

    def hittest(self, obj):
        if (obj.x - self.x) ** 2 + (obj.y - self.y) ** 2 <= (obj.r + self.r) ** 2:
            return True
        else:
            return False

class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x0 = 20
        self.y0 = 450
        self.mpx = 0
        self.mpy = 0
    def fire2_start(self, k):
        self.f2_on = k

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls
        new_ball = Ball(self.screen)
        if event.pos[0] > self.x0:
            self.an = math.atan((-event.pos[1] + self.y0) / (event.pos[0] - self.x0))
        if event.pos[0] < self.x0:
            self.an = math.pi + math.atan((-event.pos[1] + self.y0) / (event.pos[0] - self.x0))
        if event.pos[0] == self.x0:
            self.an = math.pi / 2
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = -self.f2_power * math.sin(self.an)
        new_ball.x = self.x0
        new_ball.y = self.y0
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            if event.pos[0] > self.x0:
                self.an = math.atan((-event.pos[1] + self.y0) / (event.pos[0] - self.x0))
            if event.pos[0] < self.x0:
                self.an = math.pi + math.atan((-event.pos[1] + self.y0) / (event.pos[0] - self.x0))
            if event.pos[0] == self.x0:
                self.an = math.pi / 2
            self.mpx = event.pos[0]
            self.mpy = event.pos[1]

    def draw(self):
        #Рисование пушки
        line(screen, self.color, (self.x0, self.y0), (math.cos(self.an) * (self.f2_power+10) + self.x0, -(math.sin(self.an) * (self.f2_power+10)) + self.y0), width=20)
        circle(screen, RED, (self.x0, self.y0), 10)
    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = (int((100 - self.f2_power)*2.5), 0, 0)
        else:
            self.color = GREY


    def move(self):
        flag = False
        if flag == True:
            if self.x0 < WIDTH:
                if keyboard.is_pressed('w'):
                    self.y0 -= 5
                if keyboard.is_pressed('a'):
                    self.x0 -= 5
                if keyboard.is_pressed('s'):
                    self.y0 += 5
                if keyboard.is_pressed('d'):
                    self.x0 += 5
            else:
                self.x0 = 40
        else:
            if self.x0 < WIDTH:
                if keyboard.is_pressed('w'):
                    self.x0 += math.cos(self.an) * 15
                    self.y0 += -(math.sin(self.an) * 15)
                if keyboard.is_pressed('a'):
                    self.x0 += -(math.cos(self.an - math.pi / 2) * 20)
                    self.y0 += (math.sin(self.an - math.pi / 2) * 20)
                if keyboard.is_pressed('s'):
                    self.x0 += -(math.cos(self.an) * 5)
                    self.y0 += math.sin(self.an) * 5
                if keyboard.is_pressed('d'):
                    self.x0 += math.cos(self.an-math.pi/2) * 20
                    self.y0 += -(math.sin(self.an-math.pi/2) * 20)

            else:
                self.x0 = 40

class BotKiller:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 50
        self.f2_on = 0
        self.an = 1
        self.color = GREY
        self.x0 = WIDTH - 20
        self.y0 = 400
        self.t = 20 # условное время попадания
    def fire(self, obj):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls
        new_ball = Ball(self.screen)
        new_ball.vx = (obj.x0 - self.x0)/self.t + random.randint(-1, 1) * random.randint(-3, 3)
        new_ball.vy = (obj.y0 - self.y0)/self.t - (new_ball.g*self.t)/2 + random.randint(-1, 1) * random.randint(-3, 3)
        new_ball.x = self.x0
        new_ball.y = self.y0
        self.dan = math.atan(((obj.y0 - self.y0)/self.t - (new_ball.g*self.t)/2)/((obj.x0 - self.x0)/self.t))
        self.f2_power = int(math.sqrt(new_ball.x**2 + new_ball.y**2))
        if self.f2_power > 100:
            self.f2_power = 100
        balls.append(new_ball)


    def targetting(self, obj):
        """Прицеливание. Зависит от положения игрока."""
        if obj.x0 > self.x0:
            self.an = math.atan((-obj.y0 + self.y0) / (obj.x0 - self.x0))
        if obj.x0 < self.x0:
            self.an = math.pi + math.atan((-obj.y0 + self.y0) / (obj.x0 - self.x0))
        if obj.x0 == self.x0:
            self.an = math.pi / 2

    def draw(self):
        #Рисование пушки
        line(screen, self.color, (self.x0, self.y0), (math.cos(self.an) * self.f2_power + self.x0, -(math.sin(self.an) * self.f2_power) + self.y0), width=20)

    def power_up(self):
        if self.f2_power > 10:
            self.color = (int((100 - self.f2_power)*2.5), 0, 0)
        else:
            self.color = GREY

    def move(self):
        self.x0 += math.cos(self.an)*1
        self.y0 -= math.sin(self.an)*1

class Target:
    def __init__(self):
        self.live = 3
        self.rmin = 10
        self.rmax = 50
        self.r = random.randint(self.rmin, self.rmax)
        self.x = random.randint(self.r + 100, WIDTH - self.r - 100)
        self.y = random.randint(self.r + 100, HEIGHT - self.r - 100)
        self.xspeed = random.randint(1, 10)
        self.yspeed = random.randint(1, 10)
        self.color = RED
        self.pr = 0
        self.zt = int(255 / self.live)
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
        self.pr = self.zt*self.live
        if self.pr < 20:
            self.pr = 0
        circle(boomscr, (255, 0, 0, abs(self.pr)), (self.x, self.y), self.r)
        screen.blit(boomscr, (0, 0))

class KaplyaOfTarget:

    def __init__(self, xx, yy, speed, color, r):
        self.g = 1
        self.x = xx
        self.y = yy
        self.r = int(r/5)
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
        self.r = int(r/2)
        self.dr = 1
        self.liveticks = 20
        self.death = 1
        self.pr = 255
        self.zt = int(self.pr/(self.liveticks/self.death))
    def draw(self):
        self.r += self.dr
        self.pr -= self.zt
        if self.pr < 20:
            self.pr = 0
        self.liveticks -= self.death
        circle(boomscr, (255, 0, 0, self.pr), (self.x, self.y), self.r)
        screen.blit(boomscr, (0, 0))

gun = Gun(screen)
bot = BotKiller(screen)
for t in range(kt):
    t = Target()
    targets.append(t)

while not finished:
    clock.tick(FPS)
    gun.draw()
    bot.targetting(gun)
    bot.draw()
    tickcounter += 1
    if tickcounter >= FPS*2:
        bot.fire(gun)
        tickcounter = 0
    else:
        bot.targetting(gun)

    for t in targets:
       t.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                finished = True
            if event.key == pygame.K_SPACE:
                auto = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(1)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)


    for b in balls:
        if b.x < -10:
            balls.remove(b)
        else:
            b.draw()
            b.move()
            for t in targets:
                if b.hittest(t) == True:
                    schet += int(10-((t.r-t.rmin)/(t.rmax-t.rmin))*10)
                    t.live -= 1
                    boom = Boom(b.x, b.y, b.r)
                    booms.append(boom)
                    if b in balls:
                        balls.remove(b)
                    k1 = random.randint(10, 20)
                    for i in range (k1):
                        kaplya = KaplyaOfTarget(int(t.x), int(t.y), t.xspeed, t.color, t.r)
                        kapli.append(kaplya)
                    if t.live == 0:
                        boom = Boom(t.x, t.y, t.r)
                        booms.append(boom)
                        targets.remove(t)
                        t = Target()
                        targets.append(t)
    for t in targets:
        t.move()
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
    gun.move()
    bot.move()
    schetv = text2.render("score:" + " " + str(schet), True, (180, 0, 0))
    screen.blit(schetv, (10, 50))
    pygame.display.update()
    screen.fill(WHITE)
    boomscr.fill(WHITE)
pygame.quit()
