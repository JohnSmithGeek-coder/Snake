import pygame
class Snake():
    def __init__(self, screen, sk_settings):
        self.screen = screen
        self.sk_settings = sk_settings
        self.color = sk_settings.snake_color
        self.width = sk_settings.snake_width
        self.height = sk_settings.snake_height
        self.body_image = pygame.transform.smoothscale(pygame.image.load("images/snake_body1.png"), (self.width, self.height))
        self.head_image = pygame.transform.smoothscale(pygame.image.load("images/snake_head.png"), (self.width, self.height))        
        self.screen_rect = screen.get_rect()
        self.head = [self.screen_rect.centerx, self.screen_rect.centery]
        self.segments = []
        self.direction = 'right'
        self.changeDirection = 'right'
    def create_snake_segments(self):
        self.segments.append(list(self.head))
        for segment_number in range(1, self.sk_settings.initial_length):
            segment_x = self.head[0] - segment_number * self.width
            segment_y = self.head[1]
            segment = [segment_x, segment_y]
            self.segments.append(segment)
    def move(self):
        if self.direction == 'up':
            self.head[1] -= self.height
        elif self.direction == 'down':
            self.head[1] += self.height
        elif self.direction == 'right':
            self.head[0] += self.width
        elif self.direction == 'left':
            self.head[0] -= self.width
    def change_direction(self):
        if self.changeDirection == 'right' and not self.direction == 'left':
            self.direction = 'right'
        elif self.changeDirection == 'left' and not self.direction == 'right':
            self.direction = 'left'
        elif self.changeDirection == 'up' and not self.direction == 'down':
            self.direction = 'up'
        elif self.changeDirection == 'down' and not self.direction == 'up':
            self.direction = 'down'
    def draw_snake(self):
        """在屏幕上绘制蛇节"""
        self.screen.blit(self.head_image, (self.segments[0][0], self.segments[0][1]))
        for segment in self.segments[1:]:
            self.screen.blit(self.body_image, (segment[0], segment[1]))
