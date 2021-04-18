import pygame
import animation
from soundManager import SoundManager
from player import Player
from bomb import Bomb
from level import Level

class Game:

    def __init__(self, level, window_size):

        self._size = window_size
        self._is_playing = False
        self._bombers =  pygame.sprite.Group()
        self._bombs = pygame.sprite.Group()
        self._fires = pygame.sprite.Group()
        self._bonuses = pygame.sprite.Group()
        self._pressed = dict()
        self._sound_manager = SoundManager()
        self._player = Player(self, (63,55), 'red')
        self._level = Level(self._size)

        
    def start(self):
        self._is_playing = True
        self._player.start_animation()

    def new_bomb(self, bomber):
        """ Create a new bomb and add it to _bombs"""
        bomb = Bomb(bomber)
        self._bombs.add(bomb)
        bomb.start_animation()
    
    def remove_bomb(self, bomb):
        self._bombs.remove(bomb)


    def draw(self, screen) :
        self._level.draw(screen)
        # Draw every bombs
        self._bombs.draw(screen)
        # for bomb in self._bombs:
        #     screen.blit(bomb.image, bomb.get_pos())

        # Draw player
        screen.blit(self._player.image, self._player.get_pos())
        #self._player.draw(screen)
        # Draw every bonuses
        self._bonuses.draw(screen)
        # Draw every bombers

    def update(self,screen):
        keys = pygame.key.get_pressed()
        self._player.listen(keys)
        self._player.animate(True)
        for i in self._bombs.sprites() :
            i.explode()
        # Draw every sprite
        self.draw(screen)

    def game_over(self):
        self._is_playing = False

    def check_collision(self, sprite, group):
        """ Return a boolean """
        return pygame.sprite.spritecollide(sprite, group, False)

    def get_is_playing(self):
        return self._is_playing
