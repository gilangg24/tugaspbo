import pygame
from Constants import *

pygame.init()
pygame.font.init()

class Tile():
    font = pygame.font.SysFont(None, 60)
    def  __init__(self, window, tileNumber):
        self.window = window
        self.tileNumber = tileNumber

        surface = pygame.Surface ((SQUARE_WIDTH, SQUARE_HEIGHT))
        if self.tileNumber == STARTING_OPEN_SQUARE_NUMBER: # draw empty image
            surface.fill(WARNA5)
            pygame.draw.rect(surface, WARNA1,
                            pygame.Rect((0, 0, SQUARE_WIDTH, SQUARE_HEIGHT)),
                            2) # black border around everything
        else: # numbered image
            surface.fill(WARNA3)
            pygame.draw.rect(surface, WARNA1,
                            pygame.Rect((0, 0, SQUARE_WIDTH, SQUARE_HEIGHT)),
                            2) # black border around everything
            centerX = SQUARE_WIDTH // 2
            centerY = SQUARE_HEIGHT // 2
            pygame.draw.circle(surface, WARNA4, (centerX, centerY), 35)
            numberAsImage = Tile.font.render(str(self.tileNumber + 1), True, WARNA1)
            widthOfNumber = numberAsImage.get_width()
            leftPos = (SQUARE_HEIGHT - widthOfNumber) // 2
            heightOfNumber = numberAsImage.get_height()