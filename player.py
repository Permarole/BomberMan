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
            self.animate()
            pos = self.get_pos()
            self.move((moveh,movev))
            if  self._game.check_collision(self, self._game._level._group) and \
                self._game.check_collision(self, self._game._level._group) :
                self.cancel_move(pos)


    def cancel_move(self, pos):
        self.rect.x = pos[0]
        self.rect.y = pos[1]