import pygame
from segment import Segment


class Digit:
    def __init__(self, x, y):
        self.segments = []


        # Make 7 segments centered around the x,y that is given
        self.segments.append(Segment(x, y + 20, upright=True))
        self.segments.append(Segment(x + 120, y + 20, upright=True))
        self.segments.append(Segment(x, y + 140, upright=True))
        self.segments.append(Segment(x + 120, y + 140, upright=True))

        self.segments.append(Segment(x + 20, y))
        self.segments.append(Segment(x + 20, y + 120))
        self.segments.append(Segment(x + 20, y + 240))

    def update(self, number):
        numbers = {
            0: [self.segments[5].active], 
            1: [self.segments[0].active, self.segments[2].active, self.segments[4].active, self.segments[5].active, self.segments[6].active],
            2: [self.segments[0].active, self.segments[3].active],
            3: [self.segments[0].active, self.segments[3].active],
            4: [self.segments[2].active, self.segments[4].active, self.segments[6].active],
            5: [],
            6: [],
            7: [],
            8: [],
            9: []
        }

    def show(self, win):
        for seg in self.segments:
            seg.show(win)
