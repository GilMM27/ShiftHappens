import pygame
import os
import sys
import math
from imageDisplay import ImageDisplay
from button import Button
import motionmeter
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('CODICON')
velocity = motionmeter.MotionMeter(screen,100,(200,200),(20,20,20),separation=13,start_value=0,end_value=260,marks=3,title="KM/H")
revolution = motionmeter.MotionMeter(screen,100,(200,500),(20,20,20),separation=7,start_value=0,end_value=7000,marks=2,title="RPM",digit=True)

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

def game_loop():
    screen.fill("#000000")

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
    
    while run:
        if image_display.current_image_index < 6:
            current_gear = image_display.current_image_index
            if car_velocity < MIN_SPEEDS[current_gear] or car_velocity > MAX_SPEEDS[current_gear]: print('No se puede cambiar a esta marcha')
            else:
                if rpm < 7000: rpm += 40
                if rpm > 7000: rpm = 7000
                if rpm == 7000:
                    maxRPMtime += 1
                    if maxRPMtime >100: print('tiempo maximo alcanzado')
                else: maxRPMtime = 0
                car_velocity += rpm * rpm_to_velocity_factor * gear_ratios[current_gear] * (1 - car_velocity / MAX_SPEEDS[current_gear])
            time = 0
        else:
            rpm = 0
            if car_velocity > 0:
                # deceleration_factor = max(0.01, car_velocity / MAX_SPEEDS[current_gear])
                car_velocity -= min(pow(time, 2), 0.05)
                if car_velocity < 0: car_velocity = 0
                time += 0.001
            if breaking == True:
                car_velocity -= 2
                if car_velocity < 0: car_velocity = 0
        print('gear ',current_gear+1, 'RPM:', rpm, 'Velocity:', car_velocity)

        for event in pygame.event.get(): # Evento pa las keys
            if event.type == pygame.KEYDOWN: # Cuando se preciona una tecla
                if event.key == pygame.K_DOWN:
                    index_map = {0: 6, 2: 7, 4: 8, 6: 1, 7: 3, 8: 5}
                    if image_display.current_image_index in index_map:
                        image_display.change_image(index_map[image_display.current_image_index])
                elif event.key == pygame.K_RIGHT:
                    if 6 <= image_display.current_image_index < 8:
                        image_display.change_image(image_display.current_image_index + 1)
                elif event.key == pygame.K_LEFT:
                    if 6 < image_display.current_image_index <= 8:
                        image_display.change_image(image_display.current_image_index - 1)
                elif event.key == pygame.K_UP:
                    index_map = {1: 6, 3: 7, 5: 8, 6: 0, 7: 2, 8: 4}
                    if image_display.current_image_index in index_map:
                        image_display.change_image(index_map[image_display.current_image_index])
                elif event.key == pygame.K_SPACE:
                    breaking = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    if 6 <= image_display.current_image_index <= 8 and not pygame.key.get_pressed()[pygame.K_LEFT] and not pygame.key.get_pressed()[pygame.K_RIGHT]:
                        image_display.change_image(7)
                if event.key == pygame.K_ESCAPE: # Pa cerrar el juego cuando suelte el Escape
                    run = False
                if event.key == pygame.K_SPACE:
                    breaking = False

            if event.type == pygame.QUIT:
                run = False
        velocity.update_Motion(car_velocity)
        revolution.update_Motion(rpm)
        clock.tick(60)
    
        
        #pygame.display.update()
        pygame.display.flip()
    pygame.quit()
main_menu()