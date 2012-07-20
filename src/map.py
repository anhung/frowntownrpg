'''
Created on Jul 19, 2012

@author: Annabel
'''

from tile import *

class Map(object):

    def __init__(self, filename):
        self.size = 64
        self.grid = []
        fp = open(filename)
        
        r = 0
        for a in fp.readlines():
            c = 0
            self.grid.append([])
            for b in range(len(a)):
                # print a[b]
                letter = a[b]
                pos = (r*self.size, c*self.size)
                if letter == 'T':
                    self.grid[r].append(Tile('../img/map_tree.png', pos))
                elif letter == 'G':
                    self.grid[r].append(Tile('../img/map_grass.png', pos))
                c += 1
            r += 1    
        
        

    def draw(self, window):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                window.blit(self.grid[x][y].image, self.grid[x][y].pos)