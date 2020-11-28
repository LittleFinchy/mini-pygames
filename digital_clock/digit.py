import pygame
from segment import Segment


class Digit:
    def __init__(self, x, y):
        self.segments = []


        # Make 7 segments centered around the x,y that is given
        self.segments.append(Segment(x, y + 20, upright=True))
        self.segments.append(Segment(x + 120, y + 20, upright=True))
        self.segments.append(Segment(x + 120, y + 140, upright=True))
        self.segments.append(Segment(x, y + 140, upright=True))

        self.segments.append(Segment(x + 20, y))
        self.segments.append(Segment(x + 20, y + 120))
        self.segments.append(Segment(x + 20, y + 240))

    def update(self):
        pass

    def show(self, win):
        for seg in self.segments:
            seg.show(win)
