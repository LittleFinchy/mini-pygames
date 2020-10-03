import pygame
from pygame.locals import *
from stick import Stick


pygame.init()

win = pygame.display.set_mode((1200,600))
NUM_OF_STICKS = 100

sticks = []

run = True
while run:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    test.show(win)

    pygame.display.update()
    win.fill((0,0,0))


pygame.quit()