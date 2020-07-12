import pygame
import sys
from time import sleep
from pygame.sprite import Group
from snake import Snake
from food import Food
from score import Score
from button import Button
from game_stats import GameStats
from settings import Settings 
import game_function as gf
def run_game():
    pygame.init()
    pygame.mixer.init()
    fpsClock = pygame.time.Clock()
    sk_settings = Settings()
    #创建游戏状态
    stats = GameStats()
    #设置屏幕
    screen = pygame.display.set_mode(sk_settings.screen_size)
    pygame.display.set_caption("Snake")
    #创建按钮
    button = Button(screen, sk_settings)
    #设置并播放背景音乐
    pygame.mixer.music.load("musics/background_music.wav")
    pygame.mixer.music.play(-1, 0.0)
    #创建🐍
    snake = Snake(screen, sk_settings)
    snake.create_snake_segments()
    #创建🍓                     
    food = Food(screen, sk_settings)
    food.set_position(snake)
    #创建分数 
    score = Score(screen, sk_settings)
    #主循环
    while True:
        gf.check_events(snake, button, stats)
        if stats.game_active:
            gf.snake_move(snake)
            gf.snake_eat(food, snake, score, stats, sk_settings)
            #检查越界
            if gf.check_death(snake, sk_settings):
                stats.game_active = False
                pygame.mouse.set_visible(True)
                if stats.music_active:
                    death_music = pygame.mixer.Sound("musics/death_music.wav")
                    death_music.play()
                if score.food > score.highest:
                    score.highest = score.food
                    score.prep_highest_score()
                sleep(0.5)
                gf.reset_game(screen, sk_settings, snake, score, stats, food)
        if stats.music_active:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()
        #更新屏幕
        gf.update_screen(screen, snake, food, score, button, stats, sk_settings)
        #控制游戏速度
        fpsClock.tick(sk_settings.game_speed)
run_game()
