import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((794, 1123))
rect(screen, (34, 43, 0), [(0, 577), (794, 1123)])
polygon(screen, (46, 69, 68), [(0, 576), (794, 576), (794, 577), (0, 577)])
rect(screen, (0, 34, 43), [(0, 0), (794, 576)]) #нарисовал фон

circle(screen, (200, 55, 55), (647, 777), 28)
lines(screen, (0, 0, 0), False, [(646, 754), (650, 746), (663, 734)], 2)
polygon(screen, (136, 170, 0), [(651, 748), (651, 739), (645, 726), (642, 726), (641, 729), (646, 743)])
polygon(screen, (0, 0, 0), [(651, 748), (651, 739), (645, 726), (642, 726), (641, 729), (644, 743)], 1)

ellipse(screen, (221, 233, 175), [602, 794, 33, 17])
ellipse(screen, (221, 233, 175), [575, 785, 27, 19])
ellipse(screen, (221, 233, 175), [485, 789, 26, 18])
ellipse(screen, (221, 233, 175), [474, 808, 15, 17])
circle(screen, (221, 233, 175), (575, 785), 15)
circle(screen, (221, 233, 175), (515, 781), 15)
circle(screen, (221, 233, 175), (485, 915), 15)
circle(screen, (221, 233, 175), (589, 928), 15)
ellipse(screen, (221, 233, 175), [496, 872, 24, 49])
ellipse(screen, (221, 233, 175), [554, 887, 24, 49])
ellipse(screen, (221, 233, 175), [498, 834, 30, 44])
ellipse(screen, (221, 233, 175), [548, 851, 30, 44])
ellipse(screen, (221, 233, 175), [512, 761, 56, 117])

ellipse(screen, (221, 233, 175), [602, 794, 33, 17])
ellipse(screen, (221, 233, 175), [602, 794, 33, 17])
ellipse(screen, (221, 233, 175), [602, 794, 33, 17])
ellipse(screen, (221, 233, 175), [602, 794, 33, 17])
ellipse(screen, (221, 233, 175), [602, 794, 33, 17])
ellipse(screen, (221, 233, 175), [602, 794, 33, 17])
ellipse(screen, (221, 233, 175), [602, 794, 33, 17])
ellipse(screen, (221, 233, 175), [602, 794, 33, 17])
ellipse(screen, (221, 233, 175), [602, 794, 33, 17])
ellipse(screen, (221, 233, 175), [602, 794, 33, 17])
ellipse(screen, (221, 233, 175), [602, 794, 33, 17])
pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
