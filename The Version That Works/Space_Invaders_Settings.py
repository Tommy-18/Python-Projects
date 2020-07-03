class Settings():
    #A class to store all settings for Space Invaders"

    def __init__(self):
        self.screen_width = 800  #screen width
        self.screen_height = 600 #screen height
        self.bg_color = (10,10,10) #This is the background colour

        #Tank's setting
        self.tank_limit = 2


        
        #Settings for the bullets
        self.bullet_width = 3 #measured in pixels
        self.bullet_height = 5 #measured in pixels
        self.bullet_color = 255,255,255
        self.bullets_allowed = 5


        #Settings for the alien
        self.fleet_drop_speed = 10
        
        #The settings for the enemy bullets
        self.enemybullet_allowed = 5
        self.enemybullet_width = 3 #measured in pixels
        self.enemybullet_height = 5 #measured in pixels
        self.enemybullet_color = 250,150,150


        #This increases the speed of the game
        self.speed_increase = 1.1

        #This increases the score point of aliens per level
        self.score_increase = 1.5
        


        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #These are the speed settings at the beginning of the game that change throughout the game
        self.alien_speed_factor = 0.75
        self.bullet_speed_factor = 2
        self.enemybullet_speed_factor = 1.5
        self.tank_speed_factor = 1.5

        self.alien_points = 50
        
        #fleet_direction of 1 represent ; -1 represents left
        self.fleet_direction = 1
        
    def increase_speed(self):
        self.tank_speed_factor *= self.speed_increase
        self.alien_speed_factor *= self.speed_increase
        self.bullet_speed_factor *= self.speed_increase
        self.enemybullet_speed_factor *= self.speed_increase
        self.alien_points = int(self.alien_points * self.score_increase)
        


        
