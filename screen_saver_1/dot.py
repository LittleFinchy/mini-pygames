import pygame
import random

COLORS = [(255, 189, 51), (255, 87, 51), (51, 255, 189), (219, 255, 51), (255, 51, 202), (104, 51, 255), (255, 141, 51), (255,255,255)]


class Dot:
    def __init__(self):
        self.color = COLORS[random.randint(0, len(COLORS)-1)]
        self.size = random.randint(3,8)
        self.speed = random.randint(self.size // 2 - 1, self.size // 2)
        self.swing = random.randint(0, 200)
        self.width, self.height = pygame.display.get_surface().get_size()
        self.pos = [self.width + random.randint(10,500), random.randint(0, self.height)]

    def reset(self):
        self.size = random.randint(3,8)
        self.speed = max(self.size - 2, 1)
        self.swing = random.randint(0, 200)
        self.pos = [self.width + random.randint(10,100), random.randint(0, self.height)]

    def update(self):
        self.pos[0] -= self.speed
        if self.pos[0] < -100:
            self.reset()


    def show(self, win):
        pygame.draw.circle(win, self.color, self.pos, self.size)