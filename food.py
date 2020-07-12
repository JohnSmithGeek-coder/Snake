import random
import pygame
class Food():
    """表示食物的类"""
    def __init__(self, screen, sk_settings):
        self.screen = screen
        self.sk_settings = sk_settings
        #食物的属性
        #self.color = self.sk_settings.food_color
        self.width = self.sk_settings.food_width
        self.height = self.sk_settings.food_height
        self.image = []
        self.image.append(pygame.transform.smoothscale(pygame.image.load("images/food.png"), (self.sk_settings.snake_width, self.sk_settings.snake_height)))
        self.image.append(pygame.transform.smoothscale(pygame.image.load("images/food1.png"), (self.sk_settings.snake_width, self.sk_settings.snake_height)))
        self.image.append(pygame.transform.smoothscale(pygame.image.load("images/apple.png"), (self.sk_settings.snake_width, self.sk_settings.snake_height)))
        self.image.append(pygame.transform.smoothscale(pygame.image.load("images/green_apple.png"), (self.sk_settings.snake_width, self.sk_settings.snake_height)))
        self.image.append(pygame.transform.smoothscale(pygame.image.load("images/banana.png"), (self.sk_settings.snake_width, self.sk_settings.snake_height)))
        self.image.append(pygame.transform.smoothscale(pygame.image.load("images/eggplant.png"), (self.sk_settings.snake_width, self.sk_settings.snake_height)))
        self.image.append(pygame.transform.smoothscale(pygame.image.load("images/carrot.png"), (self.sk_settings.snake_width, self.sk_settings.snake_height)))
        self.image.append(pygame.transform.smoothscale(pygame.image.load("images/small_cherry.png"), (self.sk_settings.snake_width, self.sk_settings.snake_height)))
        self.image.append(pygame.transform.smoothscale(pygame.image.load("images/big_cherry.png"), (self.sk_settings.snake_width, self.sk_settings.snake_height)))
        self.image_number = 0
        #食物的位置
        self.x = 0
        self.y = 0
    def generate_position(self):
        """设置食物的位置"""
        self.x = random.randint(2, self.sk_settings.screen_size[0] // self.width - 2) * self.width
        self.y = random.randint(2, self.sk_settings.screen_size[1] // self.height - 2) * self.height

    def set_position(self, snake):
        self.generate_position()
        while True:
            for segment in snake.segments:
                if segment[0] == self.x and segment[1] == self.y:
                    self.generate_position()
                    break
            if segment == snake.segments[-1]:
                break
            
    def draw_food(self):
        """在屏幕上显示食物"""
        self.screen.blit(self.image[self.image_number], (self.x, self.y))

