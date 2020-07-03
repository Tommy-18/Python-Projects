import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    #A class to represent a single alien in the fleet

    def __init__(self,ai_settings, screen):
        #Initialize the alien and set its starting position
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        
            
        #This loads the alien image and set its rect attributes
        self.image = pygame.image.load('ALIEN.png')
        #30 pixel width  22 height
        self.rect = self.image.get_rect()


        #Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #Store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        #Draws the alien at its location
        self.screen.blit(self.image, self.rect)
        

    def update(self):
        #Moves the alien right
        #Move the alien right or left
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x


    def check_edges(self):
        #Returns a Boolean value if the alien is at the edge of the screen
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True


