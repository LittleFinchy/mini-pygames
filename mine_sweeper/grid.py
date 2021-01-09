import pygame
import random
from cell import Cell


class Grid:
    def __init__(self, size):
        self.cols, self.rows = size
        self.x_spacing = pygame.display.get_surface().get_size()[0] / self.cols
        self.y_spacing = pygame.display.get_surface().get_size()[1] / self.rows

        self.cells = []
        for i in range(self.cols):
            self.cells.append([])
            for j in range(self.rows):
                self.cells[i].append(Cell(i*self.x_spacing, j*self.y_spacing, self.x_spacing, self.y_spacing))
                if random.randint(0,16) == 0:
                    self.cells[i][j].is_bomb = True

    def update(self):
        pass
        
    def countNeighbors(self, x, y):
        count = 0
        for i in range(-1,2):
            for j in range(-1,2):
                col = (x + i + self.cols) % self.cols
                row = (y + j + self.rows) % self.rows
                if self.cells[col][row].is_bomb:
                    count += 1
        return count

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
                self.cells[i][j].show(win)