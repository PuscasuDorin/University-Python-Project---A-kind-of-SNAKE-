from ast import Global
from hmac import new
from tkinter import CENTER, image_names
from turtle import Screen, delay
import pygame
import math
import random
import ctypes
ctypes.windll.user32.SetProcessDPIAware()
from pygame.sprite import Group, Sprite
import time
from pygame import mixer, mixer_music
import Buttons
import Walls
import Food
import Snakes


pygame.init()
mixer.init()

resolutiaEcranului = pygame.display.Info()
screen = pygame.display.set_mode((resolutiaEcranului.current_w, resolutiaEcranului.current_h))

walls_screen = pygame.display.set_mode((1920,1080))

BG = pygame.image.load('grafici/BACKGROUND.png')
background = pygame.transform.scale(BG, (resolutiaEcranului.current_w, resolutiaEcranului.current_h))
bg = pygame.image.load('grafici/bg_menu.png')
bg_menu = pygame.transform.scale(bg, (resolutiaEcranului.current_w, resolutiaEcranului.current_h))
mixer.music.load('Sound/background_music.mp3')
mixer.music.play(loops= -1)


pygame.display.set_caption("A kind of SNAKE")
icon = pygame.image.load('grafici/icon.png')
pygame.display.set_icon(icon)


clock = pygame.time.Clock()
FPS = 7

gap_scale = 50
global level
level = 1
angle = 0
wall_group = pygame.sprite.Group()

yummy_sound = pygame.mixer.Sound('Sound/yummy.mp3')
yak_sound = pygame.mixer.Sound('Sound/yak.mp3')
button_sound = pygame.mixer.Sound('Sound/button_pressed.mp3')

score1 = 0
score2 = 0

startIMG = pygame.image.load('grafici/start.png').convert_alpha()
exitIMG = pygame.image.load('grafici/exit.png').convert_alpha()
menu_but = pygame.image.load('grafici/menu.png').convert_alpha()
menuIMG = pygame.transform.scale(menu_but, (100, 100))
mini = pygame.image.load('grafici/mini_menu.jpg').convert_alpha()
mini_menuIMG = pygame.transform.scale(mini, (800, 900))
mainmenuIMG = pygame.image.load('grafici/mainmenu.png').convert_alpha()
quitIMG = pygame.image.load('grafici/quit.png').convert_alpha()
resumeIMG = pygame.image.load('grafici/resume.png').convert_alpha()
play_img = pygame.image.load('grafici/music_play.png').convert_alpha()
music_playIMG = pygame.transform.scale(play_img, (80, 80))
stop_img = pygame.image.load('grafici/music_stop.png').convert_alpha()
music_stopIMG = pygame.transform.scale(stop_img, (80, 80))
restart_menuu = pygame.image.load('grafici/restart_menu.png').convert_alpha()
restart_menuIMG = pygame.transform.scale(restart_menuu, (800, 500))
restartIMG = pygame.image.load('grafici/restart.png').convert_alpha()
return1 = pygame.image.load('grafici/return.png').convert_alpha()
returnIMG = pygame.transform.scale(return1, (80, 80))

mapsIMG = pygame.image.load('grafici/maps_button.png').convert_alpha()
map1= pygame.image.load('grafici/map1.png').convert_alpha()
map1IMG = pygame.transform.scale(map1, (410, 180))
map2= pygame.image.load('grafici/map2.png').convert_alpha()
map2IMG = pygame.transform.scale(map2, (410, 180))
map3= pygame.image.load('grafici/map3.png').convert_alpha()
map3IMG = pygame.transform.scale(map3, (410, 180))
map4= pygame.image.load('grafici/map4.png').convert_alpha()
map4IMG = pygame.transform.scale(map4, (410, 180))

game_font = pygame.font.Font('Font/PoetsenOne-Regular.ttf',30)

snake1 = Snakes.snake1(random.randint(0,37),random.randint(1,19))

snake2 = Snakes.snake2(random.randint(0,37),random.randint(1,19))


hamburger = Food.hamburger(0,0)   
hamburger.move()


brocoli = Food.brocoli(0,0)   
brocoli.move()


def IsCollision1(xs1, ys1, xh, yh):

    if (int(xs1/gap_scale) == xh) and (int(ys1/gap_scale)+1 == yh):
        return True
    else:
        return False
    
def IsCollision2(xs2, ys2, xb, yb):
    
    if (int(xs2/gap_scale) == xb) and (int(ys2/gap_scale)+1 == yb):
        return True
    else:
        return False
    
def grid(dist_linii):
    left_and_right_border = bx = 10
    up_and_down_border = by = 40
    row = 21 
    col = 38
    for x in range(row):
        pygame.draw.line(screen, (0,0,0), (bx, by+ x*gap_scale), (bx + 1900, by + x * gap_scale))  # horizontal lines
        for y in range(col):
            pygame.draw.line(screen, (0,0,0), (bx + y * gap_scale, by), (bx + y * gap_scale, by + 1000))  # vertical lines
            
font_style = pygame.font.SysFont(None, 50)
font_style2 = pygame.font.SysFont(None, 100)

def message(msg,color):
    mesg = font_style2.render(msg, True, color)
    screen.blit(mesg, [670, 500])
    
def message_mapa1(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg,(290,250))
 
def message_mapa2(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg,(1260,250))
    
def message_mapa3(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg,(290,790))
    
def message_mapa4(msg,color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg,(1260,790))

def draw_score1():
    score_text= str(score1)
    score_surface = game_font.render(score_text,True,(0,0,0))
    score_rect = score_surface.get_rect(center = (60,20))
    hamburger_rect = Food.hamburgerIMG.get_rect(midright = (score_rect.left-5,score_rect.centery))
    
    screen.blit(score_surface,score_rect)
    screen.blit(Food.hamburgerIMG,hamburger_rect)
    
def draw_score2():
    score_text= str(score2)
    score_surface = game_font.render(score_text,True,(0,0,0))
    score_rect = score_surface.get_rect(center = (1900,20))
    brocoli_rect = Food.brocoliIMG.get_rect(midright = (score_rect.left-5,score_rect.centery))
    
    screen.blit(score_surface,score_rect)
    screen.blit(Food.brocoliIMG,brocoli_rect)
    
def level_chose(level):
    world_data = []
    wall_group.empty()
    if level == 1:
        with open('Levels/level1.txt', 'r') as world:
            for line in world:
                world_data.append(line)
            
    if level == 2:
        with open('Levels/level2.txt', 'r') as world:
            for line in world:
                world_data.append(line)
                
    if level == 3:
        with open('Levels/level3.txt', 'r') as world:
            for line in world:
                world_data.append(line)
                
    if level == 4:
        with open('Levels/level4.txt', 'r') as world:
            for line in world:
                world_data.append(line)
        

    for row, tiles in enumerate(world_data):
        for col, tile in enumerate(tiles):
            if tile == '1':
                wall = Walls.walls(col, row)
                wall_group.add(wall)
            


def main_menu():
    menu = True
    music = True   
    music_c = True

    while menu:
        screen.blit(bg_menu, (0,0))
        screen.blit(Snakes.snake1IMG_rescale,(830,180))
        screen.blit(Snakes.snake2IMG_rescale,(970,180))
        start_button = Buttons.Button(550,450,startIMG)
        exit_button = Buttons.Button(1100,450,exitIMG)
        music_play = Buttons.Button(165,95,music_playIMG)
        maps_button = Buttons.Button(850,600,mapsIMG)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                menu = False
                
            if music_play.draw(screen):
                music_c = not music_c
                mixer_music.play(loops=-1)
                
        if music_c == True:
            screen.blit(music_playIMG, (165,95))      
        if music_c == False: 
            mixer_music.stop()
            screen.blit(music_stopIMG, (165,95))
            
        if start_button.draw(screen):
            button_sound.play()
            global score1
            global score2
            score1 = 0
            score2 = 0
            snake1.x = random.randint(0,37)
            snake1.y = random.randint(1,19) + 0.6
            snake2.x = random.randint(0,37)
            snake2.y = random.randint(1,19) + 0.6
            snake1.x1 = 0
            snake1.y1 = 0
            snake2.x2 = 0
            snake2.y2 = 0
            menu = False
            game()
            
                     
        if exit_button.draw(screen):
            button_sound.play()
            menu = False
            pygame.quit()
            
        if maps_button.draw(screen):
            button_sound.play()
            menu = False
            maps_menu()
            
        pygame.display.update()
        
def maps_menu():
    maps= True
    while maps:
        screen.blit(bg_menu, (0,0))
        
        return_button = Buttons.Button(165,900,returnIMG)
        map1 = Buttons.Button(274,180,map1IMG)
        map2 = Buttons.Button(1235,180, map2IMG)
        map3 = Buttons.Button(274,720,map3IMG)
        map4 = Buttons.Button(1235,720, map4IMG)
        
        screen.blit(map1IMG,(274,180))
        screen.blit(map2IMG,(1235,180))
        screen.blit(map3IMG,(274,720))
        screen.blit(map4IMG,(1235,720))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                maps = False
        if return_button.draw(screen):
            button_sound.play()
            time.sleep(0.3)
            maps = False
            quit
            main_menu()
            
        if map1.draw(screen):
            level_chose(1)
            button_sound.play()
            message_mapa1('Map has been selected!', (0,250,0))
            pygame.display.update()
            time.sleep(2)
        if map2.draw(screen):
            level_chose(2)
            button_sound.play()
            message_mapa2('Map has been selected!', (0,250,0))
            pygame.display.update()
            time.sleep(2)
        if map3.draw(screen):
            level_chose(3)
            button_sound.play()
            message_mapa3('Map has been selected!', (0,250,0))
            pygame.display.update()
            time.sleep(2)
        if map4.draw(screen):
            level_chose(4)
            button_sound.play()
            message_mapa4('Mapa a fost selectata!', (0,250,0))
            pygame.display.update()
            time.sleep(2)
            
        pygame.display.update()  
                
        
def in_game_menu():
    mini_menu = True
    music = True   
    music_c = True
    
    while mini_menu:
                
        screen.blit(mini_menuIMG, (550,110))
        
        menu_resume = Buttons.Button(650,250,resumeIMG)
        mainmenu = Buttons.Button(650,500,mainmenuIMG)
        menu_quit = Buttons.Button(650,750,quitIMG)
        music_play = Buttons.Button(580,140,music_playIMG)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mini_menu = False
                
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game()
                    
            if music_play.draw(screen):
                music_c = not music_c
                mixer_music.play(loops=-1)
                
        if music_c == True:
            screen.blit(music_playIMG, (580,140))
        if music_c == False: 
            mixer_music.stop()
            screen.blit(music_stopIMG, (580,140))        

        if menu_resume.draw(screen):
            button_sound.play()
            mini_menu = False
            game()
        if mainmenu.draw(screen):
            button_sound.play()
            mini_menu = False
            time.sleep(0.3)
            main_menu()
            
            
        if menu_quit.draw(screen):
            button_sound.play()
            pygame.quit()
        
        
        pygame.display.update()  
        
def restart_menu():
    rest_menu = True
    while rest_menu:
        screen.blit(restart_menuIMG, (550,250))
        
        restart_button = Buttons.Button(650,280,restartIMG)
        mainmenu = Buttons.Button(650,500,mainmenuIMG)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rest_menu = False
        
        if restart_button.draw(screen):
            button_sound.play()
            global score1
            global score2
            score1 = 0
            score2 = 0
            snake1.x = random.randint(0,37)
            snake1.y = random.randint(1,19) + 0.6
            snake2.x = random.randint(0,37)
            snake2.y = random.randint(1,19) + 0.6
            snake1.x1 = 0
            snake1.y1 = 0
            snake2.x2 = 0
            snake2.y2 = 0
            game()
            
        if mainmenu.draw(screen):
            button_sound.play()
            main_menu()
            
        pygame.display.update()
            
def game():
    run = True
    global level
    print(level)
    while run:
        clock.tick(FPS)
        menu_button = Buttons.Button(900,-30,menuIMG)
                
        screen.blit(background,(0,0))
        
        grid(gap_scale)
        
        if menu_button.draw(screen):
            button_sound.play()
            in_game_menu()
        
        hamburger.update()
        xh= hamburger.x
        yh= hamburger.y
    
        brocoli.update()
        xb= brocoli.x
        yb= brocoli.y
    
        snake1.update() 
        snake1.move()
        xs1= snake1.rect.x
        ys1= snake1.rect.y
   
        snake2.update() 
        snake2.move()
        xs2= snake2.rect.x
        ys2= snake2.rect.y
    
        wall_group.draw(walls_screen)
        
        draw_score1()
        draw_score2()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    in_game_menu()
            

            if event.type == pygame.KEYDOWN:
                print("Snake1 se misca")
                if event.key == pygame.K_a:
                    snake1.x1 = -snake1.miscare
                    snake1.y1 = 0
                    global angle
                    angle = 270
                    snake1.scaled_image = pygame.transform.rotate(Snakes.snake1IMG, 270)
                if event.key == pygame.K_d:
                    snake1.x1 = snake1.miscare
                    snake1.y1 = 0
                    angle = 90
                    snake1.scaled_image = pygame.transform.rotate(Snakes.snake1IMG, 90)
                if event.key == pygame.K_w:
                    snake1.y1 = -snake1.miscare
                    snake1.x1 = 0
                    angle = 180
                    snake1.scaled_image = pygame.transform.rotate(Snakes.snake1IMG, 180)
                if event.key == pygame.K_s:
                    snake1.y1 = snake1.miscare
                    snake1.x1 = 0
                    angle = 0
                    snake1.scaled_image = pygame.transform.rotate(Snakes.snake1IMG, 0)
       
               
            if event.type == pygame.KEYDOWN:
                print("Snake2 se misca")
                if event.key == pygame.K_LEFT:
                    snake2.x2 = -snake2.miscare
                    snake2.y2 = 0
                    angle = 270
                    snake2.scaled_image = pygame.transform.rotate(Snakes.snake2IMG, 270)
                if event.key == pygame.K_RIGHT:
                    snake2.x2 = snake2.miscare
                    snake2.y2 = 0
                    angle = 90
                    snake2.scaled_image = pygame.transform.rotate(Snakes.snake2IMG, 90)
                if event.key == pygame.K_UP:
                    snake2.y2 = -snake2.miscare
                    snake2.x2 = 0
                    angle = 180
                    snake2.scaled_image = pygame.transform.rotate(Snakes.snake2IMG, 180)
                if event.key == pygame.K_DOWN:
                    snake2.y2 = snake2.miscare
                    snake2.x2 = 0
                    angle = 0
                    snake2.scaled_image = pygame.transform.rotate(Snakes.snake2IMG, 0)
                

        

        collision1 = IsCollision1(xs1, ys1, xh, yh)
        if collision1:
            yummy_sound.play()
            global score1
            score1 = score1 + 1
            print(score1)
            hamburger.move()
    
        collision1_2 = IsCollision1(xs1, ys1, xb, yb)
        if collision1_2:
            yak_sound.play()
           
            score1 = score1 - 1
            print(score1)
            brocoli.move()
        
        collision2 = IsCollision2(xs2, ys2, xb, yb)
        if collision2:
            yummy_sound.play()
            global score2
            score2 = score2 + 1
            print(score2)
            brocoli.move()
        
        collision2_2 = IsCollision2(xs2, ys2, xh, yh)
        if collision2_2:
            yak_sound.play()
            score2 = score2 - 1
            print(score2)
            hamburger.move()
            
        if hamburger.x == brocoli.x and hamburger.y == brocoli.y:
            hamburger.move()

        if xs1 == xs2 and ys1 == ys2:
            message('The snakes collided', (183, 28, 28))
            pygame.display.update()
            time.sleep(2)
            restart_menu()
        if snake1.x >= 38 or snake1.x < 0 or snake1.y >= 20.6 or snake1.y < 0:
            message('Red Snake Lost', (183, 28, 28))
            pygame.display.update()
            time.sleep(2)
            restart_menu()
        if snake2.x >= 38 or snake2.x < 0 or snake2.y >= 20.6 or snake2.y < 0:
            message('Green Snake Lost', (183, 28, 28))
            pygame.display.update()
            time.sleep(2)
            restart_menu()
       
        for wall in wall_group:
            col = wall.x + 0.8
            row = wall.y + 0.2
            obj_rect1 = pygame.Rect(xs1, ys1, gap_scale, gap_scale)
            obj_rect2 = pygame.Rect(xs2, ys2, gap_scale, gap_scale)
            wall_rect = wall.rect
  
            if( wall_rect.x-10)/50 == obj_rect1.x/50 and ( wall_rect.y-10)/50 == obj_rect1.y/50:
                if angle == 270:
                    snake1.x1 = 0
                    snake1.x += 1
                if angle == 90:
                    snake1.x1 = 0
                    snake1.x -= 1
                if angle == 180:
                    snake1.y1 = 0
                    snake1.y +=1
                if angle == 0:
                    snake1.y1 = 0
                    snake1.y -= 1
                                
                            
            if( wall_rect.x-10)/50 == obj_rect2.x/50 and ( wall_rect.y-10)/50 == obj_rect2.y/50:
                if angle == 270:
                    snake2.x2 = 0
                    snake2.x += 1
                if angle == 90:
                    snake2.x2 = 0
                    snake2.x -= 1
                if angle == 180:
                    snake2.y2 = 0
                    snake2.y +=1
                if angle == 0:
                    snake2.y2 = 0
                    snake2.y -= 1
                    
            if col == hamburger.x and row == hamburger.y:       
                hamburger.move()
            if col == brocoli.x and row == brocoli.y:       
                brocoli.move()
            
        pygame.display.update()   
        
main_menu()