import pygame
try:   
    from Country import *
except:
    from country import *
    
def updateScreen(selectedCountry, screen):
    pygame.draw.rect(screen, [255, 255, 255],(0,540,300,180))
    
    font = pygame.font.Font(None, 32)
    try:
        text = font.render("Country: "+str(selectedCountry.name[0].upper()+selectedCountry.name[1:-1]+selectedCountry.name[-1]), True, (10, 10, 10))
    except:
        text = font.render("Country: None Selected", True, (10, 10, 10))
    textpos = text.get_rect(x=10, y=550)
    screen.blit(text, textpos)
    
    font = pygame.font.Font(None, 25)
    try:
        text = font.render("Troops: "+str(selectedCountry.troops), True, (10, 10, 10))
    except:
        text=font.render("Troops: N/A", True, (10, 10, 10))
    textpos = text.get_rect(x=10, y=575)
    screen.blit(text, textpos)
            
    try:
        text = font.render("Controled By: "+str(selectedCountry.controled.name), True, (10, 10, 10))
    except:
        text=font.render("Controled By: N/A", True, (10, 10, 10))
    textpos = text.get_rect(x=10, y=595)
    screen.blit(text, textpos)
    
    try:
        text = font.render("Abbreviation: "+str(selectedCountry.abr), True, (10, 10, 10))
    except:
        text=font.render("Abbreviation: N/A", True, (10, 10, 10))
    textpos = text.get_rect(x=10, y=615)
    screen.blit(text, textpos)
    
    try:
        text = font.render("Borders: "+str(selectedCountry.borders), True, (10, 10, 10))
    except:
        text=font.render("Borders: N/A", True, (10, 10, 10))
    textpos = text.get_rect(x=10, y=635)
    screen.blit(text, textpos)
