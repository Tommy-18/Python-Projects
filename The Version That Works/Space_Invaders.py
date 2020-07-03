import sys 
#must be run python 32 bit 3.6
from pygame.sprite import Group
import pygame
from Space_Invaders_Settings import Settings #A class from a file called Space_Invaders_Settings
from User_Tank import Tank
import game_functions as gf #renames game_function to gf
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init() #Initialize game settings
    
    ai_settings = Settings() #This allows me to remember what call easier
    
    screen = pygame.display.set_mode((ai_settings.screen_width , ai_settings.screen_height))
    #.display() creates a screen
    #.set_mode() allows you to set the (width,height) of the entire window
    #it also adds all of this as an object (surface) to the class 'pygame'
    #any game element is a surface.

    #This makes a group to store bullets in
    bullets = Group()
    
    #This makes a group to store aliens
    aliens = Group()

    #This makes a group for the alien's bullets 
    enemybullets = Group()

    #This makes a tank
    tank = Tank(ai_settings, screen)

    #Create the fleet of aliens
    gf.create_fleet(ai_settings, screen, tank, aliens)

    #Creates an instance to store game statistics and scoreboard
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    play_button = Button(ai_settings, screen, "Play")
    
    #This calls the window Space Invaders
    pygame.display.set_caption("Space Invaders")
    
    #This makes a play button
    while True:
        gf.check_events(ai_settings, screen, stats, play_button, sb, 
                        tank, aliens, bullets, enemybullets)
        if stats.game_active: #This only runs whilst game_active = True
            tank.update()
            gf.update_bullets(ai_settings,sb, stats, screen, tank, aliens, bullets, enemybullets)
            gf.update_aliens(ai_settings, stats, screen, sb, tank, aliens, bullets, enemybullets)
        gf.update_screen(ai_settings, screen, stats, tank,sb,
                         aliens, bullets, enemybullets, play_button)

run_game()
