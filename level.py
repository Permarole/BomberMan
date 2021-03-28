import numpy as np
import enum
import block
import pygame 
from random import randint
class Cases(enum.Enum):
    VOID = 0
    SPAWN = 1
    BLOCK = 2
    UNBREAKABLE = 3

# '■' '□'


class Level:

    def __init__(self, size):
        self._row = 13
        self._col = 17
        self._cases = np.empty([self._row, self._col])
        self._unbreakable_image = pygame.image.load(f'assets/unbreakable.png')
        self._unbreakable_image = pygame.transform.scale(self._unbreakable_image, (int(size[0]/self._col),int(size[1]/self._row)))
        self._block_image = pygame.image.load(f'assets/block.png')
        self._block_image = pygame.transform.scale(self._block_image, (int(size[0]/self._col),int(size[1]/self._row)))
        self._spawn_image = pygame.image.load(f'assets/spawn.png')
        self._spawn_image = pygame.transform.scale(self._spawn_image, (int(size[0]/self._col),int(size[1]/self._row)))
        
        self.load_map("map1")

    def generate_map(self):
        """ """
        for row in range(len(self._cases)):
            for col in range(len(self._cases[row])):
                if row == 0 or row == self._row-1 or col == 0 or col == self._col-1 :
                    self._cases[row][col] = 3
                else :
                    self._cases[row][col] =  randint(0,3)
        print(self._cases)

#TODO : excepetion read error
    def load_map(self, name):
        """ load map from file"""
        with open(f'maps/{name}.bombermap', 'r') as file:
            row = 0
            for line in file:
                values = line.split('   ')
                col = 0
                for value in values :
                    self._cases[row][col] = int(value)
                    col = col + 1
                row = row + 1


    def draw(self,screen):
        """draw the level and the block components"""
        for row in range(len(self._cases)):
            for col in range(len(self._cases[row])):
                if self._cases[row][col] == Cases.BLOCK.value :
                    pos = (screen.get_width()/self._col*col,screen.get_height()/self._row*row)
                    screen.blit(self._block_image,pos) 
                elif self._cases[row][col] == Cases.UNBREAKABLE.value :
                    pos = (screen.get_width()/self._col*col,screen.get_height()/self._row*row)
                    screen.blit(self._unbreakable_image,pos) 
                elif self._cases[row][col] == Cases.SPAWN.value :
                    pos = (screen.get_width()/self._col*col,screen.get_height()/self._row*row)
                    screen.blit(self._spawn_image,pos) 
    def is_coliding_with(self,animation):
        pass
    # TODO : accessor