class Settings():
    """存储贪吃蛇中的设置"""
    def __init__(self):
        #屏幕设置
        self.bg_color = (230, 230, 230)
        self.screen_size = (800, 640)
        #蛇节设置
        self.snake_width = 40
        self.snake_height = 40
        self.snake_color = (0, 255, 0)
        #初始蛇长
        self.initial_length = 3
        #食物设置
        self.food_width = 40
        self.food_height = 40
        self.food_color = (255, 0, 0)
        #游戏速度
        self.game_speed = 5
