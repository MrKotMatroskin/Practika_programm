import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((794, 1123))
rect(screen, (34, 43, 0), [(0, 577), (794, 1123)])
polygon(screen, (46, 69, 68), [(0, 576), (794, 576), (794, 577), (0, 577)])
rect(screen, (0, 34, 43), [(0, 0), (794, 576)])  # нарисовал фон


def luna(x, y, r, color):
    if color == "white1":
        cl = (242, 242, 242)
    if color == "white2":
        cl = (215, 215, 215)
    circle(screen, cl, (x, y), r)


def oblako(x, y, h, k, color):
    if color == "grey":
        clr = (102, 102, 102)
    if color == "black":
        clr = (51, 51, 51)
    ellipse(screen, clr, [x, y, h * k, h])

def korable(x, y, k):
    x1=174/k
    y1=438/k
    dx=x-x1
    dy=y-y1
    polygon(screen, (250, 250, 250), [(19/k+dx, 735/k+dy), (344/k+dx, 735/k+dy), (174/k+dx, 438/k+dy)])
    ellipse(screen, (153, 153, 153), [6/k+dx, 398/k+dy, 355/k, 111/k])
    ellipse(screen, (204, 204, 204), [57/k+dx, 384/k+dy, 255/k, 83/k])
    ellipse(screen, (230, 230, 230), [25/k+dx, 443/k+dy, 43/k, 18/k])
    ellipse(screen, (230, 230, 230), [69/k+dx, 465/k+dy, 43/k, 18/k])
    ellipse(screen, (230, 230, 230), [126/k+dx, 475/k+dy, 43/k, 18/k])
    ellipse(screen, (230, 230, 230), [191/k+dx, 477/k+dy, 43/k, 18/k])
    ellipse(screen, (230, 230, 230), [247/k+dx, 466/k+dy, 43/k, 18/k])
    ellipse(screen, (230, 230, 230), [303/k+dx, 443/k+dy, 43/k, 18/k])
def inp(k, x, y,
        b):  # очевидно функция рисования инопришеленца, k - коэфициент гомотетии, x и y - координаты, куда надо поставить, b - флаг (0 - не отражать, 1 - отразить), все преобразования относительно центра яблочка
    x1 = 647 / k
    y1 = 777 / k
    dx = x - x1
    dy = y - y1
    circle(screen, (200, 55, 55), (647 / k + dx, 777 / k + dy), 28 / k)
    lines(screen, (0, 0, 0), False,
          [(646 / k + dx + b * 2 * (x1 - 646 / k), 754 / k + dy), (650 / k + dx + b * 2 * (x1 - 650 / k), 746 / k + dy),
           (663 / k + dx + b * 2 * (x1 - 663 / k), 734 / k + dy)], 2)
    polygon(screen, (136, 170, 0), [(651 / k + dx + b * 2 * (x1 - 651 / k), 748 / k + dy),
                                    (651 / k + dx + b * 2 * (x1 - 651 / k), 739 / k + dy),
                                    (645 / k + dx + b * 2 * (x1 - 645 / k), 726 / k + dy),
                                    (642 / k + dx + b * 2 * (x1 - 642 / k), 726 / k + dy),
                                    (641 / k + dx + b * 2 * (x1 - 641 / k), 729 / k + dy),
                                    (646 / k + dx + b * 2 * (x1 - 646 / k), 743 / k + dy)])
    polygon(screen, (0, 0, 0), [(651 / k + dx + b * 2 * (x1 - 651 / k), 748 / k + dy),
                                (651 / k + dx + b * 2 * (x1 - 651 / k), 739 / k + dy),
                                (645 / k + dx + b * 2 * (x1 - 645 / k), 726 / k + dy),
                                (642 / k + dx + b * 2 * (x1 - 642 / k), 726 / k + dy),
                                (641 / k + dx + b * 2 * (x1 - 641 / k), 729 / k + dy),
                                (644 / k + dx + b * 2 * (x1 - 644 / k), 743 / k + dy)], 1)
    ellipse(screen, (221, 233, 175), [602 / k + dx + b * ((x1 - 602 / k) * 2 - 33 / k), 794 / k + dy, 33 / k, 17 / k])
    ellipse(screen, (221, 233, 175), [575 / k + dx + b * ((x1 - 575 / k) * 2 - 27 / k), 785 / k + dy, 27 / k, 19 / k])
    ellipse(screen, (221, 233, 175), [485 / k + dx + b * ((x1 - 485 / k) * 2 - 26 / k), 789 / k + dy, 26 / k, 18 / k])
    ellipse(screen, (221, 233, 175), [474 / k + dx + b * ((x1 - 474 / k) * 2 - 15 / k), 808 / k + dy, 15 / k, 17 / k])
    circle(screen, (221, 233, 175), (575 / k + dx + b * 2 * (x1 - 575 / k), 785 / k + dy), 15 / k)
    circle(screen, (221, 233, 175), (515 / k + dx + b * 2 * (x1 - 515 / k), 781 / k + dy), 15 / k)
    circle(screen, (221, 233, 175), (485 / k + dx + b * 2 * (x1 - 485 / k), 915 / k + dy), 15 / k)
    circle(screen, (221, 233, 175), (589 / k + dx + b * 2 * (x1 - 589 / k), 928 / k + dy), 15 / k)
    ellipse(screen, (221, 233, 175), [496 / k + dx + b * ((x1 - 496 / k) * 2 - 24 / k), 872 / k + dy, 24 / k, 49 / k])
    ellipse(screen, (221, 233, 175), [554 / k + dx + b * ((x1 - 554 / k) * 2 - 24 / k), 887 / k + dy, 24 / k, 49 / k])
    ellipse(screen, (221, 233, 175), [498 / k + dx + b * ((x1 - 498 / k) * 2 - 30 / k), 834 / k + dy, 30 / k, 44 / k])
    ellipse(screen, (221, 233, 175), [548 / k + dx + b * ((x1 - 548 / k) * 2 - 30 / k), 851 / k + dy, 30 / k, 44 / k])
    ellipse(screen, (221, 233, 175), [512 / k + dx + b * ((x1 - 512 / k) * 2 - 56 / k), 761 / k + dy, 56 / k, 117 / k])
    polygon(screen, (221, 233, 175), [(539 / k + dx + b * 2 * (x1 - 539 / k), 770 / k + dy),
                                      (560 / k + dx + b * 2 * (x1 - 560 / k), 770 / k + dy),
                                      (609 / k + dx + b * 2 * (x1 - 609 / k), 689 / k + dy),
                                      (588 / k + dx + b * 2 * (x1 - 588 / k), 676 / k + dy),
                                      (506 / k + dx + b * 2 * (x1 - 506 / k), 677 / k + dy),
                                      (498 / k + dx + b * 2 * (x1 - 498 / k), 689 / k + dy)], 0)
    ellipse(screen, (221, 233, 175), [502 / k + dx + b * ((x1 - 502 / k) * 2 - 13 / k), 660 / k + dy, 13 / k, 18 / k])
    ellipse(screen, (221, 233, 175), [490 / k + dx + b * ((x1 - 490 / k) * 2 - 19 / k), 642 / k + dy, 19 / k, 21 / k])
    ellipse(screen, (221, 233, 175), [478 / k + dx + b * ((x1 - 478 / k) * 2 - 23 / k), 629 / k + dy, 23 / k, 15 / k])
    ellipse(screen, (221, 233, 175), [472 / k + dx + b * ((x1 - 472 / k) * 2 - 28 / k), 609 / k + dy, 28 / k, 23 / k])
    circle(screen, (221, 233, 175), (601 / k + dx + b * 2 * (x1 - 601 / k), 676 / k + dy), 10 / k)
    ellipse(screen, (221, 233, 175), [602 / k + dx + b * ((x1 - 602 / k) * 2 - 13 / k), 659 / k + dy, 13 / k, 18 / k])
    circle(screen, (221, 233, 175), (614 / k + dx + b * 2 * (x1 - 614 / k), 651 / k + dy), 9 / k)
    ellipse(screen, (221, 233, 175), [625 / k + dx + b * ((x1 - 625 / k) * 2 - 17 / k), 635 / k + dy, 17 / k, 13 / k])
    ellipse(screen, (221, 233, 175), [646 / k + dx + b * ((x1 - 646 / k) * 2 - 26 / k), 632 / k + dy, 26 / k, 30 / k])
    ellipse(screen, (0, 0, 0), [519 / k + dx + b * ((x1 - 519 / k) * 2 - 37 / k), 691 / k + dy, 37 / k, 34 / k])
    ellipse(screen, (0, 0, 0), [569 / k + dx + b * ((x1 - 569 / k) * 2 - 25 / k), 698 / k + dy, 25 / k, 26 / k])
    circle(screen, (255, 255, 255), (542 / k + dx + b * 2 * (x1 - 542 / k), 711 / k + dy), 5 / k)
    circle(screen, (255, 255, 255), (585 / k + dx + b * 2 * (x1 - 585 / k), 714 / k + dy), 4 / k)

luna(502, 258, 125, "white1")
oblako(-50, 50, 100, 3, "grey")
oblako(450, 30, 40, 10, "grey")
oblako(370, 145, 40, 5, "grey")
oblako(-40, 250, 60, 8, "grey")
oblako(470, 310, 50, 6, "grey")
oblako(450, 200, 150, 3, "black")
oblako(300, 150, 40, 10, "black")
oblako(270, 145, 40, 5, "black")
oblako(-20, 199, 60, 8, "black")
oblako(600, 310, 50, 6, "black")
korable(175, 450, 1)
korable(350, 540, 4)
korable(660, 440, 2)
inp(1, 646, 777, 0)
inp(3, 190, 670, 1)
inp(3, 70, 740, 1)
inp(3, 335, 740, 0)
inp(2, 200, 900, 1)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()