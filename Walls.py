import pygame
import random


wallIMG = pygame.image.load('grafici/wall.png')
gap_scale = 50

class walls(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        
        self.x = x+0.2
        self.y = y+0.8
        self.image = wallIMG
        self.scaled_image= pygame.transform.scale(self.image,(gap_scale, gap_scale))
        self.rect = self.scaled_image.get_rect()
        
        self.rect.x = self.x * gap_scale
        self.rect.y = self.y * gap_scale