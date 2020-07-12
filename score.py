import pygame.font
class Score():
    def __init__(self, screen, sk_settings):
        self.screen = screen
        self.sk_settings = sk_settings
        self.food = 0
        self.highest = 0
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont('arial', 25)
        self.prep_food_score()
        self.prep_highest_score()
    def prep_food_score(self):
        score_str = "{:,}".format(self.food) 
        self.food_score_image = self.font.render(score_str, True, self.text_color, (87, 138, 52))
        self.food_score_rect = self.food_score_image.get_rect()
        self.food_score_rect.centerx = self.sk_settings.snake_width * 3 - self.sk_settings.snake_width // 2
        self.food_score_rect.top = self.sk_settings.snake_height // 8
    def prep_highest_score(self):
        score_str = "{:,}".format(self.highest) 
        self.highest_score_image = self.font.render(score_str, True, self.text_color, (87, 138, 52))
        self.highest_score_rect = self.highest_score_image.get_rect()
        self.highest_score_rect.centerx = self.sk_settings.snake_width * 4 + self.sk_settings.snake_width // 2
        self.highest_score_rect.top = self.sk_settings.snake_height // 8
    def show(self):
        self.screen.blit(self.food_score_image, self.food_score_rect)
        self.screen.blit(self.highest_score_image, self.highest_score_rect)
