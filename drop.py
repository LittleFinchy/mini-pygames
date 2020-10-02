import random
import pygame

class Drop:
    def __init__(self):
        self.x = random.randint(0, pygame.display.get_surface().get_size()[0])
        self.y = -100 #random.randint(pygame.display.get_surface().get_size()[1] - 100, pygame.display.get_surface().get_size()[1])
        self.len_ = random.randint(5, 10)/2
        self.speed = random.randint(1,4) / 10

    def fall(self):
        self.y += self.speed

        if self.y > pygame.display.get_surface().get_size()[1]:
            self.y = -100 #random.randint(pygame.display.get_surface().get_size()[1] - 100, pygame.display.get_surface().get_size()[1])

    def show(self, win):
        pygame.draw.line(win, (138, 42, 240), (self.x, self.y), (self.x, self.y + self.len_))

    def doctor(self):
        print('X: ', self.x)
        print('Y: ', self.y)
        print('speed: ', self.speed)