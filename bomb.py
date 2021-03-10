import animation


class Bomb(animation.Animation):

    def __init__(self, bomber, power=3):
        super().__init__('bomb.png')
        self._bomber = bomber
        self._power = power
        self._rect = self.image.get_rect()
        self._rect_x = None
        self._rect_y = None

    # TODO : accessor

    def explode(self):
        """ Create fire animation and free one bomber's stack if it still exists """
        pass


