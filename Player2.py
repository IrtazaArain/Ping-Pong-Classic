import sys
import pygame
from pygame.locals import *
import main

speed = 5

class Pong(object):

    def __init__(self, screensize):

        self.screensize = screensize
        self.hit_edge_left = False
        self.hit_edge_right = False
        self.ping_sfx = pygame.mixer.Sound("sounds/ping.WAV")
        self.pong_sfx = pygame.mixer.Sound("sounds/pong.WAV")
        self.WHITE = (255, 255, 255)
        self.ball()

    def ball(self):

        self.centerx = int(self.screensize[0] * 0.5)
        self.centery = int(self.screensize[1] * 0.5)
        self.radius = 8
        self.rect = pygame.Rect(self.centerx - self.radius,
                                self.centery - self.radius,
                                self.radius * 2, self.radius * 2)

        self.color = self.WHITE
        self.direction = [1, 1]
        self.speed()

    def ball_reset(self):

        self.centerx = int(self.screensize[0] * 0.5)
        self.centery = int(self.screensize[1] * 0.5)
        self.radius = 8
        self.rect = pygame.Rect(self.centerx - self.radius,
                                self.centery - self.radius,
                                self.radius * 2, self.radius * 2)

        self.color = self.WHITE
        self.direction = [-1, 1]
        self.speed()

    def speed(self):

        global speed
        self.speedx = speed
        self.speedy = speed
        speed += 0.5


    def update(self, player_paddle, ai_paddle):

        global speed
        self.centerx += self.direction[0] * self.speedx
        self.centery += self.direction[1] * self.speedy

        self.rect.center = (self.centerx, self.centery)

        if self.rect.top <= 0:
            self.direction[1] = 1
        elif self.rect.bottom >= self.screensize[1] - 1:
            self.direction[1] = -1

        if self.rect.right >= self.screensize[0] - 1:
            self.hit_edge_right = True
            self.ball_reset()
            speed = 5
        elif self.rect.left <= 0:
            self.hit_edge_left = True
            self.ball()
            speed = 5

        if self.rect.colliderect(player_paddle.rect):
            self.direction[0] = -1
            self.ping_sfx.play()
            self.speed()
        if self.rect.colliderect(ai_paddle.rect):
            self.direction[0] = 1
            self.pong_sfx.play()
            self.speed()

    def render(self, screen):
        pygame.draw.circle(screen, self.color, self.rect.center, self.radius, 0)
        pygame.draw.circle(screen, (0, 0, 0), self.rect.center, self.radius, 1)

#creates the AI paddle
class PlayerPaddle2(object):
    def __init__(self, screensize):
        self.screensize = screensize

        self.centerx = 5
        self.centery = int(screensize[1]*0.5)

        #player paddle dimensions
        self.height = 100
        self.width = 20

        self.rect = pygame.Rect(0, self.centery-int(self.height*0.5),     self.width, self.height)

        self.color = (255,255,255)

        #player paddle speed
        self.speed = 10
        self.direction = 0

    def update(self):
        self.centery += self.direction*self.speed

        self.rect.center = (self.centerx, self.centery)
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screensize[1]-1:
            self.rect.bottom = self.screensize[1]-1

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0,0,0), self.rect, 1)

#creates the player paddle
class PlayerPaddle1(object):
    def __init__(self, screensize):
        self.screensize = screensize
        self.font = pygame.font.Font("fonts/PressStart2.ttf", 40)

        self.centerx = screensize[0]-5
        self.centery = int(screensize[1]*0.5)

        #player paddle dimensions
        self.height = 100
        self.width = 20

        self.rect = pygame.Rect(0, self.centery-int(self.height*0.5),     self.width, self.height)

        self.color = (255,255,255)

        #player paddle speed
        self.speed = 10
        self.direction = 0

    def update(self):
        self.centery += self.direction*self.speed

        self.rect.center = (self.centerx, self.centery)
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screensize[1]-1:
            self.rect.bottom = self.screensize[1]-1

    def render(self, screen):
        pygame.draw.rect(screen, self.color, self.rect, 0)
        pygame.draw.rect(screen, (0,0,0), self.rect, 1)

class EndScreen():
    
    def __init__(self, screen):
        self.screen = screen
        self.width = screen.get_width()
        self.height = screen.get_height()
        self.win_sfx = pygame.mixer.Sound("sounds/win.WAV")
        self.font = pygame.font.Font("fonts/PressStart2.ttf", 40)
        self.font2 = pygame.font.Font("fonts/PressStart2.ttf", 10)

    def p1_win(self):

        self.win_sfx.play()
        self.screen.fill(0)
        surface = self.font.render("Player 1 Win!", True, 'white')
        text_rect = surface.get_rect(center=(self.width//2,200))
        text_surface = self.font2.render("Press space bar to play again", True, 'white')
        text_rect2 = text_surface.get_rect(center=(self.width//2,300))

        self.screen.blit(text_surface, text_rect2)
        self.screen.blit(surface, text_rect)

        pygame.display.flip()

        waiting = True
        while waiting:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    pygame.quit()
                    sys.exit()
                   
                if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_SPACE:
                      waiting = False
                      obj = main
                      obj.main_loop()
                      pygame.quit()
                      sys.exit()

    def p2_win(self):

        self.win_sfx.play()
        self.screen.fill(0)
        surface = self.font.render("Player 2 Win!", True, 'white')
        text_rect = surface.get_rect(center=(self.width//2,200))
        text_surface = self.font2.render("Press space bar to play again", True, 'white')
        text_rect2 = text_surface.get_rect(center=(self.width//2,300))

        self.screen.blit(text_surface, text_rect2)
        self.screen.blit(surface, text_rect)

        pygame.display.flip()

        waiting = True
        while waiting:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting = False
                    pygame.quit()
                    sys.exit()
                   
                if event.type == pygame.KEYDOWN:
                   if event.key == pygame.K_SPACE:
                      waiting = False
                      obj = main
                      obj.main_loop()
                      pygame.quit()
                      sys.exit()


def main_game():

    pygame.init()

    screensize = (960,540)

    BLACK = (0,0,0)
    WHITE = (255,255,255)

    screen = pygame.display.set_mode(screensize)

    pygame.display.set_caption("Ping-Pong Classic")

    clock = pygame.time.Clock()

    pong = Pong(screensize)
    player_paddle2 = PlayerPaddle2(screensize)
    player_paddle1 = PlayerPaddle1(screensize)

    running = True

    scoreA = 0
    scoreB = 0

    while running:

        clock.tick(64)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    player_paddle1.direction = -1
                elif event.key == K_DOWN:
                    player_paddle1.direction = 1
            if event.type == KEYUP:
                if event.key == K_UP and player_paddle1.direction == -1:
                    player_paddle1.direction = 0
                elif event.key == K_DOWN and player_paddle1.direction == 1:
                    player_paddle1.direction = 0

            if event.type == KEYDOWN:
                if event.key == K_w:
                    player_paddle2.direction = -1
                elif event.key == K_s:
                    player_paddle2.direction = 1
            if event.type == KEYUP:
                if event.key == K_w and player_paddle2.direction == -1:
                    player_paddle2.direction = 0
                elif event.key == K_s and player_paddle2.direction == 1:
                    player_paddle2.direction = 0


        player_paddle2.update()
        player_paddle1.update()
        pong.update(player_paddle1, player_paddle2)

        if pong.hit_edge_left:
            if scoreB <4:
                scoreB+=1
                pong.hit_edge_left = False
            else:
                Obj = EndScreen(screen)
                Obj.p1_win()

            
        if pong.hit_edge_right:
            if scoreA <4:
                scoreA+=1
                pong.hit_edge_right = False
            else:
                Obj = EndScreen(screen)
                Obj.p2_win()
            

        screen.fill(BLACK)

        pygame.draw.line(screen, WHITE, [480, 0], [480, 540], 10)
        player_paddle2.render(screen)
        player_paddle1.render(screen)
        pong.render(screen)

        #Display scores:
        font = pygame.font.Font(None, 74)
        text = font.render(str(scoreA), 1, WHITE)
        screen.blit(text, (410,10))
        text = font.render(str(scoreB), 1, WHITE)
        screen.blit(text, (525,10))

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_game()
