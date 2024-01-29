import pygame
from Country import *


class Player:
    def __init__(self, name):
        self.name=name
        self.countrys=[]
        
    def attack(self):
        pass
    
    def defend(self):
        pass

    def __str__(self):
        
        countryNames=[]
        
        for country in self.countrys:
            countryNames+=[country.name]
        c=str(self.name)
        for i in countryNames:
            c+="\n"
            c+=str(i)
            
            
            
        return c
