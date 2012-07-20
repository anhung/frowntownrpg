'''
Created on Jul 19, 2012

@author: Annabel
'''

import pygame, sys
from pygame.locals import *
from character import *
from tile import *
from map import *

pygame.init()
fpsClock = pygame.time.Clock()
windowWidth = 640
windowHeight = 640
windowTitle = 'My Python RPG'
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption(windowTitle)
pygame.key.set_repeat(1, 1)

player = Character('Player', (100,100), '../img/pinkblob.png')
thisMap = Map('../maps/walled_field.txt')

# Game loop
while True:
    thisMap.draw(window)
    
    window.blit(player.image, player.pos)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # elif event.type === MOUSEMOTION:
        # elif event.type === MOUSEBUTTONUP:
        elif event.type == KEYDOWN:
            player.x = player.pos[0]
            player.y = player.pos[1]
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