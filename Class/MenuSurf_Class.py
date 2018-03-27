import pygame, sys
from pygame.locals import *

class Menu(object):

    def __init__(self, surf):

        self.SURF = surf
        self.FONT = pygame.font.Font('8-BIT WONDER.ttf', 300)
        self.FONT2 = pygame.font.Font('8-BIT WONDER.ttf', 40)
        
        self.MSURF = pygame.Surface((450, 360), flags=SRCALPHA, depth=32)
        self.DSURF = pygame.Surface((450, 600), flags=SRCALPHA, depth=32)
        self.ISURF = pygame.Surface((450, 600), flags=SRCALPHA, depth=32)
        self.TCO = (210, 210, 210)
        self.JCO = (100, 100, 100)
        self.HCO = (220, 220, 220)
        self.SCO = (50, 50, 50)

    def disMsurf(self, Mjudge):

        textsurf1 = self.FONT.render('Press Enter to Start', True, self.TCO, None)
        textsurf1 = pygame.transform.scale(textsurf1, (450, 80))
        textsurf2 = self.FONT.render('Press I for Instruction', True, self.TCO, None)
        textsurf2 = pygame.transform.scale(textsurf2, (450, 80))

        textsurf3 = self.FONT.render('ACORN HUNTER', True, self.SCO, None)
        textsurf3 = pygame.transform.scale(textsurf3, (450, 120))

        if Mjudge:

            self.MSURF.blit(textsurf3, (0,0))            
            self.MSURF.blit(textsurf1, (0,160))
            self.MSURF.blit(textsurf2, (0,240))
            self.SURF.blit(self.MSURF, (100, 150))

    def disDsurf(self, Djudge, SCL):

        textsurf1 = self.FONT.render('Press R to RETRY', True, self.JCO, None)
        textsurf1 = pygame.transform.scale(textsurf1, (450, 80))
        textsurf2 = self.FONT.render('HIGH SCORE', True, self.TCO, None)
        textsurf2 = pygame.transform.scale(textsurf2, (250, 40))
        textscore1 = self.FONT2.render('1   ' + str(SCL[0]), True, self.SCO, None)
        textscore2 = self.FONT2.render('2  ' + str(SCL[1]), True, self.SCO, None)
        textscore3 = self.FONT2.render('3  ' + str(SCL[2]), True, self.SCO, None)
        textscore4 = self.FONT2.render('4  ' + str(SCL[3]), True, self.SCO, None)
        textscore5 = self.FONT2.render('5  ' + str(SCL[4]), True, self.SCO, None)
        textscore6 = self.FONT2.render('6  ' + str(SCL[5]), True, self.SCO, None)
        
        if Djudge:

            self.DSURF = pygame.Surface((450, 600), flags=SRCALPHA, depth=32)
            self.DSURF.blit(textsurf1, (0,0))
            self.DSURF.blit(textsurf2, (100, 100))
            self.DSURF.blit(textscore1, (50, 180))
            self.DSURF.blit(textscore2, (50, 230))
            self.DSURF.blit(textscore3, (50, 280))
            self.DSURF.blit(textscore4, (50, 330))
            self.DSURF.blit(textscore5, (50, 380))
            self.DSURF.blit(textscore6, (50, 430))
            self.SURF.blit(self.DSURF, (100, 130))

    def disIsurf(self, Ijudge):

        textsurf1 = self.FONT.render('Press SPACE to JUMP', True, self.TCO, None)
        textsurf1 = pygame.transform.scale(textsurf1, (450, 80))
        textsurf2 = self.FONT.render('Collect acorns for score', True, self.TCO, None)
        textsurf2 = pygame.transform.scale(textsurf2, (450, 80))
        textsurf3 = self.FONT.render('Try to avoid obstacles', True, self.TCO, None)
        textsurf3 = pygame.transform.scale(textsurf3, (450, 80))
        textsurf4 = self.FONT.render('Golden acorns give more score', True, self.TCO, None)
        textsurf4 = pygame.transform.scale(textsurf4, (450, 80))
        textsurf5 = self.FONT.render('Press I to Return', True, self.JCO, None)
        textsurf5 = pygame.transform.scale(textsurf5, (450, 80))
        textsurf6 = self.FONT.render('It becomes harder when score rises', True, self.HCO, None)
        textsurf6 = pygame.transform.scale(textsurf6, (450, 80))

        if Ijudge:

            self.ISURF.blit(textsurf1, (0,0))
            self.ISURF.blit(textsurf2, (0,100))
            self.ISURF.blit(textsurf3, (0,200))
            self.ISURF.blit(textsurf4, (0,300))
            self.ISURF.blit(textsurf5, (0,500))
            self.ISURF.blit(textsurf6, (0,400))
            self.SURF.blit(self.ISURF, (100, 100))
        
