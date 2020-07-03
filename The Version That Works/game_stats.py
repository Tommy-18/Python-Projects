import copy #This is an module that allows the user to copy values

class GameStats():
    #This tracks the Statistics of the game

    def __init__(self, ai_settings):
        #This starts the statistics
        self.ai_settings = ai_settings
        self.life = copy.copy(self.ai_settings.tank_limit) #This is an shallow copy
        self.reset_stats()

        #This is the highest score achieved on this game
        self.high_score = 0
        self.level = 1
        
        #This makes the game in a paused state
        self.game_active = False

        
    def reset_stats(self):
        # This initialize statistics that may vary throughout the game
        self.life = self.ai_settings.tank_limit
        self.score = 0
        
    
