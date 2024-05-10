import pygame
try:   
    from Country import *
except:
    from country import *

class Neutral:
    def __init__(self, country):
        self.country=country
        self.name="__Neutral__"
        
    def attack(self):
        pass
    
    def defend(self):
        nTroops=self.country.troops
        
        if Ntroops >=2:
            roll=2
        else:
            roll = 1
        
        return roll
    def __str__(self):
        c="Neutral\n"
        c+=str(self.country.name)
        return c
