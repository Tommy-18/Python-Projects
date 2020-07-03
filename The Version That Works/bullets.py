import pygame
from pygame.sprite import Sprite

#This class inherits from Sprite, which we imported from the pygame,sprite module
#When you use sprites, you can group together related elements and act on all the grouped elements at once
#To create bullet instance, __init__ needs ai_settings,screen and ship instances

class Bullet(Sprite):
    #A class to manages the bullets fired from the ships

    def __init__(self, ai_settings, screen, tank):
        
        #Creates a bullet object at tank's current position
        super(Bullet,self).__init__() #We call super() to inherit properly from Sprite
        self.screen = screen

        #Creates a bullet rect at the position (0,0) and then set correct position
        self.rect = pygame.Rect(0,0, ai_settings.bullet_width,
                                ai_settings.bullet_height)
        self.rect.centerx = tank.rect.centerx #This makes the bullet have the same rect.centerx. as the tank
        self.rect.top = tank.rect.top #This makes the bullets seem like they are emerging from the top of the tank

        #Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):#This updates the position of the bullet

        #Moves the bullet up the screen (when the bullet moves up the screen, the y value decrease))
        self.y -= self.speed_factor

        #Updates the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        #Draws the bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
        
