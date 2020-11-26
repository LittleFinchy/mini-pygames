import pygame


class Segment:
    def __init__(self, x, y, upright=False, active=False):
        self.x = x
        self.y = y
        self.upright = upright
        self.active = active
        self.h = 20
        self.w = 20

        if self.upright:
            self.h += 80
        else:
            self.w += 80

    def update(self):
        pass

    def show(self, win):
        pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.w, self.h))