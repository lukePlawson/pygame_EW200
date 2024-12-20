#Imports
import pygame
import math
from truck import Truck
import time

# pygame setup # Set up the screen of the game, clock
pygame.init()
HEIGHT = 600
WIDTH = 800 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

#Track display     g is grass,  t is track,     s is water,     f is finish line
log_list=[['g','g','g','g','g','g','g','g','g','g','s','s','s','g','g','g','g','g','g','g','g','g','g','s','s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','g','g','g','g','g','s','s','g','g','g','t','t','g','g','g','g','g','g','g','g','s','s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','g','g','g','g','s','s','g','g','t','t','t','t','t','t','g','g','g','g','g','g','s','s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','f','s','s','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','f','s','s','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','t','t','t','t','t','t','t','g','g','t','t','t','t','t','t','t','f','s','s','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g'],
          ['g','g','g','t','t','t','t','s','g','g','g','g','g','g','s','s','s','g','g','s','s','s','s','g','s','s','s','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','t','g','g','g'],
          ['g','g','g','t','t','t','g','g','s','g','g','g','s','s','s','s','s','s','s','s','g','s','s','s','s','g','s','s','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','t','g','g'],
          ['g','g','g','t','t','t','g','g','s','g','g','s','s','g','t','t','t','g','g','g','g','g','g','s','g','g','g','s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','t','t','g'],
          ['g','g','g','t','s','t','g','g','g','s','s','s','g','t','t','t','t','t','t','t','g','t','g','g','g','g','g','s','s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','g'],
          ['g','g','g','t','s','t','g','g','g','s','g','g','t','t','t','t','t','t','t','t','g','t','t','t','g','g','g','g','s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','t','t','t','t','g'],
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
          ['g','g','g','s','t','s','g','g','g','g','g','g','t','t','t','t','t','g','g','s','s','s','g','g','g','g','s','t','s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','g','s','s','s','s','s'],
          ['g','g','g','s','t','s','g','g','g','g','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','g','t','s','s','g','g','g','g','g','g','g','g','g','g','g','g','g','g','s','s','s','s','s','g','g'],
          ['g','g','g','s','t','s','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','g','t','g','s','s','g','g','g','g','g','g','g','g','g','g','g','g','g','s','s','s','s','s','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','t','g','g','s','s','s','g','g','g','g','g','g','g','g','g','g','g','g','s','s','s','s','s','g','g','g'],
          ['g','g','g','t','t','t','g','g','g','g','g','t','t','t','t','g','g','g','g','g','g','g','g','g','t','g','g','g','s','s','s','s','g','g','g','g','g','g','g','g','g','s','s','s','s','g','g','g','g','g'],
          ['g','g','g','t','s','t','g','g','g','g','g','t','t','t','g','g','g','g','g','g','g','g','g','t','g','g','g','g','g','s','s','s','s','g','g','g','g','g','g','g','s','s','s','s','g','g','g','g','g','g'],
          ['g','g','g','t','s','t','g','g','g','g','t','t','t','t','t','t','t','t','t','t','t','t','t','g','g','g','g','g','g','s','s','s','s','g','g','g','g','g','g','s','s','s','g','g','g','g','g','g','g','g'],
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
background = pygame.Surface((WIDTH, HEIGHT))                    #Creates Surface
background.fill((50, 50, 50))                                   #fills bachgroudn
land = pygame.image.load('assets2/Tiles/tile_0001.png')         #LAND IMAGE
track = pygame.image.load('assets2/Tiles/tile_0130.png')        #TRACK IMAGE
water= pygame.image.load('assets2/Tiles/tile_0037.png')         #WATER IMAGE
TILE_SIZE = land.get_width() #can be called for width or height of tiles b/c squares
black=(0,0,0)                                                   #black color
white=(255,255,255)                                             #white color

#Scenic images
big_rock=pygame.image.load('assets/PNG/Retina/Tiles/tile_66.png')
small_rock=pygame.image.load('assets/PNG/Retina/Tiles/tile_67.png')
bush1=pygame.image.load('assets/PNG/Retina/Tiles/tile_70.png')
bush2=pygame.image.load('assets/PNG/Retina/Tiles/tile_71.png')
bush3=pygame.image.load('assets/PNG/Retina/Tiles/tile_72.png')


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
        'THE BLACK IS THE FINISH LINE',
        '',
        'The grass slows you down, the water does more',
        '',
        'After you press a key a 3 second timer will begin',]
    
    #This will get a font called i_font and render in the instructiuons above blitting them on the screen.
    i_font = pygame.font.Font('assets4/Fonts/Kenney Pixel.ttf',size=30)
    spacing = 30
    for j in range(len(instructions)):
        font_surf = i_font.render(instructions[j], True, white)
        font_rect = font_surf.get_rect()                           #gets the rect
        font_rect.center = (WIDTH//2, spacing+ j*spacing)       #centers it
        screen.blit(font_surf, font_rect)                          #blits to screen

#this will wait for a key to be pressed and then it will quit out pf the screen and move on
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
countdown=['3','2','1',"GO"]


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

#Prints onto the screen the countdown and then delays for a second and disappeares then presenting following code
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
truck = Truck(440, 67)


###############    FInish screen
def gameover(screen, time2):
    font_over=pygame.font.Font('assets4/Fonts/Kenney Pixel.ttf', 50)
    message= f"GAME OVER. Your Time Was {time2:.2f}s"
    m_surf= font_over.render(message, True, white) #can change
    m_rect= m_surf.get_rect(center=(WIDTH//2, HEIGHT//2)) #alwasy this
    screen.blit(m_surf,m_rect)


    file_path = 'highscore.txt' 
    original_high = high_score(file_path)           #Gets high score
    if time2<original_high:                         #If its a new better score 
        message= f"NEW HIGH SCORE: {time2:.2f}s!"           #rewrites and displays
        m_surf= font_over.render(message, True, white)
        screen.blit(m_surf, (WIDTH//2, HEIGHT//2   +50))
        w_high_score(file_path, time2)
    else:
        message= f"Current High Score: {original_high:.2f}s"        #Otherwise it just prints the old one
        m_surf = font_over.render(message, True, white)
        screen.blit(m_surf, (WIDTH // 2, HEIGHT //2  +50)) 
        
    pygame.display.flip()
    pygame.time.delay(5000) #5 seconds

######################## HIGH SCORE or not
def high_score(file_path):
    try:
        with open(file_path, 'r') as file:
            return float(file.read())
    except FileNotFoundError:
        return float(10000) #Returns a beatable score if theres no file

#writes in score 
def w_high_score(file_path, new_high_score):
    with open(file_path, 'w') as file:
        file.write(f"{new_high_score:.2f}")


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
    #SCENIC PIECES
    background.blit(big_rock,(500,350))
    background.blit(small_rock,(-30,-30))
    background.blit(bush1,(80,250))
    background.blit(bush3,(150,500))
    background.blit(bush2,(540,100))

############
    ################ Gives a time information
    time2=(pygame.time.get_ticks()-time1)/1000
    timer= f'{time2:.2f}' #.2 cuts to 2 decimal places
    timer_surface = i_font2.render(timer, True, black)

##############    CONSTANT UPDATES  
    keys = pygame.key.get_pressed()    # Get key presses for truck movement
    screen.blit(background, (0, 0))   #Blits the background
    screen.blit(timer_surface, (620, 500)) #Displays time at a location on the screen
    
    if truck.update(keys,log_list)==True: #Haults game if its on finish
        running=False
        gameover(screen,time2)
    truck.update(keys,log_list)      # Update the truck's position if not on Finish

    truck.blit(screen)     #Blits the truck on the screen
    pygame.display.flip()       #Updates the display
    clock.tick(60)    #Limits FPS to 60
pygame.quit()
