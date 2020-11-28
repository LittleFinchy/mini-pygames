import pygame
import os
from segment import Segment
from digit import Digit

os.environ['SDL_VIDEO_CENTERED']='1'
pygame.init()

width, height = 800, 800
fps = 60
win = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

### colors
WHITE = (255,255,255)
BLACK = (0,0,0)


seg1 = Segment(40,40, upright=True)
seg2 = Segment(60,20)

dig = Digit([seg1, seg2])

run = True
while run:
    clock.tick(fps)

    pygame.display.update()
    win.fill(BLACK)


    dig.show(win)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()