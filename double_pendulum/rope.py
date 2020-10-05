import pygame
import math

class Rope:
    def __init__(self, x, y, r, a, m):
        self.x1 = x
        self.y1 = y
        self.r = r
        self.a = a
        self.m = m
        self.point1 = [self.x1, self.y1]

        self.acc = 0
        self.vel = 0

        self.x2 = int(self.r * math.sin(self.a)) + self.x1
        self.y2 = int(self.r * math.cos(self.a))
        self.point2 = [self.x2, self.y2]

        self.color = (255,255,255)

    
    def show(self, win):
        pygame.draw.line(win, self.color, self.point1, self.point2, 2)
        pygame.draw.circle(win, self.color, self.point2, self.m//4)

    def update(self, slave=None):
        if slave:
            self.x1 = slave.x2
            self.y1 = slave.y2
            self.point1 = [self.x1, self.y1]

        self.x2 = int(self.r * math.sin(self.a)) + self.x1
        self.y2 = int(self.r * math.cos(self.a)) + self.y1
        self.point2 = [self.x2, self.y2]

        self.vel += self.acc
        self.a += self.vel
