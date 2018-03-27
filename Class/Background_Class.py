import pygame, sys
from pygame.locals import *
from random import randint


class BackGround(object):

    def __init__(self, surf):
    
        self.RATE = 5
        self.TreeY = 0
        x = randint(-200, 278)
        y = -randint(300, 900)
        self.X = x
        self.Y = y
        self.SURF = surf
        self.TSL = pygame.image.load('IMAGE/tree_l.png')
        self.TSR = pygame.image.load('IMAGE/tree_r.png')
        self.CLOUD = pygame.image.load('IMAGE/cloud.png').convert_alpha()

    def displaytrees(self, NCLLS):

        if NCLLS:

            self.TreeY += self.RATE

        self.SURF.blit(self.TSL, (-28, self.TreeY%576))
        self.SURF.blit(self.TSR, (550, self.TreeY%576))
        self.SURF.blit(self.TSL, (-28, self.TreeY%576-576))
        self.SURF.blit(self.TSR, (550, self.TreeY%576-576))
        self.SURF.blit(self.TSL, (-28, self.TreeY%576+576))
        self.SURF.blit(self.TSR, (550, self.TreeY%576+576))

    def displayClouds(self, NCLLS):
        
        if NCLLS:

            self.Y += 3

        self.SURF.blit(self.CLOUD, (self.X, self.Y))
