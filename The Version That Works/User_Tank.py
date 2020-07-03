import pygame
from pygame.sprite import Sprite
class Tank(Sprite):
    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings
        self.image = pygame.image.load("Tank.png")
        super(Tank,self).__init__()
        self.rect = self.image.get_rect()
        self.screen_rect= screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        #Store a decimal value for the tank's center
        self.center = float(self.rect.centerx)
        
        #Movement Flag
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        #This updates the tank's location based on the movement flag
        if self.moving_right and self.rect.right < self.screen_rect.right:
            #This checks that the position of the image is not off the screen by being too far to the right
            self.center += self.ai_settings.tank_speed_factor
            
        if self.moving_left and self.rect.left > 0:
            #This checks that the position of the image is not off the screen by being too far to the left
            self.center -= self.ai_settings.tank_speed_factor

        # This updates the rect object from self.center.
        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)


    def center_tank(self):
        #Center the ship on the screen
        self.center = self.screen_rect.centerx
