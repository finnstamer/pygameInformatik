from objects.player.Skins import Skins
import pygame, sys
import pygame
from pygame import mixer
from base.core.Game import Game
from level.hub import Hub
from level.level1 import Level1
from level.level2 import Level2
from level.level3 import Level3
from button import Button
#musik ins hauptverzeichnis und dann den namen hier der liste hinzufügen damit es im spiel eine option wird
music_list=["sounds/background.wav","sounds/backgroun2.wav"]
cpt_music=0
thresh_hold_music=music_list.__len__()
path_skin=r'E:\dev\pygameInformatik\images'
# für das menü
skin_list=["\player\skin1.png","\player\skin2.png",]
#skin an die spieler-klasse senden
skin_list_prime=["\player\skin1.png","\player\skin2.png",]
cpt_skin=0
thresh_hold_skin=skin_list.__len__()

pygame.init()

music_global=True
SCREEN = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Menu")

BG = pygame.image.load("images/background.png")

def get_font(size): # Ergibt den Press-Start-2P font in der gewünschten größe
    return pygame.font.Font("assets/font.ttf", size)

def play():
        Skins.setCurrentSkin(cpt_skin)
        Game.addLevel(Level1(), Level2(), Level3())
        Game.setLevel(2)
        Game.start()    
        
def selectSkin():
    global cpt_skin
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))
        SKIN_TEXT = get_font(30).render("Choose the best Skin for you.", True, "Black")
        SKIN_RECT = SKIN_TEXT.get_rect(center=(540, 60))
        SCREEN.blit(SKIN_TEXT,SKIN_RECT)
        
        image = pygame.image.load(path_skin+skin_list[cpt_skin]).convert_alpha(SCREEN)
        SCREEN.blit(image, pygame.Rect(350, 175, 100, 100))
        # button.color = (200, 200,200)0
        
        SKIN_START = Button(image=None, pos=(540, 540), 
                            text_input="START", font=get_font(60), base_color="Black", hovering_color="Green")

        SKIN_START.changeColor(OPTIONS_MOUSE_POS)
        SKIN_START.update(SCREEN)

        SKIN_Next = Button(image=None, pos=(940,400 ), 
                            text_input="NEXT", font=get_font(60), base_color="Black", hovering_color="Red")

        SKIN_Next.changeColor(OPTIONS_MOUSE_POS)
        SKIN_Next.update(SCREEN)

        SKIN_Prec = Button(image=None, pos=(140,400 ), 
                            text_input="PREC", font=get_font(60), base_color="Black", hovering_color="Red")

        SKIN_Prec.changeColor(OPTIONS_MOUSE_POS)
        SKIN_Prec.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                  if SKIN_START.checkForInput(OPTIONS_MOUSE_POS):
                    play()
                  
                  if SKIN_Next.checkForInput(OPTIONS_MOUSE_POS):
                    cpt_skin = cpt_skin+1
                    if cpt_skin==thresh_hold_skin:
                        cpt_skin=thresh_hold_skin-1 
                   
                      
                  if SKIN_Prec.checkForInput(OPTIONS_MOUSE_POS):
                    if cpt_skin > 0:
                        cpt_skin=cpt_skin -1
                    else :
                        cpt_skin = 0    
        pygame.display.update()                 
                   
                    
def options():
    global music_global
    global cpt_music
    while True:
        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        
        SCREEN.blit(BG, (0, 0))
        OPTIONS_TEXT = get_font(30).render("This is the OPTIONS screen.", True, "Black")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(540, 60))
        SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

        OPTIONS_Pause = Button(image=None, pos=(540, 260), 
                            text_input="PAUSE", font=get_font(60), base_color="Black", hovering_color="Green")

        OPTIONS_Pause.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_Pause.update(SCREEN)

        OPTIONS_Play = Button(image=None, pos=(540,400 ), 
                            text_input="PLAY", font=get_font(60), base_color="Black", hovering_color="Green")

        OPTIONS_Play.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_Play.update(SCREEN)

        OPTIONS_Back = Button(image=None, pos=(540, 540), 
                            text_input="Back", font=get_font(60), base_color="Black", hovering_color="Green")

        OPTIONS_Back.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_Back.update(SCREEN)

        OPTIONS_Next = Button(image=None, pos=(940,400 ), 
                            text_input="NEXT", font=get_font(60), base_color="Black", hovering_color="Red")

        OPTIONS_Next.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_Next.update(SCREEN)

        OPTIONS_Prec = Button(image=None, pos=(140,400 ), 
                            text_input="PREC", font=get_font(60), base_color="Black", hovering_color="Red")

        OPTIONS_Prec.changeColor(OPTIONS_MOUSE_POS)
        OPTIONS_Prec.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if OPTIONS_Pause.checkForInput(OPTIONS_MOUSE_POS):
                    mixer.music.fadeout(100)
                    music_global = False
                if OPTIONS_Play.checkForInput(OPTIONS_MOUSE_POS):
                    mixer.music.play(-1) 
                    music_global=True 
                if OPTIONS_Back.checkForInput(OPTIONS_MOUSE_POS):
                    main_menu() 
                if OPTIONS_Next.checkForInput(OPTIONS_MOUSE_POS):
                    cpt_music = cpt_music+1
                    if cpt_music==thresh_hold_music:
                        cpt_music=thresh_hold_music-1 
                    mixer.music.load(music_list[cpt_music])
                    if music_global==True:
                        mixer.music.play(-1)  
                if OPTIONS_Prec.checkForInput(OPTIONS_MOUSE_POS):
                    if cpt_music > 0:
                        cpt_music=cpt_music -1
                    else :
                        cpt_music = 0     
                    mixer.music.load(music_list[cpt_music])
                    if music_global==True:
                        mixer.music.play(-1)


        pygame.display.update()

def main_menu():
    
    if music_global ==True :
        mixer.music.load(music_list[cpt_music])
        mixer.music.play(-1)
    else:
        pass    

    print(music_global)
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(540, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(540, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(540, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(540, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    selectSkin()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

main_menu()