import pygame
import os
from dot import Dot

os.environ['SDL_VIDEO_CENTERED']='1'
pygame.init()

width, height = 1200, 800
fps = 30
win = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

### colors
WHITE = (255,255,255)
BLACK = (0,0,0)

all_dots = []
for i in range(100):
    all_dots.append(Dot())

run = True
while run:
    clock.tick(fps)

    pygame.display.update()
    win.fill(BLACK)


    for dot in all_dots:
        dot.update()
        dot.show(win)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

pygame.quit()







'''
everything moves to the left
dots move up and down
dots are different sizes
lines are more bright if they are connected to bigger dots
lines fade out after a little while
lines connect from one dot to another and get slower as they get closer
dots are differnt colors
some dots flash around in the background
'''