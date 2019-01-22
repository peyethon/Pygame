import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption('Simmy')
running = True
FPS = 60
clock = pygame.time.Clock()


def update():
    pass


def draw():
    pass


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()

    update()
    draw()

    clock.tick(FPS)
    pygame.display.update()
