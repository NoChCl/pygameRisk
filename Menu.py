import pygame, sys, math, random, os, pathlib
from countryinfo import *
try:   
    from Country import *
except:
    from country import *
from Game import *
from infoScreen import *
from Player import *
from Neutral import *

def menu(size, screen):
    menuOpen=True
    
    #newGame
    newGameImage=pygame.Surface([700,75])
    newGameImage.fill([125,140,140])
    
    font = pygame.font.Font(None, 80)
    text = font.render("New Game", True, (10, 10, 10))
    textpos = text.get_rect(x=350-(294/2), y=10)
    newGameImage.blit(text, textpos)
        
    newGameButton=menuObject(newGameImage,[370,300])
    
    #loadGame
    loadGameImage=pygame.Surface([700,75])
    loadGameImage.fill([125,140,140])
    
    font = pygame.font.Font(None, 80)
    text = font.render("Load Game", True, (10, 10, 10))
    textpos = text.get_rect(x=350-(294/2), y=10)
    loadGameImage.blit(text, textpos)
        
    loadGameButton=menuObject(loadGameImage,[370,400])
    
    #Neutral
    selNeutralImage=pygame.Surface([700,75])
    selNeutralImage.fill([125,140,140])
    
    font = pygame.font.Font(None, 80)
    text = font.render("Neutral Game", True, (10, 10, 10))
    textpos = text.get_rect(x=350-(294/2), y=10)
    selNeutralImage.blit(text, textpos)
        
    neutralButton=menuObject(selNeutralImage,[370,350])
    
    #Equal
    selEqualImage=pygame.Surface([700,75])
    selEqualImage.fill([125,140,140])
    
    font = pygame.font.Font(None, 80)
    text = font.render("Equal Game", True, (10, 10, 10))
    textpos = text.get_rect(x=350-(294/2), y=10)
    selEqualImage.blit(text, textpos)
        
    equalButton=menuObject(selEqualImage,[370,450])
    
    
    #Select
    selImage=pygame.Surface([700,75])
    selImage.fill([125,140,140])
    
    font = pygame.font.Font(None, 80)
    text = font.render("Select Game", True, (10, 10, 10))
    textpos = text.get_rect(x=350-(294/2), y=10)
    selImage.blit(text, textpos)
        
    selectButton=menuObject(selImage,[370,350])
    
    #Random
    randomImage=pygame.Surface([700,75])
    randomImage.fill([125,140,140])
    
    font = pygame.font.Font(None, 80)
    text = font.render("Random Game", True, (10, 10, 10))
    textpos = text.get_rect(x=350-(294/2), y=10)
    randomImage.blit(text, textpos)
        
    randomButton=menuObject(randomImage,[370,450])
    
    #quitGame
    quitImage=pygame.Surface([700,75])
    quitImage.fill([125,140,140])
    
    font = pygame.font.Font(None, 80)
    text = font.render("Quit Game", True, (10, 10, 10))
    textpos = text.get_rect(x=350-(294/2), y=10)
    quitImage.blit(text, textpos)
        
    quitButton=menuObject(quitImage,[370,500])
    
    #backArrow
    backArrow=menuObject(pygame.image.load("backArrow.png"),[10,10])
    
    
    mousePos = pygame.mouse.get_pos()
    
    leftMouseDown=False
    
    newGame=False
    
    while menuOpen:
        leftMouseDown=False
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
        if leftMouseDown:
            if quitButton.clicked(mousePos):
                quit()
            if loadGameButton.clicked(mousePos):
                load=loadGame(screen)
                if not load==None:
                    return load
            if newGameButton.clicked(mousePos):
                newGame=True
                
                while newGame:
                    leftMouseDown=False
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
                    if leftMouseDown:
                        if backArrow.clicked(mousePos):
                            newGame=False
                        if neutralButton.clicked(mousePos):
                            return["new","games/Countrys.info", "neutral", 5]
                        if equalButton.clicked(mousePos):
                            Equal=True
                            
                            while Equal:
                                leftMouseDown=False
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
                                if leftMouseDown:
                                    if selectButton.clicked(mousePos):
                                        return["new","games/Countrys.info","select", 5]
                                    if randomButton.clicked(mousePos):
                                        return["new","games/Countrys.info","random", 5]
                                    if backArrow.clicked(mousePos):
                                        Equal=False
                                screen.blit(backArrow.image, backArrow.rect)
                                screen.blit(selectButton.image, neutralButton.rect)
                                screen.blit(randomButton.image, equalButton.rect)
                                
                                pygame.display.flip()
                            
                    
                    screen.blit(backArrow.image, backArrow.rect)
                    screen.blit(neutralButton.image, neutralButton.rect)
                    screen.blit(equalButton.image, equalButton.rect)
                    
                    pygame.display.flip()
                    
        screen.blit(quitButton.image, quitButton.rect)
        screen.blit(loadGameButton.image, loadGameButton.rect)
        screen.blit(newGameButton.image, newGameButton.rect)
        
        pygame.display.flip()
def loadGame(screen):
    backArrow=menuObject(pygame.image.load("backArrow.png"),[10,10])
    
    font = pygame.font.Font(None, 80)
    gameText=font.render("Games:", True, (10, 10, 10))
    gameTextPos=gameText.get_rect(x=370, y=190)
    
    files=list(os.listdir(str(pathlib.Path(__file__).parent.resolve())+"/games"))
    games=[]
    for f in files:
        if ".info" in f:
            games+=[f]
    gameButtons=[]
    for x, game in enumerate(games):
        Image=pygame.Surface([700,75])
        Image.fill([125,140,140])
        text = font.render(game, True, (10, 10, 10))
        textpos = text.get_rect(x=20, y=10)
        Image.blit(text, textpos)
        gameButtons+=[menuObject(Image,[370,250+85*x])]
        
    while True:
        leftMouseDown=False
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
        if leftMouseDown:
            if backArrow.clicked(mousePos):
                return None
            for x,button in enumerate(gameButtons):
                if button.clicked(mousePos):
                    return ["load","games/"+games[x]]
        
        for button in gameButtons:
            screen.blit(button.image, button.rect)
        screen.blit(backArrow.image, backArrow.rect)
        screen.blit(gameText, gameTextPos)
        pygame.display.flip()
    
    
class menuObject():
    def __init__(self, image, pos):
        self.image=image
        self.rect=self.image.get_rect()
        self.rect=self.rect.move(pos)
        self.mask=pygame.mask.from_surface(image)
        
    def clicked(self, mousePos):
        mouse=pygame.Surface([1,1])
        mouseMask=pygame.mask.from_surface(mouse)
        
        if self.mask.overlap(mouseMask, (mousePos[0]-self.rect.x, mousePos[1]-self.rect.y)):
            return True

if __name__ == "__main__":
    pygame.init()
    size = [1440, 720]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("RISK")
    clock = pygame.time.Clock();
    font = pygame.font.Font(None, 16)

    menu(size, screen)
