import sys, pygame
import random
import numpy as np
pygame.init()


def runProgram(grid):
    """
    Runs the map program
    """
    # four times the size of the original map
    map_size = (600, 640)

    black = (0, 0, 0)
    darkgreen = (0, 80, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    pretty_pink = (255, 0, 255)

    # make pygame background
    surface_bg = pygame.display.set_mode(map_size)
    surface_bg.fill(green)

    # add title to pygame window
    pygame.display.set_caption("Amstelhaege")


    #iterate over grid
    #comments magic numbers
    for depth in range(0, 15):
        for width in range(0, 15):
            # draw darkgreen squares for required free space
            if grid[width, depth] == 1:
                pygame.draw.rect(surface_bg, darkgreen, ((width * 4), (depth * 4), 4, 4), 0)
            # draw black squares for small house
            elif grid[width, depth] == 2:
                pygame.draw.rect(surface_bg, black, ((width * 4), (depth * 4), 4, 4), 0)
                pygame.display.update()
            # draw red squares for medium house
            elif grid[width, depth] == 3:
                pygame.draw.rect(surface_bg, red, ((width * 4), (depth * 4), 4, 4), 0)
                pygame.display.update()
            # draw pink squares for large house
            elif grid[width, depth] == 4:
                pygame.draw.rect(surface_bg, pretty_pink, ((width * 4), (depth * 4), 4, 4), 0)
                pygame.display.update()
            # draw blue squares for water
            elif grid[width, depth] == 5:
                pygame.draw.rect(surface_bg, blue, ((width * 4), (depth * 4), 4, 4), 0)
                pygame.display.update()

        pygame.display.update()

    # keep program running until told otherwise               
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
              sys.exit()


# grid = np.zeros((300,320), dtype = int)
# grid[20:60, 20:60] = 3

# runProgram(grid)