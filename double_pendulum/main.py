import pygame
import os
import math
import random
from pygame.locals import *
from rope import Rope


os.environ['SDL_VIDEO_CENTERED']='1'
pygame.init()


fps = 60
win = pygame.display.set_mode((800,800))
clock = pygame.time.Clock()

mid = pygame.display.get_surface().get_size()[0] // 2
start_y = pygame.display.get_surface().get_size()[1] // 2

r1 = 150
r2 = 220
a1 = math.pi/4
a2 = math.pi
m1 = 30
m2 = 20
g = 2



line_1 = Rope(mid, start_y, r1, a1, m1)
line_2 = Rope(line_1.x2, line_1.y2, r2, a2, m2)
paint_points = []


def swing(line_1, line_2):
    num1 = -g * (2* line_1.m + line_2.m) * math.sin(line_1.a)
    num2 = -line_2.m * g * math.sin(line_1.a - 2 * line_2.a)
    num3 = -2 * math.sin(line_1.a - line_2.a) * line_2.m
    num4 = line_2.vel ** 2 * line_2.r + line_1.vel ** 2 * line_1.r * math.cos(line_1.a - line_2.a)
    den = line_1.r * (2 * line_1.m + line_2.m - line_2.m * math.cos(2 * line_1.a - 2 * line_2.a))
    line_1.acc = (num1 + num2 + num3 * num4) / den

    num1 = 2 * math.sin(line_1.a - line_2.a)
    num2 = (line_1.vel ** 2 * line_1.r * (line_1.m + line_2.m))
    num3 = g * (line_1.m + line_2.m) * math.cos(line_1.a)
    num4 = line_2.vel ** 2 * line_2.r * line_2.m * math.cos(line_1.a - line_2.a)
    den = line_2.r * (2 * line_1.m + line_2.m - line_2.m * math.cos(2 * line_1.a - 2 * line_2.a))
    line_2.acc = (num1 * (num2 + num3 + num4)) / den


run = True
while run:
    clock.tick(fps)

    R = random.randint(1,255)
    B = random.randint(1,255)
    G = random.randint(1,255)

    if len(paint_points) > 1:
        pygame.draw.aalines(win, (R,G,B), False, paint_points)

    ### USE THIS DRAW OPTION IF YOUR COMPUTER IS REALLY SLOW!! (insead of the draw option above)
    '''
    for point in paint_points:
        pygame.draw.circle(win, (255,0,0), point, 1)
    '''

    line_1.show(win)
    line_2.show(win)
    swing(line_1, line_2)
    line_1.update()
    line_2.update(line_1)

    paint_points.append(line_2.point2)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONUP:
            g = 2
            r1 = random.randint(50,200)
            r2 = random.randint(50,200)
            a1 = math.pi / random.randint(1,5)
            a2 = math.pi / random.randint(1,5)
            m1 = random.randint(10,40)
            m2 = random.randint(10,40)
            line_1 = Rope(mid, start_y, r1, a1, m1)
            line_2 = Rope(line_1.x2, line_1.y2, r2, a2, m2)
            paint_points = []

    pygame.display.update()
    win.fill((0,0,0))


pygame.quit()