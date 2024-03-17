import pygame
import pygame.gfxdraw
import math

class MotionMeter:
    def __init__(self, screen=int,size=int,coords=(0,0),color=(20,20,20),separation=10,start_value=0,end_value=360,marks=2,title="",digit=False):
        self.screen = screen
        self.size = size
        self.coords = coords
        self.color = color
        self.separation = separation
        self.start_value = start_value
        self.end_value = end_value
        self.marks=marks
        self.title=title
        self.digit=digit

    def __process_coords(self,coords,angle,size):
        new_coords = (coords[0]+(size*math.cos(math.radians(angle))),coords[1]+(size*math.sin(math.radians(angle))))
        return new_coords

    def __create_marks(self,separation,large,width,color):
        for i in range(separation+1):
            pygame.draw.line(self.screen,color,self.__process_coords(self.coords,(130+((280*i)/separation)),self.size-(large*0.01)*self.size),self.__process_coords(self.coords,(130+((280*i)/separation)),self.size),width=width)
            if large == 10:
                if self.digit: 
                    self.__create_text(f"{str(int(self.start_value + ((self.end_value-self.start_value)/separation)*i))[0]}",self.__process_coords(self.coords,(130+((280*i)/separation)),self.size-(23*0.01)*self.size),size=int(self.size*0.14))
                else:
                     self.__create_text(f"{int(self.start_value + ((self.end_value-self.start_value)/separation)*i)}",self.__process_coords(self.coords,(130+((280*i)/separation)),self.size-(23*0.01)*self.size),size=int(self.size*0.14))

    def __create_text(self,texto, coords, color=(255, 255, 255), size=14, font="arial"):
        font = pygame.font.SysFont(font, size)
        text = font.render(texto, True, color)
        textRect = text.get_rect()
        textRect.center = (coords[0],coords[1])
        self.screen.blit(text, textRect)
    
    def __createIndicator(self,angle):
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
          
        self.__create_text(str(int(angle)),(self.coords[0],self.coords[1]+self.size-int(self.size*0.3)),size=int(self.size*0.2))
        self.__create_text(self.title,(self.coords[0],self.coords[1]+self.size+int(self.size*0.2)),size=int(self.size*0.2))


    def update_Motion(self,angle):
        self.create_Motion(angle)