import pygame
import random as rd
import mysql.connector

from questions import *
from bd_conn import *
from settings import *

# conexao com o banco
conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password=SENHA_BD,
    database="dungeonQuest"
)

cursor = conexao.cursor()


class RoomBG(pygame.sprite.Sprite):
    def __init__(self) :
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load('assets/sprites/backgrounds/dungeon_entrance/dungeon_entrance.png').convert_alpha(), 6)
        self.rect = self.image.get_rect(center = (WIDTH/2, HEIGHT/2))

class MiniPlayer(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        # imagens
        self.idle = [pygame.transform.scale_by(pygame.image.load('assets\sprites\characters\mini player\mini_player_idle_1.png').convert_alpha(), 6), pygame.transform.scale_by(pygame.image.load('assets\sprites\characters\mini player\mini_player_idle_2.png').convert_alpha(), 6)]
        # times e indices de animacao
        self.idle_index = rd.randint(0,1)
        self.idle_timer = 0
        # componentes de sprite
        self.image = self.idle[self.idle_index]
        self.rect = self.image.get_rect(center = (WIDTH/2, HEIGHT/2))
    
    def animate(self):
        self.idle_timer += 1
        if self.idle_timer == 30:
            if self.idle_index == 0: self.idle_index += 1
            elif self.idle_index == 1: self.idle_index -= 1
            self.image = self.idle[self.idle_index]
            self.idle_timer = rd.randint(0,5)

# componentes de sala
#   título da sala
class RoomTitle:
    def __init__(self):
        self.room_title_text = ''
    
    def def_owner(self, owner):
        try:
            self.room_title_text = 'Sala de ' + owner
        except:
            self.room_title_text = 'Sala de indefinido'
#   capacidade     
class Capacity:
    def __init__(self, room_id, curr_players):
        self.room_id = room_id
        self.curr_players = curr_players
        self.cap = 10
#   botao iniciar jogo
class StartGameButton:
    def __init__(self):
        self.rect = pygame.Rect((WIDTH/2-115), HEIGHT/1.2, (WIDTH/4)/1.05, 85)
        self.color_active = (255,255,255)
        self.color_inactive = (0,0,0)
        self.color_border = self.color_active
        self.color = self.color_inactive
        self.join_room_label = 'Iniciar Jogo'
        self.join_room_label_surf = ''
        self.join_room_label_rect = ''
#   botao fechar sala
class CloseGameButton:
    def __init__(self):
        self.rect = pygame.Rect((WIDTH/2-115), HEIGHT/1.2, (WIDTH/4)/1.05, 85)
        self.color_active = (255,255,255)
        self.color_inactive = (0,0,0)
        self.color_border = self.color_active
        self.color = self.color_inactive
        self.join_room_label = 'Fechar Sala'
        self.join_room_label_surf = ''
        self.join_room_label_rect = ''
    
    def close_room(self, user):
        query = 'DELETE FROM Sala WHERE donoSala = %s'
        cursor.execute(query, (user.id,))
        conexao.commit()
#   room token
class RoomTokenText:
    def __init__(self):
        self.text = 'Código da sala: '
        self.color = 'white'
        self.image = ''
        self.rect = ''

class ReturnButton(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load('assets/sprites/ui/buttons/returnbutton.png'), 6)
        self.rect = self.image.get_rect(topleft = (30, 30))
        self.color = 'white'

# sala
class Room:
    def __init__(self, room_id, token, owner, current_players, subject, levels):
        self.room_id = room_id
        self.subject = subject
        self.token = token
        self.levels = levels
        self.owner_id = owner
        # fundo da sala
        self.room_bg = pygame.sprite.GroupSingle()
        self.room_bg.add(RoomBG())
        # titulo da sala
        self.room_title = RoomTitle()
        self.room_title.def_owner(self.find_owner_name(owner))
        # capacidade
        self.capacity = Capacity(room_id, self.get_player_qty())
        # código da sala
        self.token_text = RoomTokenText()
        # botão de iniciar jogo
        self.start_game_button = StartGameButton()
        # botão deletar sala
        self.close_room_button = CloseGameButton()
        # jogadores
        self.players = pygame.sprite.Group()
        self.spawn_players()

    def find_owner_name(self, owner):
        query = "SELECT loginUsuario FROM Usuario WHERE idUsuario = %s"
        cursor.execute(query, (owner,))
        result = cursor.fetchone()
        return result[0]
    
    def spawn_players(self):
        y = HEIGHT - 425
        for player in range(10):
            mini_player = MiniPlayer()
            mini_player.rect.x, mini_player.rect.y = rd.randint(325, WIDTH-325), y
            self.players.add(mini_player)
            y += rd.randint(5, 12)

    def update_players(self):
        qty = self.get_player_qty()
        for p in self.players.sprites():
            if self.players.sprites().index(p) < qty:
                p.image.set_alpha(255)
            else:
                p.image.set_alpha(0)
            
    def get_player_qty(self):
        query = "SELECT qntdJogadores FROM Sala WHERE idSala = %s"
        cursor.execute(query, (self.room_id,))
        result = cursor.fetchone()
        return result[0]


class RoomScreen:
    def __init__(self):
        self.room_side = ''
        self.room = ''
        # botão de sair da sala
        self.return_button = pygame.sprite.GroupSingle()
        self.return_button.add(ReturnButton())

    def set_room_side(self, user):
        query = "SELECT * FROM Sala WHERE donoSala = %s"

        # Executar a consulta passando o token como parâmetro
        cursor.execute(query, (user.id,))

        # Recuperar o resultado da consulta
        exists = cursor.fetchone()

        # Retornar True se o token existe, False caso contrário
        if bool(exists) == True:
            self.room_side = 'owner'
        else:
            self.room_side = 'player'




