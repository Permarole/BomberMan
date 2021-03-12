import pygame
import animation
from soundManager import SoundManager
from player import Player
from bomb import Bomb


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
        self._player = Player(self, (0,0), "red")
        self._level = level

    def start(self):
        self._is_playing = True

    def new_bomb(self, bomber):
        """ Create a new bomb and add it to _bombs"""
        self._bombs.add(Bomb(bomber))

    def draw(self, screen) :
        # Draw every bombs
        self._bombs.draw(screen)
        # Draw player
        self._player.draw(screen)
        # Draw every bonuses
        self._bonuses.draw(screen)
        # Draw every bombers
        self._bombers.draw(screen)

    def update(self,screen):
        keys = pygame.key.get_pressed()
        self._player.listen(keys)

        # Draw every sprite
        self.draw(screen)

    def game_over(self):
        self._is_playing = False

    def check_collision(self, sprite, group):
        """ Return a boolean """
        return pygame.sprite.spritecollide(sprite, group, False)

    def get_is_playing(self):
        return self._is_playing
