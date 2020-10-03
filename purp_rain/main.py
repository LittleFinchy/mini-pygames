import pygame
from pygame.locals import *
from drop import Drop
from umbrella import Umbrella

pygame.init()

win = pygame.display.set_mode((1200,600))
clock = pygame.time.Clock()

RED = (20,0,0)
NUM_OF_DROPS = 1200

pygame.display.set_caption('I only want to see you bathing in the purple rain')

all_drops = []
for i in range(NUM_OF_DROPS):
    all_drops.append(Drop())


umb = Umbrella([i//2 for i in pygame.display.get_surface().get_size()])


show_umb = False
run = True
while run:

    for i in range(NUM_OF_DROPS):
        all_drops[i].fall()
        all_drops[i].show(win)
        all_drops[i].check_umb(umb)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # if event.type == MOUSEBUTTONDOWN:
        #     show_umb = True        
        # if event.type == MOUSEBUTTONUP:
        #     show_umb = False
    
    #if show_umb:
    umb.update()
    umb.show(win)

    pygame.display.update()
    win.fill((0,0,0))


pygame.quit()