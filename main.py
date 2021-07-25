import cv2
import numpy as np
import random

from env import Env
from display import Display
from sensors import LaserSensor
from agent import Agent

SEED = 0
random.seed(SEED)
np.random.seed(SEED)


def test_arr():
    map_ = np.zeros((6, 8, 3))
    map_[:, :, :] = [255, 255, 255]
    map_[3, 1, :] = [0, 0, 0]
    map_[3, 2, :] = [0, 0, 0]
    map_[3, 3, :] = [0, 0, 0]
    return map_


# map_ = test_arr()
map_ = cv2.imread("./map.png")
H, W, _ = map_.shape

disp = Display(W, H)

env = Env(map_)
init_pos = np.array([400, 400])
lidar = LaserSensor(env, init_pos, 50, 10)
agent = Agent(env, init_pos, lidar)

while True:
    # move the agent
    new_pos = agent.step(None, size=5)
    data = agent.sense()

    # plot map
    disp.plot(map_)
    for point in data:
        disp.add_sensor_point(point, c=(0, 255, 0), r=5)
    disp.add_sensor_point(agent.pos, c=(255, 255, 0), r=5)
    disp.show(fps=10)

    # plot agent map
    disp.plot(agent.local_map)
    disp.add_sensor_point(agent.pos, c=(255, 255, 0), r=5)
    disp.show("agent map", fps=10)
