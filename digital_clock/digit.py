import pygame
from digit import Digit


class Digit:
    def __init__(self, segments):
        self.segments = segments

    def build(self, x, y):
        # Make 7 segments centered around the x,y that is given
        for i in range(5):
            self.segments.append(Digit())

    def update(self):
        pass

    def show(self, win):
        for seg in self.segments:
            seg.show(win)

'''
seg1 = Segment(40,40, upright=True)
seg2 = Segment(60,20)
seg3 = Segment(160,40, upright=True)
seg4 = Segment(60,140)
seg5 = Segment(160,160, upright=True)
seg6 = Segment(40,160, upright=True)
seg7 = Segment(60,260)
'''