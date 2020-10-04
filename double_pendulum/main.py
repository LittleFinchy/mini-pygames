import pygame
from pygame.locals import *
from string import String

pygame.init()

win = pygame.display.set_mode((600,600))

mid = pygame.display.get_surface().get_size()[0] // 2
r1 = 200
r2 = 150
a1 = 0 #3.14/6
a2 = 0 #-3.14/4
m1 = 25
m2 = 25

line_1 = String(mid, 50, r1, a1, m1)
line_2 = String(line_1.x2, line_1.y2, r2, a2, m2)


run = True
while run:

    line_1.show(win)
    line_2.show(win)
    line_1.update()
    line_2.update(line_1)

    # line_1.a = pygame.mouse.get_pos()[0] / 100
    # line_2.a = pygame.mouse.get_pos()[1] / 100

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    win.fill((0,0,0))



pygame.quit()