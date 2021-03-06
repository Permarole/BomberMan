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
        super().__init__('bomber_'+color, (63,55))
        self._game = game
        self._shield = shield
        self._stack = stack
        self._fire_power = fire_power
        self._speed = speed
        self.rect = self.image.get_rect()
        self.direction = directions.NONE
        self._last_deplacement = (0,0)
        self.set_mask(self.rect)
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self._on_bomb = False


    def get_pos(self):
        """ Return bomber's position"""
        return self.rect.x, self.rect.y

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

        # if not self._game.check_collision(self, self._game._level):
        self.rect.x += direction[0]* self._speed
        self.rect.y += direction[1]* self._speed
        self._last_deplacement = direction
        if not self._game.check_collision(self, self._game._bombs) :
            self._on_bomb = False
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
        if self._stack > 0:
            if self._game.new_bomb(self) :
                self._stack -= 1

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



        
