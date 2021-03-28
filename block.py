import animation


class Block(animation.AnimateSprite):

    def __init__(self, pos, size, resistance=1):
        super().__init__('block', size)
        self._resistance = resistance
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(pos)

    def desintegrate(self):
        """ Remove block and chances to spawn bonus """
        pass
