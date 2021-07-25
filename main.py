import numpy as np
import random

from generate_env import generate_human_map
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


map_ = generate_human_map()
H, W, _ = map_.shape

disp = Display(W, H)

env = Env(map_)
env.start = (100, 100)
env.goal = (400, 400)


agent = Agent(env, env.start)
lidar = LaserSensor(env, agent.pos, 50, 10)
agent.sensor = lidar

while True:
    # move the agent
    new_pos = agent.step(None, size=5)
    data = agent.sense()

    # plot map
    disp.plot(map_)
    for point in data:
        disp.add_point(point, c=(0, 255, 0), r=5)
    disp.add_point(agent.pos, c=(255, 255, 0), r=5)
    disp.show(fps=1000)

    # plot agent map
    disp.plot(agent.local_map, "agent map")
    disp.add_point(agent.pos, c=(255, 255, 0), r=5)
    disp.show(fps=10)
