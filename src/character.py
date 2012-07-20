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
        self.adjustRect()
        self.speed = 5
        
    def move(self, direction):
        if direction == 'left':
            self.x -= self.speed
        elif direction == 'right':
            self.x += self.speed
        elif direction == 'up':
            self.y -= self.speed
        elif direction == 'down':
            self.y += self.speed
        self.pos = (self.x, self.y)
        self.adjustRect()
        
    def adjustRect(self):
        self.rect.centerx = self.pos[0]
        self.rect.centery = self.pos[1]