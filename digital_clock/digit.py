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
        for i in range(7):
            self.segments[i].active = True
        numbers = {
            0: [self.segments[5]], 
            1: [self.segments[0], self.segments[2], self.segments[4], self.segments[5], self.segments[6]],
            2: [self.segments[0], self.segments[3]],
            3: [self.segments[0], self.segments[3]],
            4: [self.segments[2], self.segments[4], self.segments[6]],
            5: [self.segments[1], self.segments[2]],
            6: [self.segments[1]],
            7: [self.segments[0], self.segments[2], self.segments[5], self.segments[6]],
            8: [],
            9: [self.segments[2], self.segments[6]]
        }

        for seg in numbers.get(number):
            seg.active = False


    def show(self, win):
        for seg in self.segments:
            seg.show(win)
