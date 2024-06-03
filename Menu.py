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

import pygame_widgets
from pygame_widgets.textbox import TextBox


def menu(size, screen, window):
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
    
    
    mousePos = getScaledMouse(size)
    
    leftMouseDown=False
    
    newGame=False
    
    while menuOpen:
        leftMouseDown=False
        screen.fill([30,144,255])
        screen.blit(pygame.image.load("menuBg.png"), (0,0))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEMOTION:
                mousePos = getScaledMouse(size)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    leftMouseDown=True
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mousePos = getScaledMouse(size)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    leftMouseDown=True
        if leftMouseDown:
            if quitButton.clicked(mousePos):
                quit()
            if loadGameButton.clicked(mousePos):
                load=loadGame(screen, window, size)
                mousePos = getScaledMouse(size)
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
                            mousePos = getScaledMouse(size)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if pygame.mouse.get_pressed()[0]:
                                leftMouseDown=True
                        if event.type==pygame.QUIT:
                            sys.exit()
                        if event.type == pygame.MOUSEMOTION:
                            mousePos = getScaledMouse(size)
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if pygame.mouse.get_pressed()[0]:
                                leftMouseDown=True
                    if leftMouseDown:
                        if backArrow.clicked(mousePos):
                            newGame=False
                        if neutralButton.clicked(mousePos):
                            new=makeGame(size, screen, window)
                            mousePos = getScaledMouse(size)
                            if not new == None:
                                return["new",new[0], "neutral", new[1]]
                        if equalButton.clicked(mousePos):
                            Equal=True
                            
                            while Equal:
                                leftMouseDown=False
                                screen.fill([30,144,255])
                                screen.blit(pygame.image.load("menuBg.png"), (0,0))
                                for event in pygame.event.get():
                                    if event.type == pygame.MOUSEMOTION:
                                        mousePos = getScaledMouse(size)
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        if pygame.mouse.get_pressed()[0]:
                                            leftMouseDown=True
                                    if event.type==pygame.QUIT:
                                        sys.exit()
                                    if event.type == pygame.MOUSEMOTION:
                                        mousePos = getScaledMouse(size)
                                    if event.type == pygame.MOUSEBUTTONDOWN:
                                        if pygame.mouse.get_pressed()[0]:
                                            leftMouseDown=True
                                if leftMouseDown:
                                    if selectButton.clicked(mousePos):
                                        new=makeGame(size, screen,window)
                                        mousePos = getScaledMouse(size)
                                        if not new == None:
                                            return["new",new[0],"select", new[1]]
                                    if randomButton.clicked(mousePos):
                                        new=makeGame(size, screen, window)
                                        mousePos = getScaledMouse(size)
                                        if not new == None:
                                            return["new",new[0],"random", new[1]]
                                    if backArrow.clicked(mousePos):
                                        Equal=False
                                screen.blit(backArrow.image, backArrow.rect)
                                screen.blit(selectButton.image, neutralButton.rect)
                                screen.blit(randomButton.image, equalButton.rect)
                                makeScreen(screen, window, size)
                            
                    
                    screen.blit(backArrow.image, backArrow.rect)
                    screen.blit(neutralButton.image, neutralButton.rect)
                    screen.blit(equalButton.image, equalButton.rect)
                    makeScreen(screen, window, size)
                    
        screen.blit(quitButton.image, quitButton.rect)
        screen.blit(loadGameButton.image, loadGameButton.rect)
        screen.blit(newGameButton.image, newGameButton.rect)
        makeScreen(screen, window, size)
        
def makeGame(size, screen, window):
    fade=pygame.Surface([600, size[1]])
    fade.fill([255,255,255])
    fade.set_alpha(150)
    
    
    font = pygame.font.Font(None, 80)
    backArrow=menuObject(pygame.image.load("backArrow.png"),[10,10])
    
    texts=[]
    textsPos=[]
    texts+=[font.render("Game Name:", True, (10, 10, 10))]
    textsPos+=[texts[0].get_rect(x=500, y=50)]
    
    font = pygame.font.Font(None, 50)

    texts+=[font.render("Number of Players:", True, (10, 10, 10))]
    textsPos+=[texts[1].get_rect(x=500, y=160)]
    
    ENTERBUTTON=pygame.Surface([400,150])
    ENTERBUTTON.fill([125,140,140])
    
    font = pygame.font.Font(None, 80)
    text = font.render("Make", True, (10, 10, 10))
    textpos = text.get_rect(x=120, y=20)
    ENTERBUTTON.blit(text, textpos)
    text = font.render("New Game", True, (10, 10, 10))
    textpos = text.get_rect(x=60, y=80)
    ENTERBUTTON.blit(text, textpos)
    
    ENTERBUTTON=menuObject(ENTERBUTTON, [500, 550])
    
    
    name=''
    pn=2
    #gameName = TextBox(screen, 500, 100, 400, 50, fontSize=30, borderColour=(0, 0, 0), textColour=(0, 0, 0), onSubmit=nameOut, radius=0, borderThickness=1)
    #playerNumber = TextBox(screen, 500, 195, 400, 50, fontSize=30, borderColour=(0, 0, 0), textColour=(0, 0, 0), onSubmit=numbOut, radius=0, borderThickness=1)
    
    gameName=InputBox(500, 100, 400, 50)
    playerNumber = InputBox(500, 195, 400, 50)
    
    mousePos = getScaledMouse(size)
    
    newGame=True
    while newGame:
        leftMouseDown=False
        screen.fill([30,144,255])
        screen.blit(pygame.image.load("menuBg.png"), (0,0))
        events=pygame.event.get()
        for event in events:
            if event.type == pygame.MOUSEMOTION:
                mousePos = getScaledMouse(size)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    leftMouseDown=True
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    leftMouseDown=True
            gameName.handle_event(event, size)
            playerNumber.handle_event(event, size)
        if leftMouseDown:
            if backArrow.clicked(mousePos):
                return None
            if ENTERBUTTON.clicked(mousePos):
                #submit()
                players=[]
                for i in range(int(playerNumber.getText())):
                    players+= [Player(i)]
    
                return ["games/"+gameName.getText()+".info",players]
        
        
        screen.blit(fade, [400, 0])
        screen.blit(backArrow.image, backArrow.rect)
        
        
        gameName.draw(screen)
        playerNumber.draw(screen)
        
        screen.blit(ENTERBUTTON.image, ENTERBUTTON.rect)
        #pygame_widgets.update(events)
        for x, text in enumerate(texts):
            screen.blit(text, textsPos[x])
        makeScreen(screen, window, size)

    
#functions for textbox    
def submit():
    nameOut(True)
    numbOut(True)
def nameOut(submit=False):
    if submit:
        global name
        name = gameName.getText()
def numbOut(submit=False):
    if submit:
        global pn
        try:
            pn = int(playerNumber.getText())
        except:
            print("ERROR!!!!!!!")
            pn=2



def loadGame(screen, window, size):
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
                mousePos = getScaledMouse(size)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    leftMouseDown=True
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEMOTION:
                mousePos = getScaledMouse(size)
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
        makeScreen(screen, window, size)
    
    
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

#IF THIS BREAKS, ITS NOT MY FALT, I DIDNT BUILD IT!!!
#https://stackoverflow.com/questions/46390231/how-can-i-create-a-text-input-box-with-pygame
class InputBox:
    def __init__(self, x, y, w, h, text=''):
        FONT = pygame.font.Font(None, h+5)
        self.COLOR_INACTIVE = pygame.Color('lightskyblue3')
        self.COLOR_ACTIVE = pygame.Color('dodgerblue2')
        self.rect = pygame.Rect(x, y, w, h)
        self.color = self.COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event, size):
        FONT = pygame.font.Font(None, int(self.rect.height)+5)
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(getScaledMouse(size)):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.COLOR_ACTIVE if self.active else self.COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, [0,0,0])
    def getText(self):
        return self.text
    def update(self):
        # Resize the box if the text is too long.
        width = max(200, self.txt_surface.get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+5, self.rect.y+5))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)




if __name__ == "__main__":
    pygame.init()
    size = [1440, 720]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("RISK")
    clock = pygame.time.Clock();
    font = pygame.font.Font(None, 16)

    menu(size, screen)
