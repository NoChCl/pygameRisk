import pygame, sys, math, random, pickle
from countryinfo import *
from Country import *
from Player import *
from Game import *
from Menu import *
from infoScreen import *


import faulthandler
faulthandler.enable()

restart=False

#pygame init and other important init's
pygame.init()
size = [1440, 720]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("RISK")
clock = pygame.time.Clock();
font = pygame.font.Font(None, 16)

selection = menu(size, screen)




works=False

while not works:
    screen.fill([30,144,255])
    screen.blit(pygame.image.load("risk.png"), [(size[0]/2)-233, 100])
    font = pygame.font.Font(None, 32)
    text = font.render("Loading...", True, (10, 10, 10))
    textpos = [(size[0]/2)-233, 400]
    screen.blit(text, textpos)
    pygame.display.flip()
    
    try:
        restart
        loadFromFile=pickle.load(open("Countrys.info","rb"))
        works=True
    except Exception as e:
        print(e)
        works=False
        countryData = getInfo(size, screen)
        pickle.dump(countryData, open( "Countrys.info", "wb" ) )
        restart = True

countryObjects=decode(loadFromFile, screen, size)


if selection[0]=="load":
    #stuff to load game
    pass
elif selection[0]=="new":
    players=[]
    for i in range(selection[2]):
        players+= [Player(i)]
    
    game=Game(players, selection[1], countryObjects)



# ~ #makes all country objects
#countryObjects=getInfo(size, screen)

# ~ #makes a country actualy be selected
selectedCountry=countryObjects[1]

# ~ #mouse mask
mousePos=pygame.mouse.get_pos()
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

leftMouseDown=False

select=False

t=0

while True:
    #get events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEMOTION:
            mousePos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                leftMouseDown=True
        if event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_w:
                if 11>= zoom:
                    zoomIn=True
                UP=True
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
    
    if select and leftMouseDown:
        onCountry=False
        for country in countryObjects:
            if country.mask.overlap(mouseMask, (mousePos[0]-country.rect.x, mousePos[1]-country.rect.y)):
                selectedCountry=country
                onCountry=True
                break
        if not onCountry:
            selectedCountry=None
            select=False
    elif leftMouseDown:
        onCountry=False
        for country in countryObjects:
            if country.mask.overlap(mouseMask, (mousePos[0]-country.rect.x, mousePos[1]-country.rect.y)):
                selectedCountry=country
                onCountry=True
                select=True
                break
        if not onCountry:
            selectedCountry=None
            select=False
    elif not select and not leftMouseDown:
        onCountry=False
        for country in countryObjects:
            if country.mask.overlap(mouseMask, (mousePos[0]-country.rect.x, mousePos[1]-country.rect.y)):
                selectedCountry=country
                onCountry=True
                break
        if not onCountry:
            selectedCountry=None
            select=False
        
    leftMouseDown=False
            
    #put things on screen
    screen.fill([30,144,255])
    

    for country in countryObjects:
        screen.blit(country.image, country.rect)
        
    updateScreen(selectedCountry, screen)
            
    if debug:
        text = font.render("FPS: "+str(clock.get_fps()), True, ((255/2)-40, (255/2)-40, (255/2)-40))
        textpos = text.get_rect(x=1380, y=0)
        screen.blit(text, textpos)
            
            
    pygame.display.flip()
    clock.tick(100000)
