import cv2


class Display:
    """
    Load an image and convert to numpy array as well a
    """
    def __init__(self, w=600, h=400):
        self.w, self.h = w, h
        self._display = None

    def plot(self, display):
        self._display = display.copy()

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

    def show(self, window_name="map", fps=10):
        img = cv2.resize(
            self._display, (self.w, self.h), interpolation=cv2.INTER_AREA
        )
        cv2.imshow(window_name, img)
        cv2.waitKey(0 if fps == 0 else 1000//fps)
