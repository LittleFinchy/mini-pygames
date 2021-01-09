import pygame


class Cell:
    def __init__(self, x, y, w, h, is_bomb=False):
        self.x = x      # left x position
        self.y = y      # top y position
        self.w = w-1    # width
        self.h = h-1    # height
        self.is_bomb = is_bomb

    def update(self):
        pass

    def show(self, win):
        if self.is_bomb:
            color = (255,255,0)
        else:
            color = (0,255,255)

        rect = (self.x, self.y, self.w, self.h)
        
        pygame.draw.rect(win, color, rect, 0)