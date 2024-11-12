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

# Set up background
background = pygame.Surface((WIDTH, HEIGHT))
background.fill((50, 50, 50))
land = pygame.image.load('assets/PNG/Retina/Tiles/tile_24.png')
TILE_SIZE = land.get_width()

# Create a truck instance at position (200, 200)
truck = Truck(200, 200)

# Run the program
running = True
while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with land tiles
    for x in range(0, WIDTH, TILE_SIZE):
        for y in range(0, HEIGHT, TILE_SIZE):
            background.blit(land, (x, y))

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