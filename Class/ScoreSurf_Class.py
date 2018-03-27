import pygame, sys
from pygame.locals import *

class SCORESURF(object):

    def __init__(self, surf, pos):

        self.SURF = surf
        self.POS = pos
        self.TCO = (200, 200, 200)
        self.FONT = pygame.font.Font('8-BIT WONDER.ttf', 20)


    def displayscore(self, score):

        textsurf = self.FONT.render('Score ' + str(score), True, self.TCO, None)
        self.SURF.blit(textsurf, self.POS)
