import pygame
from pygame.locals import *
from drop import Drop

pygame.init()

win = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()

RED = (255,0,0)

pygame.display.set_caption('This was just a test')


test = Drop()

run = True
while run:
    test.fall()
    test.show(win)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
    win.fill((0,0,0))


pygame.quit()