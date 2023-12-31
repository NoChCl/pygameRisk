import pygame, sys, math, random
from countryinfo import *
from country import *
from Game import *
#from infoScreen import *

#pygame init and other important init's
pygame.init()
size = [1440, 720]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("RISK")
clock = pygame.time.Clock();

'''
works=False
while not works:
    try:
        loadFromFile=open("Countrys.info","r")
        works=True
    except:
        works=False
        loadFromFile=open("Countrys.info","x")
        loadFromFile.write(str(getInfo(size)))
countryObjects=loadFromFile.read()
loadFromFile.close()
'''


#makes all country objects
countryObjects=getInfo(size, screen)

#makes a country actualy be selected
selectedCountry=countryObjects[1]

#mouse mask
mouse=pygame.Surface([1,1])
mouseMask=pygame.mask.from_surface(mouse)

#made zoom variable
zoom=1

#made left right up and down vars
LEFT=False
RIGHT=False
UP=False
DOWN=False

while True:
	#get events
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
                
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
    
    #moving the countrys
    if UP:countryObjects=action(countryObjects, "moveU")
    if DOWN:countryObjects=action(countryObjects, "moveD")
    if LEFT:countryObjects=action(countryObjects, "moveL")
    if RIGHT:countryObjects=action(countryObjects, "moveR")



    
    #put things on screen
    screen.fill([30,144,255])

    for country in countryObjects:
        screen.blit(country.image, country.rect)
        
    updateScreen(selectedCountry, screen)
            
    pygame.display.flip()
    #clock.tick(60)
