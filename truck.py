import pygame
import math

#This class is for the truck and will do all functions related to it
class Truck():
    def __init__(self, x, y, theta=0, speed=1):
        self.x = x
        self.y = y
        self.speed = speed
        self.degrees = theta  # degrees
        self.radians = math.radians(theta) #radians 
        self.image = pygame.transform.rotozoom(pygame.image.load('assets5/PNG/Cars/car_blue_small_3.png'),-90,.35)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.screen_width = 800
        self.screen_height = 600
        self.tile_size=16 #size of grass and track width /heught

    def update(self, k, log_list):
        ####For checkingh grass/track/water ##########
        #Checks the truck to see if its on grass track or water
        tile_x = int(self.x // self.tile_size)
        tile_y = int(self.y // self.tile_size)
        if self.on_grass(tile_x, tile_y, log_list):
            self.speed = 0.1 #speed grass
        elif self.on_water(tile_x, tile_y, log_list):
            self.speed = 0.005 #speed water
        else:
            self.speed = .5 #Normal speed

        ###CHECKS FOR FINISH
        if self.on_finish(tile_x, tile_y, log_list):
            return True

        ### for checking key movements
        if k[pygame.K_UP]: #Move forward
            x_dot = math.cos(self.radians) * self.speed
            y_dot = math.sin(self.radians) * self.speed
            self.x += x_dot
            self.y -= y_dot

        if k[pygame.K_DOWN]: #Move back
            x_dot = math.cos(self.radians) * self.speed
            y_dot = math.sin(self.radians) * self.speed
            self.x -= x_dot
            self.y += y_dot

        if k[pygame.K_LEFT]:
            self.degrees += 3  # Rotate left
            self.radians = self.deg_to_rad(self.degrees)

        if k[pygame.K_RIGHT]:
            self.degrees -= 3 # Rotate right
            self.radians = self.deg_to_rad(self.degrees)


        #clamps the truck to only allow values on the screen size. 
        self.x = self.clamp_screen(self.x, self.rect.width//2, self.screen_width-self.rect.width//2)
        self.y = self.clamp_screen(self.y, self.rect.height//2, self.screen_height-self.rect.height//2)

        # Update the position
        self.rect.center = (self.x, self.y)

    #THE TWO CLAMP PIECES ... the clamp_ screen returns the max of the min val 
    #and the min returns the smaller of the value and max value
    #the self x is taken in abover and it runs the clmap_screen, passes in the 
    # x and y then this sets their values to stay in the screen
    #Bceause we are at the center of the car, the //2 makes sure that the center cant reach the edge, but only the edge can


    #sets and returns value to be called with the update function above
    def clamp_screen(self, value, min_val, max_val):
        return max(min_val, min(value, max_val))
    
    #can be called in other methods to access a new updated radians value
    def deg_to_rad(self, degrees):
        return math.radians(degrees)

    def blit(self, screen):# blits and rotates
        rotated_image = pygame.transform.rotate(self.image, self.degrees)
        new_rect = rotated_image.get_rect(center=self.rect.center)  
        screen.blit(rotated_image, new_rect.topleft) 
    

    #The next 3 functions will identify the tile the center of the car is on through the log list
    #They take the log list and tiles     if (tile y is greater or = to 0 and less than the last y tile) and x is under the same conditions
    # the tile is taken and the tiles actual letter gets returned

    def on_grass(self, tile_x, tile_y, log_list):
    #Check if the current tile is 'g'
        if (tile_y >= 0 and tile_y < len(log_list)) and (tile_x >= 0 and tile_x < len(log_list[tile_y])):
            tile = log_list[tile_y][tile_x]
            return tile == 'g'  # True if it's grass
        return False
    
    def on_water(self, tile_x, tile_y, log_list):
    #Check if the current tile is 's'
        if (tile_y >= 0 and tile_y < len(log_list)) and (tile_x >= 0 and tile_x < len(log_list[tile_y])):
            tile = log_list[tile_y][tile_x]
            return tile == 's'  # True if it's water
        return False
    

    def on_finish(self, tile_x, tile_y, log_list):
    #Check if the current tile is 'f'
        if (tile_y >= 0 and tile_y < len(log_list)) and (tile_x >= 0 and tile_x < len(log_list[tile_y])):
            tile = log_list[tile_y][tile_x]
            return tile == 'f'  #True if it's finish line
        return False
