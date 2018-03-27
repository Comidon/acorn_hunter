import pygame, sys
from pygame.locals import *
import time
from Class.Animation_Class import Anima
from Class.Background_Class import BackGround
from Class.OB_Class import Obstacle
from Class.GoldAcorn import GAcorn
from Class.NormalAcorn import NAcorn
from Class.ScoreSurf_Class import SCORESURF
from Class.MenuSurf_Class import Menu
from random import *


pygame.init()

pygame.mixer.pre_init(44100, -16, 2, 1024*4)

DHEIGHT = 800
DWEIGHTH = 650

pygame.display.set_caption('Acorn Hunter')

DISPLAYSURF = pygame.display.set_mode((DWEIGHTH, DHEIGHT), 0, 32)
mainClock = pygame.time.Clock()
BGCOLOR = (130, 180, 220)
DISPLAYSURF.fill(BGCOLOR)
ObLIST = pygame.sprite.Group()
GaLIST = pygame.sprite.Group()
NaLIST = pygame.sprite.Group()
CloudList = []

Animation = Anima(DISPLAYSURF)
Bcgrnd = BackGround(DISPLAYSURF)

scoreSurf = SCORESURF(DISPLAYSURF, (400, 50))
MenuSurf = Menu(DISPLAYSURF)

def makeAcorns():

    GaLIST.add(GAcorn(DISPLAYSURF))

    acorns = 5

    while acorns > 0:

        NaLIST.add(NAcorn(DISPLAYSURF))
        acorns -= 1


def makeCloud():

    CloudList.append(BackGround(DISPLAYSURF))


def makeObs(timer):
    
    if timer == 90:
        ob = Obstacle(DISPLAYSURF, -DHEIGHT // 2)
        ob.creatOb()
        ObLIST.add(ob)
        return randint(0, 30)

    else:
        return timer

def highscoreStart():
    hisc=open("highscore.txt","r")
    highscore = ""
    for x in hisc:
        highscore += x
    highscoreList = highscore.split()
    highscoreList = list(map(float, highscoreList))
    highscoreList = list(map(int, highscoreList))
    LH = 2*len(highscoreList)        
    highscoreList = sorted(highscoreList, reverse=True)
    hisc.close()
    return highscoreList


def changerate(sc, ra):

    ra +=  sc//2000
    return ra


def main():

    makeCloud()

    acorn_sound = pygame.mixer.Sound("SOUND/acorn1.wav")
    acorn_sound.set_volume(0.3)
    death_sound = pygame.mixer.Sound("SOUND/squirreldeath1.wav")
    death_sound.set_volume(0.8)
    BGM = pygame.mixer.music.load("SOUND/BGM4.mp3")
    pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    TIMER = 0
    makeAcorns()
    Score = 0.0
    JUDGE = True
    START = False
    IDIS = False
    MDIS = True
    FPS = 60
    
    while True:

        TIMER = 0
        Score = 0.0
        JUDGE = True
        FPS = 60
        death_check = True

        for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and (not IDIS):
                        START = True
                        IDIS = False
                    elif event.key == K_i:
                        if IDIS:
                            IDIS = False
                            MDIS = True
                        else:
                            IDIS = True
                            MDIS = False
                            
        DISPLAYSURF.fill(BGCOLOR)
        Bcgrnd.displaytrees(JUDGE)
        Animation.PlayAnima(JUDGE)
        MenuSurf.disMsurf(MDIS)
        MenuSurf.disIsurf(IDIS)
                        
        pygame.display.update()
        mainClock.tick(60)

        while START:

            INTScore = int(Score)

            FPS = 60 + INTScore // 100

            TIMER += 1  
            DISPLAYSURF.fill(BGCOLOR)

            TIMER = makeObs(TIMER)
                
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_SPACE:
                        Animation.jumpchv()
                    elif event.key == K_r and (not JUDGE):
                        for OB in ObLIST:
                            ObLIST.remove(OB)
                        for GA in GaLIST:
                            GaLIST.remove(GA)
                        for NA in NaLIST:
                            NaLIST.remove(NA)
                        Animation.animareset()
                        START = False

            if len(NaLIST) < 3:
                makeAcorns()
                makeCloud()

            OBSQcollisions = pygame.sprite.spritecollide(Animation, ObLIST, False)
            GaSQcollisions = pygame.sprite.spritecollide(Animation, GaLIST, True)
            NaSQcollisions = pygame.sprite.spritecollide(Animation, NaLIST, True)

            
            JUDGE = not OBSQcollisions

            if JUDGE:
                Score += 0.1
                if GaSQcollisions:
                    Score += 200
                    acorn_sound.play()
                if NaSQcollisions:
                    Score += 50
                    acorn_sound.play()

            for CL in CloudList:
                if CL.Y < DHEIGHT:
                    CL.displayClouds(JUDGE)
                else:
                    CloudList.remove(CL)

            Bcgrnd.displaytrees(JUDGE)
            
            for OB in ObLIST:
                if OB.rect.y < DHEIGHT:
                    OB.displayObstacle(JUDGE)
                else:
                    ObLIST.remove(OB)

            for GA in GaLIST:
                if GA.rect.y < DHEIGHT:
                    GA.disGacorn(JUDGE)
                else:
                    GaLIST.remove(GA)

            for NA in NaLIST:
                if NA.rect.y < DHEIGHT:
                    NA.disNacorn(JUDGE)
                else:
                    NaLIST.remove(NA)                

            Animation.PlayAnima(JUDGE)

            if not JUDGE:
                if death_check:
                    death_sound.play()
                    hisc=open("highscore.txt","a")
                    hisc.write(str(INTScore) + "\n")
                    hisc.close()
                    death_check = False

                highscoreList = highscoreStart()
                MenuSurf.disDsurf(not JUDGE, highscoreList)
                
            scoreSurf.displayscore(INTScore)
                            
            pygame.display.update()
            mainClock.tick(FPS)

if __name__ == '__main__': main()
