import cv2
import numpy as np

from env import Env


#map_ = cv2.imread("./map.png")
map_ = np.array([[1, 1], [0, 0]]).astype(np.float32)

env = Env(map_)
while True:
    env.show()
