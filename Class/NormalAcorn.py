import pygame, sys
from pygame.locals import *
from random import randint

class NAcorn(pygame.sprite.Sprite):

    def __init__(self, surf):
        
        pygame.sprite.Sprite.__init__(self)
     
        self.SURF = surf
        self.NRATE = 7

        self.Nima = pygame.image.load('IMAGE/N_acorn.png').convert_alpha()
        self.SIZE = self.Nima.get_size()
        self.XPOS = randint(100, 550 - self.SIZE[0])
        self.YPOS = -randint(400, 2000)
        self.rect = self.Nima.get_rect()
        self.rect.x = self.XPOS
        self.rect.y = self.YPOS

    def disNacorn(self, NCLLS):

        if NCLLS:
            self.YPOS += self.NRATE
            self.rect.y += self.NRATE
            
        self.SURF.blit(self.Nima, (self.XPOS, self.YPOS))
