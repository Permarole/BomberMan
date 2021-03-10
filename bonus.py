import animation
import enum
import bomber

class Type(enum.Enum):
    SPEED = 0
    SHIELD = 1
    FIRE = 2
    STACK = 3


class Bonus(animation.AnimateSprite):
    """"Upgrade that can be gathered by a bomber"""
    def __init__(self,type):
        self.type = type
    
    def upgrade(self,bomber):
        """Apply the upgrade to the bomber and remove the bonus """
        if type == Type.SPEED :
            pass
        elif type == Type.SHIELD :
            pass
        elif type == Type.FIRE :
            pass
        elif type == Type.STACK :
            pass
        self.remove()


