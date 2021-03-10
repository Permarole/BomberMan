import pygame
import animation
from soundManager import SoundManager
from player import Player


class Game:

    def __init__(self, level, window_size):

        self._size = window_size
        self._is_playing = False
        self._bombers = dict()
        self._bombs = dict()
        self._fires = dict()
        self._pressed = dict()
        self._bonuses = dict()
        self._sound_manager = SoundManager()
        self._player = Player((0,0),"red") 
        self._level = level

    def start(self):
        self._is_playing = True

    def update(self):
        pass

    def game_over(self):
        self._is_playing = False

    def get_is_playing(self):
        return self._is_playing
