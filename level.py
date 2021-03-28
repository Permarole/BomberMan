import numpy as np
import enum
from block import Block
from unbreakable import Unbreakable
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
        # self._unbreakable_image = pygame.image.load(f'assets/unbreakable.png')
        # self._unbreakable_image = pygame.transform.scale(self._unbreakable_image, (int(size[0]/self._col),int(size[1]/self._row)))
        # self._spawn_image = pygame.image.load(f'assets/spawn.png')
        # self._spawn_image = pygame.transform.scale(self._spawn_image, (int(size[0]/self._col),int(size[1]/self._row)))
        self._size = size
        self._group = pygame.sprite.Group()
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
            for row in range(len(self._cases)):
                for col in range(len(self._cases[row])):
                    if self._cases[row][col] == Cases.BLOCK.value :
                        pos = (self._size[0]/self._col*col,self._size[1]/self._row*row)
                        self._group.add(Block(pos,(int(self._size[0]/self._col),int(self._size[1]/self._row))))
                    elif self._cases[row][col] == Cases.UNBREAKABLE.value :
                        pos = (self._size[0]/self._col*col,self._size[1]/self._row*row)
                        self._group.add(Unbreakable(pos, (int(self._size[0]/self._col),int(self._size[1]/self._row))))


    def draw(self,screen):
        """draw the level and the block components"""
        self._group.draw(screen)

    def is_coliding_with(self,animation):
        pass
    # TODO : accessor