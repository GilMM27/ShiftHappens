import pygame
import os
import sys
import math
import random
from imageDisplay import ImageDisplay
from button import Button
import motionmeter
#import road
 
pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('CODICON')

mode = 'medium' # Default mode
background_load = pygame.image.load('assets/bg.jpg') #cambiar de imagen a una que no se pixelee
background = pygame.transform.scale(background_load, (screen_width, screen_height))
velocity = motionmeter.MotionMeter(screen,100,(200,200),(20,20,20),separation=13,start_value=0,end_value=260,marks=3,title="KM/H")
revolution = motionmeter.MotionMeter(screen,100,(200,500),(20,20,20),separation=7,start_value=0,end_value=7000,marks=2,title="RPM",digit=True)

def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("assets/BlackHanSans-Regular.ttf", size)

def create_text(texto, coords, color=(255, 255, 255), size=14, font="arial"):
        font = pygame.font.SysFont(font, size)
        text = font.render(texto, True, color)
        textRect = text.get_rect()
        textRect.center = (coords[0],coords[1])
        screen.blit(text, textRect)

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


def Fail(explication="The engine fails", points=1000):
    while True:
        screen.fill("#000000") 

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        EXPLANATION = get_font(70).render(explication, True, "#fc031c")
        EXPLANATION_RECT =EXPLANATION.get_rect(center=(640, 100))
        screen.blit(EXPLANATION, EXPLANATION_RECT)
        
        POINTS = get_font(40).render(f"You made: {points} points", True, "#ffffff")
        POINTS_RECT =POINTS.get_rect(center=(640, 200))
        screen.blit(POINTS, POINTS_RECT)


        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 360), text_input="RETURN", font=get_font(60), base_color="white", hovering_color="gray")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550), text_input="QUIT", font=get_font(60), base_color="white", hovering_color="gray")

        
        for button in [PLAY_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(screen)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    main_menu()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

# cosas dana.
def random_coeff():
    return [random.uniform(-1,0), random.uniform(-5,5), random.uniform(-5,5), 0 ]

def roadFun(pos_x, coeff):
    return coeff[0] * (pos_x ** 3) + coeff[1] * (pos_x ** 2) + coeff[2] * pos_x + coeff[3]

def der_roadFun(pos_x, coeff): #esto solo se usaria si se quiere calcular la vel max para el derrape
    return 3 * coeff[0] * pos_x ** 2 + 2 * coeff[1] * pos_x + coeff[2]

def der2_roadFun(pos_x, coeff): #esto solo se usaria si se quiere calcular la vel max para el derrape
    return 6 * coeff[0] * pos_x + 2 * coeff[1]
    
def vel_max(x_pos, coeffs):
    R = (1+ der_roadFun(x_pos, coeffs)**2)**(3/2) / abs(der2_roadFun(x_pos, coeffs))
    coeffFriction = 0.8
    vmax = math.sqrt( R * 9.81 * coeffFriction ) * 3.6 #m/s a km/h
    return vmax

vel_list = []

def calculate_roadpoints(_coeff):
    points = []
    i = 0
    for x in range(-1000, 1000, 2): # TODO cortar esto para que no haya tanta linea aburrida
        points.append((i, roadFun(x / 100, _coeff) + (screen_height / 2)))
        vel_list.append(vel_max(x,_coeff))
        i += 1
    return points

def join_road_points(points, new_points): #habrá una segunda funcion como buffer
    offset_x = points[-1][0] - new_points[0][0]
    offset_y = points[-1][1] - new_points[0][1]
    for point in range(len(new_points)): #hay una manera mas bonita, solo no se me ocurrio anoche :c
        point_list = list(new_points[point])
        point_list[0] += offset_x
        point_list[1] += offset_y
        points.append(point_list)
    return points

def distancia_puntos(punto1, punto2):
    return math.sqrt((punto1[0] - punto2[0]) ** 2 + (punto1[1] - punto2[1]) ** 2)

def punto_mas_cercano(road_points, screen_width, screen_height):
    #pos de tupla mas cercano al centro virtual
    objetivo = (screen_width // 2, screen_height // 2)
    distancia_minima = float('inf')
    posicion_minima = None

    for i, punto in enumerate(road_points):
        distancia = distancia_puntos(punto, objetivo)
        if distancia < distancia_minima:
            distancia_minima = distancia
            posicion_minima = i

    return posicion_minima

def drawSpeedlimit(speed):
    image = pygame.image.load("assets/speedlimit.png")
    imageX = 250
    imageY = 250
    image = pygame.transform.scale(image, (imageX, imageY))
    screen.blit(image, (screen_width-300, 50))
    speedText = get_font(70).render(str(speed), True, (0, 0, 0))
    screen.blit(speedText, (screen_width-215, 125))
    maxText = get_font(15).render("Limite de velocidad", True, (0, 0, 0))
    screen.blit(maxText, (screen_width-255, 190))

def game_loop():
    flag = False
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
    MIN_SPEEDS = [0, 20, 40, 60, 80, 100]  # Velocidades mínimas para cada marcha en km/h

    # Clock for controlling the frame rate
    clock = pygame.time.Clock()
    maxRPMtime = 0
    
    breaking = False
    clutch = False
    run = True

    carSizeX = 75
    carSizeY = 150
    # pygame.draw.rect(screen, [255,255,255], [1280/2-carSizeX/2, 720/2-carSizeY/2, carSizeX, carSizeY], 4)
    car = pygame.image.load("assets/carrito.png").convert_alpha()
    car = pygame.transform.scale(car, (carSizeX, carSizeY))
    
    #cosas dana
    road_points = calculate_roadpoints(random_coeff())
    new_road_points = calculate_roadpoints(random_coeff())
    speed = 30 #speed de la transmision
    mov_x = 0
    mov_y = 0
    # vel_list = []
    # derrape = False

    point_time=0
    
    while run:
        screen.fill("#000000")
        
        # road stuff
        speed = car_velocity*0.1
        #Background
        screen.fill((255, 255, 255))
        screen.blit(background, (0,0))

        i = 0
        while i < len(road_points):
            x, y = road_points[i]
            road_points[i] = (x + mov_x, y + mov_y)
            if road_points[i][1] > 1500:
                road_points.pop(i)
            else:
                i += 1

        if road_points[-1][1] > -2000:
            coeff = random_coeff()
            new_road_points = calculate_roadpoints(coeff)
            road_points = join_road_points(road_points, new_road_points)

        #print road
        for point in road_points:
            pygame.draw.circle(screen, (0, 0, 0), (point), 50)  # Draw a black circle at each point

        # if not derrape:
        near_origin = punto_mas_cercano(road_points, screen_width, screen_height)
        theta = math.atan( (road_points[near_origin+10][1] - road_points[near_origin][1])/ (road_points[near_origin+10][0] - road_points[near_origin][0]) )
        vx = speed*math.cos(theta)
        vy = speed*math.sin(theta)
        mov_x = -vx
        mov_y = -vy
        # else:
        #     theta = -0.78

        # if speed > vel_list[near_origin]:
        #     print("sobrepaso el limite de velocidad en ", road_points[near_origin])
        #     derrape = True

        # Car stuff
        angle = abs(math.degrees(theta))
        carRotated = pygame.transform.rotate(car, angle - 90)
        car_rect = carRotated.get_rect(center=(640, 340))
        screen.blit(carRotated, car_rect)

        # Gear shifting
        if image_display.current_image_index < 6 and clutch == False:
            current_gear = image_display.current_image_index
            if car_velocity < MIN_SPEEDS[current_gear] or car_velocity > MAX_SPEEDS[current_gear]: Fail("You are not in the right speed", point_time)
            else:
                if rpm < 7000: rpm += aumentoRPM
                if rpm > 7000: rpm = 7000
                if rpm == 7000:
                    maxRPMtime += 1
                    if maxRPMtime >100: Fail("You are not shifting gears", point_time)
                else: maxRPMtime = 0
                car_velocity += rpm * rpm_to_velocity_factor * gear_ratios[current_gear] * (1 - car_velocity / MAX_SPEEDS[current_gear])
            time = 0
        else:
            if rpm > 0: rpm -= 150
            if rpm < 0: rpm = 0
            if car_velocity > 0:
                # deceleration_factor = max(0.01, car_velocity / MAX_SPEEDS[current_gear])
                car_velocity -= min(pow(time, 2), 0.05)
                if car_velocity < 0: car_velocity = 0
                time += 0.001
            if breaking == True:
                car_velocity -= 1
                if car_velocity < 0: car_velocity = 0
        # print('gear ',current_gear+1, 'RPM:', rpm, 'Velocity:', car_velocity)

        # Event handling
        for event in pygame.event.get(): # Evento pa las keys
            if event.type == pygame.KEYDOWN: # Cuando se preciona una tecla
                if clutch == True:
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
                    if event.key == pygame.K_SPACE:
                        breaking = True
                if event.key == pygame.K_c:
                    clutch = True
                if event.key == pygame.K_SPACE and clutch == False:

                    Fail("You are not using the clutch", point_time)

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    if 6 <= image_display.current_image_index <= 8 and not pygame.key.get_pressed()[pygame.K_LEFT] and not pygame.key.get_pressed()[pygame.K_RIGHT] and not pygame.key.get_pressed()[pygame.K_UP] and not pygame.key.get_pressed()[pygame.K_DOWN]:
                        image_display.change_image(7)
                if event.key == pygame.K_ESCAPE: # Pa cerrar el juego cuando suelte el Escape
                    main_menu()
                    run = False
                if event.key == pygame.K_SPACE:
                    breaking = False
                if event.key == pygame.K_c:
                    clutch = False                

            if event.type == pygame.QUIT:
                run = False
        
        if car_velocity == 0 and flag == False:
            flag=False
            create_text("Points: 0", (640, 680), size=70,font="assets/BlackHanSans-Regular.ttf")
            point_time = 0
        else:
            if flag == False:
                times = pygame.time.get_ticks()
                flag=True
            if pygame.time.get_ticks() - times > 2000:
                point_time += int(car_velocity)
                times = pygame.time.get_ticks()
            create_text(f"Points: {point_time}", (640, 680), size=70,font="assets/BlackHanSans-Regular.ttf")
        
        
        # time_update +=

        velocity.update_Motion(car_velocity)
        revolution.update_Motion(rpm)
        # drawSpeedlimit(vel_list[near_origin])
        clock.tick(60)
        # image_display.show_image(image_display.current_image_index, pygame.math.Vector2(950, 400))
        image_display.show_image()
        #pygame.display.update()f
        pygame.display.flip()
   
    pygame.quit()

main_menu()