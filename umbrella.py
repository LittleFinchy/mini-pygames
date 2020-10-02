import pygame
import math

class Umbrella:
    def __init__(self, center):
        self.center = pygame.mouse.get_pos()
        self.w = 100
        self.h = 60
        self.left = self.center[0] - self.w/2
        self.top = self.center[1] - self.h/2 - 50
        

    def update(self):
        self.center = pygame.mouse.get_pos()
        self.left = self.center[0] - self.w/2
        self.top = self.center[1] - self.h/2

    def show(self, win):
        pygame.draw.arc(win, (255,0,0), (self.left, self.top, self.w, self.h), math.pi/6, 5*math.pi/6)

