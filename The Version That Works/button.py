import pygame.font
#This code creates a button that cana be used for anything in a game
#it simply makes a filled rectangle with a label
class Button():
    def __init__(self, ai_settings, screen, msg):
        #This starts the button attributes
        self.screen = screen
        self.screen_rect = screen.get_rect()

        #This sets the dimensions and properties of the button
        self.width, self.height = 200, 50 #This sets two variables with values
        self.button_color = (0,250,0)
        self.text_color = (255,255,255)

        
        #This prepares the font attribute for rendering text
        self.font = pygame.font.SysFont(None, 48) #(Font Style, Size)
        #The None argument tells python to use the default font 

        #This makes the button's rect object and centers it
        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #The button message needss to be prepped only once
        self.prep_msg(msg)
        
        




    def prep_msg(self,msg):
        #Turns msg into an image and renders it and centers the text on the button
        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
        #font.render() turns the text that is stored in msg into an image
        #Then it takes a Booelan value to turn antialiasing on or off (antialiasing makes the edge of text smoother)
        #The remaining arguments are for the specified colour for text and background

        self.msg_image_rect = self.msg_image.get_rect()
        #This just centers the image on the button
        self.msg_image_rect.center = self.rect.center



    def draw_button(self):
        #This draws a blank button and then draws the message
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
        
        
