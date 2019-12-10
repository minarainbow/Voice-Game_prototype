import pygame
from pygame.locals import *

from init_functions import drawGrid
from init_functions import initPlayer

def main():

    pygame.init()

    screensize = 1000

    width = 7
    height = 7

    block_size = int(screensize / 8)

    window = pygame.display.set_mode((screensize, screensize))
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        drawGrid(7, 7, block_size, window)
        player = initPlayer(width, height, block_size, window)
        
        pygame.display.flip()


main()
