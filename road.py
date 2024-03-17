import pygame
import os

import random
import math

pygame.init()
screen_width, screen_height = 1280, 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('CODICON')

background_load = pygame.image.load('assets/1ra.png') #cambiar de imagen a una que no se pixelee
background = pygame.transform.scale(background_load, (screen_width, screen_height))

''''''
def random_coeff():
    return [random.randrange(-5,0), random.randrange(-5,5), random.randrange(-5,5), 0 ]

def roadFun(pos_x, coeff):
    return coeff[0] * (pos_x ** 3) + coeff[1] * (pos_x ** 2) + coeff[2] * pos_x + coeff[3]

def der_roadFun(pos_x): #esto solo se usaria si se quiere calcular la vel max para el derrape
    return 3 * coeff[0] * pos_x ** 2 + 2 * coeff[1] * pos_x + coeff[2]

def der2_roadFun(pos_x): #esto solo se usaria si se quiere calcular la vel max para el derrape
    return 6 * coeff[0] * pos_x + 2 * coeff[1]

def calculate_roadpoints(_coeff):
    points = []
    i = 0
    for x in range(-1000, 1000, 2): # TODO cortar esto para que no haya tanta linea aburrida
        points.append((i, roadFun(x / 100, _coeff) + (screen_height / 2)))
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

''''''
#def __init__:
road_points = calculate_roadpoints(random_coeff())
new_road_points = calculate_roadpoints(random_coeff())

speed = 10 #speed de la transmision

mov_x = 0
mov_y = 0


''''''

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
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

    near_origin = punto_mas_cercano(road_points, screen_width, screen_height)
    theta = math.atan( (road_points[near_origin+10][1] - road_points[near_origin][1])/ (road_points[near_origin+10][0] - road_points[near_origin][0]) )
    vx = speed*math.cos(theta)
    vy = speed*math.sin(theta)
    mov_x = -vx
    mov_y = -vy



    pygame.display.flip()
    clock = pygame.time.Clock()

    #pygame.time.wait(500 // 60)
pygame.quit()





'''

 % Curvaturas
    R(i)= (1+fp(x(i))^2)^(3/2)/abs(fpp(x(i)));

    % Velocidades máximas durante la curva
    if (x(i) > 63 && x(i) < 98) || (x(i) > 175 && x(i) < 214)
        vmax(i) = sqrt( R(i) * 9.81 * ( (sin(peralte) + coeffFriccion*cos(peralte)) / (cos(peralte) - coeffFriccion*sin(peralte)) ) );
    else
        constante = ( (sin(0) + coeffFriccion*cos(0)) / (cos(0) - coeffFriccion*sin(0)) );
        vmax(i) = sqrt( R(i) * 9.81 * constante );
    end

'''