import math

mid = pygame.display.get_surface().get_size()[0] // 2

class String:
    def __init__(self, x, y, r, a):
        self.x1 = x
        self.y2 = y
        self.r = r
        self.a = a
        self.point1 = (self.x1, self.y1)

        self.x2 = int(r1 * math.sin(a1)) + mid
        self.y2 = y1 = int(r1 * math.cos(a1))
        self.point2 = (self.x2, self.y2)