import pygame
import os
from star import Star

os.environ['SDL_VIDEO_CENTERED']='1'
pygame.init()

width, height = 1200, 800
fps = 100
win = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

### colors
WHITE = (255,255,255)
BLACK = (0,0,0)

NUM_OF_STARS = 1000
stars = []
for i in range(NUM_OF_STARS):
    stars.append(Star(width, height))


run = True
while run:
    clock.tick(fps)

    pygame.display.update()
    win.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #print(stars[0].r)

    for star in stars:
        star.update()
        star.show(win)

pygame.quit()