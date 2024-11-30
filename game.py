#Imports
import pygame
import math
from truck import Truck
import time

# pygame setup
pygame.init()

# Set up the screen of the game, clock
HEIGHT = 600
WIDTH = 800 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#Track display
log_list=[['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','t','t','t','t','t','t','t','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','t','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','g'],
          ['g','g','g','t','g','t','g','g','g','g','g','g','g','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','g'],
          ['g','g','g','t','g','t','g','g','g','g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','t','t','t','t','t','t','t','t','g','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','g','g'],
          ['g','g','g','g','t','g','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','t','t','t','t','g','g','g'],
          ['g','g','g','g','t','g','g','g','g','g','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','g','g','g','g','t','t','t','t','t','t','g','g','g','g'],
          ['g','g','g','g','t','g','g','g','g','g','g','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','g','t','g','g','g','g','g','g','g','g','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','g','t','g','g','g','g','g','g','g','g','g','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','g','g','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','g','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','t','g','g','g','g','g','g','g','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','t','g','g','g','g','g','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','t','g','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','t','t','t','t','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','g','t','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','g','t','g','g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','t','g','g','g','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g',],
          ['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g',],
          ['g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g',],          
          ]
#Set up background
background = pygame.Surface((WIDTH, HEIGHT))
background.fill((50, 50, 50))
land = pygame.image.load('assets2/Tiles/tile_0001.png')
track = pygame.image.load('assets2/Tiles/tile_0130.png')
TILE_SIZE = land.get_width() #can be called for width or height of tiles b/c squares
print(TILE_SIZE)
black=(0,0,0)
white=(255,255,255)

##############Instructions screen #################################################
def instructions(screen):
    screen.fill(black) #Makes screen black
    instructions = [
        'The up arrow key move your truck forward',
        'The down arrow key move your truck backwards',                     #Displays on screen
        'The right arrow key rotates your truck right',
        'The left arrow key rotates your truck left',
        '',
        'Go around the track in the fastest time possible',
        '',
        'The grass slows you down',
        '',
        'After you press a key a 10 second timer will begin',]
    

    i_font = pygame.font.Font('assets4/Fonts/Kenney Pixel.ttf',size=30)
    spacing = 30
    for j in range(len(instructions)):
        font_surf = i_font.render(instructions[j], True, white)
        font_rect = font_surf.get_rect()                           #gets the rect
        font_rect.center = (WIDTH//2, spacing+ j*spacing)       #centers it
        screen.blit(font_surf, font_rect)                          #blits to screen

flag=1
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            flag = 0
        if event.type == pygame.KEYDOWN: #when any key gets pressed we leave the loop
            flag = 0

    instructions(screen)
    pygame.display.flip()
##########################################
################    Starts Countdown #############
#Countdown for the race
countdown=["10",'9','8','7','6','5','4','3','2','1',"... wont display"]

screen.fill(black)
spacing=45
flagger=1
while flagger:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    i_font2 = pygame.font.Font('assets4/Fonts/Kenney Pixel.ttf',size=100)
    for j in range(len(countdown)):
        font_surf2 = i_font2.render(countdown[j], True, white)
        font_rect2 = font_surf2.get_rect()                           #gets the rect
        font_rect2.center = (WIDTH//2, spacing+ j*spacing)                     #centers it
        screen.blit(font_surf2, font_rect2)                          #blits to screen

        pygame.time.delay(1000)
        pygame.display.update()
    
    flagger=0
    

#Create a truck at the Start line of the track
truck = Truck(410, 67, log_list)

################## GAME LOOP ####################################################
#Run the program to display and update pygame
running = True
while running:
    # Poll for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

#############   BACKGROUND
    #Fill background tiles based on log_list above
    for y in range(len(log_list)):  
        for x in range(len(log_list[y])):
            tile = log_list[y][x]
            # if statements to blit land or track tiles
            if tile == 'g':
                background.blit(land,(x*TILE_SIZE, y*TILE_SIZE))
            elif tile == 't':
                background.blit(track,(x*TILE_SIZE, y*TILE_SIZE))

############


##############    CONSTANT UPDATES    
    keys = pygame.key.get_pressed()    # Get key presses for truck movement
    truck.update(keys)      # Update the truck's position
    screen.blit(background, (0, 0))   #Blits the truck on the screen
    truck.blit(screen)     #Blits the truck on the screen
    pygame.display.flip()       #Updates the display
    clock.tick(60)    #Limits FPS to 60

pygame.quit()
