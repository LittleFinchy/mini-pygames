import math

class String:
    def __init__(self, x, y, r, a):
        self.x1 = x
        self.y1 = y
        self.r = r
        self.a = a
        self.point1 = [self.x1, self.y1]

        self.x2 = int(self.r * math.sin(self.a)) + self.x1
        self.y2 = int(self.r * math.cos(self.a))
        self.point2 = [self.x2, self.y2]

        self.color = (255,255,255)