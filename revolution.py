import pygame
import pygame.gfxdraw
import os
import math

pygame.init()
screen = pygame.display.set_mode((1280, 720))
screen.fill((100,100,100))
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

class MotionMeter:
    def __init__(self, screen=int,size=int,coords=(0,0),color=(20,20,20),separation=10,start_value=0,end_value=360,marks=2,title=""):
        self.screen = screen
        self.size = size
        self.coords = coords
        self.color = color
        self.separation = separation
        self.start_value = start_value
        self.end_value = end_value
        self.marks=marks
        self.title=title

    def __process_coords(self,coords,angle,size):
        new_coords = (coords[0]+(size*math.cos(math.radians(angle))),coords[1]+(size*math.sin(math.radians(angle))))
        return new_coords

    def __create_marks(self,separation,large,width,color):
        for i in range(separation+1):
            pygame.draw.line(self.screen,color,self.__process_coords(self.coords,(130+((280*i)/separation)),self.size-(large*0.01)*self.size),self.__process_coords(self.coords,(130+((280*i)/separation)),self.size),width=width)
            if large == 10:
               self.__create_text(f"{int(self.start_value + ((self.end_value-self.start_value)/separation)*i)}",self.__process_coords(self.coords,(130+((280*i)/separation)),self.size-(23*0.01)*self.size),size=int(self.size*0.14))

    def __create_text(self,texto, coords, color=(255, 255, 255), size=14, font="arial"):
        font = pygame.font.SysFont(font, size)
        text = font.render(texto, True, color)
        textRect = text.get_rect()
        textRect.center = (coords[0],coords[1])
        self.screen.blit(text, textRect)
    
    def __createIndicator(self,angle):
        print((280*angle)/(self.end_value-self.start_value)+130)
        pygame.draw.line(self.screen,(200,0,0),self.coords,self.__process_coords(self.coords,(280*angle)/(self.end_value-self.start_value)+130,self.size-self.size*0.15),width=5) 
        pygame.draw.circle(self.screen,(30,30,30),self.coords,self.size*0.2)

    def create_Motion(self,angle):
        pygame.draw.circle(self.screen,self.color,self.coords,self.size)
        pygame.gfxdraw.arc(self.screen,self.coords[0],self.coords[1],self.size,130,410,(200,200,200))
        if self.marks == 2:
            self.__create_marks((self.separation*2),5,2,(200,200,200))
        elif self.marks == 3:
            self.__create_marks((self.separation*10),2.5,1,(195,195,195))
            self.__create_marks((self.separation*2),5,2,(200,200,200))
        self.__create_marks(self.separation,10,2,(255,255,255))
        self.__createIndicator(angle)
          
        self.__create_text(str(angle),(self.coords[0],self.coords[1]+self.size-int(self.size*0.3)),size=int(self.size*0.2))
        self.__create_text(self.title,(self.coords[0],self.coords[1]+self.size+int(self.size*0.2)),size=int(self.size*0.2))


    def update_Motion(self,angle):
        self.screen.fill((100,100,100))
        self.create_Motion(angle)
        pygame.display.flip()
        pygame.display.update()
    
        
# Create an instance of the ImageDisplay class
image_display = ImageDisplay(screen)
revolutions = MotionMeter(screen,100,(200,200),(20,20,20),separation=13,start_value=0,end_value=260,marks=3,title="RPM")
revolutions.create_Motion(0)


run = True
while run:

    revolutions.update_Motion(80)
    
    
    pygame.display.update()
    pygame.display.flip()
pygame.quit()
