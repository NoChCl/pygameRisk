import pygame
from Country import *


class Neutral:
    def __init__(self, country):
        self.countrys=[country]
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
        c+=str(self.countrys.name)
        return c
