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
log_list=[['g','g','g','g','g','g','g','g','g','g','s','s','s','g','g','g','g','g','g','g','g','g','g','s','s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','g','g','g','g','g','s','s','g','g','g','t','t','g','g','g','g','g','g','g','g','s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','g','g','g','g','s','s','g','g','t','t','t','t','t','t','g','g','g','g','g','g','s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','f','s','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','f','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','t','t','t','t','t','t','t','g','g','t','t','t','t','t','t','t','f','s','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','s','g','g','g','g','g','g','s','s','s','g','g','s','s','s','g','g','s','s','s','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','t','g','g','g'],
          ['g','g','g','t','t','t','g','g','s','g','g','g','s','s','s','s','s','s','s','s','g','s','s','s','s','g','s','s','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','g','g'],
          ['g','g','g','t','t','t','g','g','s','g','g','s','s','g','t','t','t','g','g','g','g','g','g','g','g','g','g','s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','g'],
          ['g','g','g','t','s','t','g','g','g','s','s','s','g','t','t','t','t','t','t','t','t','t','g','g','g','g','g','s','s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','g'],
          ['g','g','g','t','s','t','g','g','g','s','g','g','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','g'],
          ['g','g','g','t','t','t','g','g','g','s','s','s','t','t','t','t','t','t','t','t','g','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','s','t','t','t','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','g','g'],
          ['g','g','g','s','t','s','g','g','g','g','g','s','t','t','t','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','t','t','t','t','g','g','g'],
          ['g','g','g','s','t','s','g','g','g','g','g','s','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','s','g','t','t','t','t','t','t','g','g','g','g','t','t','t','t','t','t','g','g','g','g'],
          ['g','g','g','s','t','s','g','g','g','g','g','s','s','t','t','t','t','g','g','g','g','g','g','g','g','g','g','s','s','g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','s','g','g','t','t','t','g','g','g','g','s','s','s','g','s','s','g','g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','s','s','g','g','t','t','t','g','g','g','s','s','s','s','s','g','g','g','g','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','g','t','g','g','g','g','g','g','g','s','g','g','t','t','t','t','g','g','g','s','s','s','s','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','g','t','g','g','g','g','g','g','g','s','s','t','t','t','t','t','g','g','s','s','s','s','s','g','g','g','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','g','g','t','t','t','t','t','g','g','g','s','s','s','s','s','g','g','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','s','s'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','g','t','t','t','t','t','s','s','g','s','s','s','s','s','s','s','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','s','s','s','s'],
          ['g','g','g','s','t','s','g','g','g','g','g','g','t','t','t','t','t','g','g','s','s','s','g','g','g','g','s','g','s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','s','s','s','s','s'],
          ['g','g','g','s','t','s','g','g','g','g','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','g','t','s','s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','s','s','s','s','s','g','g'],
          ['g','g','g','s','t','s','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','t','g','s','s','g','g','g','g','g','g','g','g','g','g','g','g','g','s','s','s','s','s','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','t','g','g','s','s','s','g','g','g','g','g','g','g','g','g','g','g','g','s','s','s','s','s','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','t','g','g','g','s','s','s','s','g','g','g','g','g','g','g','g','g','s','s','s','s','g','g','g','g','g'],
          ['g','g','g','t','s','t','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','t','g','g','g','g','g','s','s','s','s','g','g','g','g','g','g','g','s','s','s','s','g','g','g','g','g','g'],
          ['g','g','g','t','s','t','g','g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','s','s','s','s','g','g','g','g','g','g','s','s','s','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','s','s','s','g','g','s','s','s','s','s','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','t','g','g','g','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','s','s','s','s','s','s','s','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','s','s','s','s','s','s','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g',],
          ['s','s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g',],
          ['s','s','s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g',],          
          ]
#Set up background
background = pygame.Surface((WIDTH, HEIGHT))
background.fill((50, 50, 50))
land = pygame.image.load('assets2/Tiles/tile_0001.png')
track = pygame.image.load('assets2/Tiles/tile_0130.png')
water= pygame.image.load('assets2/Tiles/tile_0037.png')
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
countdown=['2','1',"GO"]
#"10",'9','8','7','6','5','4','3',
def countdown_screen(screen, i_font2):
    screen.fill(black)
    spacing=45

    for j in range(len(countdown)):
        font_surf2 = i_font2.render(countdown[j], True, white)
        font_rect2 = font_surf2.get_rect()                           #gets the rect
        font_rect2.center = (WIDTH//2, spacing+ j*spacing)           #centers it
        screen.blit(font_surf2, font_rect2)                          #blits to screen

        pygame.time.delay(1000)
        pygame.display.update()

flagger=1
i_font2 = pygame.font.Font('assets4/Fonts/Kenney Pixel.ttf',size=100)
while flagger:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    countdown_screen(screen, i_font2)
    flagger=0
    

#Create a truck at the Start line of the track
truck = Truck(410, 67)

################## GAME LOOP ####################################################
##############################################################################
#Run the program to display and update pygame
running = True
time1=pygame.time.get_ticks()
time2=0
while running:
    #Poll for events
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
            elif tile== 's':
                background.blit(water,(x*TILE_SIZE, y*TILE_SIZE))
            else:
                None

############
    ################ Gives a time information
    time2=(pygame.time.get_ticks()-time1)/1000
    timer= f'{time2:.2f}' #.2 cuts to 2 decimal places
    timer_surface = i_font2.render(timer, True, black)

##############    CONSTANT UPDATES    
    keys = pygame.key.get_pressed()    # Get key presses for truck movement
    screen.blit(background, (0, 0))   #Blits the background
    screen.blit(timer_surface, (620, 500)) #Displays time at a location on the screen
    truck.update(keys,log_list)      # Update the truck's position
    truck.blit(screen)     #Blits the truck on the screen
    pygame.display.flip()       #Updates the display
    clock.tick(60)    #Limits FPS to 60






pygame.quit()


