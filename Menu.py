import pygame, sys, math, random
from countryinfo import *
from Country import *
from Game import *
from infoScreen import *
from Player import *
from Neutral import *

def menu(size, screen):
    menuOpen=True
    menuState='main'
    
    quitImage=pygame.Surface([700,75])
    quitImage.fill([125,140,140])
    
    font = pygame.font.Font(None, 80)
    text = font.render("Quit Game", True, (10, 10, 10))
    textpos = text.get_rect(x=350-(294/2), y=10)
    quitImage.blit(text, textpos)
        
    quitButton=menuObject(quitImage,[370,500])
    
    
    
    while menuOpen:
        screen.fill([30,144,255])
        screen.blit(pygame.image.load("menuBg.png"), (0,0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mousePos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    leftMouseDown=True
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mousePos = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    leftMouseDown=True
                    
        screen.blit(quitButton.image, quitButton.rect)
                    
        pygame.display.flip()
        
class menuObject():
    def __init__(self, image, pos):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect=self.rect.move(pos)
        self.mask=pygame.mask.from_surface(image)

if __name__ == "__main__":
    pygame.init()
    size = [1440, 720]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("RISK")
    clock = pygame.time.Clock();
    font = pygame.font.Font(None, 16)

    menu(size, screen)
