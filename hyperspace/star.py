import pygame
import random

class Star:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.x = random.randint(-width//2, width//2)
        self.y = random.randint(-height//2, height//2)
        self.z = random.randint(self.width // 2, self.width)
        self.pz = self.z

        self.sx = 0
        self.sy = 0
        self.s = 10
        self.r = 0

    def update(self):
        self.z -= self.s

        if self.z < 1:
            self.z = random.randint(self.width // 2, self.width)
            self.x = random.randint(-self.width/2, self.width/2)
            self.y = random.randint(-self.height/2, self.height/2)
            self.pz = self.z
        
        self.sx = (self.x / self.z) * self.width / 2 + self.width / 2
        self.sy = (self.y / self.z) * self.height / 2 + self.height / 2
        self.r = 4 - (self.z / self.width) * 4
        


    def show(self, win):
        pygame.draw.circle(win, (255,255,255), (int(self.sx), int(self.sy)), int(self.r))