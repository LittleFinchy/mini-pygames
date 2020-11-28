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
        # self.hour1.update(hour)
        # self.hour2.update(hour)
        # self.minute1.update(minute)
        # self.minute2.update(minute)

    def show(self, win):
        self.col.show(win)
        self.hour1.show(win)
        self.hour2.show(win)
        self.minute1.show(win)
        self.minute2.show(win)