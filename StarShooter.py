import pygame

print('Setup Start')
pygame.init() # Required to initialize Pygame
window = pygame.display.set_mode(size=(600,480))# Window siz

print('Setup End')


print('Loop Start')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()# Close Window
            quit()# End pygame