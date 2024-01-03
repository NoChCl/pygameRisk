import pygame, sys, math, random
from countryinfo import *


class Country():
    def __init__(self, size, name, cont):
        self.name=name
        
        #list of South Amarican Countrys,
        #liberary only seperates as "amarica's" not North/South
        #saCountrys is a list of south amarican countrys so that one can seperate the contenents
        saCountrys = "Argentina, Bolivia, Brazil, Chile, Colombia, Ecuador, Guyana, Paraguay, Peru, Suriname, Uruguay, Venezuela, French Guiana, trinidad and tobago, falkland islands"
        
        try:
            self.contenent=cont
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
            self.contenent = None
            print("!!!", cont, "is unrecognised")
            self.color = [random.randint(0,255),random.randint(0,255),random.randint(0,255), 255]
        
        #size is size
        self.size = size
        #start troops is 0
        self.troops = 0
        #starts uncontroled
        self.controled = ""
        
        self.regions = []
        regions = CountryInfo(name).geo_json()["features"][0]["geometry"]["coordinates"]
        for i, region in enumerate(regions): 
            if len(regions) < 2:
                self.regions += regions[i][0]
            else:
                self.regions += regions[i]
            
        for region in self.regions:
            for n in region:
                n[0] += 180
                n[0] *= 4
                n[1] *= -1
                n[1] += 90
                n[1] *= 4
            
        self.image = pygame.Surface(self.size, flags=pygame.SRCALPHA)
        for region in self.regions:
            pygame.draw.polygon(self.image, self.color, region)
            pygame.draw.polygon(screen, [0, 0, 0,255], region, 1)
        self.rect = self.image.get_rect()
        
        self.mask = pygame.mask.from_surface(self.image)
        
    
    def addRegions(self, regions):
        self.regions+=regions

        
    def update(self):
        pass
        
        
if __name__ == "__main__":
    pygame.init()
    size = [1440, 720]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("RISK")
    clock = pygame.time.Clock();
    
    c = Country((1024,768), "united states of america", "americas")
    
    while True:
        #get events
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
         
            
        screen.fill([30,144,255])
        screen.blit(c.image, c.rect)
        pygame.display.flip()
        clock.tick(60)
    
    
