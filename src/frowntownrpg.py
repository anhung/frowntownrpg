'''
Created on Jul 19, 2012

@author: Annabel
'''

import pygame, sys
from pygame.locals import *
from player import *
from tile import *
from map import *

pygame.init()
fpsClock = pygame.time.Clock()
windowWidth = 640
windowHeight = 640
windowTitle = 'My Python RPG'
window = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption(windowTitle)
pygame.key.set_repeat() # use args to enable

player = Player('Player', (0,0), '../img/pinkblob.png')
blue = Character('Blue Blob', (8*64, 64), '../img/blueblob.png')
thisMap = Map('../maps/mixed.txt')

pygame.mixer.init()
pygame.mixer.music.load('../music/dirediredocks.mp3')
pygame.mixer.music.play()

# Game loop
while True:
    thisMap.draw(window)
    
    window.blit(player.image, player.pos)
    window.blit(blue.image, blue.pos)
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        # elif event.type === MOUSEMOTION:
        # elif event.type === MOUSEBUTTONUP:
        elif event.type == KEYDOWN:
            player.x = player.pos[0]
            player.y = player.pos[1]
            if (event.key == K_LEFT) and (player.x - player.speed >= 0):
                player.move('left')
            elif (event.key == K_RIGHT) and (player.x + player.speed < windowWidth):
                player.move('right')
            elif (event.key == K_UP) and (player.y - player.speed >= 0):
                player.move('up')
            elif (event.key == K_DOWN) and (player.y + player.speed < windowHeight):
                player.move('down')
            elif (event.key == K_s):
                pygame.mixer.music.pause()
            elif (event.key == K_a):
                pygame.mixer.music.unpause()
            # elif event.key === K_a

    # collisions
    if pygame.sprite.collide_rect(player, blue):
        print "Collided!"
    
    pygame.display.update()
    fpsClock.tick(30)