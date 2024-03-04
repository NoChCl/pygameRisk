import pygame, sys, math, random, pickle
from countryinfo import *


class Country():
    def __init__(self, size, name, debug = False):
        if debug: print(name) 
        self.name=name
        self.info = CountryInfo(name)
        self.contenent = self.info.region()
        
        try:
            self.borders = self.info.borders()
        except:
            print(self.name)
            self.borders = None
            
            
        #list of South Amarican Countrys,
        #liberary only seperates as "amarica's" not North/South
        #saCountrys is a list of south amarican countrys so that one can seperate the contenents
        saCountrys = "Argentina, Bolivia, Brazil, Chile, Colombia, Ecuador, Guyana, Paraguay, Peru, Suriname, Uruguay, Venezuela, French Guiana, trinidad and tobago, falkland islands"
        
        
        try:
            #if amarican contenent
            if self.contenent.lower() == "americas":
				#if contenent is South Amarican
                if self.name.lower() in saCountrys.lower():
                    self.contenent="South America"
                #If its amarican, but not south amarican, its North amarican
                else:
                    self.contenent="North America"   
            #russia is in asia and not europe 
            if name.lower() == "russia":
                self.contenent="Asia"
            #if contenent is africa, it makes the color a random red
            if self.contenent.lower() == "africa":
                self.color = [random.randint(150,255),random.randint(0,50),random.randint(0,50), 255]
            #if contenent is asia, make the color a random green
            elif self.contenent.lower() == "asia":
                self.color = [random.randint(0,50),random.randint(50,255),random.randint(0,50), 255]
            #if contenent is europe, make the color a random blue
            elif self.contenent.lower() == "europe":
                self.color = [random.randint(0,50),random.randint(0,50),random.randint(150,255), 255]
            #if contenent is south amarica, make the color a random teal
            elif self.contenent == "South America":
                self.color = [random.randint(0,50),random.randint(150,200),random.randint(150,200), 255]
            #if contenent is north amarica, make the color a random yellow
            elif self.contenent == "North America":
                self.color = [random.randint(175,255),random.randint(175,255),random.randint(0,100), 255]
            #if contenent is none of those, make the color a random purple
            else:
                self.color = [random.randint(100,255),random.randint(0,50),random.randint(100,255), 255]
        except:
			#in the imposible case that fails, contenent is none, and color is completely random
            print("!!!", self.contenent, "is unrecognised")
            self.contenent = None
            self.color = [random.randint(0,255),random.randint(0,255),random.randint(0,255), 255]
        
        #size is size
        self.size = size
        #start troops is 0
        self.troops = 0
        #starts uncontroled
        self.controled = None
        
        self.regions = []
        
        regions = self.info.geo_json()["features"][0]["geometry"]["coordinates"]
        
        
        if debug: 
            print(len(regions))
            for region in regions:
                print(region)
                print("--------------", len(region))
        if len(regions) == 1:
            if (name == "sweden"):
                self.regions += [regions[0][0]]
            else:
                self.regions += [regions[0]]
        elif len(regions) > 1:
            for i, region in enumerate(regions): 
                if len(region) == 1:
                    self.regions += region
                else:
                    self.regions += [region]
        else:
            print("ummm mate, you got's no regions...are you even a country??")
        
           
        for region in self.regions:
            for n in region:
                n[0] += 180
                n[0] *= 4
                n[1] *= -1
                n[1] += 90
                n[1] *= 4
        big=[0,0]
        bign=10000000000
        small=[bign,bign]
        for region in self.regions:
            for point in region:
                if point[0]<small[0]:
                    small[0]=point[0]
                if point[0]>big[0]:
                    big[0]=point[0]
                    
                if point[1]<small[1]:
                    small[1]=point[1]
                if point[1]>big[1]:
                    big[1]=point[1]
            
        small[0]-=10
        big[0]+=10
        small[1]-=10
        big[1]+=10
        if big[0]<small[0] or big[1]<small[1]:
            print(self.name, small, big)
            
        self.screenSize=[big[0]-small[0], big[1]-small[1]]
        
        for region in self.regions:
            for point in region:
                point[0]-=small[0]
                point[1]-=small[1]
        self.small = small
        self.big = big    
       
        self.pos=[0,0]
        self.pos[0]=-self.size[0]/2
        self.pos[1]=-self.size[1]/2
        
        self.zoomLvl=1
        
        
    def picklePrep(self):
        #self.image = pygame.image.tobytes(self.image)
        pass
        
    def unpickle(self):
        #self.image = pygame.image.frombytes(self.image)
        self.image = pygame.Surface(self.screenSize, flags=pygame.SRCALPHA)
        #r=self.image.get_rect()
        #r.move(small)
        
        for region in self.regions:
            pygame.draw.polygon(self.image, self.color, region)
            pygame.draw.polygon(self.image, [0, 0, 0,255], region, 1)
        self.rect = self.image.get_rect()
        
        self.rect = self.rect.move(self.small)
        
        self.mask = pygame.mask.from_surface(self.image)
        
        for region in self.regions:
            for point in region:
                point[0]+=self.small[0]
                point[1]+=self.small[1]
        
    
    def makeRects(self):
        self.rects = [self.rect, 
        self.rect.move([0, self.size[1]*self.zoomLvl]),
        self.rect.move([0, -self.size[1]*self.zoomLvl]),
        
        self.rect.move([self.size[0]*self.zoomLvl, self.size[1]*self.zoomLvl]),
        self.rect.move([self.size[0]*self.zoomLvl, 0]),
        self.rect.move([self.size[0]*self.zoomLvl, -self.size[1]*self.zoomLvl]),
        
        self.rect.move([-self.size[0]*self.zoomLvl, -self.size[1]*self.zoomLvl]),
        self.rect.move([-self.size[0]*self.zoomLvl, 0]),
        self.rect.move([-self.size[0]*self.zoomLvl, self.size[1]*self.zoomLvl]),]
        
    
    def update(self):
        if self.name=="united states":
            #print(self.pos)
            pass
            
        if self.pos[0]>=self.size[0]/2*self.zoomLvl:
            self.rect=self.rect.move(-self.size[0]*self.zoomLvl, 0)
            self.pos[0]-= self.size[0]*self.zoomLvl
            
        elif self.pos[0]<=-((self.size[0]/2*self.zoomLvl)+self.size[0]*self.zoomLvl):
            self.rect=self.rect.move(self.size[0]*self.zoomLvl, 0)
            self.pos[0]+=self.size[0]*self.zoomLvl
            
        elif self.pos[1]>=self.size[1]/2*self.zoomLvl:
            self.rect=self.rect.move(0, -self.size[1]*self.zoomLvl)
            self.pos[1]-= self.size[1]*self.zoomLvl
            
        elif self.pos[1]<=-((self.size[1]/2*self.zoomLvl)+self.size[1]*self.zoomLvl):
            self.rect=self.rect.move(0, self.size[1]*self.zoomLvl)
            self.pos[1]+=self.size[1]*self.zoomLvl
                    
    def move(self, speed):
        self.rect = self.rect.move(speed)
        self.pos[0]+=speed[0]
        self.pos[1]+=speed[1]
        
        
    def blit(self, screen):
        self.makeRects()
        for rect in self.rects:
            screen.blit(self.image, rect)
        
        '''
        #center
        screen.blit(self.image, self.rect)
        screen.blit(self.image, self.rect.move([0, self.size[1]*self.zoomLvl]))
        screen.blit(self.image, self.rect.move([0, -self.size[1]*self.zoomLvl]))
        
        #right side
        screen.blit(self.image, self.rect.move([self.size[0]*self.zoomLvl, self.size[1]*self.zoomLvl]))
        screen.blit(self.image, self.rect.move([self.size[0]*self.zoomLvl, 0]))
        screen.blit(self.image, self.rect.move([self.size[0]*self.zoomLvl, -self.size[1]*self.zoomLvl]))
        
        #left side
        screen.blit(self.image, self.rect.move([-self.size[0]*self.zoomLvl, -self.size[1]*self.zoomLvl]))
        screen.blit(self.image, self.rect.move([-self.size[0]*self.zoomLvl, 0]))
        screen.blit(self.image, self.rect.move([-self.size[0]*self.zoomLvl, self.size[1]*self.zoomLvl]))
        '''
        
    def zoom(self, direction):
        if direction =="-":
            self.zoomLvl/=1.25
            self.pos[0]/=1.25
            self.pos[1]/=1.25
            for region in self.regions:
                for point in region:
                    point[0]/=1.25
                    point[1]/=1.25
        if direction =="+":
            self.zoomLvl*=1.25
            self.pos[0]*=1.25
            self.pos[1]*=1.25
            for region in self.regions:
                for point in region:
                    #point[0]-=self.size[0]/2
                    point[0]*=1.25
                    #point[1]-=self.size[1]/2
                    point[1]*=1.25

        
        big=[0,0]
        bign=10000000000
        small=[bign,bign]
        for region in self.regions:
            for point in region:
                if point[0]<small[0]:
                    small[0]=point[0]
                if point[0]>big[0]:
                    big[0]=point[0]
                    
                if point[1]<small[1]:
                    small[1]=point[1]
                if point[1]>big[1]:
                    big[1]=point[1]
            
        small[0]-=10
        big[0]+=10
        small[1]-=10
        big[1]+=10
        if big[0]<small[0] or big[1]<small[1]:
            print(self.name, small, big)
            
        screenSize=[big[0]-small[0], big[1]-small[1]]
        
        for region in self.regions:
            for point in region:
                point[0]-=small[0]
                point[1]-=small[1]
            
        self.image = pygame.Surface(screenSize, flags=pygame.SRCALPHA)
        #r=self.image.get_rect()
        #r.move(small)
        
        for region in self.regions:
            pygame.draw.polygon(self.image, self.color, region)
            pygame.draw.polygon(self.image, [0, 0, 0,255], region, 1)
        self.rect = self.image.get_rect()
        
        self.rect = self.rect.move(small)
        
        self.mask = pygame.mask.from_surface(self.image)
        
        for region in self.regions:
            for point in region:
                point[0]+=small[0]
                point[1]+=small[1]
        
        m=[self.pos[0]+(self.size[0]/2), self.pos[1]+(self.size[1]/2)]
        
        
        self.rect = self.rect.move(m)
        if self.name=="united states":
            #print(self.pos)
            pass
        
    def __str__(self):
        s=self.name
        s+=":"
        s+=str(self.contenent)
        s+=":"
        s+= str(self.size)
        s+=":"
        s+=str(self.regions)
        s+="\n"
        return s
        
if __name__ == "__main__":
    pygame.init()
    size = [1440, 720]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("RISK")
    clock = pygame.time.Clock();
    
    us = Country((1024,768), "united states of america", False)
    
    works=False
    while not works:
        try:
            loadFromFile=pickle.load(open("test.info","rb"))
            us = loadFromFile
            us.unpickle()
            works=True
            print("Loaded")
        except Exception as e:
            print(e)
            print("Creating File")
            works=False
            #countryData = getInfo(size, screen)
            pickle.dump(us, open( "test.info", "wb" ) )
    #pickle.dump(us, open( "test.info", "wb" ) )
    while True:
        #get events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
         
            
        screen.fill([30,144,255])
        screen.blit(us.image, us.rect)
        pygame.display.flip()
        clock.tick(60)
    
    
