import math
import pygame

class Truck():
    def __init__(self, x, y, theta=270,speed=1):
        self.x= x
        self.y= y
        self.speed=speed
        self.degrees= theta #degrees
        self.radians= math.radians(theta)
        self.image= pygame.image.load('assets2/Tiles/tile_0168.png')
    
    def update(self, k):
        if k[pygame.K_UP]:
            x_dot= math.cos(self.radians)*self.speed
            y_dot= math.sin(self.radians)*self.speed
            self.x+= x_dot
            self.y-= y_dot

        if keys[pygame.K_DOWN]:
            x_dot= math.cos(self.radians)*self.speed
            y_dot= math.sin(self.radians)*self.speed
            self.x-= x_dot
            self.y+= y_dot

        if keys[pygame.K_LEFT]:
            self.degrees+= 5  # Rotate left
            self.radians= self.deg_to_rad(self.degrees)  # Update radians

        if keys[pygame.K_RIGHT]:
            self.degrees-= 5  # Rotate right
            self.radians= self.deg_to_rad(self.degrees)

    def blit(self, screen):
        truck= self.image
        screen.blit(truck,self.x,self.y)

