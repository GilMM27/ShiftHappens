import pygame

class ImageDisplay:
    def __init__(self, screen):
        self.screen = screen
        self.images = ['assets/1ra.png', 'assets/2da.png', 'assets/3ra.png','assets/4ta.png','assets/5ta.png','assets/6ta.png','assets/n1.png','assets/n2.png','assets/n3.png']  # List of image filenames
        self.current_image_index = 7

    def show_image(self):
        image = pygame.image.load(self.images[self.current_image_index])
        self.screen.blit(image, (950, 400))
        pygame.display.flip()

    def change_image(self, index):
        if index >= 0 and index < len(self.images):
            self.current_image_index = index
            self.show_image()