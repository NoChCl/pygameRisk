import pygame, sys, math, random, pickle
from countryinfo import *
try:   
    from Country import *
except:
    from country import *
from Player import *
from Game import *
from Menu import *
from infoScreen import *


import faulthandler
faulthandler.enable()


#pygame init and other important init's
pygame.init()
print("Thank you for using countryinfo: https://pypi.org/project/countryinfo/")
size = [1440, 720]
screen = pygame.display.set_mode(size)
pygame.display.set_caption("RISK")
clock = pygame.time.Clock();
font = pygame.font.Font(None, 16)

selection = menu(size, screen)



screen.fill([30,144,255])
screen.blit(pygame.image.load("risk.png"), [(size[0]/2)-233, 100])
font = pygame.font.Font(None, 32)
text = font.render("Loading...", True, (10, 10, 10))
textpos = [(size[0]/2)-233, 400]
screen.blit(text, textpos)
pygame.display.flip()

gameName=selection[1]


if selection[0]=="load":
    loadFromFile=pickle.load(open(gameName,"rb"))
else:
    loadFromFile = getInfo(size, screen)
    
countryObjects=decode(loadFromFile, screen, size)

del loadFromFile

if selection[0]=="new":
    pass
    #pickle.dump(game, open(gameSave, "wb" ))
else:
    #game=pickle.load(open(gameSave,"rb"))
    pass

# ~ #makes all country objects
#countryObjects=getInfo(size, screen)

# ~ #makes a country actualy be selected
selectedCountry=None

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
ZOOMIN=False
ZOOMOUT=False

debug = False

gameName=selection[1]

leftMouseDown=False

select=False

t=0

phase="placement"
#currentPlayer=players[0]

        
while True:
    #get events
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quitGame(countryObjects, gameName, zoom, screen, size)
        if event.type == pygame.MOUSEMOTION:
            mousePos = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]:
                leftMouseDown=True
        if event.type == pygame.KEYDOWN:
            if  event.key == pygame.K_w or event.key == pygame.K_UP:
                if 11>= zoom:
                    zoomIn=True
                UP=True
            if  event.key == pygame.K_a or event.key == pygame.K_LEFT:
                LEFT=True
            if  event.key == pygame.K_s or event.key == pygame.K_DOWN:
                DOWN=True
                if 1<= zoom:
                    zoomOut=True
            if  event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                RIGHT=True
            if  event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                shift=True
            if  event.key == pygame.K_e:
                if 11>= zoom:
                    ZOOMIN=True
            if  event.key == pygame.K_q:
                if 1<= zoom:
                    ZOOMOUT=True
                
                
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
            if  event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT:
                shift=False
            if  event.key == pygame.K_w or event.key == pygame.K_UP:
                #Intentonal bug.
                #Line below is fix
                #zoomIn=False
                
                UP=False
            if  event.key == pygame.K_s or event.key == pygame.K_DOWN:
                #Another intentonal bug.
                #Line below is fix
                #zoomIn=False
                
                DOWN=False
            if  event.key == pygame.K_a or event.key == pygame.K_LEFT:
                LEFT=False
            if  event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                RIGHT=False
        
    #zoooooms
    if zoomIn and shift:
        zoom+=1
        countryObjects=action(countryObjects, "+")
        zoomIn=False
    elif ZOOMIN:
        zoom+=1
        countryObjects=action(countryObjects, "+")
        ZOOMIN=False
    
    if zoomOut and shift:
        zoom-=1
        countryObjects=action(countryObjects, "-")
        zoomOut=False
    elif ZOOMOUT:
        zoom-=1
        countryObjects=action(countryObjects, "-")
        ZOOMOUT=False
    
    if shift:
        UP=False
        DOWN=UP  
        
    
    #moving the countrys
    if UP and not shift:countryObjects=action(countryObjects, "moveU")
    if DOWN and not shift:countryObjects=action(countryObjects, "moveD")
    if LEFT and not shift:countryObjects=action(countryObjects, "moveL")
    if RIGHT and not shift:countryObjects=action(countryObjects, "moveR")
    
    for country in countryObjects:
        country.update()
    
    found=False
    
    #country select
    if select and leftMouseDown:
        onCountry=False
        for country in countryObjects:
            for rect in country.rects:
                if country.mask.overlap(mouseMask, (mousePos[0]-rect.x, mousePos[1]-rect.y)):
                    selectedCountry=country
                    onCountry=True
                    found=True
                    break
            if found:
                break
        if not onCountry:
            selectedCountry=None
            select=False
    elif leftMouseDown:
        onCountry=False
        for country in countryObjects:
            for rect in country.rects:
                if country.mask.overlap(mouseMask, (mousePos[0]-rect.x, mousePos[1]-rect.y)):
                    selectedCountry=country
                    onCountry=True
                    select=True
                    found=True
                    break
            if found:
                break
        if not onCountry:
            selectedCountry=None
            select=False
    elif not select and not leftMouseDown:
        onCountry=False
        for country in countryObjects:
            for rect in country.rects:
                if country.mask.overlap(mouseMask, (mousePos[0]-rect.x, mousePos[1]-rect.y)):
                    selectedCountry=country
                    onCountry=True
                    found=True
                    break
            if found:
                break
        if not onCountry:
            selectedCountry=None
            select=False
        
    leftMouseDown=False
    #end country select
    
    
    #place for game to run
    
    #game.play(currentPlayer, phase)
    
    
    
    
    
    
    
    
    
    
    
    #put things on screen
    screen.fill([30,144,255])
    

    for country in countryObjects:
        country.blit(screen)
        
    updateScreen(selectedCountry, screen)
            
    if debug:
        text = font.render("FPS: "+str(int(100*clock.get_fps())/100), True, ((255/2)-40, (255/2)-40, (255/2)-40))
        textpos = text.get_rect(x=10, y=0)
        screen.blit(text, textpos)
            
            
    pygame.display.flip()
    clock.tick(100000)
