import bomb
import animation

class Fire(animation.AnimateSprite):

    def __init__(self, bomb, direction, speed=8, timer=30):
        super(Fire, self).__init__('fire')
        self.rect = self.image.get_rect()
        self.rect_x = bomb.get_pos()[0]
        self.rect_y = bomb.get_pos()[1]
        self._length = bomb.get_power()
        self._timer = timer
        self._speed = speed
        self._direction = direction

    def update(self):
        pass

