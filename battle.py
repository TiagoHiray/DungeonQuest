import pygame
import random as rd

from questions import *
from char import *
from campaign import *

from settings import *
from main import *

class TryAgainButton:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH/4 + 125, HEIGHT - 200, (WIDTH/4)/1.05, 85)
        self.color_active = (255,255,255)
        self.color_inactive = (0,0,0)
        self.color_border = self.color_active
        self.color = self.color_inactive
        self.try_again_button_label = 'Tente Novamente'

class ContinueButton:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH/4 + 125, HEIGHT - 200, (WIDTH/4)/1.05, 85)
        self.color_active = (255,255,255)
        self.color_inactive = (0,0,0)
        self.color_border = self.color_active
        self.color = self.color_inactive
        self.continue_button_label = 'Continuar'
        
class Victory:
    def __init__(self, obt_score, enemy):
        self.victory_label = f'Você venceu!'
        self.enemy_defeat_label = f'{enemy.sprite.screename} foi derrotado! Por agora...'
        self.points_obtained = f'Pontos obtidos: {obt_score}'
        self.continue_button = ContinueButton()

class GameOver:
    def __init__(self, player):
        self.defeat_label = f'Fim da Linha...'
        self.defeat_player_label = f'{player.sprite.screename}, não desista! Se levante e tente novamente!'
        self.try_again_button_label = 'Tente Novamente'
        self.try_again_button = TryAgainButton()

class AnswerFairy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale_by(pygame.image.load('C:/Users/tihir/Downloads/dungeon_quest-main (3)/dungeon_quest-main/game/assets/sprites/characters/answer fairy/answer_fairy.png').convert_alpha(), 6)
        self.rect = self.image.get_rect(bottomleft = (100, 225))
        self.up = False
        self.bounce_vlt = 1
    
    def bounce(self):
        if self.rect.y <= 150:
            self.up = False
        elif self.rect.y >= 200:
            self.up = True
        if self.up == False:
            self.rect.y += self.bounce_vlt
        else:
            self.rect.y -= self.bounce_vlt


class TextBox:
    def __init__(self):
        self.border_rect = pygame.Rect(0, HEIGHT/2+30, WIDTH, 200)
        self.rect = pygame.Rect(6, HEIGHT/2+36, WIDTH-12, 200-12)
        self.color = (0,0,0)
        self.color_border = (255,255,255)

class QuestionAlternativeBox:
    def __init__(self, pos):
        self.color_inactive = (0,0,0)
        self.color_active = (255,255,255)
        self.color_border_inactive = 'gray15'
        self.color_border_active = (255,255,255)

        self.color = self.color_inactive
        self.color_border = self.color_border_inactive
        self.color_text = self.color_active
        self.hover = False
        self.clicked = False

        if pos == 1:
            self.border_rect = pygame.Rect(0, HEIGHT/2 + 200 +30, WIDTH/2, 100)
            self.rect = pygame.Rect(6, HEIGHT/2 + 206 +30, WIDTH/2-12, 100-12)
        elif pos == 2:
            self.border_rect = pygame.Rect(WIDTH/2, HEIGHT/2 + 200 +30, WIDTH/2, 100)
            self.rect = pygame.Rect(WIDTH/2 + 6, HEIGHT/2 + 206 +30, WIDTH/2-12, 100-12)
        elif pos == 3:
            self.border_rect = pygame.Rect(0, HEIGHT/2 + 300 +30, WIDTH/2, 100)
            self.rect = pygame.Rect(6, HEIGHT/2 + 306 +30, WIDTH/2-12, 100-12)
        else:
            self.border_rect = pygame.Rect(WIDTH/2, HEIGHT/2 + 300 +30, WIDTH/2, 100)
            self.rect = pygame.Rect(WIDTH/2 + 6, HEIGHT/2 + 306 +30, WIDTH/2-12, 100-12)


class Battle:
    def __init__(self, player, enemy):
        self.battle_status = 0
        # 0 - em andamento
        # 1 - derrota
        # 2 - vitória
        self.text_on_screen = 0
        self.proceedable = False
        self.jogador_atacando = False
        self.inimigo_atacando = False
        self.questoes = questoes
        self.questoes_reserva = questoes
        # score
        self.scoreboard_surf = ''
        self.scoreboard_rect = ''
        self.curr_score = 0
        self.answer_streak = 1
        # montar ui
        self.text_box = TextBox()
        self.alternative1 = QuestionAlternativeBox(1)
        self.alternative2 = QuestionAlternativeBox(2)
        self.alternative3 = QuestionAlternativeBox(3)
        self.alternative4 = QuestionAlternativeBox(4)
        self.text_box_text_line_1 = ''
        self.text_box_text_line_2 = ''
        self.text_box_text_line_3 = ''
        self.text_box_text_line_4 = ''
        self.alternative1_text = ''
        self.alternative2_text = ''
        self.alternative3_text = ''
        self.alternative4_text = ''
        # montar cenário
        #   fundo
        #       chão
        self.floor_img = pygame.transform.scale_by(pygame.image.load('dungeon_quest-main/game/assets/sprites/backgrounds/floor/floor.png').convert_alpha(), 6)
        self.floor_rect = self.floor_img.get_rect(topleft = (0,-325))
        #       luz
        self.light_img = pygame.transform.scale_by(pygame.image.load('dungeon_quest-main/game/assets/sprites/backgrounds/light/light.png').convert_alpha(), 6)
        self.light_rect = self.light_img.get_rect(topleft = (0,-325))
        #   iterar personagens
        #       jogador
        self.player = pygame.sprite.GroupSingle()
        self.player.add(player)
        #       inimigo
        self.enemy = pygame.sprite.GroupSingle()
        self.enemy.add(enemy)
        # tela game over e tela vitoria
        self.victory = Victory(self.curr_score, self.enemy)
        self.defeat = GameOver(self.player)
        #       fada das respostas
        self.fairy = pygame.sprite.GroupSingle()
        self.fairy.add(AnswerFairy())
        # áudio
        #   sons
        self.select_audio = pygame.mixer.Sound('dungeon_quest-main/game/assets/audio/effects/select.wav')
        self.correct_audio = pygame.mixer.Sound('dungeon_quest-main/game/assets/audio/effects/correct.wav')
        #   métodos
        self.update_text()
    
    def set_enemy(self, enemy):
        self.enemy = pygame.sprite.GroupSingle()
        self.enemy.add(enemy)
    
    def update_score(self, value):
        if self.enemy.sprite.type == 'normal': self.curr_score += int(((value * self.enemy.sprite.health_bar.hp_max)/15 + (value * self.answer_streak)) + value * 0.5)    
        else: self.curr_score += int((value * self.enemy.sprite.health_bar.hp_max)/15 + value * self.answer_streak)

    def update_text(self):
        self.proceedable = False
        if self.text_on_screen == 0:
            self.text_box_text = f'* Cuidado, {self.player.sprite.name}! Você encontrou um {self.enemy.sprite.screename}!'
            self.text_on_screen = 1
            self.proceedable = True
        elif self.text_on_screen == 1:
            self.text_box_text = f'* {self.enemy.sprite.screename}: Sucumba!'
            self.text_on_screen = 2
            self.proceedable = True
        elif self.text_on_screen == 2:
            self.update_questao()
        elif self.text_on_screen == 3:
            self.update_score(75)
            pygame.mixer.Sound.play(self.correct_audio)
            self.text_box_text = f'* Resposta correta!'
            self.answer_streak += 1
            self.text_on_screen = 5
            self.proceedable = True
        elif self.text_on_screen == 4:
            self.text_box_text = f'* Resposta incorreta!'
            self.answer_streak = 1
            self.text_on_screen = 6
            self.proceedable = True
        elif self.text_on_screen == 5:
            self.text_box_text = f'* {self.player.sprite.name} realiza um ataque devastador em {self.enemy.sprite.screename}!'
            self.player.sprite.atacar(self.enemy.sprite)
            self.jogador_atacando = True
            self.text_on_screen = 2
            self.proceedable = True
        elif self.text_on_screen == 6:
            self.text_box_text = f'* {self.enemy.sprite.screename} ataca {self.player.sprite.name} brutalmente!'
            self.enemy.sprite.atacar(self.player.sprite)
            self.inimigo_atacando = True
            self.text_on_screen = 9
            self.proceedable = True
        elif self.text_on_screen == 7:
            self.text_box_text = f'* {self.player.sprite.name} foi derrotado! Não desista! Tente novamente...'
            self.text_on_screen = ''
            self.proceedable = True
        elif self.text_on_screen == 8:
            self.text_box_text = f'* {self.enemy.sprite.screename} foi derrotado! Vá em frente {self.player.sprite.screename}!'
            self.text_on_screen = ''
            self.proceedable = True
        elif self.text_on_screen == 9:
            self.text_box_text = f'* Fada das Respostas: {self.active_question.feedback}'
            self.text_on_screen = 2
            self.proceedable = True
        elif self.player.sprite.dead == True and self.text_on_screen == '':
            self.battle_status = 1
        elif self.enemy.sprite.dead == True and self.text_on_screen == '':
            self.battle_status = 2
        else:
            pygame.quit()

    def proceed_text(self):
        if self.proceedable == True:
            self.update_text()
    
    def update_questao(self):
        if self.player.sprite.dead == False and self.enemy.sprite.dead == False:
            self.proceedable = False
            if self.questoes == []:
                self.questoes = self.questoes_reserva
            self.questao_escolhida = rd.choice(self.questoes)
            self.questoes.remove(self.questao_escolhida)
            self.active_question = self.questao_escolhida
                    # organizar atributos do objeto questao na ui
            self.text_box_text = '* ' + self.active_question.enunciation
            self.alternative1_text = 'a) ' + self.active_question.alternatives[0]
            self.alternative2_text = 'b) ' + self.active_question.alternatives[1]
            self.alternative3_text = 'c) ' + self.active_question.alternatives[2]
            self.alternative4_text = 'd) ' + self.active_question.alternatives[3]
        elif self.player.sprite.dead == True:
            self.text_box_text = ''
            self.alternative1_text = ''
            self.alternative2_text = ''
            self.alternative3_text = ''
            self.alternative4_text = ''
            self.text_on_screen = 7
            self.update_text()
        else:
            self.text_box_text = ''
            self.alternative1_text = ''
            self.alternative2_text = ''
            self.alternative3_text = ''
            self.alternative4_text = ''
            self.text_on_screen = 8
            self.update_text()      

    def selecionar_alternativa(self, alternativa):
        pygame.mixer.Sound.play(self.select_audio)
        if self.active_question.answer == alternativa:
            self.text_on_screen = 3
            self.proceedable = True
            self.update_text()
        else:
            self.text_on_screen = 4
            self.proceedable = True
            self.update_text()


class BattleScreen:
    def __init__(self):
        pass
    
    def play_battle_music(self):
        #   música
        pygame.mixer.music.stop()
        self.music = pygame.mixer.music.load('dungeon_quest-main/game/assets/audio/music/battle.wav')
        pygame.mixer.music.play(-1)
        
