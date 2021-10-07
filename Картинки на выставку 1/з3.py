import pygame
from pygame.draw import *

pygame.init()
FPS = 30

  #  maximum lenght and hight of display possible
a = 1920
b = 1020

  #  length and height of display to use
height = 1123
length = 794

    
  #  size of sky (distanse from upper to lower bound)
c = 577

  #  size of dawn (strip width)
d = 1

screen = pygame.display.set_mode((length,height))

  #  setting colors
white = (255, 255, 255)
darkwhite = (230, 230, 230)
black = (50, 50, 50)
darkblack = (0, 0, 0)
grey = (100, 100, 100)
darkgrey = (150, 150, 150)
lightgrey = (204, 204, 204)
red = (200, 55, 55)
darkgreen = (34, 43, 0)
green = (136, 170, 0)
darkblue = (0, 34, 43)
lightblue = (46, 69, 69)
skin = (221, 233, 175)


def moon (x, y, r, color):
    '''
Draws a moon.

x,y coordinates of the center.

r = radius
    '''
    circle(screen, color, (x, y), r)


def cloud (x, y, thickness, ratio, color):
    
    '''
x,y  are  the coordinates of the upper left corner of correletated rectangle.

ratio  is lengh / thickness.
    '''
    
    ellipse(screen, color, [x, y, thickness * ratio, thickness])


def spaceship(x, y, size):
    
    '''
Draws a spaceship on ship_surf, which is  then blitted on screen.

x,y are the coordinates of upper left corner of
corresponding to cabin-ellipse rectangle.

size is proportional to the size of the ship.

Has inner function for drawing headlightes.
    '''
	
    ship_surf = pygame.Surface((round(size*a), round(size*b)))
    ship_surf.set_colorkey(darkblack)
                          
    polygon(ship_surf, white, [(19*size, 735*size), (344*size, 735*size),
                               (174*size, 438*size)])  #  mainlight
    
    ellipse(ship_surf,  darkgrey, [6*size, 398*size,
                                   355*size, 111*size])  #  body
    
    ellipse(ship_surf, lightgrey, [57*size, 384*size,
                                   255*size, 83*size]) #  cabin



    def headlight(x, y, color):
        
        '''
Inner function of spaceship.

Draws a colored headlight in ship_surf.

x and y are the coordinates of upper left corner of the correspoding rectangle.
        '''
        
        length = 43*size
        thickness = 18*size
        
        ellipse(ship_surf, color, (x, y, length, thickness))

    #  tuple of coordinates of upper left corner
    Headlights = ([25*size, 443*size], [69*size, 465*size],
                  [126*size, 475*size],[191*size, 477*size],
                  [303*size, 443*size],[247*size, 466*size])  
                 
    
        
    for item in Headlights:  #  drawing darkwhite headlights
        headlight((*item), darkwhite)

    screen.blit(ship_surf, (x - 57*size, y - 384*size))
    

def apple(surface, x, y, size ):
    
    '''
Draws an apple on given surface.

x,y are the coordinates of the center.

size is propotional to the size of the apple.

    '''
    
    apple_surf = pygame.Surface((round(size*a), round(size*b)))
    apple_surf.fill(white)
    apple_surf.set_colorkey(white)
    
    circle(apple_surf, red, (647*size, 777*size), 28*size)  #  apple
    
    lines(apple_surf, black, False,  #  stick
          [(646*size, 754*size), (650*size, 746*size),
           (663*size, 734*size)], 2)
    
    polygon(apple_surf, green, [(651*size, 748*size),  #  leaf
                                (651*size, 739*size),(645*size, 726*size),
                                (642*size, 726*size),(641*size, 729*size),
                                (646*size, 743*size)])
     #  leaf outline
    polygon(apple_surf, darkblack, [(651*size, 748*size), (651*size, 739*size), 
                                    (645*size, 726*size), (642*size, 726*size),
                                    (641*size, 729*size),
                                    (644*size, 743*size)], 1)  
    


    surface.blit(apple_surf, (x - 647*size, y - 777*size))

def alien (x, y, size, turned):
    
    '''
Draws an alien with an apple

x,y are the coordinates of the apple center,it holds (!)

size is propotional to the size of the alien.

turned can be 0 or 1.
0 = alien looking right.
1 = alien looking left.
    '''
    
    alien_surf = pygame.Surface((round(size*a),round(size*b)))
    alien_surf.fill(grey)
    alien_surf.set_colorkey(grey)
    
    ext_color = skin
    
    apple(alien_surf, 647*size, 777*size, size)  #  apple in his hand

      #  face 
    polygon(alien_surf, ext_color, [(539*size, 770*size),(560*size, 770*size),
                                    (609*size, 689*size), (588*size, 676*size),
                                    (506*size, 677*size),(498*size, 689*size)])
      #  eye left       
    ellipse(alien_surf, darkblack, [519*size, 691*size, 37*size, 34*size])

      #  eye  right
    circle(alien_surf, white, (542*size, 711*size), 5*size)
    ellipse(alien_surf, darkblack, [569*size, 698*size, 25*size, 26*size]) 
    circle(alien_surf, white, (585*size, 714*size), 4*size) 

    #  torso
    ellipse(alien_surf, ext_color, [512*size, 761*size, 56*size, 117*size])
      
      #  right hand
    ellipse(alien_surf, ext_color, [602*size, 794*size, 33*size, 17*size]) 
    ellipse(alien_surf, ext_color, [575*size, 785*size, 27*size, 19*size])
    circle(alien_surf, ext_color, (575*size, 785*size), 15*size) 

      #  left hand
    ellipse(alien_surf, ext_color, [485*size, 789*size, 26*size, 18*size])
    ellipse(alien_surf, ext_color, [474*size, 808*size, 15*size, 17*size])
    circle(alien_surf, ext_color, (515*size, 781*size), 15*size) 

      #  left leg
    circle(alien_surf, ext_color, (485*size, 915*size), 15*size) 
    ellipse(alien_surf, ext_color, [496*size, 872*size, 24*size, 49*size]) 
    ellipse(alien_surf, ext_color, [498*size, 834*size, 30*size, 44*size])

      #  right leg
    circle(alien_surf, ext_color, (589*size, 928*size), 15*size) 
    ellipse(alien_surf, ext_color, [554*size, 887*size, 24*size, 49*size])    
    ellipse(alien_surf, ext_color, [548*size, 851*size, 30*size, 44*size]) 

     #  left antenna                               
    ellipse(alien_surf, ext_color, [502*size, 660*size, 13*size, 18*size]) 
    ellipse(alien_surf, ext_color, [490*size, 642*size, 19*size, 21*size]) 
    ellipse(alien_surf, ext_color, [478*size, 629*size, 23*size, 15*size]) 
    ellipse(alien_surf, ext_color, [472*size, 609*size, 28*size, 23*size]) 
    
      #  right antenna
    circle(alien_surf, ext_color, (601*size, 676*size), 10*size) 
    ellipse(alien_surf, ext_color, [602*size, 659*size, 13*size, 18*size])
    circle(alien_surf, ext_color, (614*size, 651*size), 9*size)
    ellipse(alien_surf, ext_color, [625*size, 635*size, 17*size, 13*size])
    ellipse(alien_surf, ext_color, [646*size, 632*size, 26*size, 30*size])


    if turned == 1:
        alien_surf = pygame.transform.flip(alien_surf, True, False)
        screen.blit(alien_surf,(x - (round(a*size) - 647*size), y - 777*size))
    elif turned == 0:
        screen.blit(alien_surf,(x - 647*size, y - 777*size))  


  #  data of objects to draw
  
Clouds = ([-50, 50, 100, 3, grey], [450, 30, 40, 10, grey], #  tuple of clouds
          [370, 145, 40, 5, grey],[-40, 250, 60, 8, grey],
          [470, 310, 50, 6, grey],[450, 200, 150, 3, black],
          [300, 150, 40, 10, black], [270, 145, 40, 5, black],
          [-20, 199, 60, 8, black], [600, 310, 50, 6, black])

Spaceships = ([57, 384, 1],[350, 560, 1/4], [600, 420, 1/2])  #  tuple of ships

Aliens = ([646, 777, 1, 0], [190, 670, 1/3, 1],  #  tuple of aliens
          [70, 740, 1/3, 1], [200, 900, 1/2, 1], [335, 740, 1/3, 0])  


 #  drawing background
rect(screen, darkgreen, [(0, c), (a, b)])
rect(screen, lightblue, [(0, c - 1), (a, d + 1)])
rect(screen, darkblue, [(0, 0), (a, c)]) 
moon(502, 258, 125, white)

for item in Clouds:  #  drawing clouds
    cloud(*item)   
for item in Spaceships:  #  drawing spaceships
    spaceship(*item)   
for item in Aliens:  #  drawing aliens
    alien(*item)

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
