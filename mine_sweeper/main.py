import pygame
import os
from grid import Grid

os.environ['SDL_VIDEO_CENTERED']='1'
pygame.init()

width, height = 900, 900
fps = 60
win = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

### colors
WHITE = (255,255,255)
BLACK = (0,0,0)

gridSize = (30,30)
grid = Grid(gridSize)

run = True
while run:
    clock.tick(fps)
    pygame.display.update()
    win.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    


    grid.show(win)



pygame.quit()