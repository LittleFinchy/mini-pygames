import pygame
from pygame.locals import *
import os
from grid import Grid

os.environ['SDL_VIDEO_CENTERED']='1'
pygame.init()

width, height = 600, 600
fps = 10
win = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

### colors
WHITE = (255,255,255)
BLACK = (0,0,0)


grid = Grid(50,50)

run = True
slow = False
while run:
    clock.tick(fps)

    pygame.display.update()
    win.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                slow = not slow
            else:
                grid.update()
        
        if event.type == pygame.MOUSEBUTTONUP:
            grid = Grid(20,20)
        

    grid.show(win)
    grid.update()


pygame.quit()