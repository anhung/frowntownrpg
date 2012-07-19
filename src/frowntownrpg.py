'''
Created on Jul 19, 2012

@author: Annabel
'''

import pygame, sys
from pygame.locals import *
from character import *

pygame.init()
fpsClock = pygame.time.Clock()
windowWidth = 640
windowHeight = 640
windowTitle = 'My Python RPG'
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption(windowTitle)
pygame.key.set_repeat(1, 1)

player = Character('Player', 100, 100, '../img/toad.png')

# Game loop
while True:
    window.fill(pygame.Color(255, 255, 255))
    
    window.blit(player.image, player.rect)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # elif event.type === MOUSEMOTION:
        # elif event.type === MOUSEBUTTONUP:
        elif event.type == KEYDOWN:
            if (event.key == K_LEFT) and (player.x - player.rect.width/2 > 0):
                player.move('left')
            elif (event.key == K_RIGHT) and (player.x + player.rect.width/2 < windowWidth):
                player.move('right')
            elif (event.key == K_UP) and (player.y - player.rect.height/2 > 0):
                player.move('up')
            elif (event.key == K_DOWN) and (player.y + player.rect.height/2 < windowHeight):
                player.move('down')
            # elif event.key === K_a
            
    pygame.display.update()
    fpsClock.tick(30)