import cv2


class Env:
    """
    Load an image and convert to numpy array as well a
    """

    EMPTY = (0, 0, 0)
    FILL = (255, 255, 255)

    def __init__(self, map_, w=600, h=400):
        self.map = map_
        self._display = self.map.copy()

        self.w, self.h = w, h

    def add_sensor(self, state):
        self._display = self.map.copy()
        x, y = state
        cv2.circle(
            self._display, (int(x), int(y)), color=(255, 0, 0), radius=2, thickness=-1
        )

    def show(self, fps=10):
        img = cv2.resize(self._display, (self.w, self.h), interpolation=cv2.INTER_AREA)
        cv2.imshow("map", img)
        cv2.waitKey(0 if fps == 0 else 1000//fps)

        # reset the display to just the map
        self._display = self.map.copy()
