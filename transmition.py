import pygame
import os
import sys
import math
from imageDisplay import ImageDisplay
from button import Button

pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('CODICON')

mode = 'medium' # Default mode

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/BlackHanSans-Regular.ttf", size)

def main_menu():
    while True:
        screen.fill("#000000")

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(85).render("SHIFT HAPPENS", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))
        MODE_TEXT = get_font(60).render(f"MODE: {mode.upper()}", True, "#b68f40")
        MODE_RECT = MODE_TEXT.get_rect(center=(640, 200))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 375), text_input="PLAY", font=get_font(60), base_color="white", hovering_color="gray")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(1067, 600), text_input="OPTIONS", font=get_font(60), base_color="white", hovering_color="gray")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), text_input="QUIT", font=get_font(60), base_color="white", hovering_color="gray")

        screen.blit(MENU_TEXT, MENU_RECT)
        screen.blit(MODE_TEXT, MODE_RECT)

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
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


def options():
    global mode
    run = True
    while run:
        screen.fill("#000000")

        OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

        OPTIONS_TEXT = get_font(85).render("OPTIONS", True, "#b68f40")
        OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 100))

        BACK_BUTTON = Button(image=pygame.image.load("assets/Back Rect.png"), pos=(640, 550), text_input="BACK", font=get_font(60), base_color="white", hovering_color="gray")
        KEY_BINDINGS_BUTTON = Button(image=pygame.image.load("assets/Key Rect.png"), pos=(1067, 100), text_input="KEYS", font=get_font(60), base_color="white", hovering_color="gray")
        EASY_BUTTON = Button(image=pygame.image.load("assets/Level Rect.png"), pos=(213, 350), text_input="EASY", font=get_font(60), base_color="#b68f40", hovering_color="#8a6d31")
        MEDIUM_BUTTON = Button(image=pygame.image.load("assets/Level Rect.png"), pos=(640, 350), text_input="MEDIUM", font=get_font(60), base_color="#b68f40", hovering_color="#8a6d31")
        DIFICULT_BUTTON = Button(image=pygame.image.load("assets/Level Rect.png"), pos=(1067, 350), text_input="DIFICULT", font=get_font(60), base_color="#b68f40", hovering_color="#8a6d31")


        screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

        BACK_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        BACK_BUTTON.update(screen)
        KEY_BINDINGS_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        KEY_BINDINGS_BUTTON.update(screen)
        EASY_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        EASY_BUTTON.update(screen)
        MEDIUM_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        MEDIUM_BUTTON.update(screen)
        DIFICULT_BUTTON.changeColor(OPTIONS_MOUSE_POS)
        DIFICULT_BUTTON.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    run = False
                if KEY_BINDINGS_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    key_bindings()
                if EASY_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    mode = 'easy'
                    run = False
                if MEDIUM_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    mode = 'medium'
                    run = False
                if DIFICULT_BUTTON.checkForInput(OPTIONS_MOUSE_POS):
                    mode = 'dificult'
                    run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        pygame.display.update()
    main_menu()

def level():
    global mode
    if mode == 'easy':
        aumentoRPM = 10
    elif mode == 'medium':
        aumentoRPM = 30
    elif mode == 'dificult':
        aumentoRPM = 50
    else:
        aumentoRPM = 30
    return aumentoRPM

def key_bindings():
    while True:
        screen.fill("#000000")

        KEY_BINDINGS_MOUSE_POS = pygame.mouse.get_pos()

        KEY_BINDINGS_TEXT = get_font(85).render("KEY BINDINGS", True, "#b68f40")
        KEY_BINDINGS_RECT = KEY_BINDINGS_TEXT.get_rect(center=(640, 100))
        MOVEMENT_TEXT = get_font(50).render("MOVEMENT", True, "#b68f40")
        MOVEMENT_RECT = MOVEMENT_TEXT.get_rect(center=(250, 250))
        BREAKS_TEXT = get_font(50).render("BREAKS!", True, "#b68f40")
        BREAKS_RECT = BREAKS_TEXT.get_rect(center=(640, 250))
        CLUTCH_TEXT = get_font(50).render("CLUTCH...", True, "#b68f40")
        CLUTCH_RECT = BREAKS_TEXT.get_rect(center=(1000, 250))

        BACK_BUTTON = Button(image=pygame.image.load("assets/Back Rect.png"), pos=(640, 550), text_input="BACK", font=get_font(60), base_color="white", hovering_color="gray")

        screen.blit(KEY_BINDINGS_TEXT, KEY_BINDINGS_RECT)
        screen.blit(MOVEMENT_TEXT, MOVEMENT_RECT)
        screen.blit(BREAKS_TEXT, BREAKS_RECT)
        screen.blit(CLUTCH_TEXT, CLUTCH_RECT)

        arrows = pygame.image.load("assets/flechas.png").convert_alpha()
        arrows = pygame.transform.scale(arrows, (196, 136))
        screen.blit(arrows, (150, 300))

        spacebar = pygame.image.load("assets/spacebar.png").convert_alpha()
        spacebar = pygame.transform.scale(spacebar, (192, 72))
        screen.blit(spacebar, (550, 330))

        c_key = pygame.image.load("assets/c_key.png").convert_alpha()
        c_key = pygame.transform.scale(c_key, (62, 62))
        screen.blit(c_key, (950, 330))

        BACK_BUTTON.changeColor(KEY_BINDINGS_MOUSE_POS)
        BACK_BUTTON.update(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if BACK_BUTTON.checkForInput(KEY_BINDINGS_MOUSE_POS):
                    options()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    options()

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
    rpm_to_velocity_factor = 0.00007  # Factor de conversión de RPM a velocidad (km/h
    aumentoRPM = level()
    print(mode)
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
    
    while run:
        screen.fill("#000000")

        pos = pygame.mouse.get_pos()
        x_dist = pos[0] - 1280/2
        y_dist = -(pos[1] - 720/2)
        angle = math.degrees(math.atan2(y_dist, x_dist))
        carRotated = pygame.transform.rotate(car, angle - 90)
        car_rect = carRotated.get_rect(center=(1280/2, 720/2))
        screen.blit(carRotated, car_rect)

        if image_display.current_image_index < 6:
            current_gear = image_display.current_image_index
            if car_velocity < MIN_SPEEDS[current_gear] or car_velocity > MAX_SPEEDS[current_gear]: print('No se puede cambiar a esta marcha')
            else:
                if rpm < 7000: rpm += aumentoRPM
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
                car_velocity -= 0.25
                if car_velocity < 0: car_velocity = 0
        print('gear ',current_gear+1, 'RPM:', rpm, 'Velocity:', car_velocity)

        for event in pygame.event.get(): # Evento pa las keys
            if event.type == pygame.KEYDOWN: # Cuando se preciona una tecla
                if image_display.current_image_index == 2 and event.key == pygame.K_DOWN and pygame.key.get_pressed()[pygame.K_RIGHT]:
                    image_display.change_image(7)
                    delay = 100
                    pygame.time.delay(delay)
                    if image_display.current_image_index == 7:
                        image_display.change_image(8)
                    
                elif image_display.current_image_index == 3 and event.key == pygame.K_UP and pygame.key.get_pressed()[pygame.K_RIGHT]:
                    image_display.change_image(7)
                    delay = 100
                    pygame.time.delay(delay)
                    if image_display.current_image_index == 7:
                        image_display.change_image(8)
                        
                elif image_display.current_image_index == 2 and event.key == pygame.K_DOWN and pygame.key.get_pressed()[pygame.K_LEFT]:
                    image_display.change_image(7)
                    delay = 100
                    pygame.time.delay(delay)
                    if image_display.current_image_index == 7:
                        image_display.change_image(6)
                
                elif image_display.current_image_index == 3 and event.key == pygame.K_UP and pygame.key.get_pressed()[pygame.K_LEFT]:
                    image_display.change_image(7)
                    delay = 100
                    pygame.time.delay(delay)
                    if image_display.current_image_index == 7:
                        image_display.change_image(6)
                elif event.key == pygame.K_DOWN:
                    index_map = {0: 6, 2: 7, 4: 8, 6: 1, 7: 3, 8: 5}
                    if image_display.current_image_index in index_map:
                        image_display.change_image(index_map[image_display.current_image_index])
                elif event.key == pygame.K_RIGHT:
                    if 6 <= image_display.current_image_index < 8:
                        image_display.change_image(image_display.current_image_index + 1)
                elif image_display.current_image_index in [0,1]:
                    image_display.change_image(6)

                elif event.key == pygame.K_LEFT:
                    if 6 < image_display.current_image_index <= 8:
                        image_display.change_image(image_display.current_image_index - 1)
                elif image_display.current_image_index in [4,5]:
                    image_display.change_image(8)
                elif event.key == pygame.K_UP:
                    index_map = {1: 6, 3: 7, 5: 8, 6: 0, 7: 2, 8: 4}
                    if image_display.current_image_index in index_map:
                        image_display.change_image(index_map[image_display.current_image_index])
                
                elif event.key == pygame.K_SPACE:
                    breaking = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    if 6 <= image_display.current_image_index <= 8 and not pygame.key.get_pressed()[pygame.K_LEFT] and not pygame.key.get_pressed()[pygame.K_RIGHT] and not pygame.key.get_pressed()[pygame.K_UP] and not pygame.key.get_pressed()[pygame.K_DOWN]:
                        image_display.change_image(7)
                if event.key == pygame.K_ESCAPE: # Pa cerrar el juego cuando suelte el Escape
                    main_menu()
                    run = False
                if event.key == pygame.K_SPACE:
                    breaking = False

            if event.type == pygame.QUIT:
                run = False
        clock.tick(60)
    
        # image_display.show_image(image_display.current_image_index, pygame.math.Vector2(950, 400))
        image_display.show_image()
        #pygame.display.update()f
        pygame.display.flip()
    pygame.quit()
main_menu()