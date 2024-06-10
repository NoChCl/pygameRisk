import pygame, sys, math, random, pickle
from countryinfo import *
try:   
    from Country import *
except:
    from country import *
from Game import *
from infoScreen import *
from actionScreen import *
from Player import *
from Neutral import *

class Game():
    def __init__(self, players, gameType, countryObjects):
        countrys=countryObjects
        
        self.players=players
        
        numbPlayers=len(self.players)
        n=[]
        if gameType=="neutral":
            count=0
            while len(countrys)>0:
                count+=1
                if count<=12:
                    for player in self.players:
                        if len(countrys)==0:
                            break
                        player.countrys+=[countrys.pop(random.randint(0,(len(countrys)-1)))]
                if len(countrys)==0:
                    break
                n+=[Neutral(countrys.pop(random.randint(0,(len(countrys)-1))))]
            self.players+=n
            
            self.countryObjects=[]
            for player in self.players:
                for country in player.countrys:
                    country.controled=player
                    countryObjects+=[country]
        elif gameType=="random":
            while len(countrys)>0:
                for player in self.players:
                    if len(countrys)==0:
                        break
                    elif len(countrys)==1:
                        player.countrys+=[countrys.pop(0)]
                    else:
                        player.countrys+=[countrys.pop(random.randint(0,(len(countrys)-1)))]
            self.countryObjects=[]
            for player in self.players:
                #print(player)
                #print("-----------------------------------")
                for country in player.countrys:
                    country.controled=player
                    countryObjects+=[country]
        players+=[None]
        
        plusButton=pygame.Surface([100,50])
        plusButton.fill([255,255,255])
        pygame.draw.rect(plusButton, (80,215,240), pygame.Rect(0,0,100,50), width=0, border_radius=25)
        
        font = pygame.font.Font(None, 25)
        text = font.render("Add Troop", True, (10, 10, 10))
        textpos = text.get_rect(x=7, y=15)
        plusButton.blit(text, textpos)
        
        self.placementPlus=buttonObject(plusButton,[1150, 635])
        #self.placementMinus=
                    
    def play(self, player, phase, country, screen):
        if phase == "placement":
            player.place()
            if country in player.countrys:
                placementScreen(country, player, screen)
            else:
                placementScreen(None, player, screen)
            screen.blit(self.placementPlus.image, self.placementPlus.rect)
        elif phase == "attack":
            pass
        elif phase == "movement":
            pass
        else:
            print("Error, phase"+phase+"is not recognised, valid phases are: placement, attack, and movement")
            quit()
            
    def rollDice():
        return random.randint(1,6)
        
    def rebuild(self):
        plusButton=pygame.Surface([100,50])
        plusButton.fill([255,255,255])
        pygame.draw.rect(plusButton, (80,215,240), pygame.Rect(0,0,100,50), width=0, border_radius=25)
        
        font = pygame.font.Font(None, 25)
        text = font.render("Add Troop", True, (10, 10, 10))
        textpos = text.get_rect(x=7, y=15)
        plusButton.blit(text, textpos)
        
        self.placementPlus=buttonObject(plusButton,[1150, 635])
        
        
        
class buttonObject():
    def __init__(self, image, pos):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect=self.rect.move(pos)
        self.mask=pygame.mask.from_surface(image)
        
    def clicked(self, mousePos):
        mouse=pygame.Surface([1,1])
        mouseMask=pygame.mask.from_surface(mouse)
        
        if self.mask.overlap(mouseMask, (mousePos[0]-self.rect.x, mousePos[1]-self.rect.y)):
            return True
    
        
        

if __name__ == "__main__":
    #pygame init and other important init's
    pygame.init()
    size = [1440, 720]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("RISK")
    clock = pygame.time.Clock();
    font = pygame.font.Font(None, 16)

    # ~ #makes all country objects
    countryObjects=getInfo(size, screen)
    
    players=[]
    for i in range(5):
        players+=[Player(str(i))]
        
    game = Game(players, "random", countryObjects)
    
    players=game.players
    
    for player in players:
        print("--------------------------------")
        print(player)
    






def action(countries, action):
    #zoom in
    if action == "+":
        for country in countries:
            country.zoom("+")
    #zoom out
    elif action == "-":
        for country in countries:
            country.zoom("-")

            #country.image = pygame.transform.scale_by(country.image, (1/2))

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
    
    
    
def quitGame(game, countryObjects, gameName, zoom, screen, window, size):
    fade=pygame.Surface(size)
    fade.fill([0,0,0])
    fade.set_alpha(150)
    screen.blit(fade, [0,0])
    
    font = pygame.font.Font(None, 100)
    text = font.render("Quitting", True, (255, 255, 255))
    textpos = text.get_rect(x=575, y=300)
    screen.blit(text, textpos)
    
    makeScreen(screen, window, size)
    
    game.placementPlus=None
    
    try:
        if zoom==0:
            countryObjects=action(countryObjects, "+")
        elif zoom==1:
            pass
        else:
            zoom-=1
            for x in range(zoom):
                countryObjects=action(countryObjects, "-")

        for country in countryObjects:
            country.picklePrep()
        
        game.countryObjects=countryObjects
        
        pickle.dump(game, open(gameName, "wb" ))
    except Exception as e:
        print(e)
        print("didnt save :(")
    print("safe to quit")
    sys.exit()
    
    
def getInfo(size, screen, window):
    font = pygame.font.Font(None, 16)
    
    killSizeThreshold=2500
    
    countryObjects=[]
    names = []
    c = CountryInfo()
    c = c.all()
    for key in c:
        names += [key]
    l=[0,20]
    
    Itext = font.render("Generating new game, this may take a while...", True, (10, 10, 10))
    Itextpos = [(size[0]/2)-233, 425]

    font = pygame.font.Font(None, 32)

    for name in names:
        
        #loading screen
        screen.fill([30,144,255])
        screen.blit(pygame.image.load("risk.png"), [(size[0]/2)-233, 100])
        pygame.draw.rect(screen, [255, 255, 255],((size[0]/2)-236,374,470,22), 1)
        l[0]+=2
        load=pygame.Surface(l)
        screen.blit(load, [(size[0]/2)-235,375])
        
        screen.blit(Itext, Itextpos)
        
        #quit on quit
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()

        #more loading screen
        try:
            text = font.render("Adding: "+str(name[0].upper()+name[1:-1]+name[-1]), True, (10, 10, 10))
        except:
            text = font.render("Adding: Other", True, (10, 10, 10))
        textpos = [(size[0]/2)-233, 400]
        screen.blit(text, textpos)
        
        makeScreen(screen, window, size)

        
        try:
            countryObjects+=[Country(size, name)]
            countryObjects[-1].picklePrep()
        except:
            pass
        
    for country in countryObjects:
        if country.info.area()==None:
            pass
        elif country.info.area()<=killSizeThreshold:
            countryObjects.remove(country)

    
    return countryObjects


def decode(countryObjects, screen, window, size):
    l=[0,20]
    font = pygame.font.Font(None, 32)
    for country in countryObjects:
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
            text = font.render("Loading: "+str(country.name[0].upper()+country.name[1:-1]+country.name[-1]), True, (10, 10, 10))
        except:
            text = font.render("Loading: Other", True, (10, 10, 10))
        textpos = [(size[0]/2)-233, 400]
        screen.blit(text, textpos)
        
        makeScreen(screen, window, size)
        
        country.unpickle()
    
    return countryObjects
    
    
def makeScreen(screen, window, size):
    width, height=pygame.display.get_surface().get_size()
    width=width/size[0]
    height=height/size[1]
    if width==height:
        window.blit(pygame.transform.scale(screen, [width*size[0], height*size[1]]), [0,0])
    elif width>height:
        window.blit(pygame.transform.scale(screen, [height*size[0], height*size[1]]), [(width-height)*(size[0]/2),0])
    elif width<height:
        window.blit(pygame.transform.scale(screen, [width*size[0], width*size[1]]), [0,(height-width)*(size[1]/2)])
    else:
        window.blit(screen, [0,0])

    pygame.display.flip()

def getScaledMouse(size):
    x, y=pygame.display.get_surface().get_size()
    xScale=size[0]/x
    yScale=size[1]/y
    
    x2=x/size[0]
    y2=y/size[1]
    
    mousex,mousey=pygame.mouse.get_pos()

    
    if x2==y2:
        offset=[0,0]
        r=[xScale*mousex, yScale*mousey]
    elif x2>y2:
        offset=[(x2-y2)*(size[0]/2),0]
        r=[yScale*(mousex-offset[0]), yScale*mousey]
    elif x2<y2:
        offset=[0,(y2-x2)*(size[1]/2)]
        r=[xScale*mousex, (mousey-offset[1])*xScale]
    else:
        print('something went wrong, check function "getScaledMouse"')
    return r
    
    
