# Example file showing a basic pygame "game loop"
import pygame

# pygame setup
pygame.init()

HEIGHT = 600
WIDTH = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

background=pygame.Surface((WIDTH,HEIGHT))
background.fill((50,50,50))
land = pygame.image.load('assets/PNG/Retina/Tiles/tile_24.png')
TILE_SIZE=land.get_width()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    

    for x in range(0,WIDTH,TILE_SIZE):
        for y in range(0,HEIGHT, TILE_SIZE):
            background.blit(land, (x,y))


    screen.blit(background,(0,0))


    # RENDER YOUR GAME HERE

    # flip() the display to put your work on screen
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()


