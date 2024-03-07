from __future__ import absolute_import, division, print_function
from itertools import cycle
import pygame,sys

class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 20)
        self.offset = - 140
        self.img = pygame.image.load("graphics/Pointing.gif")
        self.image = pygame.image.load("graphics/img.png")

    def draw_cursor(self):
        self.game.display_image(self.img,self.cursor_rect.x,self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()

class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Player 1"
        self.player1x, self.player1y = self.mid_w, self.mid_h + 30
        self.player2x, self.player2y = self.mid_w, self.mid_h + 70
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 110
        self.quitx, self.quity = self.mid_w, self.mid_h + 150
        self.startx, self.starty = self.mid_w, self.mid_h + 70
        self.cursor_rect.midtop = (self.player1x + self.offset, 280)
        

    def interface(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text("Press F1 to Start", 20, self.startx, self.starty)
            self.game.display_image(self.image,0,100)
            self.blit_screen()            

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            
            self.game.draw_text("1 PLAYER", 20, self.player1x, self.player1y)
            self.game.draw_text("2 PLAYER", 20, self.player2x, self.player2y)
            self.game.draw_text("CREDITS", 20, self.creditsx, self.creditsy)
            self.game.draw_text("QUIT", 20, self.quitx, self.quity)
            self.game.display_image(self.image,0,100)
            self.draw_cursor()
            self.blit_screen()


    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Player 1':
                self.cursor_rect.midtop = (self.player2x + self.offset, 315)
                self.state = 'Player 2'
            elif self.state == 'Player 2':
                self.cursor_rect.midtop = (self.creditsx + self.offset, 355)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.player1x + self.offset, 395)
                self.state = 'Quit'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.player1x + self.offset, 280)
                self.state = 'Player 1'
        elif self.game.UP_KEY:
            if self.state == 'Player 1':
                self.cursor_rect.midtop = (self.creditsx + self.offset, 395)
                self.state = 'Quit'
            elif self.state == 'Player 2':
                self.cursor_rect.midtop = (self.player1x + self.offset, 280)
                self.state = 'Player 1'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (self.player2x + self.offset, 315)
                self.state = 'Player 2'
            elif self.state == 'Quit':
                self.cursor_rect.midtop = (self.player1x + self.offset, 355)
                self.state = 'Credits'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Player 1':
                self.game.playing1 = True
            elif self.state == 'Player 2':
                self.game.playing2 = True
            elif self.state == 'Credits':
                self.credits()
            elif self.state == 'Quit':
                pygame.quit()
                sys.exit()

            self.run_display = False


    def credits(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.BACK_KEY:
                self.display_menu()
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Credits', 40, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by:', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 20)
            self.game.draw_text('Irtaza Arain', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 50)
            self.blit_screen()
