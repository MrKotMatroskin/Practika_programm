import pygame
from pygame.draw import *

pygame.init()
FPS = 30

  #  lenght and hight of display ()
a = 794 
b = 1123
  #  size of sky
c = 577
  #  size of dawn(strip)
d = 1

screen = pygame.display.set_mode((a, b))

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

  #  drawing background
rect(screen, darkgreen, [(0, c), (a, b)])
rect(screen, lightblue, [(0, c - 1), (a, d + 1)])
rect(screen, darkblue, [(0, 0), (a, c)]) 


def moon (x, y, r, color):
   
    circle(screen, color, (x, y), r)


def cloud (x, y, thickness, ratio, color):
	'''
	
x,y  are coordinates of the uppert left corner of correletated rectangle
ratio  is lengh / thickness 

	'''
    
	ellipse(screen, color, [x, y, thickness * ratio, thickness])


def spaceship(x, y, size):
    '''

draws a spaceship on surf, which is blitted on screen
x,y are the coordinates of upper left corner of
corresponding to cabin-ellipse rectangle
size parameter changes the size of the surface
(>1 == bigger than standart spaceship)
all the strange numbers are calculated by hand and kindly provided
by the original author, so the proportions (except headlights) are constant

    '''
	
    ship_surf = pygame.Surface((a, b))
    ship_surf.set_colorkey(darkblack)
                          
    polygon(ship_surf, white, [(19, 735), (344, 735), (174, 438)])  #  mainlight
    
    ellipse(ship_surf,  darkgrey, [6, 398, 355, 111])  #  body
    
    ellipse(ship_surf, lightgrey, [57, 384, 255, 83]) #  cabin



    def headlight(x, y, color):
        
        '''
inner function of spaceship
draws a  colored headlight in surf,
x and y are the coordinates of upper left corner of the correspoding rectangle

        '''
        
        length = 43
        thickness = 18
        
        ellipse(ship_surf, color, (x, y, length, thickness))


    Headlights = ([25, 443], [69,465],
                  [126, 475],[191,477], [303,443],
                  [247, 466])  # tuple of coordinates of upper left corner
                 
    
    for item in Headlights:  #  drawing darkwhite headlights
        headlight((*item), darkwhite)

    ship_surf = pygame.transform.scale(ship_surf,
                                       (round(ship_surf.get_width()*size),
                                        round(ship_surf.get_height()*size)))

    screen.blit(ship_surf, (x - 57*size, y - 384*size))
    

def apple(surface, x, y, size ):
    '''
draws an apple on surface
>1 size is biger than standart
x,y are the coordinates of the center
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
    
    polygon(apple_surf, darkblack, [(651 , 748), (651, 739),
                                    (645, 726), (642, 726),
                                    (641, 729), (644, 743)], 1)  # leaf outline
    
    apple_surf = pygame.transform.scale(apple_surf,
                                        (round(apple_surf.get_width()*size),
                                         round(apple_surf.get_height()*size)))
    
    surface.blit(apple_surf, (x - 647*size, y - 777*size))

def alien (x, y, size, turned):
    
    '''

draws an alien
x,y are the coordinates of apple in its right(to us) hand(?!)
size>1 means bigger than standart
orientation can be 0 or 1
0 - alien looking right
1 - alien looking left



    '''
    
    alien_surf = pygame.Surface((a,b))
    alien_surf.fill(grey)
    alien_surf.set_colorkey(grey)
    
    ext_color = skin
    
    apple(alien_surf, 647, 777, 1)  #  apple in his hand

      #  face 
    polygon(alien_surf, skin, [(539, 770),(560, 770),(609, 689),  
                                      (588, 676), (506, 677),(498, 689)])
    ellipse(alien_surf, darkblack, [519, 691, 37, 34])  #  eye left
    circle(alien_surf, white, (542, 711), 5)  #  inner 
    ellipse(alien_surf, darkblack, [569, 698, 25, 26]) #  eye  right
    circle(alien_surf, white, (585, 714), 4) # inner

    ellipse(alien_surf, ext_color, [512, 761, 56, 117])  #  torso
      
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
    ellipse(alien_surf, ext_color, [602 , 659 , 13 , 18])
    circle(alien_surf, ext_color, (614, 651), 9)
    ellipse(alien_surf, ext_color, [625, 635, 17, 13])
    ellipse(alien_surf, ext_color, [646, 632, 26, 30])


    alien_surf = pygame.transform.scale(alien_surf,
                                       (round(alien_surf.get_width()*size),
                                        round(alien_surf.get_height()*size)))
    
    if turned == 1:
        alien_surf = pygame.transform.flip(alien_surf, True, False)
        screen.blit(alien_surf,(x - 647*size - (a - 2*647)*size, y - 777*size))
    elif turned == 0:
        screen.blit(alien_surf,(x - 647*size, y - 777*size))  #rework

  #  now we begin drawing
  #  drawing is not exactly similar, but i guess it's OK
  
moon(502, 258, 125, white)

Clouds = ([-50, 50, 100, 3, grey], [450, 30, 40, 10, grey], #  tuple of clouds
          [370, 145, 40, 5, grey],[-40, 250, 60, 8, grey],
          [470, 310, 50, 6, grey],[450, 200, 150, 3, black],
          [300, 150, 40, 10, black], [270, 145, 40, 5, black],
          [-20, 199, 60, 8, black], [600, 310, 50, 6, black])

for item in Clouds: # drawing clouds
	cloud(*item)
	

Spaceships = ([57, 384, 1],[450, 500, 0.3], [600,400, 0.5])  #  tuple of spaceships

for item in Spaceships:  #  drawing spaceships
    spaceship(*item )
apple(screen, 0, 0, 1)

alien(500,300,1,0)
alien(500,300,1,1)
	

'''
korable(175, 450, 1)
korable(350, 540, 4)
korable(660, 440, 2)
inp(1, 646, 777, 0)
inp(3, 190, 670, 1)
inp(3, 70, 740, 1)
inp(3, 335, 740, 0)
inp(2, 200, 900, 1)'''

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
