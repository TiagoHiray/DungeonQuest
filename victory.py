from settings import *
import pygame

class VictoryTitle:
    def __init__(self):
        self.text = ''
        self.color = 'white'

class ScoreResult:
    def __init__(self):
        self.text = 'Sua pontuação final: '
        self.color = 'white'

class ReturnMainMenuButton:
    def __init__(self):
        self.rect = pygame.Rect((WIDTH/2) - 110, HEIGHT/1.3, (WIDTH/4)/1.05, 85)
        self.color_active = (255,255,255)
        self.color_inactive = (0,0,0)
        self.color_border = self.color_active
        self.color = self.color_inactive
        self.return_label = 'Retornar ao menu'
        self.return_label_surf = ''
        self.return_label_rect = ''

class VictoryScreen:
    def __init__(self):
        self.victory_title = VictoryTitle()
        self.score_result = ScoreResult()
        self.return_menu_button = ReturnMainMenuButton()

    def play_victory_music(self):
        #   música
        pygame.mixer.music.stop()
        self.music = pygame.mixer.music.load('assets/audio/music/victory.wav')
        pygame.mixer.music.play(-1)