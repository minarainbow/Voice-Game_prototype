import pygame
from pygame.locals import *

from init_functions import drawGrid
from init_functions import initPlayer

def main():

    pygame.init()

    screensize = 1000

    width = 7
    height = 7

    block_size = int((screensize - 3 * max(width, height)) / max(width, height))

    window = pygame.display.set_mode((screensize, screensize))
    done = False

    posX = 0
    posY = 6
    player = initPlayer (block_size, window)
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    posX += 1
                if event.key == pygame.K_LEFT:
                    posX -= 1
                if event.key == pygame.K_UP:
                    posY -= 1
                if event.key == pygame.K_DOWN:
                    posY += 1

        drawGrid(width, height, block_size, window)
        
        position = (posX * (block_size + 3), posY * (block_size + 3))
        window.blit(player, position)
        pygame.display.update()


        pygame.display.flip()


main()
