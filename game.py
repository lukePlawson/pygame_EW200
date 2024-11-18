import pygame
import math
from truck import Truck

# pygame setup
pygame.init()

# Set up the screen of the game, clock
HEIGHT = 600
WIDTH = 800 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#new screen alteration
log_list=[['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','t','t','t','t','t','t','t','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','t','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','g','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','t','t','t','t','t','t','t','t','g','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','t','t','t','t','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','g','g','g','g','t','t','t','t','t','t','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','g','g','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','g','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','t','t','t','t','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g',],
          ['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g',],
          ['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g',],          
          ]

# Set up background
background = pygame.Surface((WIDTH, HEIGHT))
background.fill((50, 50, 50))
land = pygame.image.load('assets2/Tiles/tile_0001.png')
track = pygame.image.load('assets2/Tiles/tile_0130.png')
TILE_SIZE = land.get_width() #can be called for width or height of tiles b/c squares

# Create a truck instance at position Start of the track
truck = Truck(200, 200)

# Run the program
running = True
while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



    # Fill background tiles based on log_list above
    for y in range(len(log_list)):  
        for x in range(len(log_list[y])):
            tile = log_list[y][x]
            # if statements to blit land or track tiles
            if tile == 'g':
                background.blit(land,(x*TILE_SIZE, y*TILE_SIZE))
            elif tile == 't':
                background.blit(track,(x*TILE_SIZE, y*TILE_SIZE))

    # Get key presses for truck movement
    keys = pygame.key.get_pressed()

    # Update the truck's position based on keys
    truck.update(keys)

    # Clear the screen and draw everything
    screen.blit(background, (0, 0))  # Redraw the background

    # Render the truck on the screen
    truck.blit(screen)

    # Update the display
    pygame.display.flip()

    # Limit FPS to 60
    clock.tick(60)

# Quit pygame
pygame.quit()