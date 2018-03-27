import pygame, sys
from pygame.locals import *
import pyganim


class Anima(pygame.sprite.Sprite):

    def __init__(self, surf):

        pygame.sprite.Sprite.__init__(self)
        
        self.ANIX = 100
        self.DPY = 450
        self.SURF = surf

        self.DJL2R = False
        self.DJR2L = False
        self.RATL = True
        self.RATR = False

        self.DIEP = pygame.image.load('IMAGE/DIE.png').convert_alpha()
      
        self.SQRR = pyganim.PygAnimation([('IMAGE/spl1.png', 0.05),
                                          ('IMAGE/spl2.png', 0.05),
                                          ('IMAGE/spl3.png', 0.05),
                                          ('IMAGE/spl4.png', 0.05),
                                          ('IMAGE/spl5.png', 0.05),
                                          ('IMAGE/spl6.png', 0.05),
                                          ('IMAGE/spl7.png', 0.05)])
        
        self.SQRL = pyganim.PygAnimation([('IMAGE/spr1.png', 0.05),
                                          ('IMAGE/spr2.png', 0.05),
                                          ('IMAGE/spr3.png', 0.05),
                                          ('IMAGE/spr4.png', 0.05),
                                          ('IMAGE/spr5.png', 0.05),
                                          ('IMAGE/spr6.png', 0.05),
                                          ('IMAGE/spr7.png', 0.05)])
        
        self.SQJPL2R = pyganim.PygAnimation([('IMAGE/spl4.png', 0.05),
                                             ('IMAGE/spl5.png', 0.05),
                                             ('IMAGE/spl6.png', 0.05),
                                             ('IMAGE/spr1.png', 0.4)])
        self.SQJPR2L = pyganim.PygAnimation([('IMAGE/spr4.png', 0.05),
                                             ('IMAGE/spr5.png', 0.05),
                                             ('IMAGE/spr6.png', 0.05),
                                             ('IMAGE/spl1.png', 0.4)])

        colima = pygame.Surface((80, 160), flags=SRCALPHA, depth=32)
        self.rect = colima.get_rect()
        self.rect.x = 100
        self.rect.y = 520

    def jumpchv(self):

        if self.RATL == True:
            self.DJL2R = True

        elif self.RATR == True:
            self.DJR2L = True

    def animareset(self):
        
        self.ANIX = 100
        self.DPY = 450

        self.DJL2R = False
        self.DJR2L = False
        self.RATL = True
        self.RATR = False
        
    def PlayAnima(self, NCLLS):

        if NCLLS:

            if self.RATR:
               self.SQRR.play()
               self.SQRR.blit(self.SURF, (460, 500))

            if self.RATL:
                self.SQRL.play()
                self.SQRL.blit(self.SURF, (100, 500))
            
            if self.DJR2L:
                self.RATR = False
                self.SQJPL2R.play()
                self.ANIX -= 12
                self.rect.x -= 12
                self.SQJPL2R.blit(self.SURF, (self.ANIX, 500))
                if self.ANIX <= 100:
                    self.DJR2L = False
                    self.RATL = True
                    self.ANIX = 100
                    self.rect.x = 100
                    self.SQJPL2R.stop()

            if self.DJL2R:
                self.RATL = False
                self.SQJPR2L.play()
                self.ANIX += 12
                self.rect.x += 12
                self.SQJPR2L.blit(self.SURF, (self.ANIX, 500))
                if self.ANIX >= 460:
                    self.DJL2R = False
                    self.RATR = True
                    self.ANIX = 460
                    self.rect.x = 460
                    self.SQJPR2L.stop()

        else:

            self.DJL2R = False
            self.DJR2L = False
            self.RATL = False
            self.RATR = False

            self.DPY += 5

            self.SURF.blit(self.DIEP, (self.ANIX, self.DPY))


            
                


