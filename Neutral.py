import pygame
try:   
    from Country import *
except:
    from country import *

class Neutral:
    def __init__(self, country):
        self.countrys=[country]
        self.name="__Neutral__"
        self.countrys[0].troops=2
        
    def place(self):
        pass
        
    def attack(self):
        pass
    
    def defend(self):
        nTroops=self.countrys[0].troops
        
        if Ntroops >=2:
            roll=2
        else:
            roll = 1
        
        return roll
    def __str__(self):
        c="Neutral\n"
        c+=str(self.countrys[0].name)
        return c
