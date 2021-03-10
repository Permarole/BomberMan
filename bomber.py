import animation


class Bomber(animation.Animation):
    """ BomberMan, everything is in the name """

    def __init__(self, pos, color, speed=5, stack=1, fire_power=3, shield=False):
        super().__init__('bomber_'+color+'.png')
        self._shield = shield
        self._stack = stack
        self._fire_power = fire_power
        self._speed = speed
        self.rect = self.image.get_rect()
        self.rect_x = pos[0]
        self.rect_y = pos[1]

    # TODO : accessor

    def free_stack(self):
        """ Increase by one the bomb stack"""
        pass

    def move(self, direction):
        """ Move bomber according to the direction"""
        pass

    def die(self):
        """ Remove bomber sprite and play death animation"""
        pass

    def bomb(self):
        """ Set one bomb on the current bomber's position """
        pass


