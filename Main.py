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

countryObjects=getInfo(size)
#stuffnstuff.close()

selectedCountry=countryObjects[1]

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

    
    
    screen.fill([30,144,255])
    
    
    
    
    for i, country in enumerate(countryObjects):
        for x in country.regions:
            pygame.draw.polygon(screen, country.color, x)
            pygame.draw.polygon(screen, [0, 0, 0,255], x, 1)
        
            
    
    pygame.draw.rect(screen, [255, 255, 255],(0,540,300,220))
    
    font = pygame.font.Font(None, 32)
    try:
        text = font.render("Country: "+str(selectedCountry.name[0].upper()+selectedCountry.name[1:-1]+selectedCountry.name[-1]), True, (10, 10, 10))
    except:
        text = font.render("Country: None Selected", True, (10, 10, 10))
    textpos = text.get_rect(x=10, y=550)
    screen.blit(text, textpos)
    
    font = pygame.font.Font(None, 25)
    try:
        text = font.render("Troops: "+str(selectedCountry.troops), True, (10, 10, 10))
    except:
        text=font.render("Troops: N/A", True, (10, 10, 10))
    textpos = text.get_rect(x=10, y=575)
    screen.blit(text, textpos)
            
    try:
        text = font.render("Controled By: "+str(selectedCountry.controled), True, (10, 10, 10))
    except:
        text=font.render("Controled By: N/A", True, (10, 10, 10))
    textpos = text.get_rect(x=10, y=595)
    screen.blit(text, textpos)
            
            
    pygame.display.flip()
    clock.tick(60)
