import pygame, sys, math, random
from countryinfo import *
from country import *
from Game import *
from infoScreen import *

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


# ~ #makes all country objects
countryObjects=getInfo(size, screen)

# ~ #makes a country actualy be selected
selectedCountry=countryObjects[1]

# ~ #mouse mask
mouse=pygame.Surface([1,1])
mouseMask=pygame.mask.from_surface(mouse)

#made zoom variable
zoom=1

#made left right up and down vars
LEFT=False
RIGHT=False
UP=False
DOWN=False
shift=False
zoomIn=False
zoomOut=False

debug = False


while True:
    #get events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mousePos = event.pos
        if event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_w:
                UP=True
                zoomIn=True
            if  event.key == pygame.K_a:
                LEFT=True
            if  event.key == pygame.K_s:
                DOWN=True
                if 1<= zoom:
                    zoomOut=True
            if  event.key == pygame.K_d:
                RIGHT=True
            if  event.key == pygame.K_LSHIFT:
                shift=True
                
                
            if  event.key == pygame.K_p:
                debug=not debug
                
                
            if  event.key == pygame.K_UP:
                t+=1
                if t==len(countryObjects):
                    t=0
            
            if  event.key == pygame.K_DOWN:
                t-=1
                if t==-1:
                    t=len(countryObjects)-1
                    
                
        if event.type == pygame.KEYUP:
            if  event.key == pygame.K_LSHIFT:
                shift=False
            if  event.key == pygame.K_w:
                #Intentonal bug.
                #Line below is fix
                #zoomIn=False
                
                UP=False
            if  event.key == pygame.K_s:
                #Another intentonal bug.
                #Line below is fix
                #zoomIn=False
                
                DOWN=False
            if  event.key == pygame.K_a:
                LEFT=False
            if  event.key == pygame.K_d:
                RIGHT=False
        

    if zoomIn and shift:
        zoom+=1
        countryObjects=action(countryObjects, "+")
        zoomIn=False
        
    if zoomOut and shift:
        zoom-=1
        countryObjects=action(countryObjects, "-")
        zoomOut=False
    
    
    
    if shift:
        UP=False
        DOWN =UP  
        

    
    
    #moving the countrys
    if UP and not shift:countryObjects=action(countryObjects, "moveU")
    if DOWN and not shift:countryObjects=action(countryObjects, "moveD")
    if LEFT and not shift:countryObjects=action(countryObjects, "moveL")
    if RIGHT and not shift:countryObjects=action(countryObjects, "moveR")



    
    #put things on screen
    screen.fill([30,144,255])
    
    if debug:
        text = font.render("FPS: "+str(clock.get_fps()), True, (255/2, 255/2, 255/2))
        textpos = text.get_rect(x=1380, y=0)
        screen.blit(text, textpos)

    for country in countryObjects:
        screen.blit(country.image, country.rect)
        
    updateScreen(selectedCountry, screen)
            
    pygame.display.flip()
    #clock.tick(60)
