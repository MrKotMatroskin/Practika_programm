import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 1000))
rect(screen, (255, 255, 255), [(0, 0), (1000, 1000)])
circle(screen, (255, 255, 0), (500, 500), 250)
circle(screen, (255, 0, 0), (400, 416), 50)
circle(screen, (0, 0, 0), (400, 416), 20)
circle(screen, (255, 0, 0), (600, 416), 35)
circle(screen, (0, 0, 0), (600, 416), 15)
polygon(screen, (0, 0, 0), [(350,600), (650,600),
                               (650,640), (350,640)])
polygon(screen, (0, 0, 0), [(470,407), (482, 390),
                               (320,264), (307,281)])
polygon(screen, (0, 0, 0), [(1000-470,407), (1000-482, 390),
                               (1000-320,264), (1000-307,281)])
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

