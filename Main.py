import pygame, sys, math, random
from countryinfo import *
from country import *
from Game import *
#from infoScreen import *

pygame.init()
size = [1440, 720]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("RISK", icontitle="RISK")
clock = pygame.time.Clock();

'''
works=False
while not works:
    try:
        stuffnstuff=open("Countrys.info","r")
        works=True
    except:
        works=False
        stuffnstuff=open("Countrys.info","x")
        stuffnstuff.write(str(getInfo(size)))'''

#print(getInfo(size))

countryObjects=getInfo(size, screen)
#stuffnstuff.close()

selectedCountry=countryObjects[1]

mouse=pygame.Surface([1,1])
mouseMask=pygame.mask.from_surface(mouse)

zoom=1


LEFT=False
RIGHT=False
UP=False
DOWN=False
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_w:
                zoom+=1
                countryObjects=action(countryObjects, "+")
            if  event.key == pygame.K_s:
                if 1<= zoom:
                    zoom-=1
                    countryObjects=action(countryObjects, "-")
            if  event.key == pygame.K_UP:
                UP=True
            if  event.key == pygame.K_DOWN:
                DOWN=True
            if  event.key == pygame.K_LEFT:
                LEFT=True
            if  event.key == pygame.K_RIGHT:
                RIGHT=True
        if event.type == pygame.KEYUP:
            if  event.key == pygame.K_UP:
                UP=False
            if  event.key == pygame.K_DOWN:
                DOWN=False
            if  event.key == pygame.K_LEFT:
                LEFT=False
            if  event.key == pygame.K_RIGHT:
                RIGHT=False
    
    if UP:countryObjects=action(countryObjects, "moveU")
    if DOWN:countryObjects=action(countryObjects, "moveD")
    if LEFT:countryObjects=action(countryObjects, "moveL")
    if RIGHT:countryObjects=action(countryObjects, "moveR")


    mousePos=pygame.mouse.get_pos()

    
    
    screen.fill([30,144,255])
    
    
    
    
    for i, country in enumerate(countryObjects):
        for x in country.regions:
            pygame.draw.polygon(screen, country.color, x)
            pygame.draw.polygon(screen, [0, 0, 0,255], x, 1)
        
    
    #updateScreen(selectedCountry, screen)
            
            
    pygame.display.flip()
    clock.tick(60)
