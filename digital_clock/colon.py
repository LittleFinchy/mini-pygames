import pygame


class Colon:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.active = True
    
    def update(self, seconds):
        self.active = False
        if seconds % 2 == 0:
            self.active = True

    def show(self, win):
        if self.active:
            pygame.draw.rect(win, (200, 0, 0), (self.x - 10, self.y - 40, 20, 20))
            pygame.draw.rect(win, (200, 0, 0), (self.x - 10, self.y + 40, 20, 20))