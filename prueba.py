import pygame
import os
import sys
import math
from imageDisplay import ImageDisplay
import numpy as np
from button import Button
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('CODICON')

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/BlackHanSans-Regular.ttf", size)

def main_menu():
    while True:
        screen.fill("#000000")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(85).render("SHIFT HAPPENS", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250), text_input="PLAY", font=get_font(60), base_color="white", hovering_color="gray")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400), text_input="OPTIONS", font=get_font(60), base_color="white", hovering_color="gray")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), text_input="QUIT", font=get_font(60), base_color="white", hovering_color="gray")

        screen.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    game_loop()
                # if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    # options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

x = []
y = []

A = 1.2
B = -1.4
C = -1.6

def function(x):
    fx = A*math.pow(x,3) + B*math.pow(x,2) + C*x
    return fx

def generate_table(start, end, step):
    i = start
    while i <= end:
        x.append(i)
        y.append(function(i))
        i+=step

def initial_points(x,y,x_size,y_size,trans_size,start):
    new_x = x[(start+trans_size)//2]
    new_y = y[(start+trans_size)//2]
    x_transformed = []
    y_transformed = []
    ratio_x = (x_size/2) - new_x
    ratio_y = (y_size/2) - new_y
    for i in range (0,len(x)):
        x_transformed.append(x[i]+ratio_x)
        y_transformed.append(y[i]+ratio_y)
    return x_transformed, y_transformed

x =[]
y= []
def draw_pista(point):
    trans_size = 1000
    if x == []:
        try:
            A= random.uniform(-3.0,-0.7)
            B= random.uniform(-2,1.4)
            C= random.uniform(0.9,2.0)
            # A = -1.89
            # B= -0.64
            # C= 1.88
            print(f"A: {A}, B: {B}, C: {C}")
            end = (-B + math.sqrt(math.pow(B,2)-4*A*C))/(2*A)
            start = (-B - math.sqrt(math.pow(B,2)-4*A*C))/(2*A)
        except: 
            print("Error")
        generate_table(end, start, (start-end)/trans_size)
        print(len(x),len(y))
        global scale
        scale = random.randint(2000,5000)
    
    x_i,y_i =initial_points(np.dot(x,scale),np.dot(y,scale),1280,720,int(trans_size*.1),point)
    for i in range(2,len(x_i)-20):
        if x_i[i] > 0 and x_i[i] <1280:
            #pygame.draw.line(screen, [255,255,255], [x_i[i],y_i[i]],[x_i[i+1],y_i[i+1]],500)
            pygame.draw.circle(screen, [40,40,40], [x_i[i],y_i[i]], 200)
            
    for i in range(2,len(x_i)-20):
        if x_i[i] > 0 and x_i[i] <1280:
            #pygame.draw.line(screen, [255,255,255], [x_i[i],y_i[i]],[x_i[i+1],y_i[i+1]],500)
            pygame.draw.circle(screen, [255,255,255], [x_i[i],y_i[i]], 5)
            
            # pygame.draw.line(screen, [255,255,255], prueba_lado(x_i[i-2],y_i[i-2],x_i[i-1],y_i[i-1],200,True),prueba_lado(x_i[i-1],y_i[i-1],x_i[i],y_i[i],200,True))
            # pygame.draw.line(screen, [255,255,255], prueba_lado(x_i[i-2],y_i[i-2],x_i[i-1],y_i[i-1],200,False),prueba_lado(x_i[i-1],y_i[i-1],x_i[i],y_i[i],200,False))
                    
def prueba_lado(x1,y1,x2,y2,sep,side):
    m  = math.pow((x2-x1),2)+ math.pow((y2-y1),2)
    angle = math.atan2(sep,(math.sqrt(m)))
    d= math.sqrt(m+(math.pow(sep,2)))
    if side:
        xf = x1 + d*math.cos(angle)
        yf = y1 + d*math.sin(angle)
    else:
        xf = x1 + d*math.cos(-angle)
        yf = y1 + d*math.sin(-angle)
    return (xf,yf)



        

    

def game_loop():

    # Create an instance of the ImageDisplay class
    image_display = ImageDisplay(screen)
    image_display.show_image()

    # Car properties
    car_velocity = 0  # Velocidad inicial del automóvil en km/h
    current_gear = 0  # Marcha actual
    rpm = 0  # RPM inicial
    rpm_to_velocity_factor = 0.00007  # Factor de conversión de RPM a velocidad
    gear_ratios = [3.5, 3, 2.5, 2, 1.5, 1]  # Relaciones de marcha para las marchas 1 a 5
    MAX_SPEEDS = [60, 100, 140, 180, 220, 260]  # Velocidades máximas para cada marcha en km/h
    MIN_SPEEDS = [0, 40, 80, 120, 150, 170]  # Velocidades mínimas para cada marcha en km/h

    # Clock for controlling the frame rate
    clock = pygame.time.Clock()
    maxRPMtime = 0
    
    breaking = False
    run = True

    carSizeX = 50
    carSizeY = 100
    # pygame.draw.rect(screen, [255,255,255], [1280/2-carSizeX/2, 720/2-carSizeY/2, carSizeX, carSizeY], 4)
    car = pygame.image.load("assets/carStolenAsset.png").convert_alpha()
    car = pygame.transform.scale(car, (carSizeX, carSizeY))
    cagada = 0
    while run:

        screen.fill("#000000")
        
        draw_pista(cagada)
        pygame.draw.circle(screen, [255,255,255], [1280//2, 720//2], 10)
        cagada+=1
        print(cagada)
        clock.tick(60)
    
        # image_display.show_image(image_display.current_image_index, pygame.math.Vector2(950, 400))
        image_display.show_image()
        #pygame.display.update()f
        pygame.display.flip()
    pygame.quit()
main_menu()