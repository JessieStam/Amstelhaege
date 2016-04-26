import sys, pygame
pygame.init()

size = (0, 0)

green = (0, 255, 0)
blue = (0, 0, 255)


#make background
surface_bg = pygame.display.set_mode(size)
surface_bg.fill(green)

pygame.display.update()

pygame.draw.rect(surface_bg, blue, (15, 15, 30, 30), 0)

pygame.display.update()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
        	sys.exit()