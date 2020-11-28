import pygame


class Segment:
    def __init__(self, x, y, upright=False, active=True):
        self.x = x
        self.y = y
        self.upright = upright
        self.active = active
        self.h = 16
        self.w = 16

        if self.upright:
            self.h += 80
        else:
            self.w += 80

    def update(self):
        pass

    def show(self, win):
        if self.active:
            pygame.draw.rect(win, (255, 0, 0), (self.x, self.y, self.w, self.h))
        if not self.upright:
            pygame.draw.polygon(win, (255, 0, 0), ((self.x - 8, self.y + 8),(self.x, self.y),(self.x, self.y + 15)))
            pygame.draw.polygon(win, (255, 0, 0), ((self.x + 96 + 8, self.y + 8),(self.x + 96, self.y),(self.x + 96, self.y + 15)))
        else:
            pygame.draw.polygon(win, (255, 0, 0), ((self.x + 8, self.y - 8),(self.x + 15, self.y),(self.x, self.y)))
            pygame.draw.polygon(win, (255, 0, 0), ((self.x + 8, self.y + 96 + 8),(self.x + 15, self.y + 96),(self.x, self.y + 96)))