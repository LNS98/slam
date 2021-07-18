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
H, W, _ = map_.shape


env = Env(map_)
env_disp = Display(map_, W, H)
init_pos = np.array([400, 400])
lidar = LaserSensor(env, init_pos, 50, 10)
agent = Agent(env, init_pos, lidar)
agent_disp = Display(agent.local_map, W, H)

while True:
    new_pos = agent.step(None, size=5)
    data = agent.sense()
    for point in data:
        env_disp.add_sensor_point(point, c=(0, 255, 0), r=5)

    env_disp.add_sensor_point(agent.pos, c=(255, 255, 0), r=5)
    env_disp.show(fps=10)
    env_disp.clear()

    # plot agent map
    agent_disp.add_sensor_point(agent.pos, c=(255, 255, 0), r=5)
    agent_disp.show("agent map", fps=10)
    agent_disp.clear()
