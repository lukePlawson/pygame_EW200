import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y,speed=5):
        self.x=x
        self.y=y
        self.speed=speed
        self.image=pygame.image.load()


    def update():
        