import pygame
import math

#This class is for the truck and will do all functions related to it
class Truck():
    def __init__(self, x, y, theta=270, speed=19):
        self.x = x
        self.y = y
        self.speed = speed
        self.degrees = theta  # degrees
        self.radians = math.radians(theta) #duh radians
        self.image = pygame.image.load('assets2/Tiles/tile_0168.png')  # Replace with the correct image
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.screen_width = 800
        self.screen_height = 600

    def update(self, k):
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
            self.degrees += 5  # Rotate left
            self.radians = self.deg_to_rad(self.degrees)

        if k[pygame.K_RIGHT]:
            self.degrees -= 5  # Rotate right
            self.radians = self.deg_to_rad(self.degrees)

        #clamps the truck to only allow values on the screen size
        self.x = self.clamp_screen(self.x, self.rect.width//2, self.screen_width-self.rect.width//2)
        self.y = self.clamp_screen(self.y, self.rect.height//2, self.screen_height-self.rect.height//2)

        # Update the position
        self.rect.center = (self.x, self.y)

    #can be called in other methods to access a new updated radians value
    def deg_to_rad(self, degrees):
        return math.radians(degrees)

    def blit(self, screen):# blits and rotates
        rotated_image = pygame.transform.rotate(self.image, self.degrees)
        new_rect = rotated_image.get_rect(center=self.rect.center)  
        screen.blit(rotated_image, new_rect.topleft) 

    #sets and returns value to be called with the update function above
    def clamp_screen(self, value, min_val, max_val):
        return max(min_val, min(value, max_val))
