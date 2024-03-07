import pygame
from menu import *
import AI
import Player2


class Game():
    def __init__(self):
        pygame.init()
        self.running, self.playing1, self.playing2 = True, False, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 960, 540
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        pygame.display.set_caption("Ping-Pong Classic")
        self.background_music = pygame.mixer.Sound("sounds/super-match.WAV")
        self.background_music.play(-1)
        self.font_name = 'fonts/PressStart2.ttf'
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.curr_menu = self.main_menu

    def game_loop(self):
        while self.playing1:
            self.background_music.stop()
            AI.main_game()
        while self.playing2:
            self.background_music.stop()
            Player2.main_game()


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_F1:
                    self.curr_menu.display_menu()
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False

    def draw_text(self, text, size, x, y):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)

    def display_image(self, image, x, y):
        self.display.blit(image, (x,y))
