import pygame


class Bird:
    def __init__(self):
        self.x = pygame.display.get_surface().get_size()[0] // 4
        self.y = 0
    
    def update(self):
        pass

    def show(self, win):
        pass