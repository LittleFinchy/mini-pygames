import pygame

class Cell:
    def __init__(self, x, y, w, h, s):
        self.x = x      # left x position
        self.y = y      # top y position
        self.w = w-1    # width
        self.h = h-1    # height
        self.s = s      # state
        self.n = s      # next state

    def show(self, win):
        color = (255,255,255)
        self.s = self.n
        if self.s:
            color = (0,0,0)
        
        rect = (self.x, self.y, self.w, self.h)

        pygame.draw.rect(win, color, rect, 0)