import pygame
import random

class Star:
    def __init__(self, width, height):
        self.x = random.randint(-width//2, width//2)
        self.y = random.randint(-height//2, height//2)
        self.z = random.randint(1,10)

    def update(self):
        pass

    def show(self):
        pass