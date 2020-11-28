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



hour1 = Digit(50, 300)
hour2 = Digit(250, 300)
minute1 = Digit(450, 300)
minute2 = Digit(650, 300)



run = True
while run:
    clock.tick(fps)

    pygame.display.update()
    win.fill(BLACK)

    #dig.show(win)

    hour1.show(win)
    hour2.show(win)
    minute1.show(win)
    minute2.show(win)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()