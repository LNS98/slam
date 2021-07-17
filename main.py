import cv2
import numpy as np
import random

from env import Env
from sensors import LaserSensor


map_ = cv2.imread("./map.png")
#map_ = np.array([[1, 1], [0, 0]]).astype(np.float32)

env = Env(map_)
sensor_location = np.array([100, 100])
sensor = LaserSensor(sensor_location, 10, 10)
while True:
    action = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    sensor.state += np.array(random.choice(action))
    env.add_sensor(sensor.state)
    env.show()
