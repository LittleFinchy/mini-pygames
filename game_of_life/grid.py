import pygame
import random
from cell import Cell

class Grid:
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.x_spacing = pygame.display.get_surface().get_size()[0] / self.cols
        self.y_spacing = pygame.display.get_surface().get_size()[1] / self.rows

        self.cells = []
        for i in range(self.cols):
            self.cells.append([])
            for j in range(self.rows):
                self.cells[i].append(Cell(i*self.x_spacing, j*self.y_spacing, self.x_spacing, self.y_spacing, random.randint(0,1)))

    def update(self):
        for i in range(self.cols):
            for j in range(self.rows):
                num = self.countNeighbors(i, j)
                if self.cells[i][j].s == 0 and num == 3:
                    self.cells[i][j].n = 1
                    #print(i,j, 'live', num)
                elif self.cells[i][j].s == 1 and (num < 2 or num > 3):
                    self.cells[i][j].n = 0
                    #print(i,j, 'dead', num)
                else:
                    self.cells[i][j].n = self.cells[i][j].s

    def countNeighbors(self, x, y):
        count = 0
        for i in range(-1,2):
            for j in range(-1,2):
                col = (x + i + self.cols) % self.cols
                row = (y + j + self.rows) % self.rows
                count += self.cells[col][row].s
        return count - self.cells[x][y].s

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

    def doctor(self):
        for i in range(self.cols):
            for j in range(self.rows):
                if self.cells[i][j].s:
                    pass
                    #print(self.countNeighbors(i,j)