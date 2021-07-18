import math
import numpy as np


class LaserSensor:
    """
    Basic Version of a sensor model.
    """

    # NOTE: I don't really want to pass the env to the sensor
    def __init__(self, env, pos, distance_range, angular_speed):
        self.r = distance_range
        self.angular_speed = angular_speed

        # the sensor will be in a state, right?
        self.env = env
        self.pos = pos

    def emit_laser(self, angle):
        x, y = self.pos

        # emit a laser at every position between the curr pos and the range of
        # the laser
        for i in range(self.r + 1):
            new_x = int(x + i*math.cos(angle))
            new_y = int(y + i*math.sin(angle))

            # here you will have to sense from the map
            obs = self.env.map[new_y, new_x, :]
            print(obs)
            if np.all(obs == self.env.FILL):
                return True, (new_x, new_y)

        return False, None

