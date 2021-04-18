import animation


class Bomb(animation.AnimateSprite):

    def __init__(self, bomber):
        super().__init__('bomb')
        self._bomber = bomber
        self._power = bomber.get_power()
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = bomber.get_pos()

    def get_pos(self):
        """Return bomb's position"""
        return self.rect.x, self.rect.y

    def explode(self):
        """ Create fire animation and free one bomber's stack if it still exists """
        self.animate()
        pass
