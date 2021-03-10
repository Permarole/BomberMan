import bomber
import pygame 

class Player(bomber.Bomber):

    def die(self):
        """ Overload bomber's method """
        pass

    def listen(self, keys):
        """Associate key pressed to player actions"""
        moveh = 0
        movev = 0
        if keys[pygame.K_RIGHT] :
            moveh += 1
        if keys[pygame.K_LEFT] :
            moveh -= 1
        if keys[pygame.K_UP] :
            movev -= 1
        if keys[pygame.K_DOWN]:
            movev += 1
        if keys[pygame.K_SPACE]:
            self.bomb()
        if moveh != 0 or movev != 0:
            self.move((moveh,moveh))