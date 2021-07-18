import cv2
import numpy as np


class Env:
    FILL = np.array([0, 0, 0])
    EMPTY = np.array([255, 255, 255])

    def __init__(self, map_):
        self.map = map_

    def is_obstacle(self, pos):
        value = self.map[int(pos[1]), int(pos[0]), :]
        return np.all(value == self.FILL)

    def __contains__(self, pos):
        # make sure that neither of the indicies are negative
        if pos[0] < 0 or pos[1] < 0:
            return False
        try:
            _ = self.map[int(pos[1]), int(pos[0]), :]
            return True
        except IndexError:
            return False


class Display:
    """
    Load an image and convert to numpy array as well a
    """
    def __init__(self, map_, w=600, h=400):
        self.map = map_
        self._display = self.map.copy()
        self.w, self.h = w, h

    def clear(self):
        self._display = self.map.copy()

    def add_sensor_point(
        self,
        state,
        c=(255, 0, 0),
        r=10
    ):
        x, y = state
        cv2.circle(
            self._display,
            (int(x), int(y)),
            color=c,
            radius=r,
            thickness=-1
        )

    def show(self, fps=10):
        img = cv2.resize(self._display, (self.w, self.h), interpolation=cv2.INTER_AREA)
        cv2.imshow("map", img)
        cv2.waitKey(0 if fps == 0 else 1000//fps)
