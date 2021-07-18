import numpy as np
import random


class Agent:
    DOWN = [0, 1]
    UP = [0, -1]
    RIGHT = [1, 0]
    LEFT = [-1, 0]
    ACTIONS = [UP, DOWN, RIGHT, LEFT]

    def __init__(self, env, pos, sensor):
        self.pos = pos
        self._env = env
        self._sensor = sensor

    def step(self, action=None, size=3):
        if action is None:
            action = random.choice(self.ACTIONS)

        action = np.array(action)
        new_pos = self.pos + size*action

        if new_pos in self._env and not self._env.is_obstacle(new_pos):
            self.pos = new_pos
            self._sensor.pos = new_pos
        else:
            new_pos = self.pos
        return new_pos

    def sense(self):
        if self._sensor:
            return self._sensor.sense()
        return []


