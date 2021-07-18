import cv2
import numpy as np
import random
import math

from env import Env, Display
from sensors import LaserSensor
from agent import Agent

#SEED = 0
#random.seed(SEED)
#np.random.seed(SEED)


def test_arr():
    map_ = np.zeros((6, 8, 3))
    map_[:, :, :] = [255, 255, 255]
    map_[3, 1, :] = [0, 0, 0]
    map_[3, 2, :] = [0, 0, 0]
    map_[3, 3, :] = [0, 0, 0]
    return map_


#map_ = test_arr()
map_ = cv2.imread("./map.png")


env = Env(map_)
disp = Display(map_, 600, 600)
init_pos = np.array([400, 300])
lidar = LaserSensor(env, init_pos, 50, 10)
agent = Agent(env, init_pos, lidar)

while True:
    new_pos = agent.step(agent.RIGHT, size=3)
    data = agent.sense()
    for point in data:
        disp.add_sensor_point(point, c=(0, 255, 0), r=10)

    print("agent pos: ", agent.pos, agent.pos in env.map)
    disp.add_sensor_point(agent.pos, c=(255, 255, 0), r=10)
    disp.show(fps=10)
    disp.clear()
