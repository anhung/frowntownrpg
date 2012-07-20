'''
Created on Jul 19, 2012

@author: Annabel
'''

from pygame.sprite import *

class Tile(pygame.sprite.Sprite):

    def __init__(self, img, pos):
        pygame.sprite.Sprite.__init__(self)
        self.width = 64;
        self.height = 64;
        self.pos = pos
        self.image = pygame.image.load(img).convert()
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos        