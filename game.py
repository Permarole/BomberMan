import pygame
import animation
from soundManager import SoundManager
from player import Player


class Game:

    def __init__(self, level, window_size):

        self._size = window_size
        self._is_playing = False
        self._bombers = pygame.sprite.Group()
        self._bombs = pygame.sprite.Group()
        self._fires = pygame.sprite.Group()
        self._bonuses = pygame.sprite.Group()
        self._pressed = dict()
        self._sound_manager = SoundManager()
        self._player = Player((0,0),"red")
        self._level = level

    def start(self):
        self._is_playing = True

    def new_bomb(self, bomber, power=3):
        """ Create a new bomb and add it to _bombs"""
        self._bombs.add(Bomb(bomber, power))

    def update(self,screen):
        keys = pygame.key.get_pressed()
        self._player.listen(keys)

    def game_over(self):
        self._is_playing = False

    def get_is_playing(self):
        return self._is_playing
