import pygame
import math

class Truck():
    def __init__(self, x, y, theta=270, speed=1):
        self.x = x
        self.y = y
        self.speed = speed
        self.degrees = theta  # degrees
        self.radians = math.radians(theta)
        self.image = pygame.image.load('assets2/Tiles/tile_0168.png')  # Replace with the correct image
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.screen_width = 800
        self.screen_height = 600

    def update(self, k):
        if k[pygame.K_UP]:
            x_dot = math.cos(self.radians) * self.speed
            y_dot = math.sin(self.radians) * self.speed
            self.x += x_dot
            self.y -= y_dot

        if k[pygame.K_DOWN]:
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


        self.x = self.clamp(self.x, self.rect.width // 2, self.screen_width - self.rect.width // 2)
        self.y = self.clamp(self.y, self.rect.height // 2, self.screen_height - self.rect.height // 2)

        # Update the position
        self.rect.center = (self.x, self.y)

    def deg_to_rad(self, degrees):
        return math.radians(degrees)

    def blit(self, screen):
        # Rotate image then blit it
        rotated_image = pygame.transform.rotate(self.image, self.degrees)
        new_rect = rotated_image.get_rect(center=self.rect.center)  
        screen.blit(rotated_image, new_rect.topleft) 

        
    def clamp(self, value, min_value, max_value):
        return max(min_value, min(value, max_value))
