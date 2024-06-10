import pygame
try:   
    from Country import *
except:
    from country import *
    
def placementScreen(selectedCountry, player, screen):
    pygame.draw.rect(screen, [255, 255, 255],(1140,540,300,180))
    
    font = pygame.font.Font(None, 32)
    try:
        text = font.render("Country: "+str(selectedCountry.name[0].upper()+selectedCountry.name[1:-1]+selectedCountry.name[-1]), True, (10, 10, 10))
    except:
        text = font.render("Country: None Selected", True, (10, 10, 10))
    textpos = text.get_rect(x=1150, y=550)
    screen.blit(text, textpos)
    
    font = pygame.font.Font(None, 25)
    try:
        text = font.render("Your Troops: "+str(player.avalableTroops), True, (10, 10, 10))
    except:
        text=font.render("Your Troops: N/A", True, (10, 10, 10))
    textpos = text.get_rect(x=1150, y=575)
    screen.blit(text, textpos)
            
    try:
        text = font.render("Countrys troops: "+str(selectedCountry.troops), True, (10, 10, 10))
    except:
        text=font.render("Countrys troops: N/A", True, (10, 10, 10))
    textpos = text.get_rect(x=1150, y=595)
    screen.blit(text, textpos)
    
    try:
        text = font.render("Adding "+str(selectedCountry.addedTroops)+" troops to country", True, (10, 10, 10))
    except:
        text=font.render("Adding 0 troops to country", True, (10, 10, 10))
    textpos = text.get_rect(x=1150, y=615)
    screen.blit(text, textpos)
    
    # ~ try:
        # ~ text = font.render("Borders: "+str(selectedCountry.borders), True, (10, 10, 10))
    # ~ except:
        # ~ text=font.render("Borders: N/A", True, (10, 10, 10))
    # ~ textpos = text.get_rect(x=10, y=635)
    # ~ screen.blit(text, textpos)
    

