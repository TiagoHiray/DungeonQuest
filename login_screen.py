import pygame
from settings import *

class SubmitButton:
    def __init__(self):
        self.border_rect = pygame.Rect(WIDTH/3, HEIGHT/1.27, WIDTH/3, 50)
        self.rect = pygame.Rect(WIDTH/3, HEIGHT/1.27, WIDTH/3, 50)
        self.color_active = (255,255,255)
        self.color_inactive = (0,0,0)
        self.color_border = self.color_active
        self.color = self.color_inactive
        self.text_color = self.color_active
        self.submit_label = ''
        self.load_delay = 0
        self.active = False
        self.loading = False
        self.connection_failed = ''

class LoginInputBox:
    def __init__(self):
        self.input_rect = pygame.Rect(WIDTH/3, HEIGHT/1.90, WIDTH/3, 50)
        self.color = (0,0,0)
        self.color_border_active = (255,255,255)
        self.color_border_inactive = 'gray5'
        self.color_border = self.color_border_inactive
        self.active = False

class PasswordInputBox:
    def __init__(self):
        self.input_rect = pygame.Rect(WIDTH/3, HEIGHT/1.55, WIDTH/3, 50)
        self.color = (0,0,0)
        self.color_border_active = (255,255,255)
        self.color_border_inactive = 'gray5'
        self.color_border = self.color_border_inactive
        self.active = False

class Logo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('assets/sprites/logo.png').convert_alpha()
        self.image = pygame.transform.scale_by(self.image, 5)
        self.rect = self.image.get_rect(midtop = (WIDTH/2, 159))
        self.gravity = 0
        self.bounce = False
        self.bounce_timer = pygame.USEREVENT  + 1
        pygame.time.set_timer(self.bounce_timer, 750)

    def logo_bounce(self):
        if self.rect.y <= 150: self.bounce = False
        elif self.rect.y >= 160: self.bounce = True
        if self.gravity >= 1: self.gravity = 0
        if self.bounce == False:
            self.gravity += 0.05
            self.rect.y += int(self.gravity)
        else:
            self.gravity += 0.05
            self.rect.y -= int(self.gravity)

class LoginBackground:
    def __init__(self):
        self.image = pygame.image.load('assets/sprites/backgrounds/login_background.png')
        self.image = pygame.transform.scale_by(self.image, 6)
        self.rect = self.image.get_rect(topleft = (0,0))


class LoginScreen:
    def __init__(self):
        self.logo = pygame.sprite.GroupSingle()
        self.logo.add(Logo())
        self.background = LoginBackground()
        self.login_label = ''
        self.login_label_rect = ''
        self.login_input = LoginInputBox()
        self.password_input = PasswordInputBox()
        self.submit_button = SubmitButton()

    # def logo_bounce(self):
    #     if self.logo.rect.y > 150:
    #         self.logo.gravity -= 1
    #     elif self.logo.rect.y < 200:
    #         self.logo.gravity += 1
        

