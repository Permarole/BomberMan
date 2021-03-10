import animation


class Block(animation.Animation):

    def __init__(self, resistance=1):
        super().__init__('block.png')
        self._resistance = resistance
        self.rect = self.image.get_rect()
        self.rect_x = pos[0]
        self.rect_y = pos[1]


    def desintegrate(self):
        """ Remove block and chances to spawn bonus """
        pass
