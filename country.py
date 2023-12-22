#
import pygame, sys, math, random
from countryinfo import *


class Country():
    def __init__(self, size, name, color):
        self.name=name
        self.size = size
        self.color = color
        self.image= pygame.Surface(self.size, flags=pygame.SRCALPHA)
        self.regions = []
    
    def addRegions(self, regions):
        self.regions+=regions
        
        
    def prints(self):
        print(self.name)
        print(self.color)
        print(self.regions)
        print("\n\n")
        
if __name__ == "__main__":
    c = Country((1024,768), "bobonia", (255,128,64, 255))
