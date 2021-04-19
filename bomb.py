import animation


class Bomb(animation.AnimateSprite):

    def __init__(self, bomber, level, pos,size):
        super().__init__('bomb',size)
        self._bomber = bomber
        self._power = bomber.get_power()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = bomber.get_pos()
        self.rect.x, self.rect.y = pos
        self._level = level
        super().start_animation()

    def __del__(self):
        self._bomber.free_stack()

    def get_pos(self):
        """Return bomb's position"""
        return self.rect.x, self.rect.y

    def explode(self):
        """ Create fire animation and free one bomber's stack if it still exists """
        self.animate()
        pass
    def animate(self):
        """ Overload, explode desapear at the end"""
        super().animate()
        if (self.animation == False):
            self._level.del_bomb(self)