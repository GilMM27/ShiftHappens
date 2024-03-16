import pygame
import os
import sys
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('CODICON')

# prueba = pygame.image.load('prueba.png')
# screen.blit(prueba, (0, 0))
# pygame.display.update()
class ImageDisplay:
    def __init__(self, screen):
        self.screen = screen
        self.images = ['1ra.png', '2da.png', '3ra.png','4ta.png','5ta.png','6ta.png','n1.png','n2.png','n3.png']  # List of image filenames
        self.current_image_index = 7

    def show_image(self):
        image = pygame.image.load(self.images[self.current_image_index])
        self.screen.blit(image, (1280/2 - 263/2, 720/2 - 274/2))
        pygame.display.flip()

    def change_image(self, index):
        if index >= 0 and index < len(self.images):
            self.current_image_index = index
            self.show_image()

# Create an instance of the ImageDisplay class
image_display = ImageDisplay(screen)
image_display.show_image()

# Car properties
car_velocity = 0  # Initial velocity in km/h
rpm = 0  # Initial RPM
rpm_to_velocity_factor = 0.000005  # Conversion factor from RPM to velocity
gear_ratios = [5, 3.5, 2, 1.5, 1.0, 0.7]  # Gear ratios for gears 1 to 5
current_gear = 1  # Initial gear

# Clock for controlling the frame rate
clock = pygame.time.Clock()

run = True
while run:
    if image_display.current_image_index < 6:
        current_gear = image_display.current_image_index
        if rpm < 7000: rpm += 30
        car_velocity += rpm * rpm_to_velocity_factor * gear_ratios[current_gear - 1]
    else:
        rpm = 0
    print('Gear:', current_gear, 'RPM:', rpm, 'Velocity:', car_velocity)

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

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                if 6 <= image_display.current_image_index <= 8 and not pygame.key.get_pressed()[pygame.K_LEFT] and not pygame.key.get_pressed()[pygame.K_RIGHT]:
                    image_display.change_image(7)
            if event.key == pygame.K_ESCAPE: # Pa cerrar el juego cuando suelte el Escape
                run = False

        if event.type == pygame.QUIT:
            run = False
    clock.tick(60)
   
    
    #pygame.display.update()
    pygame.display.flip()
pygame.quit()
