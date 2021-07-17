import pygame


class Env:

    WHITE = (255, 255, 255)

    def __init__(self, map_file, w, h):
        pygame.init()
        self.w, self.h = w, h
        self.surface = pygame.display.set_mode((self.w, self.h))
        self.surface.fill(self.WHITE)
        pygame.display.set_caption("map")

        # create a surface object, image is drawn on it.
        map_ = pygame.image.load(map_file)
        self.surface.blit(map_, (0, 0))

    def display(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            pygame.display.update()

