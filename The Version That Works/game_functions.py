import sys
import pygame
from bullets import Bullet
from alien import Alien
from time import sleep #This is a module that basically works as a delay/ timer system
from enemy_bullets import Enemy_Bullet
import random
import tkinter



def check_events(ai_settings, screen, stats, play_button, sb,
                 tank, aliens, bullets, enemybullets):
    for event in pygame.event.get():
        #an event is any action done by the user
        if  event.type == pygame.QUIT:
            sys.exit() #exits the game when the user closes the program

        elif event.type == pygame.KEYDOWN: #Whenever a key is pressed the event, the event known as KEYDOWN
            check_keydown_events(event, ai_settings, screen, tank, bullets)

        elif event.type == pygame.KEYUP: #KEYUP is for when the key has been released
            check_keyup_events(event,tank)

        elif event.type == pygame.MOUSEBUTTONDOWN: #This checks when the mouse has been clicked
            mouse_x, mouse_y = pygame.mouse.get_pos() #This retrieves the tuple of the mouse's location (x,y) 
            check_play_button(ai_settings, screen, stats,sb, play_button, tank,
                      aliens, bullets, mouse_x, mouse_y, enemybullets)


def check_play_button(ai_settings, screen, stats,sb, play_button, tank,
                      aliens, bullets, mouse_x, mouse_y , enemybullets):
    
    #This causes the game to start when the button has been clicked on
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y) #collidepoint() checks if the point overlaps with region defined by the Play Button's rect
    if button_clicked and not stats.game_active:
        stats.reset_stats()
        ai_settings.initialize_dynamic_settings()
        stats.game_active = True

        #This hides the mouse cursor when the game playing
        pygame.mouse.set_visible(False)

        #Empty the list of aliens and bullets
        aliens.empty()
        bullets.empty()
        enemybullets.empty()

        #Reset the score images
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_tanks()
        #Create a new fleet and centers the tank
        create_fleet(ai_settings, screen, tank, aliens)
        tank.center_tank()
    


def check_keydown_events(event, ai_settings, screen, tank, bullets):
   
    if event.key == pygame.K_RIGHT: #This action happens when the right arrow key is pressed
        #Move the tank right
        tank.moving_right = True
                

    if event.key == pygame.K_LEFT: #This action happens when the left arrow key is pressed
        #Move the tank left
        tank.moving_left = True

        
    elif event.key == pygame.K_SPACE:
    #Create a new bullet and add it to the bullets group
        fire_bullets(ai_settings, screen, tank, bullets)

    elif event.key == pygame.K_q:
        sys.exit()




def fire_bullets(ai_settings, screen, tank, bullets):
    #This allows bullets to be fired when the amount of bullets on screen is within an allowed range
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings,screen, tank)
        bullets.add(new_bullet)
                



def check_keyup_events(event, tank):
    if event.key == pygame.K_RIGHT:
        tank.moving_right = False

    if event.key == pygame.K_LEFT:
        tank.moving_left = False



                
def update_screen(ai_settings, screen, stats, tank, sb,
                  aliens, bullets, enemybullets, play_button):

    #This fills the screen to the desired colour
    screen.fill(ai_settings.bg_color)

    sb.show_self()

    #Redraw all bullets after the ship and aliens
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    for enemybullet in enemybullets.sprites():
        enemybullet.draw_bullet()

    tank.blitme()
    aliens.draw(screen)

    
    if not stats.game_active:
        play_button.draw_button()
    
    pygame.display.flip()
    #This makes the recently drawn screen visible. In this case it draws an empty screen
    #each time through the while loop to erase the old one.
    #pygame.display.flip() will continuely update the screen and make it look smooth




def update_bullets(ai_settings, sb, stats, screen, tank, aliens, bullets, enemybullets):
    #This will update the position of the bullets and gets rid of old ones
    #Updates the bullet position
    bullets.update()
    enemybullets.update()

    for bullet in bullets.copy(): #This goes through every bullet in the group
        if bullet.rect.bottom <= 0: #This is to see if the bullet goes off screen
            bullets.remove(bullet) #This removes the bullets

    for bullet in enemybullets.copy():
        if bullet.rect.bottom >= 600:
            enemybullets.remove(bullet) #This removes any bullets that are off screen 
            
    #checks if there are any collisions
    check_bullet_alien_collisions(ai_settings, screen, stats, sb,
                                  tank, aliens, bullets, enemybullets)
    check_bullet_tank_collisions(ai_settings, stats, screen, sb, tank, aliens, bullets, enemybullets)



def check_bullet_alien_collisions(ai_settings, screen, stats, sb,
                                  tank, aliens, bullets, enemybullets):
    #This checks if any bullets has hit the aliens
    #If so, it gets rid of both the alien and the bullet
    collision = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collision:
        for aliens in collision.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats,sb)
    if len(aliens) == 0:
        #This destroys the existing bullets and creates a new fleet and speeds the game up
        bullets.empty()
        ai_settings.increase_speed()

        #Increases the level
        stats.level += 1
        sb.prep_level()
        enemybullets.empty()
        create_fleet(ai_settings, screen, tank, aliens)



def check_bullet_tank_collisions(ai_settings,stats, screen,sb, tank, aliens, bullets, enemybullets):
    #This checks if any bullets has hit the tank
    #If so, it runs the tank hit function
    for bullet in enemybullets.sprites():
        collision = pygame.sprite.collide_rect(bullet, tank) #This checks if any single sprites have collided and returns a boolean value
        if collision == True:
            #This destroys the existing bullets and creates a new fleet
            tank_hit(ai_settings, stats, screen,sb, tank, aliens, bullets, enemybullets)


    #------------------------------------ALIEN RELATED GAME FUNCTIONS BELOW-------------------------------

      
def get_number_rows(ai_settings, tank_height, alien_height):
    #This calculates how many rows of aliens that fit on the screen
    available_space_y = (ai_settings.screen_height -
                         (3 * alien_height) - tank_height)
    number_of_rows = (int(available_space_y / ( 2 * alien_height)) - 1)
    return number_of_rows




        
def get_number_aliens_x(ai_settings, alien_width):
    #This then checks how many aliens that can possibly fit in an a row
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_alien_x = int(available_space_x / (2 * alien_width))
    return number_alien_x




def create_alien(ai_settings, screen, aliens, alien_number,row_number):
    #Create an alien and then place it in the row
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width * alien_number)
    alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)
    alien.rect.x = alien.x
    aliens.add(alien)




def create_fleet(ai_settings, screen, tank, aliens):
    #creates the fleet that is going to attack the player
    #This starts by creating an alien
    #It then creates that row and makes equal spacing between the aliens
    alien = Alien(ai_settings, screen)
    number_alien_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_of_rows = get_number_rows(ai_settings, tank.rect.height,
                                     alien.rect.height)
    
    #This creates the rows
    for row_number in range(number_of_rows):
        for alien_number in range(number_alien_x):
            create_alien(ai_settings, screen,
                         aliens, alien_number,
                         row_number)
    



def check_fleet_edges(ai_settings, aliens):
    #This calls the following function if any aliens reach an edge
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break




def change_fleet_direction(ai_settings, aliens):
    #Drops of an alien and changes the alien's direction
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1




def tank_hit(ai_settings, stats, screen, sb, tank, aliens, bullets, enemybullets):
    #This is response that is displayed when the tank is hit by an Alien
    #This selcetion statement checks that the amount of lives is greater than 0
    if stats.life > 0:
        #The amount of lives decrements
        stats.life -= 1

        sb.prep_tanks()
        #This empties the list of aliens and bullets
        aliens.empty()
        bullets.empty()
        enemybullets.empty()

        #Create a new fleet and center the ship
        create_fleet(ai_settings, screen, tank, aliens)
        tank.center_tank()

        #This makes the user wait 0.5 seconds before starting again
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)



def check_aliens_bottom(ai_settings, stats, screen, sb, tank, aliens, bullets, enemybullets):
    #Check if any of the aliens has managed to reach the bottom of the screen
    screen_rect = screen.get_rect() #Checks the dimensions of the screen
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            tank_hit(ai_settings, stats, screen, sb, tank, aliens, bullets, enemybullets)
            break


def update_aliens(ai_settings, stats, screen, sb, tank, aliens, bullets, enemybullets):
    # Check if an alien is at the edge,
    # and then updates the position of it
    check_fleet_edges(ai_settings, aliens)
    enemy_fire_bullets(ai_settings, screen, aliens, enemybullets) #This makes the enemy fire
    aliens.update()

    check_aliens_bottom(ai_settings, stats, screen, sb, tank, aliens, bullets, enemybullets) #This checks if the aliens are at the bottom of the screen
    if pygame.sprite.spritecollideany(tank, aliens):
        print("The tank has been hit")
        tank_hit(ai_settings, stats, screen, tank, aliens, bullets , enemybullets)
        

def enemy_fire_bullets(ai_settings, screen, aliens, enemybullets):
    for alien in aliens.sprites(): #This searches through all of the aliens
        val = random.randint(0,10) #creates a random value for an alien
        enemy = alien
        if val > 5: #This checks the randomly generated value to see if it should shoot
            if len(enemybullets) < ai_settings.enemybullet_allowed: #This checks if it is allowed to shoot
                new_bullet = Enemy_Bullet(ai_settings,screen, enemy) 
                enemybullets.add(new_bullet) #This adds the bullet to the enemybullets
                
def check_high_score(stats, sb):
    #Checks if the user's current score is higher than the current highest score
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()
