import cv2


class Display:
    """
    Load an image and convert to numpy array as well a
    """
    def __init__(self, w=600, h=400):
        self.w, self.h = w, h
        self._display = self._named_window = None

    def plot(self, display, window_name="image"):
        self._window_name = window_name
        self._display = display.copy()
        cv2.namedWindow(self._window_name)

    def mouse_callback(self, mouse_callback_func):
        cv2.setMouseCallback(self._window_name,  mouse_callback_func)

    def add_point(
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
        img = cv2.resize(
            self._display, (self.h, self.w), interpolation=cv2.INTER_AREA
        )
        cv2.imshow(self._window_name, img)
        return cv2.waitKey(0 if fps == 0 else 1000//fps)
