import pygame
import random
from tkinter import CENTER, image_names
from turtle import Screen
import ctypes
ctypes.windll.user32.SetProcessDPIAware()

pygame.init()
resolutiaEcranului = pygame.display.Info()
screen = pygame.display.set_mode((resolutiaEcranului.current_w, resolutiaEcranului.current_h))
hamburgerIMG = pygame.image.load('grafici/hamburger.png')
brocoliIMG = pygame.image.load('grafici/broccoli.png')
gap_scale = 50

class hamburger:
    def __init__(self, x, y):
        self.x=x
        self.y=y 
        self.image = hamburgerIMG
        self.scaled_image = pygame.transform.scale(self.image,(gap_scale-10, gap_scale-10))
        self.rect = self.scaled_image.get_rect(topleft=(self.x, self.y))
    
    def update(self):
        self.rect.x = self.x * gap_scale+15
        self.rect.y = self.y * gap_scale-5
        screen.blit(self.scaled_image, self.rect)
        
    def move(self):
        self.x = random.randint(0,37)
        self.y = random.randint(1,20)
        

class brocoli:
    def __init__(self, x, y):
        self.x=x
        self.y=y 
        self.image = brocoliIMG
        self.scaled_image = pygame.transform.scale(self.image,(gap_scale-10, gap_scale-10))
        self.rect = self.scaled_image.get_rect(topleft=(self.x, self.y))
    
    def update(self):
        self.rect.x = self.x * gap_scale+15
        self.rect.y = self.y * gap_scale-5
        screen.blit(self.scaled_image, self.rect)
        
    def move(self):
       self.x = random.randint(0,37)
       self.y = random.randint(1,20)



