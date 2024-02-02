import pygame, sys, math, random
from countryinfo import *
from Country import *
from Game import *
from infoScreen import *
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
                if count<=3:
                    for player in self.players:
                        if len(countrys)==0:
                            break
                        player.countrys+=[countrys.pop(random.randint(0,(len(countrys)-1)))]
                if len(countrys)==0:
                    break
                n+=[Neutral(countrys.pop(random.randint(0,(len(countrys)-1))))]
            self.players+=n
        elif gameType=="random":
            while len(countrys)>0:
                for player in self.players:
                    if len(countrys)==0:
                        break
                    elif len(countrys)==1:
                        player.countrys+=[countrys.pop(0)]
                    else:
                        player.countrys+=[countrys.pop(random.randint(0,(len(countrys)-1)))]
            
            
            for player in self.players:
                for country in player.countrys:
                    country.controled=player.name
        
        
        

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
            text = font.render("Adding: "+str(name[0].upper()+name[1:-1]+name[-1]), True, (10, 10, 10))
        except:
            text = font.render("Adding: Other", True, (10, 10, 10))
        textpos = [(size[0]/2)-233, 400]
        screen.blit(text, textpos)
        
        pygame.display.flip()

        
        try:
            countryObjects+=[Country(size, name)]
            countryObjects[-1].picklePrep()
        except:
            pass
        
        
    # ~ #Sweden just doesn't work, so why let it?
    # ~ for country in countryObjects:
        # ~ if country.name == "sweden":
            # ~ countryObjects.remove(country)
            # ~ break

    
    return countryObjects


def decode(code, screen, size):
	font = pygame.font.Font(None, 32)
	l=[0,20]
	countrys=code.split("\n")
	countryObjects=[]
	for country in countrys:
		if not country =="":
			info=country.split(":")
			
			name = info[0]
			
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
				text = font.render("Loaded: "+str(name[0].upper()+name[1:-1]+name[-1]), True, (10, 10, 10))
			except:
				text = font.render("Loaded: Other", True, (10, 10, 10))
			textpos = [(size[0]/2)-233, 400]
			screen.blit(text, textpos)
		
			pygame.display.flip()
			
			r = ""
			
			for i in info[3]:
				if i !="'":
					r+=i
			if info[0]=="norway":
				print()
				print(r)
				print("\n")
				
			r=r.split()
					
					
			if info[0]=="norway":
				print()
				print(r)
				print("\n")
			
			countryObjects+=[Country(size,info[0],info[1])]
			for regions in r:
				countryObjects[-1].addRegions([int(i) for i in regions])
	return countryObjects
    
def returnList(S):
	L=[]
	
	for i, s in enumerate(S):
		if s=="]":
			return L
		elif s=="[":
			l+=returnList(S[i:-1])
		
