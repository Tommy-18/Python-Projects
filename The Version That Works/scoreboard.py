import pygame.font
from pygame.sprite import Group
from User_Tank import Tank
class Scoreboard():
    #This is a class that displys the scoring information

    def __init__(self, ai_settings, screen, stats):
        #This initializes the scoring attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        #These are the font settiings for the scoring information
        self.font_color = (240,240,240)
        self.font = pygame.font.SysFont(None, 34)        

        #Prepare the initial score image
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_tanks()



    def prep_score(self):
        #The turns the rounded score into a rendered image
        rounded_score = int(round(self.stats.score,-1)) #This rounds the score to the nearest 10
        #round will get the value to the nearest 10,100,1000 etc depending on the 2nd argument

        
        score_string = "{:,}". format(rounded_score)
        #This makes the program to put commas into the string


        
        self.score_image = self.font.render(score_string, True ,self.font_color, self.ai_settings.bg_color)

        #Displays the score at the top right of the screen
        self.score_rect = self.score_image.get_rect()

        #The rightmost part is 20 pixels left from the edge of the screen
        self.score_rect.right = self.screen_rect.right - 20

        #The top of the text must be at 20 pixels. 
        self.score_rect.top = 20

    def show_self(self):
        #This draws the score onto the screen
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.tanks.draw(self.screen)


    def prep_high_score(self):
        #This is turns the highest score achieved into an image
        high_score = int(round(self.stats.high_score, -1))
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.font_color,self.ai_settings.bg_color)

        #Centers it at the top of the screen
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top


    def prep_level(self):
        self.level_image = self.font.render(str(self.stats.level), True,
                                                 self.font_color,self.ai_settings.bg_color)

        #This makes the level be positioned below the score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.top + 30


    def prep_tanks(self):
        #Displays how many lives there are left
        self.tanks  = Group()
        for tank_number in range(self.stats.life):
            tank = Tank(self.ai_settings,self.screen)
            tank.rect.x = 10 + tank_number * tank.rect.width
            tank.rect.y = 10
            self.tanks.add(tank)
