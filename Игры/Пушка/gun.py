import math
import random
from random import choice
import pygame
import pygame.freetype
from pygame.draw import *

pygame.font.init()
pygame.init()
screen: pygame.Surface

text2 = pygame.font.Font(None, 36)
schet = 0
FPS = 60

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

WIDTH = 1920
HEIGHT = 1080


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
        self.r = 10
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

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = math.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        #Рисование пушки
        line(screen, self.color, (20, 450), (math.cos(self.an) * self.f2_power + 20, math.sin(self.an) * self.f2_power + 450), width=7)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = (int((100 - self.f2_power)*2.5), 0, 0)
        else:
            self.color = GREY


class Target:
    def __init__(self):
        self.points = 0
        self.live = 1
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        self.r = random.randint(10, 50)
        self.x = random.randint(self.r + 100, WIDTH - self.r - 100)
        self.y = random.randint(self.r + 100, HEIGHT - self.r - 100)
        self.color = RED


    def draw(self):
        circle(screen, self.color, (self.x, self.y), self.r)


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 1
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target()
finished = False

while not finished:
    clock.tick(FPS)
    gun.draw()
    target.draw()
    for b in balls:
        b.draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(target) == True:
            schet += 1
            target.live = 0
            target.new_target()
    gun.power_up()
    schetv = text2.render("score:" + " " + str(schet), True, (180, 0, 0))
    screen.blit(schetv, (10, 50))
    pygame.display.update()
    screen.fill(WHITE)
pygame.quit()
