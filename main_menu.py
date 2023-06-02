import pygame
from settings import *
from main import *
from game import *

# main menu
#   botao de entrar em sala
class JoinRoomButton:
    def __init__(self):
        self.rect = pygame.Rect((WIDTH/4), HEIGHT/2, (WIDTH/4)/1.05, 85)
        self.color_active = (255,255,255)
        self.color_inactive = (0,0,0)
        self.color_border = self.color_active
        self.color = self.color_inactive
        self.join_room_label = 'Juntar-se à Sala'
        self.join_room_label_surf = ''
        self.join_room_label_rect = ''
#   botao de criar sala
class CreateRoomButton:
    def __init__(self):
        self.rect = pygame.Rect((WIDTH/4) + (WIDTH/4)/1.2 + 50, HEIGHT/2, (WIDTH/4)/1.05, 85)
        self.color_active = (255,255,255)
        self.color_inactive = (0,0,0)
        self.color_border = self.color_active
        self.color = self.color_inactive
        self.create_room_label = 'Criar Sala'
        self.create_room_label_surf = ''
        self.create_room_label_rect = ''
#   fundo do menu principal
class MainMenuBackground:
    def __init__(self):
        self.image = pygame.image.load('dungeon_quest-main/game/assets/sprites/backgrounds/login_background.png')
        self.image = pygame.transform.scale_by(self.image, 6)
        self.rect = self.image.get_rect(topleft = (0,0))
#   logo do menu
class Logo(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('dungeon_quest-main/game/assets/sprites/logo.png').convert_alpha()
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

# join room menu
#   titulo do menu
class MenuTitle:
    def __init__(self):
        self.text = 'Insira o código da sala:'
        self.color = 'white'
#   botao de deletar texto do input
class DeleteInputButton:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH/3 + 370, HEIGHT/2.5 + 50, 75, 75)
        self.color = 'white'

    def deletar_texto(self, input_text):
        input_text = ''
        return input_text
#   input do token de sala
class RoomTokenInput:
    def __init__(self):
        self.input_rect = pygame.Rect(WIDTH/3 - 25, HEIGHT/2.5, WIDTH/3 + 50, 125)
        self.color_border_active = (255,255,255)
        self.color_border_inactive = 'gray5'
        self.color = (0,0,0)
        self.color_border = self.color_border_inactive
        self.active = False
        self.border_radius = 2
        self.room_token_text_surf = ''
        self.room_token_text_rect = ''
        self.delete_input_button = DeleteInputButton()
#   botao de conectar a sala
class RoomConnectButton:
    def __init__(self):
        self.rect = pygame.Rect((WIDTH/2) - 110, HEIGHT/1.3, (WIDTH/4)/1.05, 85)
        self.color_active = (255,255,255)
        self.color_inactive = (0,0,0)
        self.color_border = self.color_active
        self.color = self.color_inactive
        self.join_room_label = 'Conectar'
        self.join_room_label_surf = ''
        self.join_room_label_rect = ''
    
    def connect_room(self):
        pass

# classes de cada submenu do menu principal
class ReturnButton:
    def __init__(self):
        self.rect = pygame.Rect(30, 30, 75, 75)
        self.color = 'white'

    def update_menu(self, menu):
        return menu

class MainMenu:
    def __init__(self):
        self.logo = pygame.sprite.GroupSingle()
        self.logo.add(Logo())
        self.background = MainMenuBackground()
        self.join_room_button = JoinRoomButton()
        self.create_room_button = CreateRoomButton()

class CreateRoomMenu:
    def __init__(self):
        self.room_token_input = RoomTokenInput()

class JoinRoomMenu:
    def __init__(self):
        self.room_token_input = RoomTokenInput()
        self.menu_title = MenuTitle()
        self.room_connect_button = RoomConnectButton()

class MainMenuScreen:
    def __init__(self):
        self.curr_menu = 0
        self.main_menu = MainMenu()
        self.create_room_menu = CreateRoomMenu()
        self.join_room_menu = JoinRoomMenu()
        self.return_button = ReturnButton()
        self.select_audio = pygame.mixer.Sound('dungeon_quest-main/game/assets/audio/effects/select.wav')
        self.play_title_music()

    def play_title_music(self):
        #   música
        pygame.mixer.music.stop()
        self.music = pygame.mixer.music.load('dungeon_quest-main/game/assets/audio/music/title.wav')
        pygame.mixer.music.play(-1)
