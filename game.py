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
        self._player = Player()
        self._level = level

    def start(self):
        pass

    def update(self):
        pass

    def game_over(self):
        pass