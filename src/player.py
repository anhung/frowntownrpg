'''
Created on Jul 19, 2012

@author: Annabel
'''

from pygame.sprite import *
from character import *

class Player(Character):
    def __init__(self, name, img, pos):
        Character.__init__(self, name, img, pos)
        self.speed = 64
        
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
        self.rect.topleft = self.pos