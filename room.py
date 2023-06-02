import pygame

from settings import *


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


# sala
class Room:
    def __init__(self, room_id, token, owner, current_players, subject_id):
        self.room_id = room_id
        self.subject_id = subject_id
        self.token = token
        # titulo da sala
        self.room_title = RoomTitle()
        self.room_title.def_owner(owner)
        # capacidade
        self.capacity = Capacity(room_id, current_players)
        # botão de iniciar jogo
        self.start_game_button = StartGameButton()
    
    def room_connect(self, inserted_token):
        if inserted_token == self.token:
            return True
        else:
            return False

class RoomScreen:
    def __init__(self):
        self.room = Room(1, '111111', 'Marquito', 0, 1)


