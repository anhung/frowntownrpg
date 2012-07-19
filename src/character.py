'''
Created on Jul 19, 2012

@author: Annabel
'''

import pygame, sys
from pygame.locals import *

class Character(pygame.sprite.Sprite):
    def __init__(self, name, posX, posY, image):
        self.name = name
        self.x = posX
        self.y = posY
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
        self.adjustRect()
        
    def adjustRect(self):
        self.rect.centerx = self.x
        self.rect.centery = self.y