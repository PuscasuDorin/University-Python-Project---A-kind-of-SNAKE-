import pygame
import random
from tkinter import CENTER, image_names
from turtle import Screen
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

pygame.init()
resolutiaEcranului = pygame.display.Info()
screen = pygame.display.set_mode((resolutiaEcranului.current_w, resolutiaEcranului.current_h))

gap_scale = 50

snake1IMG = pygame.image.load('grafici/snake1.png')
snake1IMG_rescale = pygame.transform.scale(snake1IMG, (120, 120))
snk1 = pygame.transform.rotate(snake1IMG, 0)

snake2IMG = pygame.image.load('grafici/snake2.png')
snake2IMG_rescale = pygame.transform.scale(snake2IMG, (120, 120))
snk2 = pygame.transform.rotate(snake2IMG, 0)


class snake1:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y + 0.6
        self.image = snk1
        self.scaled_image = pygame.transform.scale(self.image,(gap_scale, gap_scale))
        self.rect = self.scaled_image.get_rect(topleft=(self.x, self.y))
         
        self.miscare = 1
        self.x1 = 0
        self.y1 = 0
    
    def update(self):
        self.rect.x = self.x * gap_scale
        self.rect.y = self.y * gap_scale
        screen.blit(self.scaled_image, self.rect)
      
    def move(self):
        self.x += self.x1
        self.y += self.y1  
        
class snake2:
    
    score2 = 0
    def __init__(self, x, y):
        self.x = x
        self.y = y + 0.6
        self.image = snk2
        self.scaled_image = pygame.transform.scale(self.image,(gap_scale, gap_scale))
        self.rect = self.scaled_image.get_rect(topleft=(self.x, self.y))
         
        self.miscare = 1
        self.x2 = 0
        self.y2 = 0
    
    def update(self):
        self.rect.x = self.x * gap_scale
        self.rect.y = self.y * gap_scale
        screen.blit(self.scaled_image, self.rect)
        
      
    def move(self):
        self.x += self.x2
        self.y += self.y2 