import pygame
from digit import Digit
from colon import Colon


class Clock:
    def __init__(self):
        self.col = Colon(400, 350//2)
        self.hour1 = Digit(30, 50)
        self.hour2 = Digit(210, 50)
        self.minute1 = Digit(450, 50)
        self.minute2 = Digit(630, 50)
    
    def update(self, hour, minute, seconds):
        self.col.update(seconds)

        if hour > 12:
            hour -= 12
        h1 = 0
        self.hour1.dim = True
        h2 = hour
        if len(str(hour)) == 2:
            self.hour1.dim = False
            h1 = int(str(hour)[0])
            h2 = int(str(hour)[1])
        self.hour1.update(h1)
        self.hour2.update(h2)

        m1 = 0
        m2 = minute
        if len(str(minute)) == 2:
            m1 = int(str(minute)[0])
            m2 = int(str(minute)[1])
        self.minute1.update(m1)
        self.minute2.update(m2)

    def show(self, win):
        self.col.show(win)
        self.hour1.show(win)
        self.hour2.show(win)
        self.minute1.show(win)
        self.minute2.show(win)