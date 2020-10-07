import pygame, os, math
from grid import Grid

os.environ['SDL_VIDEO_CENTERED']='1'
pygame.init()

width, height = 800, 800
fps = 30
win = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

### colors
WHITE = (255,255,255)
BLACK = (0,0,0)


### make grid --> fill grid with shapes
gridSize = (10,10)
grid = Grid(gridSize)

run = True
while run:
    clock.tick(fps)

    pygame.display.update()
    win.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            grid = Grid(gridSize)
    
    if grid.delta >= 2 * math.pi:
        grid = Grid(gridSize)

    grid.show(win)
    grid.update()


pygame.quit()