'''
Created on Jul 19, 2012

@author: Annabel
'''

import pygame, sys
from pygame.sprite import *

class Character(pygame.sprite.Sprite):
    def __init__(self, name, pos, image):
        self.name = name
        self.pos = pos
        self.x = self.pos[0]
        self.y = self.pos[1]
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos