import pygame
from pygame.locals import *
from stick import Stick


pygame.init()

win = pygame.display.set_mode((1200,600))
NUM_OF_STICKS = 100
stick_spacing = pygame.display.get_surface().get_size()[0] // NUM_OF_STICKS

sticks = []
for i in range(NUM_OF_STICKS):
    sticks.append(Stick(i*stick_spacing, stick_spacing/2))

run = True
while run:

    for i in range(len(sticks)):
        #sticks[-i].color = (50,205,50)
        for j in range(len(sticks) - i - 1):
            if sticks[j] > sticks[j+1]:
                sticks[j+1].color = (50,205,50)
                sticks[j].h, sticks[j+1].h = sticks[j+1].h, sticks[j].h

                for stick in sticks:
                    stick.show(win)
                pygame.display.update()
                win.fill((0,0,0))
                sticks[j+1].color = (155,0,0)


    for stick in sticks:
        stick.show(win)


    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.display.update()
    win.fill((0,0,0))


pygame.quit()