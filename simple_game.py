import pygame
from pygame.locals import *

from init_functions import drawGrid

def main():

    pygame.init()

    screensize = 1000

    width = 7
    height = 7

    block_size = 15

    window = pygame.display.set_mode((screensize, screensize))
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        drawGrid(7, 7, screensize / 8, window)
        
        pygame.display.flip()


main()
