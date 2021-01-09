import pygame
import random
# Rect(left, top, width, height)

class Pipe:
    def __init__(self):
        self.x = pygame.display.get_surface().get_size()[0] + 20
        self.y = random.randint(20, pygame.display.get_surface().get_size()[1] - 220)
        self.gap = random.randint(100, 200)
        self.w = 20
    
    def update(self):
        if self.x < -10:
            self.x = pygame.display.get_surface().get_size()[0] + 20
            self.y = random.randint(20, pygame.display.get_surface().get_size()[1] - 320)
            self.gap = random.randint(200, 300)
        
        self.x -= 2

    def show(self, win):
        RED = (255, 0, 0)
        GRAY = (150, 150, 150)
        rect1 = (self.x, 0, self.w, self.y)
        rect2 = (self.x, self.y + self.gap, self.w, pygame.display.get_surface().get_size()[1] - self.y + self.gap)

        pygame.draw.rect(win, RED, rect1)
        pygame.draw.rect(win, RED, rect2)