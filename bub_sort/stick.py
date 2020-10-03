import pygame
import random

class Stick:
    def __init__(self, x, w):
        self.x = x
        self.w = w
        self.h = random.randint(10,500)
        self.top = pygame.display.get_surface().get_size()[1] - self.h
    
    def __gt__(self, other):
        if self.h > other.h:
            return True
        return False

    def __lt__(self, other):
        if self.h < other.h:
            return True
        return False

    def show(self, win):
        pygame.draw.rect(win, (155,0,0), (self.x, self.top, self.w, self.h))