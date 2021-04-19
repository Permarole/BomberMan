import numpy as np
import enum
from block import Block
from unbreakable import Unbreakable
import pygame 
from random import randint
from bomber import Bomber
from bomb import Bomb

class Cases(enum.Enum):
    VOID = 0
    SPAWN = 1
    BLOCK = 2
    UNBREAKABLE = 3
    BOMB = 4

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
        self._imageSize = (int(self._size[0]/self._col),int(self._size[1]/self._row))
        self._group = pygame.sprite.Group()
        self._bombs = []#pygame.sprite.Group()
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
                        self._group.add(Unbreakable(pos, self._imageSize ))

    def new_bomb(self , bomber):
        x_index  =int((bomber.get_pos()[0]+bomber.rect.width/2)//self._imageSize[0])
        y_index  =int((bomber.get_pos()[1]+bomber.rect.height/2)//self._imageSize[1])
        if int(self._cases[y_index][x_index]) <= Cases.SPAWN.value :# x = col / y = row
            x = x_index*self._imageSize[0]
            y = y_index*self._imageSize[1]
            self._bombs.append(Bomb(bomber,self, (x,y),self._imageSize))
            self._cases[y_index][x_index] = Cases.BOMB.value
            return True
        return False
    
    def del_bomb(self,bomb):
        x_index  =int(bomb.get_pos()[0]//self._imageSize[0])
        y_index  =int(bomb.get_pos()[1]//self._imageSize[1])
        if self._cases[y_index][x_index] == Cases.BOMB.value:
            self._cases[y_index][x_index] = Cases.VOID.value
            self._bombs.remove(bomb)
        

    def draw(self,screen):
        """draw the level and the block components"""
        self._group.draw(screen)
        for iBomb in range(len(self._bombs)) :            
            screen.blit(self._bombs[iBomb].image, self._bombs[iBomb].get_pos())
        for iBomb in range(len(self._bombs)-1,-1,-1) :            
            self._bombs[iBomb].animate() #anime have to be after the blit

    def is_coliding_with(self,animation):
        pass
    # TODO : accessor