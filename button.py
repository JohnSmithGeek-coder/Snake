import pygame
class Button():
    def __init__(self, screen, sk_settings):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.sk_settings = sk_settings
        #play按钮
        self.play_image = pygame.image.load("images/play.png")
        self.play_rect = self.play_image.get_rect()
        self.play_rect.centerx = self.screen_rect.centerx
        self.play_rect.centery = self.screen_rect.centery
        #音量/静音按钮
        self.volume_images = []
        self.volume_image = pygame.transform.smoothscale(pygame.image.load("images/volume_button.png"), (30, 30))
        self.volume_images.append(self.volume_image)
        self.volume_image = pygame.transform.smoothscale(pygame.image.load("images/mute_button.png"), (30, 30))
        self.volume_images.append(self.volume_image)
        self.volume_rect = self.volume_image.get_rect()
        self.volume_rect.x = self.sk_settings.screen_size[0] - 80
        self.volume_rect.centery = 20
        #退出按钮

        #重玩按钮
        self.replay_image = pygame.image.load("images/replay.png")
        self.replay_rect = self.replay_image.get_rect()
        self.replay_rect.centerx = self.screen_rect.centerx
        self.replay_rect.centery = self.screen_rect.centery
    def draw_play_button(self):
        self.screen.blit(self.play_image, self.play_rect)
    def draw_volume_button(self, number):
        self.screen.blit(self.volume_images[number], self.volume_rect)
    def draw_replay_button(self):
        self.screen.blit(self.replay_image, self.replay_rect)

