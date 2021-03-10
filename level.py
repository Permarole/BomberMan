import numpy as np
import enum

class Cases(enum.Enum):
    VOID = 0
    SPAWN = 1
    BLOCK = 2
    UNBREAKABLE = 3


# '■' '□'

class Level:

    def __init__(self):
        self._cases = np.empty([11, 15])

    def generate_map(self):
        """ """
        pass

    def load_map(self, PATH):
        """ load map from file"""
        pass

    # TODO : accessor