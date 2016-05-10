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

    yellow = (255, 255, 0)
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
    for depth in range(0, 320):
        for width in range(0, 300):
            # draw darkgreen squares for required free space
            # changed depth and with positions, because orientation was off
            if grid[depth, width] == 1:
                pygame.draw.rect(surface_bg, darkgreen, ((width * 2), (depth * 2), 2, 2), 0)
            # draw yellow squares for small house
            elif grid[depth, width] == 2:
                pygame.draw.rect(surface_bg, yellow, ((width * 2), (depth * 2), 2, 2), 0)
                pygame.display.update()
            # draw red squares for medium house
            elif grid[depth, width] == 3:
                pygame.draw.rect(surface_bg, red, ((width * 2), (depth * 2), 2, 2), 0)
                pygame.display.update()
            # draw pink squares for large house
            elif grid[depth, width] == 4:
                pygame.draw.rect(surface_bg, pretty_pink, ((width * 2), (depth * 2), 2, 2), 0)
                pygame.display.update()
            # draw blue squares for water
            elif grid[depth, width] == 5:
                pygame.draw.rect(surface_bg, blue, ((width * 2), (depth * 2), 2, 2), 0)
                pygame.display.update()

        pygame.display.update()

    # pygame.image.save(img, "image.jpg")    

    # keep program running until told otherwise               
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
              sys.exit()


# grid = np.zeros((300,320), dtype = int)
# grid[20:60, 20:60] = 3

# runProgram(grid)