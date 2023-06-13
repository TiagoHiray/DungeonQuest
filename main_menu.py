import pygame
import random as rd
import mysql.connector

from settings import *
from bd_conn import *

from game import *
from room import *

# main menu
#   bem vindo jogador
class WelcomePlayer:
    def __init__(self):
        self.text = 'Seja bem vindo, '
        self.color = 'white'
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
        self.image = pygame.image.load('assets/sprites/backgrounds/login_background.png')
        self.image = pygame.transform.scale_by(self.image, 6)
        self.rect = self.image.get_rect(topleft = (0,0))
#   logo do menu
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

# join room menu
#   titulo do menu
class JoinMenuTitle:
    def __init__(self):
        self.text = 'Insira o código da sala:'
        self.color = 'white'
#   botao de deletar texto do input
class DeleteInputButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load('assets/sprites/ui/buttons/xbutton.png'), 6)
        self.rect = self.image.get_rect(topleft = (WIDTH/3 + 370, HEIGHT/2.5 + 25))
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
    
    def connect_room(self, token):
        query = "SELECT * FROM Sala WHERE tokenSala = %s"

        # Executar a consulta passando o token como parâmetro
        cursor.execute(query, (token,))
        result = cursor.fetchone()

        room = Room(result[0], result[2], result[5], result[3], result[1], result[4])

        return room

    def increase_capacity(self, room_id):
        query = "UPDATE Sala SET qntdJogadores = qntdJogadores + 1 WHERE idSala = %s"
        cursor.execute(query, (room_id,))
        conexao.commit()

#   aviso de erro
class ConnectionErrorPopup:
    def __init__(self, text):
        self.message = text
        self.color = 'white'
        self.active = False
        self.active_timer = 0

    def get_owner_room_token(self, user):
        query = 'SELECT * FROM Sala WHERE donoSala = %s'
        cursor.execute(query, (user.id,))
        resultado = cursor.fetchone()
        if resultado == None:
            resultado = ''
        else:
            resultado = resultado[2]
        return resultado

# create room menu
#   titulo do menu
class CreateMenuTitle:
    def __init__(self):
        self.text = 'Crie sua sala:'
        self.color = 'white'
#   botao de capacidade
class LevelButton(pygame.sprite.Sprite):
    def __init__(self, qty):
        super().__init__()
        self.qty = qty
        self.active = False
        self.inactive_surf = pygame.transform.scale_by(pygame.image.load(f'assets/sprites/ui/buttons/capacitybutton{str(qty)}.png').convert_alpha(), 6)
        self.active_surf = pygame.transform.scale_by(pygame.image.load(f'assets/sprites/ui/buttons/capacitybutton{str(qty)}_active.png').convert_alpha(), 6)
        self.image = self.inactive_surf
        if qty == 5:
            self.x_pos = WIDTH/3
        elif qty == 10:
            self.x_pos = WIDTH/3 + 95
        else:
            self.x_pos = WIDTH/3 + 190
        self.x_pos += 15
        self.rect = self.image.get_rect(bottomleft = (self.x_pos, 350))
    
    def toggle_button(self):
        if self.active == True:
            self.image = self.active_surf
        else:
            self.image = self.inactive_surf
#   botao de materias
class SubjectButton(pygame.sprite.Sprite):
    def __init__(self, subj):
        super().__init__()
        self.subj = subj
        self.active = False
        self.inactive_surf = pygame.transform.scale_by(pygame.image.load(f'assets/sprites/ui/buttons/{subj}_button.png').convert_alpha(), 6)
        self.active_surf = pygame.transform.scale_by(pygame.image.load(f'assets/sprites/ui/buttons/{subj}_button_active.png').convert_alpha(), 6)
        self.image = self.active_surf
        if subj == 'lp':
            self.x_pos = WIDTH/4 + 35
        elif subj == 'poo':
            self.x_pos = WIDTH/4 + 35 + 95
        elif subj == 'moo':
            self.x_pos = WIDTH/4 + 35 + 190
        else:
            self.x_pos = WIDTH/4 + 35 + 285
        self.x_pos += 15
        self.rect = self.image.get_rect(bottomleft = (self.x_pos, 475))

    def toggle_button(self):
        if self.active == True:
            self.image = self.active_surf
        else:
            self.image = self.inactive_surf
#   botao de confirmar sala
class ConfirmRoomButton:
    def __init__(self):
        self.rect = pygame.Rect((WIDTH/2) - 110, HEIGHT/1.3, (WIDTH/4)/1.05, 85)
        self.color_active = (255,255,255)
        self.color_inactive = (0,0,0)
        self.color_border = self.color_active
        self.color = self.color_inactive
        self.confirm_room_label = 'Criar Sala'
        self.confirm_room_label_surf = ''
        self.confirm_room_label_rect = ''

#   sala a ser criada
class RoomToCreate:
    def __init__(self):
        self.levels = 0
        self.subj = ''
        self.token = ''

    def gerar_token(self):
        for digit in range(6):
            digit = rd.randint(0,9)
            digit = str(digit)
            self.token = self.token + digit

    def inserir_dados(self, user):
        # Inserir os dados na tabela
            sql = "INSERT INTO Sala (materia, tokenSala, levels, qntdJogadores, donoSala) VALUES (%s, %s, %s, 0, %s)"
            valores = (self.subj, self.token, self.levels, user.id)
            cursor.execute(sql, valores)

            # Confirmar a inserção
            conexao.commit()

# submenus
class ReturnButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load('assets/sprites/ui/buttons/returnbutton.png'), 6)
        self.rect = self.image.get_rect(topleft = (30, 30))
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
        self.welcome_player = WelcomePlayer()

class CreateRoomMenu:
    def __init__(self):
        self.menu_title = CreateMenuTitle()
        self.room_to_create = RoomToCreate()
        self.levelsbuttons = pygame.sprite.Group()
        self.levelsbuttons.add(LevelButton(5), LevelButton(10), LevelButton(15))
        self.subjectbuttons = pygame.sprite.Group()
        self.subjectbuttons.add(SubjectButton('lp'),SubjectButton('poo'),SubjectButton('moo'),SubjectButton('bd'))
        self.confirm_room_button = ConfirmRoomButton()
        self.create_error_popup = ConnectionErrorPopup('Sala já registrada, use esse código para acessar-la: ')

class JoinRoomMenu:
    def __init__(self):
        self.room_token_input = RoomTokenInput()
        self.menu_title = JoinMenuTitle()
        self.room_connect_button = RoomConnectButton()
        self.room_error_popup = ConnectionErrorPopup('Erro ao tentar conectar')

# tela menu
class MainMenuScreen:
    def __init__(self):
        self.curr_menu = 0
        self.main_menu = MainMenu()
        self.create_room_menu = CreateRoomMenu()
        self.join_room_menu = JoinRoomMenu()
        self.return_button = pygame.sprite.GroupSingle()
        self.return_button.add(ReturnButton())
        self.delete_input_button = pygame.sprite.GroupSingle()
        self.delete_input_button.add(DeleteInputButton())
        self.select_audio = pygame.mixer.Sound('assets/audio/effects/select.wav')
        self.play_title_music()


    def play_title_music(self):
        #   música
        pygame.mixer.music.stop()
        self.music = pygame.mixer.music.load('assets/audio/music/title.wav')
        pygame.mixer.music.play(-1)
