import animation

class Bomber(animation.AnimateSprite):
    """ BomberMan, everything is in the name """

    def __init__(self, game, pos, color, speed=5, stack=1, fire_power=3, shield=False):
        super().__init__('bomber_'+color+'.png')
        self._game = game
        self._shield = shield
        self._stack = stack
        self._fire_power = fire_power
        self._speed = speed
        self._rect = self.image.get_rect()
        self._rect_x = pos[0]
        self._rect_y = pos[1]

    def get_pos(self):
        """ Return bomber's position"""
        return self._rect_x, self._rect_y

    def get_power(self):
        """ Return bomber's fire power"""
        return self._fire_power

    def free_stack(self):
        """ Increase by one the bomb stack"""
        self._stack += 1

    def move(self, direction):
        """ Move bomber according to the direction"""
        # TODO : verification for collisions
        self._rect_x += direction[0]* self._speed
        self._rect_y += direction[1]* self._speed
        print('moving')
        

    def die(self):
        """ Remove bomber sprite and play death animation"""
        pass

    def bomb(self):
        """ Set one bomb on the current bomber's position """
        self._game.new_bomb(self)
