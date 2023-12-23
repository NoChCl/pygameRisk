import pygame, sys, math, random
from countryinfo import *


class Country():
    def __init__(self, size, name):
        self.name=name
        
        saCountrys = "Argentina, Bolivia, Brazil, Chile, Colombia, Ecuador, Guyana, Paraguay, Peru, Suriname, Uruguay, Venezuela, French Guiana, trinidad and tobago, falkland islands"
        
        try:
            self.contenent=CountryInfo(name).region()
            if self.contenent.lower() == "americas":
                if self.name.lower() in saCountrys.lower():
                    self.contenent="South America"
                else:
                    self.contenent="North America"    
            if name.lower() == "russia":
                self.contenent="Asia"
            if self.contenent.lower() == "africa":
                self.color = [random.randint(150,255),random.randint(0,50),random.randint(0,50), 255]
            elif self.contenent.lower() == "asia":
                self.color = [random.randint(0,50),random.randint(50,255),random.randint(0,50), 255]
            elif self.contenent.lower() == "europe":
                self.color = [random.randint(0,50),random.randint(0,50),random.randint(150,255), 255]
            elif self.contenent == "South America":
                self.color = [random.randint(0,50),random.randint(150,200),random.randint(150,200), 255]
            elif self.contenent == "North America":
                self.color = [random.randint(175,255),random.randint(175,255),random.randint(0,100), 255]
            else:
                self.color = [random.randint(100,255),random.randint(0,50),random.randint(100,255), 255]
        except:
            self.contenent = None
            self.color = [random.randint(0,255),random.randint(0,255),random.randint(0,255), 255]
        
        self.size = size
        self.troops = 0
        self.controled = ""
        self.image= pygame.Surface(self.size, flags=pygame.SRCALPHA)
        self.regions = []
        self.mask = pygame.mask.from_surface(self.image)
    
    def addRegions(self, regions):
        self.regions+=regions
        
        
    def update(self):
        pass
        
        
if __name__ == "__main__":
    c = Country((1024,768), "bobonia", (255,128,64, 255))
