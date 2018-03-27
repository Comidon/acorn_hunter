import pygame, sys
from pygame.locals import *
from random import randint

class GAcorn(pygame.sprite.Sprite):

    def __init__(self, surf):
        
        pygame.sprite.Sprite.__init__(self)
        
        self.SURF = surf
        self.GRATE = 10

        self.Gima = pygame.image.load('IMAGE/G_acorn.png').convert_alpha()
        self.SIZE = self.Gima.get_size()
        self.XPOS = randint(100, 550 - self.SIZE[0])
        self.YPOS = -randint(400, 1000)
        self.rect = self.Gima.get_rect()
        self.rect.x = self.XPOS
        self.rect.y = self.YPOS


    def disGacorn(self, NCLLS):

        if NCLLS:
            self.YPOS += self.GRATE
            self.rect.y += self.GRATE
            
        self.SURF.blit(self.Gima, (self.XPOS, self.YPOS))
