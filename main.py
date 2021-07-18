import cv2
import numpy as np
import random
import math

from env import Env
from sensors import LaserSensor


map_ = cv2.imread("./map.png")
#map_ = np.array([[1, 1], [0, 0]]).astype(np.float32)

env = Env(map_)
sensor_location = np.array([100, 400])
sensor = LaserSensor(env, sensor_location, 50, 10)

while True:
    actions = [[0, 5], [5, 0], [0, -5], [-5, 0]]
    #sensor.pos += np.array(random.choice(actions))
    sensor.pos += np.array(actions[1])
    data = sensor.sense()
    for point in data:
        env.add_sensor(point, c=(0, 255, 0), r=4)

    env.add_sensor(sensor.pos)
    env.show()
    env.clear()
