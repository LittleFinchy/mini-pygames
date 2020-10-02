import random
import pygame

class Drop:
    def __init__(self):
        self.x = random.randint(0, pygame.display.get_surface().get_size()[0])
        self.y = random.randint(-500, -10)
        self.len_ = random.randint(5, 10)/2
        self.speed = random.randint(5,10) / 2

    def fall(self):
        self.y += self.speed

        if self.y > pygame.display.get_surface().get_size()[1]:
            self.y = random.randint(-200, -10)
            self.x = random.randint(0, pygame.display.get_surface().get_size()[0])
            self.speed = random.randint(5,10) / 2

    def show(self, win):
        pygame.draw.line(win, (138, 42, 240), (self.x, self.y), (self.x, self.y + self.len_))