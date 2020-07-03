import pygame
from pygame.sprite import Sprite
#This class inherits from Sprite, which we imported from the pygame,sprite module
#When you use sprites, you can group together related elements and act on all the grouped elements at once
#To create bullet instance, __init__ needs ai_settings,screen and alien instances

class Enemy_Bullet(Sprite):
    #A class to manages the bullets fired from the ships

    def __init__(self, ai_settings, screen, enemy):
        
        #Creates a bullet object at the alien's current position
                    
        super(Enemy_Bullet,self).__init__() #We call super() to inherit properly from Sprite
        self.screen = screen

        #Creates a bullet rect at the position (0,0) and then set correct position
        self.rect = pygame.Rect(0,0, ai_settings.enemybullet_width,
                                            ai_settings.enemybullet_height)
        self.rect.centerx = enemy.rect.centerx #This makes the bullet have the same rect.centerx. as the alien
        self.rect.top = enemy.rect.top #This makes the bullets seem like they are emerging from the top of the alien

        #Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

        self.color = ai_settings.enemybullet_color
        self.speed_factor = ai_settings.enemybullet_speed_factor

        

    def update(self):#This updates the position of the bullet

        #Moves the bullet up the screen (when the bullet moves down the screen, the y value increases)
        self.y += self.speed_factor

        #Updates the rect position
        self.rect.y = self.y

    def draw_bullet(self):
        #Draws the bullet to the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        
        

