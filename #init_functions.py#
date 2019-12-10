import pygame
from pygame.locals import *

def drawGrid(width, height, block_size, window):
    background_colour = (0,0,0)
    window.fill(background_colour)
    
    for y in range(width):
        for x in range(height):
            rect = pygame.Rect(x*(block_size + 3), y*(block_size + 3), block_size, block_size)
            pygame.draw.rect(window, (255,255,255), rect)


