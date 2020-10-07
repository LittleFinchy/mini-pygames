import pygame, math
from shape import Shape

class Grid:
    def __init__(self, size):
        self.cols, self.rows = size
        self.shapes = [[]]
        self.x_spacing = pygame.display.get_surface().get_size()[0] / self.cols
        self.y_spacing = pygame.display.get_surface().get_size()[1] / self.rows
        self.delta = 0
        self.rate = math.pi / 100

        for i in range(self.cols):
            self.shapes.append([])
            for j in range(self.rows):
                if i ^ j:
                    self.shapes[i].append(Shape(i*self.x_spacing, j*self.y_spacing, self.x_spacing, self.y_spacing, max(i,j)))
                else:
                    self.shapes[i].append(Shape(i*self.x_spacing, j*self.y_spacing, self.x_spacing, self.y_spacing))

    def update(self):
        self.delta += self.rate
        for i in range(self.cols):
            for j in range(self.rows):
                shape = self.shapes[i][j]
                if i and j: # for shapes that are not on the edge of the grid
                    x = self.shapes[i][0].cx
                    y = self.shapes[0][j].cy
                    shape.update(x, y)
                else: # edge cases of grid
                    newdelta = shape.speed * self.delta
                    x, y = shape.x + shape.w / 2 + math.cos(newdelta) * shape.w / 2, shape.y + shape.h / 2 + math.sin(newdelta) * shape.h / 2
                    shape.update(x, y)

    def show(self, win):
        # draw vertical lines
        for i in range(0, self.cols):
            pygame.draw.line(win, (155,155,155), (i*self.x_spacing,0), (i*self.x_spacing, pygame.display.get_surface().get_size()[1]))

        # draw horizontal lines
        for i in range(0, self.rows):
            pygame.draw.line(win, (155,155,155), (0,i*self.y_spacing), (pygame.display.get_surface().get_size()[0],i*self.y_spacing))

        # show each cell
        for i in range(self.cols):
            for j in range(self.rows):
                if i or j:
                    self.shapes[i][j].show(win)