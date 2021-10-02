import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((794, 1123))
rect(screen, (34, 43, 0), [(0, 577), (794, 1123)])
polygon(screen, (46, 69, 68), [(0, 576), (794, 576), (794, 577), (0, 577)])
rect(screen, (0, 34, 43), [(0, 0), (794, 576)]) #нарисовал фон
circle(screen, (200, 55, 55), (647, 777), 28)
aalines(screen, (0, 0, 0), False, [(646, 754), (650, 746), (663, 734)], 2)
aalines(screen, (0, 0, 0), True, [(651, 748), (651, 739), (645, 726), (642, 726), (642, 738), (645, 743)], 2) #очевидно яблочко
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
