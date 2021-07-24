import numpy as np


class Env:
    FILL = np.array([0, 0, 0])
    EMPTY = np.array([255, 255, 255])

    def __init__(self, map_):
        self._map = map_
        self.map_size = self._map.shape

    def is_obstacle(self, pos):
        if pos not in self:
            return False
        value = self._map[int(pos[1]), int(pos[0]), :]
        return np.all(value == self.FILL)

    def __contains__(self, pos):
        # make sure that neither of the indicies are negative
        if pos[0] < 0 or pos[1] < 0:
            return False
        try:
            _ = self._map[int(pos[1]), int(pos[0]), :]
            return True
        except IndexError:
            return False

