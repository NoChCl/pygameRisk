import pygame, random
from countryinfo import *
from country import *


def action(countries, action):
    #zoom in
    if action == "+":
        for country in countries:
            for region in country.regions:
                for c in region:
                    c[0] *=1.25
                    c[1] *=1.25
                    c[1]-=720/8
                    c[0]-=1440/8
    #zoom out
    elif action == "-":
        for country in countries:
            for region in country.regions:
                for c in region:
                    c[0]+=1440/8
                    c[1]+=720/8
                    c[0] /=1.25
                    c[1] /=1.25

    #move left
    if action == "moveL":
        for country in countries:
            country.move([10,0])
            
    #move right
    elif action == "moveR":
        for country in countries:
            country.move([-10,0])
    #move up
    elif action == "moveU":
        for country in countries:
            country.move([0,10])
    #move down
    elif action == "moveD":
        for country in countries:
            country.move([0,-10])
    
    return countries
    
    
    
    
    
    
    
def getInfo(size, screen):
    
    font = pygame.font.Font(None, 32)
    
    countryObjects=[]
    names = []
    c = CountryInfo()
    c = c.all()
    for key in c:
        names += [key]
    l=[0,20]
    for name in names:
        
        #loading screen
        screen.fill([30,144,255])
        screen.blit(pygame.image.load("risk.png"), [(size[0]/2)-233, 100])
        pygame.draw.rect(screen, [255, 255, 255],((size[0]/2)-236,374,470,22), 1)
        l[0]+=2
        load=pygame.Surface(l)
        screen.blit(load, [(size[0]/2)-235,375])
        
        #quit on quit
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

        #more loading screen
        try:
            text = font.render("Added: "+str(name[0].upper()+name[1:-1]+name[-1]), True, (10, 10, 10))
        except:
            text = font.render("Added: Other", True, (10, 10, 10))
        textpos = [(size[0]/2)-233, 400]
        screen.blit(text, textpos)
        
        pygame.display.flip()

        
        try:
            countryObjects+=[Country(size, name)]
        except:
            pass
        

    # ~ #Sweden just doesn't work, so why let it?
    # ~ for country in countryObjects:
        # ~ if country.name == "sweden":
            # ~ countryObjects.remove(country)
            # ~ break

    
    return countryObjects


    
    
