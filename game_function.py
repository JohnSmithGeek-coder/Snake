import sys
import pygame
import random
from snake import Snake
from food import Food

def edges(piece, sk_settings):
    """在屏幕绘制时检查是否为边界"""
    if piece[0] == 0 or piece[1] == 0:
        return True
    if piece[0] == sk_settings.screen_size[0] - sk_settings.snake_width or piece[1] == sk_settings.screen_size[1] - sk_settings.snake_height:
        return True
    return False

def draw_screen(screen, sk_settings):
    """绘制屏幕"""
    pieces = []
    flag = 1
    for x in range(0, sk_settings.screen_size[0], sk_settings.snake_width):
        for y in range(0, sk_settings.screen_size[1], sk_settings.snake_height):
            piece = [x,y]
            pieces.append(list(piece))
    for piece in pieces:
        if piece[1] == sk_settings.snake_height:
            if flag == 1:
                flag = 0
            elif flag == 0:
                flag = 1
        if flag == 0 and not edges(piece, sk_settings):
            pygame.draw.rect(screen, (167, 217, 72), ((piece[0], piece[1]), (sk_settings.snake_width, sk_settings.snake_height)))
            flag = 1
            continue
        if flag == 1 and not edges(piece, sk_settings):
            pygame.draw.rect(screen, (142, 204, 57), ((piece[0], piece[1]), (sk_settings.snake_width, sk_settings.snake_height)))
            flag = 0
            continue
        if edges(piece, sk_settings):
            pygame.draw.rect(screen, (87, 138, 52), ((piece[0], piece[1]), (sk_settings.snake_width, sk_settings.snake_height)))
    #绘制得分板
    food_score_image = pygame.transform.smoothscale(pygame.image.load("images/food_score.png"), (sk_settings.snake_width - 4, sk_settings.snake_height - 4))
    screen.blit(food_score_image, (sk_settings.snake_width,2))
    highest_score_image = pygame.transform.smoothscale(pygame.image.load("images/highest_score.png"), (sk_settings.snake_width - 4, sk_settings.snake_height - 4))
    screen.blit(highest_score_image, (sk_settings.snake_width * 3, 2))

def check_keydown_events(event, snake, stats):
    if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
        snake.changeDirection = 'right'
    elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
        snake.changeDirection = 'left'
    elif event.key == pygame.K_UP or event.key == pygame.K_w:
        snake.changeDirection = 'up'
    elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
        snake.changeDirection = 'down'
    
def check_events(snake, button, stats):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, snake, stats)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            play_button_clicked = button.play_rect.collidepoint(mouse_x, mouse_y)
            if play_button_clicked:
                pygame.mouse.set_visible(False)
                stats.game_active = True
            volume_button_clicked = button.volume_rect.collidepoint(mouse_x, mouse_y)
            if volume_button_clicked:
                if stats.music_active:
                    stats.music_active = False
                else:
                    stats.music_active = True        

def check_death(snake, sk_settings):
    if snake.head[0] < sk_settings.snake_width or snake.head[0] >= sk_settings.screen_size[0] - sk_settings.snake_width:
        return True
    if snake.head[1] < sk_settings.snake_height or snake.head[1] >= sk_settings.screen_size[1] - sk_settings.snake_height:
        return True
    for segment in snake.segments[1:]:
        if snake.head[0] == segment[0] and snake.head[1] == segment[1]:
            return True
    return False

def snake_move(snake):
    snake.change_direction()
    snake.move()
    snake.segments.insert(0, list(snake.head))

def snake_eat(food, snake, score, stats, sk_settings):
    if snake.head[0] == food.x and snake.head[1] == food.y:
        if stats.music_active:
            eat_music = pygame.mixer.Sound("musics/eat_music.wav")
            eat_music.play()
        food.set_position(snake)
        food.image_number = random.randint(0,8)
        score.food += 1
        if score.food > 3:
            sk_settings.game_speed = 6
        score.prep_food_score()
    else:
        snake.segments.pop()

def reset_game(screen, sk_settings, snake, score, stats, food):
    stats.first_game = False
    snake.head = [snake.screen_rect.centerx, snake.screen_rect.centery]
    snake.segments = []
    snake.direction = 'right'
    snake.changeDirection = 'right'
    snake.create_snake_segments()
    food.set_position(snake)
    score.food = 0
    score.prep_food_score()

def update_screen(screen, snake, food, score, button, stats, sk_settings):
    screen.fill(sk_settings.bg_color)
    draw_screen(screen, sk_settings)
    score.show()
    if stats.music_active:
        button.draw_volume_button(0)
    else:
        button.draw_volume_button(1)
    if stats.game_active:
        snake.draw_snake()
        food.draw_food()
    else:
        if stats.first_game:
            button.draw_play_button()
        else:
            button.draw_replay_button()
        
    pygame.display.flip()
