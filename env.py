import cv2


class Env:
    """
    Load an image and convert to numpy array as well a
    """

    EMPTY = (0, 0, 0)
    FILL = (255, 255, 255)

    def __init__(self, map_, w=600, h=400):
        self.map_ = map_

        self.w, self.h = w, h

    def show(self, fps=10):
        img = cv2.resize(self.map_, (self.w, self.h), interpolation=cv2.INTER_AREA)
        cv2.imshow("map", img)
        cv2.waitKey(0 if fps == 0 else 1000//fps)
