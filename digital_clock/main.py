import pygame
import os
import time
from clock import Clock


os.environ['SDL_VIDEO_CENTERED']='1'
pygame.init()

width, height = 800, 350
fps = 60
win = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

### colors
WHITE = (255,255,255)
BLACK = (0,0,0)


my_clock = Clock()


run = True
while run:
    clock.tick(fps)

    pygame.display.update()
    win.fill(BLACK)



    hours = time.localtime()[3]
    minutes = time.localtime()[4]
    seconds = time.localtime()[5]

    my_clock.update(hours, minutes, seconds)
    my_clock.show(win)



    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()