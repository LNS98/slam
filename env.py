import numpy as np


class Env:
    FILL = np.array([0, 0, 0])
    EMPTY = np.array([255, 255, 255])

    def __init__(self, map_):
        self._map = map_
        self.map_size = self._map.shape

        self._start = self._goal = None

    @property
    def start(self):
        return self._start

    @start.setter
    def start(self, loc):
        if loc in self:
            self._start = loc

    @property
    def goal(self):
        return self._goal

    @goal.setter
    def goal(self, loc):
        if loc in self:
            self._goal = loc

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
            self._map[int(pos[1]), int(pos[0]), :]
            return True
        except IndexError:
            return False
