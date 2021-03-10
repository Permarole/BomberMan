import animation


class Bomb(animation.AnimateSprite):

    def __init__(self, bomber, power=3):
        super().__init__('bomb.png')
        self._bomber = bomber
        self._power = power
        self._rect = self.image.get_rect()
        self._rect_x, self._rect_y = bomber.get_pos()

    def get_pos(self):
        """Return bomb's position"""
        return self._rect_x, self._rect_y

    def explode(self):
        """ Create fire animation and free one bomber's stack if it still exists """

        pass
