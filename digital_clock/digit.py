import pygame


class Digit:
    def __init__(self, segments):
        self.segments = segments

    def update(self):
        pass

    def show(self, win):
        for seg in self.segments:
            seg.show(win)