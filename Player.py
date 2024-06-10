import pygame
try:   
    from Country import *
except:
    from country import *

class Player:
    def __init__(self, name):
        self.name=name
        self.countrys=[]
    
    def place(self):
        self.avalableTroops=int(len(self.countrys)/3)
        if self.avalableTroops>3:
            self.avalableTroops=3
        
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
