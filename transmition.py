import pygame
import os
pygame.init()
screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption('CODICON')

# prueba = pygame.image.load('prueba.png')
# screen.blit(prueba, (0, 0))
# pygame.display.update()
class ImageDisplay:
    def __init__(self, screen):
        self.screen = screen
        self.images = ['1ra.png', '2da.png', '3ra.png','4ta','5ta','6ta','n1','n2','n3']  # List of image filenames
        self.current_image_index = 0

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

# Call the change_image method to display a specific image
image_display.change_image(2)

run = True
while run:

    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYUP:
            image_display.show_image(1)
            if image_display.current_image_index == 0:
                if event.key == pygame.K_DOWN:
                    image_display.change_image(7)
            if event.key == pygame.K_RIGHT:
                image_display.change_image(image_display.current_image_index + 1)
            if event.key == pygame.K_LEFT:
                image_display.change_image(image_display.current_image_index - 1)
            #if event.key == pygame.K_DOWN:

            #if event.key == pygame.K_UP:
   
    
    #pygame.display.update()
    pygame.display.flip()
pygame.quit()
