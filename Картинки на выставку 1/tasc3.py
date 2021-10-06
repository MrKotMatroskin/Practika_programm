import pygame
from pygame.draw import *

pygame.init()
FPS = 30

  #  lenght and hight of display 
a = 794 
b = 1123

  #  size of sky (distansefrom upper to lower bound)
c = 577

  #  size of dawn (strip width)
d = 1

screen = pygame.display.set_mode((a, b))

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

size (float from 0 to 1) is proportional to the size of the ship.
Note: one may use floats > 1 for size, but quality significantly drops.

Has inner function for drawing headlightes.
    '''
	
    ship_surf = pygame.Surface((a, b))
    ship_surf.set_colorkey(darkblack)
                          
    polygon(ship_surf, white, [(19, 735), (344, 735), (174, 438)])  #  mainlight
    
    ellipse(ship_surf,  darkgrey, [6, 398, 355, 111])  #  body
    
    ellipse(ship_surf, lightgrey, [57, 384, 255, 83]) #  cabin



    def headlight(x, y, color):
        
        '''
Inner function of spaceship.

Draws a colored headlight in ship_surf.

x and y are the coordinates of upper left corner of the correspoding rectangle.
        '''
        
        length = 43
        thickness = 18
        
        ellipse(ship_surf, color, (x, y, length, thickness))


    Headlights = ([25, 443], [69, 465],
                  [126, 475],[191, 477], [303, 443],
                  [247, 466])  # tuple of coordinates of upper left corner
                 
    
    for item in Headlights:  #  drawing darkwhite headlights
        headlight((*item), darkwhite)

    ship_surf = pygame.transform.scale(ship_surf,
                                       (round(ship_surf.get_width()*size),
                                        round(ship_surf.get_height()*size)))


    screen.blit(ship_surf, (x - 57*size, y - 384*size))
    

def apple(surface, x, y, size ):
    
    '''
Draws an apple on given surface.

x,y are the coordinates of the center.

size  (float from 0 to 1)  is propotional to the size of the apple.
Note: one may use floats > 1 for size, but quality significantly drops.
    '''
    
    apple_surf = pygame.Surface.copy(surface)
    apple_surf.fill(white)
    apple_surf.set_colorkey(white)
    
    circle(apple_surf, red, (647, 777), 28)  #  apple
    
    lines(apple_surf, black, False,  #  stick
          [(646, 754), (650, 746),
           (663, 734)], 2)
    
    polygon(apple_surf, green, [(651, 748),(651, 739), (645, 726),  #  leaf
                                    (642, 726), (641, 729), (646 , 743)])
    
    polygon(apple_surf, darkblack, [(651 , 748), (651, 739),  #  leaf outline
                                    (645, 726), (642, 726),
                                    (641, 729), (644, 743)], 1)  
    
    apple_surf = pygame.transform.scale(apple_surf,
                                        (round(apple_surf.get_width()*size),
                                         round(apple_surf.get_height()*size)))
    
    surface.blit(apple_surf, (x - 647*size, y - 777*size))

def alien (x, y, size, turned):
    
    '''
Draws an alien with an apple

x,y are the coordinates of the apple center,it holds (!)

size (float from 0 to 1) is propotional to the size of the alien.
Note: one may use floats > 1 for size, but quality significantly drops.

turned can be 0 or 1.
0 = alien looking right.
1 = alien looking left.
    '''
    
    alien_surf = pygame.Surface((a,b))
    alien_surf.fill(grey)
    alien_surf.set_colorkey(grey)
    
    ext_color = skin
    
    apple(alien_surf, 647, 777, 1)  #  apple in his hand

      #  face 
    polygon(alien_surf, ext_color, [(539, 770),(560, 770),(609, 689),  
                                      (588, 676), (506, 677),(498, 689)])
    ellipse(alien_surf, darkblack, [519, 691, 37, 34])  #  eye left
    circle(alien_surf, white, (542, 711), 5)
    ellipse(alien_surf, darkblack, [569, 698, 25, 26]) #  eye  right
    circle(alien_surf, white, (585, 714), 4) 

    #  torso
    ellipse(alien_surf, ext_color, [512, 761, 56, 117])
      
      #  right hand
    ellipse(alien_surf, ext_color, [602, 794, 33, 17]) 
    ellipse(alien_surf, ext_color, [575, 785, 27, 19])
    circle(alien_surf, ext_color, (575, 785), 15) 

      #  left hand
    ellipse(alien_surf, ext_color, [485, 789, 26, 18])
    ellipse(alien_surf, ext_color, [474, 808, 15, 17])
    circle(alien_surf, ext_color, (515, 781), 15) 

      #  left leg
    circle(alien_surf, ext_color, (485, 915), 15) 
    ellipse(alien_surf, ext_color, [496, 872, 24, 49]) 
    ellipse(alien_surf, ext_color, [498, 834, 30, 44])

      #  right leg
    circle(alien_surf, ext_color, (589, 928), 15) 
    ellipse(alien_surf, ext_color, [554, 887, 24, 49])    
    ellipse(alien_surf, ext_color, [548, 851, 30, 44]) 

     #  left antenna                               
    ellipse(alien_surf, ext_color, [502, 660, 13, 18]) 
    ellipse(alien_surf, ext_color, [490, 642, 19, 21]) 
    ellipse(alien_surf, ext_color, [478, 629, 23, 15]) 
    ellipse(alien_surf, ext_color, [472, 609, 28, 23]) 
    
      #  right antenna
    circle(alien_surf, ext_color, (601, 676), 10) 
    ellipse(alien_surf, ext_color, [602, 659, 13, 18])
    circle(alien_surf, ext_color, (614, 651), 9)
    ellipse(alien_surf, ext_color, [625, 635, 17, 13])
    ellipse(alien_surf, ext_color, [646, 632, 26, 30])


    alien_surf = pygame.transform.scale(alien_surf,
                                       (round(alien_surf.get_width()*size),
                                        round(alien_surf.get_height()*size)))
    
    if turned == 1:
        alien_surf = pygame.transform.flip(alien_surf, True, False)
        screen.blit(alien_surf,(x - size*(a - 647), y - 777*size))
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
