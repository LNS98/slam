

class LaserSensor:
    """
    Basic Version of a sensor model.
    """

    def __init__(self, distance_range, angular_speed):
        self.dstance_range = distance_range
        self.angular_speed = angular_speed

        # the sensor will be in a state, right?
        self.state = None

    def sense(self, obs):
        pass

    def emit_laser(self):
        pass

