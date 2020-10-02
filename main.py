import pygame
from pygame.locals import *
from drop import Drop

pygame.init()

win = pygame.display.set_mode((1200,600))
clock = pygame.time.Clock()

RED = (20,0,0)
NUM_OF_DROPS = 1200

pygame.display.set_caption('I only want to see you bathing in the purple rain')

all_drops = []
for i in range(NUM_OF_DROPS):
    all_drops.append(Drop())

run = True
while run:

    for i in range(NUM_OF_DROPS):
        all_drops[i].fall()
        all_drops[i].show(win)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    win.fill(RED)


pygame.quit()