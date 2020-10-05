import pygame
import math
from pygame.locals import *
from string import String

pygame.init()

win = pygame.display.set_mode((800,800))

mid = pygame.display.get_surface().get_size()[0] // 2
start_y = pygame.display.get_surface().get_size()[1] // 2 #300
r1 = 201
r2 = 127
a1 = 3.14/4
a2 = 3.14/2
m1 = 25
m2 = 25
g = 1 #9.81

line_1 = String(mid, start_y, r1, a1, m1)
line_2 = String(line_1.x2, line_1.y2, r2, a2, m2)
paint_points = [(mid, start_y+r1+r2), (mid, start_y+r1+r2)]


def swing(line_1, line_2):
    num1 = -g * (2* line_1.m + line_2.m) * math.sin(line_1.a)
    num2 = -line_2.m * g * math.sin(line_1.a - 2 * line_2.a)
    num3 = -2 * math.sin(line_1.a - line_2.a) * line_2.m
    num4 = line_2.vel ** 2 * line_2.r + line_1.vel ** 2 * line_1.r * math.cos(line_1.a - line_2.a)
    den = line_1.r * (2 * line_1.m + line_2.m * math.cos(2 * line_1.a - 2* line_2.a))
    line_1.a += (num1 + num2 + num3 * num4) / den

    num1 = 2 * math.sin(line_1.a - line_2.a)
    num2 = (line_1.vel * line_1.a * line_1.r * (line_1.m + line_2.m))
    num3 = g * (line_1.m + line_2.m) * math.cos(line_1.a)
    num4 = line_2.vel ** 2 * line_2.r * line_2.m * math.cos(line_1.a - line_2.a)
    den = line_2.r * (2 * line_1.m + line_2.m * math.cos(2 * line_1.a - 2* line_2.a))
    line_2.a += ((num1 * (num2 + num3 + num4))) / den



cycle = 0
run = True
while run:
    cycle += 1

    line_1.show(win)
    line_2.show(win)
    swing(line_1, line_2)
    line_1.update()
    line_2.update(line_1)
    
    print(line_1.a, line_2.a)

    if cycle % 40 == 0:
        paint_points.append(line_2.point2)
    #pygame.draw.aalines(win, (255,0,0), False, paint_points)
    for point in paint_points:
        pygame.draw.circle(win, (255,0,0), point, 1)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    win.fill((0,0,0))



pygame.quit()