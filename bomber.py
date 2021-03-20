import animation
import enum

class directions(enum.Enum):
    NONE = 0
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4

class Bomber(animation.AnimateSprite):
    """ BomberMan, everything is in the name """

    def __init__(self,game, pos, color, speed=5, stack=1, fire_power=3, shield=False):
        super().__init__('bomber_'+color)
        self._game = game
        self._shield = shield
        self._stack = stack
        self._fire_power = fire_power
        self._speed = speed
        self._rect = self.image.get_rect()
        self._rect_x = pos[0]
        self._rect_y = pos[1]
        self.direction = directions.NONE
        self._last_deplacement = (0,0)

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
        # Manage the movment
        
        self._rect_x += direction[0]* self._speed
        self._rect_y += direction[1]* self._speed
        self._last_deplacement = direction
        # Manage the animation
#        if direction[0] == 1 and self.direction == directions.NONE : 
#            self.direction = directions.RIGHT
#        elif direction[0] == -1 and self.direction == directions.NONE:
#            self.direction = directions.LEFT
#        if direction[1] == 1 and self.direction == directions.NONE: 
#            self.direction = directions.DOWN                
#        elif direction[1] == -1 and self.direction == directions.NONE:
#            self.direction = directions.UP
#        if direction[0] == 0 and direction[1] == 0:
#            self.direction = directions.NONE


           
                    
    def die(self):
        """ Remove bomber sprite and play death animation"""
        pass

    def bomb(self):
        """ Set one bomb on the current bomber's position """
        self._game.new_bomb(self)

    def animate(self, loop=False):
        """"""""
        if(self._last_deplacement != (0,0)):
            super().animate(True)
            multiply = 0
            if self._last_deplacement [0] == 1 : 
                multiply = 1
            elif self._last_deplacement [0] == -1 :
                multiply = 3
            if self._last_deplacement [1] == 1 : 
                multiply = 2              
            elif self._last_deplacement [1] == -1:
                multiply = 0
            self.set_current_image(multiply*7+self.get_current_image()%7)
            self._last_deplacement = (0,0)



        
