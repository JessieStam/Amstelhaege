import pygame
pygame.init()


GREEN = (100, 200, 200)

DISPLAYSURF = pygame.display.set_mode((1024, 768), 0, 32)
DISPLAYSURF.fill(GREEN)
pygame.draw.rect(DISPLAYSURF, GREEN, (10, 30, 150, 160))

pygame.time.delay(10000) 