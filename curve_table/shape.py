import pygame

class Shape:
    def __init__(self, x, y, w, h, speed = 0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = speed

        self.cx = 0
        self.cy = 0
        self.lines = []

    def update(self, newX, newY):
        self.cx = newX
        self.cy = newY
        self.lines.append((self.cx, self.cy))



    def show(self, win):
        if len(self.lines) > 1:
            pygame.draw.aalines(win, (255,255,255), False, self.lines)
        circle = (int(self.cx), int(self.cy))
        pygame.draw.circle(win, (255,0,0), circle, 3)
