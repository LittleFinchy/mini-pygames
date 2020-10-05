import pygame
from pygame.locals import *
from string import String

pygame.init()

win = pygame.display.set_mode((800,800))

mid = pygame.display.get_surface().get_size()[0] // 2
start_y = pygame.display.get_surface().get_size()[1] // 2 #300
r1 = 201
r2 = 127
a1 = 0
a2 = 0
m1 = 25
m2 = 25

line_1 = String(mid, start_y, r1, a1, m1)
line_2 = String(line_1.x2, line_1.y2, r2, a2, m2)
paint_points = [(mid, start_y+r1+r2), (mid, start_y+r1+r2)]

cycle = 0
run = True
while run:
    cycle += 1

    line_1.show(win)
    line_2.show(win)
    line_1.update()
    line_2.update(line_1)

    if cycle % 30 == 0:
        paint_points.append(line_2.point2)
    #pygame.draw.aalines(win, (255,0,0), False, paint_points)
    for point in paint_points:
        pygame.draw.circle(win, (255,0,0), point, 1)

    line_1.a += 0.0055
    line_2.a += 0.008

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    win.fill((0,0,0))



pygame.quit()