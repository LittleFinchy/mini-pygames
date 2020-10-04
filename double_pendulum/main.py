import pygame
from pygame.locals import *
from string import String


pygame.init()

win = pygame.display.set_mode((600,600))

mid = pygame.display.get_surface().get_size()[0] // 2
r1 = 200
r2 = 200
a1 = 0
a2 = 0
m1 = 10
m2 = 10

line1 = String(mid, 50, r1, a1)


run = True
while run:

    pygame.draw.line(win, line1.color, line1.point1, line1.point2)

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.display.update()
    win.fill((0,0,0))


pygame.quit()