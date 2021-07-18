import cv2
import numpy as np


class Env:
    """
    Load an image and convert to numpy array as well a
    """

    FILL = np.array([0, 0, 0])
    EMPTY = np.array([255, 255, 255])

    def __init__(self, map_, w=600, h=400):
        self.map = map_
        self._display = self.map.copy()

        self.w, self.h = w, h

    def clear(self):
        self._display = self.map.copy()

    def add_sensor(self, state, c=(255, 0, 0)):
        x, y = state
        cv2.circle(
            self._display,
            (int(x), int(y)),
            color=c,
            radius=10,
            thickness=-1
        )

    def show(self, fps=10):
        img = cv2.resize(self._display, (self.w, self.h), interpolation=cv2.INTER_AREA)
        cv2.imshow("map", img)
        cv2.waitKey(0 if fps == 0 else 1000//fps)
