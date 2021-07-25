"""
Make random environments for the agent to navigate in.
For now (2021-07-24) it should create a kind of maze.
"""
import numpy as np
import cv2

from display import Display

GREEN = (0, 255, 0)
BLUE = (255, 0, 0)

W, H = 500, 500
map_ = np.zeros((W, H, 3), np.uint8)


class CoordinateStore:
    def __init__(self):
        self.points = []

    def select_point(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            cv2.circle(map_, (x, y), 3, (0, 0, 255), 0)
            self.points.append((x, y))

        if len(self.points) == 2:
            cv2.rectangle(map_, self.points[0], self.points[1], (0, 0, 255), -1)
            self.points = []


def try_1():
    disp = Display()
    # make array of size w, h
    w, h = 10, 10
    map_ = np.zeros((w, h, 3))

    # decide a start and end goal.
    start = [int(np.random.choice(w, 1)), int(np.random.choice(w, 1))]
    while True:
        end = [int(np.random.choice(w, 1)), int(np.random.choice(w, 1))]
        if end != start:
            break

    # put obstacles inside between the start and end
    def vertical_slab(size, start_loc):
        start_x, start_y = start_loc
        return [(start_x, start_y + y) for y in range(size)]

    def horizontal_slab(size, start_loc):
        start_x, start_y = start_loc
        return [(start_x + x, start_y) for x in range(size)]

    obs = []
    for _ in range(2):
        start_loc = [int(np.random.choice(w//2, 1)), int(np.random.choice(w//2, 1))]
        size = int(np.random.choice(w, 1))
        obs += vertical_slab(size, start_loc)

    # display result
    disp.plot(map_)
    disp.add_sensor_point(start, c=(0, 255, 0), r=0)
    for point in obs:
        disp.add_sensor_point(point, c=(0, 255, 255), r=0)
    disp.add_sensor_point(end, c=(255, 0, 0), r=0)
    disp.show(fps=0)


def generate_human_env():
    store_coords = CoordinateStore()
    disp = Display(W, H)
    # Create a black image, a window and bind the function to window
    start, end = (10, 10), (400, 400)
    map_[start] = GREEN
    map_[end] = BLUE
    while True:
        disp.plot(map_)
        disp.add_point(start, c=GREEN)
        disp.add_point(end, c=BLUE)
        disp.mouse_callback(store_coords.select_point)
        k = disp.show(fps=1000)
        if k == 27:
            break
    cv2.destroyAllWindows()

    return map_


if __name__ == "__main__":
    generate_human_env()
