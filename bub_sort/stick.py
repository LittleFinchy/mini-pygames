import pygame
import random

class Stick:
    def __init__(self, x, w):
        self.x = x
        self.w = w
        self.h = random.randint(10,pygame.display.get_surface().get_size()[1] - 100)

        self.color = (155,0,0)
    
    def __gt__(self, other):
        if self.h > other.h:
            return True
        return False

    def __lt__(self, other):
        if self.h < other.h:
            return True
        return False

    def show(self, win):
        self.top = pygame.display.get_surface().get_size()[1] - self.h
        pygame.draw.rect(win, self.color, (self.x, self.top, self.w, self.h))