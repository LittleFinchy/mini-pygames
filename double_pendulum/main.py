import pygame
import math
from pygame.locals import *


pygame.init()

win = pygame.display.set_mode((600,600))

mid = pygame.display.get_surface().get_size()[0] // 2
r1 = 200
r2 = 200
a1 = 0
a2 = 0
m1 = 10
m2 = 10
x1 = int(r1 * math.sin(a1)) + mid
y1 = int(r1 * math.cos(a1))


run = True
while run:

    pygame.draw.line(win,(255,0,0), (mid,50), (x1, y1))

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.display.update()
    win.fill((0,0,0))


pygame.quit()