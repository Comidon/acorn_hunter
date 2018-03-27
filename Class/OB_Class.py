import pygame, sys
from pygame.locals import *
from random import randint


class Obstacle(pygame.sprite.Sprite):

    def __init__(self, surf, Ypos):

        pygame.sprite.Sprite.__init__(self)
        
        self.ANIX = 0
        self.SURF = surf
        self.RATE = 5
        self.YPOS = Ypos
        self.XPOS = 0
        self.Image = pygame.image.load('IMAGE/branch1_r.png').convert_alpha()
        self.rect = self.Image.get_rect()
        self.rect.x = 0
        self.rect.y = self.YPOS


    def creatOb(self):

        wh = randint(0,7)

        if wh == 0:
            self.Image = pygame.image.load('IMAGE/branch1_r.png').convert_alpha()
            self.rect = self.Image.get_rect()
            self.SIZE = self.Image.get_size()
            self.XPOS = 100 - 14
            self.rect.x = self.XPOS

        elif wh == 1:
            self.Image = pygame.image.load('IMAGE/branch2_r.png').convert_alpha()
            self.rect = self.Image.get_rect()
            self.SIZE = self.Image.get_size()
            self.XPOS = 100 - 14
            self.rect.x = self.XPOS

        elif wh == 2:
            self.Image = pygame.image.load('IMAGE/branch3_r.png').convert_alpha()
            self.rect = self.Image.get_rect()
            self.SIZE = self.Image.get_size()
            self.XPOS = 100 - 14
            self.rect.x = self.XPOS

        elif wh == 3:
            self.Image = pygame.image.load('IMAGE/branch1_l.png').convert_alpha()
            self.rect = self.Image.get_rect()
            self.SIZE = self.Image.get_size()
            self.XPOS = 550 - self.SIZE[0] + 14
            self.rect.x = self.XPOS

        elif wh == 4:
            self.Image = pygame.image.load('IMAGE/branch2_l.png').convert_alpha()
            self.rect = self.Image.get_rect()
            self.SIZE = self.Image.get_size()
            self.XPOS = 550 - self.SIZE[0] + 14
            self.rect.x = self.XPOS

        elif wh == 5:
            self.Image = pygame.image.load('IMAGE/branch3_l.png').convert_alpha()
            self.rect = self.Image.get_rect()
            self.SIZE = self.Image.get_size()
            self.XPOS = 550 - self.SIZE[0] + 14
            self.rect.x = self.XPOS

        elif wh == 6:
            self.Image = pygame.image.load('IMAGE/hole_r.png').convert_alpha()
            self.rect = self.Image.get_rect()
            self.SIZE = self.Image.get_size()
            self.XPOS = 100 - self.SIZE[0]
            self.rect.x = self.XPOS + 2

        elif wh == 7:
            self.Image = pygame.image.load('IMAGE/hole_l.png').convert_alpha()
            self.rect = self.Image.get_rect()
            self.SIZE = self.Image.get_size()
            self.XPOS = 550
            self.rect.x = self.XPOS - 15


    def displayObstacle(self, NCLLS):

        if NCLLS:
            self.YPOS += 5
            self.rect.y = self.YPOS

        self.SURF.blit(self.Image, (self.XPOS, self.YPOS))
