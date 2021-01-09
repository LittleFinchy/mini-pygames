import pygame
from bird import Bird
from pipe import Pipe


class Game:
    def __init__(self):
        self.bird = Bird()
        self.pipes = []

        for i in range(4):
            self.pipes.append(Pipe())
            self.pipes[i].x = i*300 + 300
        
    def update(self):
        for p in self.pipes:
            p.update()

    def show(self, win):
        for p in self.pipes:
            p.show(win)