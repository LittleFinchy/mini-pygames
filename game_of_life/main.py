import pygame
import os
from grid import Grid

os.environ['SDL_VIDEO_CENTERED']='1'
pygame.init()

width, height = 800, 800
fps = 10
win = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

### colors
WHITE = (255,255,255)
BLACK = (0,0,0)

grid = Grid(50,50)

grid.cells[10][10].s = 1
grid.cells[11][10].s = 1
grid.cells[12][10].s = 1

run = True
while run:
    clock.tick(fps)

    pygame.display.update()
    win.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            grid = Grid(50,50)

    grid.show(win)
    grid.update(grid.cells)


pygame.quit()