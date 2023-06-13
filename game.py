import pygame, sys

from login_screen import *
from main_menu import *
from battle import *
from room import *
from roadmap import *
from victory import *
from cadastro_questoes import *

from campaign import *
from user import *
from settings import *

class Game:

    # configs iniciais
    def __init__(self, user):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Dungeon Quest')
        self.clock = pygame.time.Clock()
        self.game_state = 1
        # self.pixel_font = pygame.font.Font('game/assets/fonts/Pixeled.ttf', 15)
        # self.pixel_font_smaller = pygame.font.Font('game/assets/fonts/Pixeled.ttf', 20)
        self.arkkos_font_bigger = pygame.font.Font('assets/fonts/ArKkos_Gmimi.ttf', 100)
        self.arkkos_font_big = pygame.font.Font('assets/fonts/ArKkos_Gmimi.ttf', 50)
        self.arkkos_font = pygame.font.Font('assets/fonts/ArKkos_Gmimi.ttf', 25)
        self.arkkos_font_smaller = pygame.font.Font('assets/fonts/ArKkos_Gmimi.ttf', 20)
        self.login_user_text = ''
        self.password_user_text = ''
        self.room_token_text = ''
        self.proceedable = False
        self.continue_campaign = False
        self.try_again_campaign = False
        # inimigos e chefes
        self.inimigos = [Enemy(0, 'skeleton', 'Esqueleto', 10, 5, 'normal'),
                         Enemy(1, 'mage', 'Mago', 15, 10, 'normal'),
                         Enemy(3, 'bats', 'Morcegos', 15, 10, 'normal'), 
                         Enemy(4, 'revenant', 'Revenã Sombrio', 20, 5, 'normal'),
                        ]
        self.chefes =   [Enemy(2, 'dragon', 'Dragão', 25, 15, 'chefe'),]
        # telas
        self.login_screen = LoginScreen()
        self.main_menu_screen = MainMenuScreen()
        self.battle_screen = BattleScreen()
        self.room_screen = RoomScreen()
        self.roadmap_screen = RoadmapScreen()
        self.victory_screen = VictoryScreen()
        # objetos
        self.campaign = Campaign()
        self.user = user

    # mudar o game state
    def change_game_state(self, state):
        self.game_state = state

    # objetos de tela
      
            # estados do jogo
            # 0 - tela de login
            # 1 - tela main menu
            # 2 - tela criar sala
            # 3 - tela entrar em sala
            # 4 - tela sala
            # 5 - tela do roadmap (meio que nem o overworld do mario com cada estágio demonstrando um monstro)
            # 6 - tela batalha
            # 7 - tela cadastrar questões
            # 8 - tela vitória

    # diferentes telas
    def tela_login(self):
                    # background
                    self.screen.blit(self.login_screen.background.image, self.login_screen.background.rect)

                    # logo
                    self.login_screen.logo.draw(self.screen)
                    self.login_screen.logo.sprite.logo_bounce()
                    self.login_screen.logo.update()

                    # rotulo fazer login
                    self.login_screen.login_label = self.arkkos_font.render('Faça seu login:', False, 'white')
                    self.login_screen.login_label_rect = self.login_screen.login_label.get_rect(center = (WIDTH/2, 375))
                    self.screen.blit(self.login_screen.login_label, self.login_screen.login_label_rect)

                    # input login
                        # rótulo
                    self.login_screen.login_input_label = self.arkkos_font_smaller.render('Nome de Usuário', False, 'white')
                    self.login_screen.login_input_label_rect = self.login_screen.login_input_label.get_rect(bottomleft = (WIDTH/3, HEIGHT/1.91))
                    self.screen.blit(self.login_screen.login_input_label, self.login_screen.login_input_label_rect)
                        # caixa de texto
                    pygame.draw.rect(self.screen, self.login_screen.login_input.color, self.login_screen.login_input.input_rect)
                    pygame.draw.rect(self.screen, self.login_screen.login_input.color_border, self.login_screen.login_input.input_rect, 2)
                    self.login_user_text_surf = self.arkkos_font.render(self.login_user_text, False, 'white')
                    self.screen.blit(self.login_user_text_surf, (self.login_screen.login_input.input_rect.x + 10, self.login_screen.login_input.input_rect.y + 12))
                    if self.login_screen.login_input.active == True:
                        self.login_screen.login_input.color_border = self.login_screen.login_input.color_border_active
                    else:
                        self.login_screen.login_input.color_border = self.login_screen.login_input.color_border_inactive

                    # input senha
                        # rótulo
                    self.login_screen.password_input_label = self.arkkos_font_smaller.render('Senha', False, 'white')
                    self.login_screen.password_input_label_rect = self.login_screen.password_input_label.get_rect(bottomleft = (WIDTH/3, HEIGHT/1.56))
                    self.screen.blit(self.login_screen.password_input_label, self.login_screen.password_input_label_rect)
                        # caixa de texto
                    pygame.draw.rect(self.screen, self.login_screen.password_input.color, self.login_screen.password_input.input_rect)
                    pygame.draw.rect(self.screen, self.login_screen.password_input.color_border, self.login_screen.password_input.input_rect, 2)
                    self.login_user_text_surf = self.arkkos_font.render(self.password_user_text, False, 'white')
                    self.screen.blit(self.login_user_text_surf, (self.login_screen.password_input.input_rect.x + 10, self.login_screen.password_input.input_rect.y + 12))
                    if self.login_screen.password_input.active == True:
                        self.login_screen.password_input.color_border = self.login_screen.password_input.color_border_active
                    else:
                        self.login_screen.password_input.color_border = self.login_screen.password_input.color_border_inactive


                    # botao conectar
                        # botao
                    pygame.draw.rect(self.screen,self.login_screen.submit_button.color, self.login_screen.submit_button.rect)
                    pygame.draw.rect(self.screen, self.login_screen.submit_button.color_border, self.login_screen.submit_button.rect, 2)
                        # texto
                    self.login_screen.submit_button.submit_label = self.arkkos_font.render(self.login_screen.submit_button.submit_label, False, self.login_screen.submit_button.text_color)
                    self.login_screen.submit_button.submit_label_rect = self.login_screen.submit_button.submit_label.get_rect(center = (WIDTH/2,HEIGHT/1.22))
                    self.screen.blit(self.login_screen.submit_button.submit_label, self.login_screen.submit_button.submit_label_rect)
                    if self.login_screen.submit_button.active == True:
                        self.login_screen.submit_button.color = self.login_screen.submit_button.color_active
                        self.login_screen.submit_button.text_color = self.login_screen.submit_button.color_inactive
                        self.login_screen.submit_button.submit_label = 'Conectando...'
                        if self.login_screen.submit_button.load_delay < 10:
                            self.login_screen.submit_button.load_delay += 0.5
                            print(self.login_screen.submit_button.load_delay)
                        # validacao de usuario
                        if self.login_screen.submit_button.load_delay == 10:
                            if self.login_user_text != '' and self.password_user_text != '':
                                self.user_index = user_list.index(self.login_user_text)
                                self.password_index = password_list.index(self.password_user_text)
                                if self.user_index == self.password_index or user_list.count(self.login_user_text) > 0:
                                    self.game_state = 1
                            else:
                                self.login_screen.submit_button.connection_failed = True
                    else:
                        self.login_screen.submit_button.color = self.login_screen.submit_button.color_inactive
                        self.login_screen.submit_button.text_color = self.login_screen.submit_button.color_active
                        self.login_screen.submit_button.submit_label = 'Conectar'

                    if self.login_screen.submit_button.connection_failed == True:
                            # feedback conexao
                            self.login_screen.feedback = self.arkkos_font.render('Falha ao conectar', False, self.login_screen.submit_button.color_inactive)
                            self.login_screen.feedback_rect = self.login_screen.feedback.get_rect(bottomleft = (WIDTH/2-100, HEIGHT/1.12))
                            self.screen.blit(self.login_screen.feedback, self.login_screen.feedback_rect)
                            self.login_screen.submit_button.load_delay = 0
                            self.login_screen.submit_button.active = False
                            self.login_screen.submit_button.loading = False
            # tela main menu
    def tela_main_menu(self):
                # background
                self.screen.blit(self.main_menu_screen.main_menu.background.image, self.main_menu_screen.main_menu.background.rect)
                if self.main_menu_screen.curr_menu != 0:
                    self.main_menu_screen.return_button.draw(self.screen)
                    self.main_menu_screen.return_button.update()
                # botao de retornar menu
                # menu principal selecionado
                if self.main_menu_screen.curr_menu == 0:
                    self.main_menu_screen.main_menu.welcome_player.image = self.arkkos_font.render(self.main_menu_screen.main_menu.welcome_player.text + self.user.name + '.', False, self.main_menu_screen.main_menu.welcome_player.color)
                    self.main_menu_screen.main_menu.welcome_player.rect = self.main_menu_screen.main_menu.welcome_player.image.get_rect(center = (WIDTH/2, HEIGHT - 500))
                    self.screen.blit(self.main_menu_screen.main_menu.welcome_player.image, self.main_menu_screen.main_menu.welcome_player.rect)

                    # logo
                    self.main_menu_screen.main_menu.logo.draw(self.screen)
                    self.main_menu_screen.main_menu.logo.sprite.logo_bounce()
                    self.main_menu_screen.main_menu.logo.update()

                    # botao de entrar em sala
                    pygame.draw.rect(self.screen, self.main_menu_screen.main_menu.join_room_button.color, self.main_menu_screen.main_menu.join_room_button.rect)
                    pygame.draw.rect(self.screen, self.main_menu_screen.main_menu.join_room_button.color_border, self.main_menu_screen.main_menu.join_room_button.rect, 4)
                    self.main_menu_screen.main_menu.join_room_button.join_room_label_surf = self.arkkos_font.render(self.main_menu_screen.main_menu.join_room_button.join_room_label, False, self.main_menu_screen.main_menu.join_room_button.color_active)
                    self.main_menu_screen.main_menu.join_room_button.join_room_label_rect = self.main_menu_screen.main_menu.join_room_button.join_room_label_surf.get_rect(topleft = (self.main_menu_screen.main_menu.join_room_button.rect.x + 12,self.main_menu_screen.main_menu.join_room_button.rect.y + 30))
                    self.screen.blit(self.main_menu_screen.main_menu.join_room_button.join_room_label_surf, self.main_menu_screen.main_menu.join_room_button.join_room_label_rect)

                    # botao de criar sala
                    pygame.draw.rect(self.screen, self.main_menu_screen.main_menu.create_room_button.color, self.main_menu_screen.main_menu.create_room_button.rect)
                    pygame.draw.rect(self.screen, self.main_menu_screen.main_menu.create_room_button.color_border, self.main_menu_screen.main_menu.create_room_button.rect, 4)
                    self.main_menu_screen.main_menu.create_room_button.create_room_label_surf = self.arkkos_font.render(self.main_menu_screen.main_menu.create_room_button.create_room_label, False, self.main_menu_screen.main_menu.create_room_button.color_active)
                    self.main_menu_screen.main_menu.create_room_button.create_room_label_rect = self.main_menu_screen.main_menu.create_room_button.create_room_label_surf.get_rect(topleft = (self.main_menu_screen.main_menu.create_room_button.rect.x + 53,self.main_menu_screen.main_menu.create_room_button.rect.y + 30))
                    self.screen.blit(self.main_menu_screen.main_menu.create_room_button.create_room_label_surf, self.main_menu_screen.main_menu.create_room_button.create_room_label_rect)
                # menu de se juntar a sala selecionado
                elif self.main_menu_screen.curr_menu == 1:
                    # input de escrever o token
                    pygame.draw.rect(self.screen, self.main_menu_screen.join_room_menu.room_token_input.color, self.main_menu_screen.join_room_menu.room_token_input.input_rect)
                    pygame.draw.rect(self.screen, self.main_menu_screen.join_room_menu.room_token_input.color_border, self.main_menu_screen.join_room_menu.room_token_input.input_rect, self.main_menu_screen.join_room_menu.room_token_input.border_radius)
                    #   selecionar input
                    if self.main_menu_screen.join_room_menu.room_token_input.active == True:
                        self.main_menu_screen.join_room_menu.room_token_input.color_border = self.main_menu_screen.join_room_menu.room_token_input.color_border_active
                        self.main_menu_screen.join_room_menu.room_token_input.border_radius = 5
                    else:
                        self.main_menu_screen.join_room_menu.room_token_input.color_border = self.main_menu_screen.join_room_menu.room_token_input.color_border_inactive
                        self.main_menu_screen.join_room_menu.room_token_input.border_radius = 2
                    # texto de escrever token
                    self.main_menu_screen.join_room_menu.room_token_input.room_token_text_surf = self.arkkos_font_bigger.render(self.room_token_text, False, 'white')
                    self.main_menu_screen.join_room_menu.room_token_input.room_token_text_rect = self.main_menu_screen.join_room_menu.room_token_input.room_token_text_surf.get_rect(bottomleft = (self.main_menu_screen.join_room_menu.room_token_input.input_rect.x + 27, self.main_menu_screen.join_room_menu.room_token_input.input_rect.y + 130))
                    self.screen.blit(self.main_menu_screen.join_room_menu.room_token_input.room_token_text_surf, self.main_menu_screen.join_room_menu.room_token_input.room_token_text_rect)
                    # botao de deletar texto do input
                    self.main_menu_screen.delete_input_button.draw(self.screen)
                    self.main_menu_screen.delete_input_button.update()
                    # titulo de tela
                    self.main_menu_screen.join_room_menu.menu_title.surf = self.arkkos_font_big.render(self.main_menu_screen.join_room_menu.menu_title.text, False, self.main_menu_screen.join_room_menu.menu_title.color)
                    self.main_menu_screen.join_room_menu.menu_title.rect = self.main_menu_screen.join_room_menu.menu_title.surf.get_rect(bottomleft = (WIDTH/5 + 45,HEIGHT/3))
                    self.screen.blit(self.main_menu_screen.join_room_menu.menu_title.surf, self.main_menu_screen.join_room_menu.menu_title.rect)
                    # botao de conectar à sala
                    pygame.draw.rect(self.screen, self.main_menu_screen.join_room_menu.room_connect_button.color, self.main_menu_screen.join_room_menu.room_connect_button.rect)
                    pygame.draw.rect(self.screen, self.main_menu_screen.join_room_menu.room_connect_button.color_border, self.main_menu_screen.join_room_menu.room_connect_button.rect, 4)
                    self.main_menu_screen.join_room_menu.room_connect_button.join_room_label_surf = self.arkkos_font.render(self.main_menu_screen.join_room_menu.room_connect_button.join_room_label, False, self.main_menu_screen.join_room_menu.room_connect_button.color_border)
                    self.main_menu_screen.join_room_menu.room_connect_button.join_room_label_rect = self.main_menu_screen.join_room_menu.room_connect_button.join_room_label_surf.get_rect(bottomleft = (self.main_menu_screen.join_room_menu.room_connect_button.rect.x + 60, self.main_menu_screen.join_room_menu.room_connect_button.rect.y + 60))
                    self.screen.blit(self.main_menu_screen.join_room_menu.room_connect_button.join_room_label_surf, self.main_menu_screen.join_room_menu.room_connect_button.join_room_label_rect)
                    # popup de erro de conexao a sala
                    self.main_menu_screen.join_room_menu.room_error_popup.image = self.arkkos_font.render(self.main_menu_screen.join_room_menu.room_error_popup.message, False, self.main_menu_screen.join_room_menu.room_error_popup.color)
                    self.main_menu_screen.join_room_menu.room_error_popup.rect = self.main_menu_screen.join_room_menu.room_error_popup.image.get_rect(center = (WIDTH/2, HEIGHT - 225))
                    if self.main_menu_screen.join_room_menu.room_error_popup.active == True:
                        self.screen.blit(self.main_menu_screen.join_room_menu.room_error_popup.image, self.main_menu_screen.join_room_menu.room_error_popup.rect)
                        self.main_menu_screen.join_room_menu.room_error_popup.active_timer += 1
                        if self.main_menu_screen.join_room_menu.room_error_popup.active_timer >= 60 * 3.5:
                            self.main_menu_screen.join_room_menu.room_error_popup.active = False
                            self.main_menu_screen.join_room_menu.room_error_popup.active_timer = 0

                # menu de criar sala selecionado
                elif self.main_menu_screen.curr_menu == 2:
                    # titulo da tela
                    self.main_menu_screen.create_room_menu.create_room_title_surf = self.arkkos_font_big.render(self.main_menu_screen.create_room_menu.menu_title.text, False, 'white')
                    self.main_menu_screen.create_room_menu.create_room_title_rect = self.main_menu_screen.create_room_menu.create_room_title_surf.get_rect(center = (WIDTH/2, HEIGHT/4))
                    self.screen.blit(self.main_menu_screen.create_room_menu.create_room_title_surf , self.main_menu_screen.create_room_menu.create_room_title_rect)
                    # botões níveis
                    self.main_menu_screen.create_room_menu.levelsbuttons.draw(self.screen)
                    self.main_menu_screen.create_room_menu.levelsbuttons.sprites()[0].toggle_button()
                    self.main_menu_screen.create_room_menu.levelsbuttons.sprites()[1].toggle_button()
                    self.main_menu_screen.create_room_menu.levelsbuttons.sprites()[2].toggle_button()
                    self.main_menu_screen.create_room_menu.levelsbuttons.update()
                    # botões matéria
                    self.main_menu_screen.create_room_menu.subjectbuttons.draw(self.screen)
                    self.main_menu_screen.create_room_menu.subjectbuttons.sprites()[0].toggle_button()
                    self.main_menu_screen.create_room_menu.subjectbuttons.sprites()[1].toggle_button()
                    self.main_menu_screen.create_room_menu.subjectbuttons.sprites()[2].toggle_button()
                    self.main_menu_screen.create_room_menu.subjectbuttons.sprites()[3].toggle_button()
                    self.main_menu_screen.create_room_menu.subjectbuttons.update()
                    # botão confirmar sala
                    pygame.draw.rect(self.screen, self.main_menu_screen.create_room_menu.confirm_room_button.color, self.main_menu_screen.create_room_menu.confirm_room_button.rect)
                    pygame.draw.rect(self.screen, self.main_menu_screen.create_room_menu.confirm_room_button.color_border, self.main_menu_screen.create_room_menu.confirm_room_button.rect, 4)
                    self.main_menu_screen.create_room_menu.confirm_room_button.confirm_room_label_surf = self.arkkos_font.render(self.main_menu_screen.create_room_menu.confirm_room_button.confirm_room_label, False, self.main_menu_screen.create_room_menu.confirm_room_button.color_border)
                    self.main_menu_screen.create_room_menu.confirm_room_button.confirm_room_label_rect = self.main_menu_screen.create_room_menu.confirm_room_button.confirm_room_label_surf.get_rect(center = (WIDTH/2, self.main_menu_screen.create_room_menu.confirm_room_button.rect.y + 45))
                    self.screen.blit(self.main_menu_screen.create_room_menu.confirm_room_button.confirm_room_label_surf, self.main_menu_screen.create_room_menu.confirm_room_button.confirm_room_label_rect)
                    # popup de erro de criar a sala
                    self.main_menu_screen.create_room_menu.create_error_popup.image = self.arkkos_font.render(self.main_menu_screen.create_room_menu.create_error_popup.message + self.main_menu_screen.create_room_menu.create_error_popup.get_owner_room_token(self.user), False, self.main_menu_screen.create_room_menu.create_error_popup.color)
                    self.main_menu_screen.create_room_menu.create_error_popup.rect = self.main_menu_screen.create_room_menu.create_error_popup.image.get_rect(center = (WIDTH/2, HEIGHT - 225))
                    if self.main_menu_screen.create_room_menu.create_error_popup.active == True:
                        self.screen.blit(self.main_menu_screen.create_room_menu.create_error_popup.image, self.main_menu_screen.create_room_menu.create_error_popup.rect)
                        self.main_menu_screen.create_room_menu.create_error_popup.active_timer += 1
                        if self.main_menu_screen.create_room_menu.create_error_popup.active_timer >= 60 * 3.5:
                            self.main_menu_screen.create_room_menu.create_error_popup.active = False
                            self.main_menu_screen.create_room_menu.create_error_popup.active_timer = 0
    def tela_batalha(self):
                if self.battle_screen.battle.battle_status == 0:

                    # background
                    self.screen.fill('black')

                    # cenário
                    # chão
                    self.screen.blit(self.battle_screen.battle.floor_img, self.battle_screen.battle.floor_rect)
                    # personagens
                    #   jogador
                    #       sombra
                    if self.battle_screen.battle.player.sprite.dead == False:
                        self.screen.blit(self.battle_screen.battle.player.sprite.shadow.image, self.battle_screen.battle.player.sprite.shadow.rect)
                    self.battle_screen.battle.player.sprite.shadow.rect.x = self.battle_screen.battle.player.sprite.rect.x - 15
                    # imagens do player
                    self.battle_screen.battle.player.sprite.image.set_alpha(self.battle_screen.battle.player.sprite.alpha)
                    self.battle_screen.battle.player.draw(self.screen)
                    self.battle_screen.battle.player.update()
                    #       animacoes
                    #           idle
                    if self.battle_screen.battle.jogador_atacando == False:
                        self.battle_screen.battle.player.sprite.idle_timer += 1
                        if self.battle_screen.battle.player.sprite.idle_timer == 30:
                            self.battle_screen.battle.player.sprite.image = self.battle_screen.battle.player.sprite.idle[1]
                        elif self.battle_screen.battle.player.sprite.idle_timer == 60:
                            self.battle_screen.battle.player.sprite.image = self.battle_screen.battle.player.sprite.idle[0]
                            self.battle_screen.battle.player.sprite.idle_timer = 0
                    #           ataque
                    if self.battle_screen.battle.jogador_atacando == True:
                        self.battle_screen.battle.player.sprite.image = self.battle_screen.battle.player.sprite.attack

                        if self.battle_screen.battle.player.sprite.atacando_state == False:
                            self.battle_screen.battle.player.sprite.acceleration = self.battle_screen.battle.player.sprite.acceleration + 2
                            if self.battle_screen.battle.player.sprite.acceleration >= 27:
                                self.battle_screen.battle.player.sprite.atacando_state = True
                                self.battle_screen.battle.player.sprite.acceleration = 0
                            self.battle_screen.battle.player.sprite.rect.x += self.battle_screen.battle.player.sprite.acceleration
                        else:

                            if self.battle_screen.battle.player.sprite.rect.x >= 150:
                                self.battle_screen.battle.player.sprite.acceleration += 2
                                self.battle_screen.battle.player.sprite.rect.x -= self.battle_screen.battle.player.sprite.acceleration
                            if self.battle_screen.battle.player.sprite.rect.x <= 150:
                                self.battle_screen.battle.player.sprite.atacando_state = False
                                self.battle_screen.battle.jogador_atacando = False
                                self.battle_screen.battle.player.sprite.acceleration = 0
                    #           morrer
                    if self.battle_screen.battle.player.sprite.hp <= 0:
                        self.battle_screen.battle.player.sprite.dead = True
                    if self.battle_screen.battle.player.sprite.dead == True:
                        if self.battle_screen.battle.player.sprite.alpha_count <= 6:
                            self.battle_screen.battle.player.sprite.alpha_timer += 5
                            if self.battle_screen.battle.player.sprite.alpha_timer == 30:
                                self.battle_screen.battle.player.sprite.alpha = 0
                                self.battle_screen.battle.player.sprite.alpha_count += 1
                            elif self.battle_screen.battle.player.sprite.alpha_timer == 60:
                                self.battle_screen.battle.player.sprite.alpha = 255
                                self.battle_screen.battle.player.sprite.alpha_timer = 0


                    #   fada das respostas
                    self.battle_screen.battle.fairy.draw(self.screen)
                    self.battle_screen.battle.fairy.sprite.bounce()
                    self.battle_screen.battle.fairy.update()

                    #   inimigo
                    #   sombra
                    if self.battle_screen.battle.enemy.sprite.dead == False:
                        self.screen.blit(self.battle_screen.battle.enemy.sprite.shadow.image, self.battle_screen.battle.enemy.sprite.shadow.rect)
                    if self.battle_screen.battle.enemy.sprite.name == 'skeleton':
                        self.battle_screen.battle.enemy.sprite.shadow.rect.x = self.battle_screen.battle.enemy.sprite.rect.x + 30
                    elif self.battle_screen.battle.enemy.sprite.name == 'mage':
                        self.battle_screen.battle.enemy.sprite.shadow.rect.x = self.battle_screen.battle.enemy.sprite.rect.x + 65
                    elif self.battle_screen.battle.enemy.sprite.name == 'bats':
                        self.battle_screen.battle.enemy.sprite.shadow.rect.x = self.battle_screen.battle.enemy.sprite.rect.x + 80
                    elif self.battle_screen.battle.enemy.sprite.name == 'golem':
                        self.battle_screen.battle.enemy.sprite.shadow.rect.x = self.battle_screen.battle.enemy.sprite.rect.x + 125
                    
                    #   inimigo
                    self.battle_screen.battle.enemy.sprite.image.set_alpha(self.battle_screen.battle.enemy.sprite.alpha)
                    self.battle_screen.battle.enemy.draw(self.screen)
                    self.battle_screen.battle.enemy.update()
                    #   animacoes
                    #       idle
                    if self.battle_screen.battle.inimigo_atacando == False:
                        self.battle_screen.battle.enemy.sprite.idle_timer += 1
                        if self.battle_screen.battle.enemy.sprite.idle_timer == 30:
                            self.battle_screen.battle.enemy.sprite.image = self.battle_screen.battle.enemy.sprite.idle[1]
                        elif self.battle_screen.battle.enemy.sprite.idle_timer == 60:
                            self.battle_screen.battle.enemy.sprite.image = self.battle_screen.battle.enemy.sprite.idle[0]
                            self.battle_screen.battle.enemy.sprite.idle_timer = 0
                    #       ataque
                    if self.battle_screen.battle.inimigo_atacando == True:
                        self.battle_screen.battle.enemy.sprite.image = self.battle_screen.battle.enemy.sprite.attack
                        if self.battle_screen.battle.enemy.sprite.atacando_state == False:
                            self.battle_screen.battle.enemy.sprite.acceleration = self.battle_screen.battle.enemy.sprite.acceleration + 2
                            if self.battle_screen.battle.enemy.sprite.acceleration >= 27:
                                self.battle_screen.battle.enemy.sprite.atacando_state = True
                                self.battle_screen.battle.enemy.sprite.acceleration = 0
                            self.battle_screen.battle.enemy.sprite.rect.x -= self.battle_screen.battle.enemy.sprite.acceleration
                        else:
                            if self.battle_screen.battle.enemy.sprite.rect.x <= self.battle_screen.battle.enemy.sprite.x_pos:
                                self.battle_screen.battle.enemy.sprite.acceleration += 2
                                self.battle_screen.battle.enemy.sprite.rect.x += self.battle_screen.battle.enemy.sprite.acceleration
                            if self.battle_screen.battle.enemy.sprite.rect.x >= self.battle_screen.battle.enemy.sprite.x_pos:
                                self.battle_screen.battle.enemy.sprite.atacando_state = False
                                self.battle_screen.battle.inimigo_atacando = False
                                self.battle_screen.battle.enemy.sprite.acceleration = 0
                    #       morrer
                    if self.battle_screen.battle.enemy.sprite.hp <= 0:
                        self.battle_screen.battle.enemy.sprite.dead = True
                    if self.battle_screen.battle.enemy.sprite.dead == True:
                        if self.battle_screen.battle.enemy.sprite.alpha_count <= 6:
                            self.battle_screen.battle.enemy.sprite.alpha_timer += 5
                            if self.battle_screen.battle.enemy.sprite.alpha_timer == 30:
                                self.battle_screen.battle.enemy.sprite.alpha = 0
                                self.battle_screen.battle.enemy.sprite.alpha_count += 1
                            elif self.battle_screen.battle.enemy.sprite.alpha_timer == 60:
                                self.battle_screen.battle.enemy.sprite.alpha = 255
                                self.battle_screen.battle.enemy.sprite.alpha_timer = 0 
                    else:
                        self.battle_screen.battle.enemy.sprite.alpha = 255                   
                    # luz
                    self.screen.blit(self.battle_screen.battle.light_img, self.battle_screen.battle.light_rect)
                    # barras de vida
                    #       jogador
                    pygame.draw.rect(self.screen, self.battle_screen.battle.player.sprite.health_bar.color_main, self.battle_screen.battle.player.sprite.health_bar.border_rect)
                    pygame.draw.rect(self.screen, self.battle_screen.battle.player.sprite.health_bar.color_bg, self.battle_screen.battle.player.sprite.health_bar.bg_rect)
                    pygame.draw.rect(self.screen, self.battle_screen.battle.player.sprite.health_bar.color_main, pygame.Rect(self.battle_screen.battle.player.sprite.health_bar.start_x, 100, self.battle_screen.battle.player.sprite.health_bar.width * 2, 25))
                    #           rótulo nome
                    self.screen.blit(self.battle_screen.battle.player.sprite.health_bar.name_label_surf, self.battle_screen.battle.player.sprite.health_bar.name_label_rect)
                    #           hp em números
                    self.player_number_hp_surf = self.arkkos_font.render(str(self.battle_screen.battle.player.sprite.hp) + '/' + str(self.battle_screen.battle.player.sprite.health_bar.hp_max) + ' hp', False, 'white')
                    self.player_number_hp_rect = self.player_number_hp_surf.get_rect(bottomleft = (125,155))
                    self.screen.blit(self.player_number_hp_surf, self.player_number_hp_rect)
                    #       inimigo
                    pygame.draw.rect(self.screen, self.battle_screen.battle.enemy.sprite.health_bar.color_main, self.battle_screen.battle.enemy.sprite.health_bar.border_rect)
                    pygame.draw.rect(self.screen, self.battle_screen.battle.enemy.sprite.health_bar.color_bg, self.battle_screen.battle.enemy.sprite.health_bar.bg_rect)
                    pygame.draw.rect(self.screen, self.battle_screen.battle.enemy.sprite.health_bar.color_main, pygame.Rect(self.battle_screen.battle.enemy.sprite.health_bar.start_x, 100, self.battle_screen.battle.enemy.sprite.health_bar.width * 2, 25))
                    #           rótulo nome
                    self.screen.blit(self.battle_screen.battle.enemy.sprite.health_bar.name_label_surf, self.battle_screen.battle.enemy.sprite.health_bar.name_label_rect)
                    #           hp em números
                    self.enemy_number_hp_surf = self.arkkos_font.render(str(self.battle_screen.battle.enemy.sprite.hp) + '/' + str(self.battle_screen.battle.enemy.sprite.health_bar.hp_max) + ' hp', False, 'white')
                    self.enemy_number_hp_rect = self.enemy_number_hp_surf.get_rect(bottomleft = (625,155))
                    self.screen.blit(self.enemy_number_hp_surf, self.enemy_number_hp_rect)

                    # ui
                    # score
                    self.battle_screen.battle.scoreboard_surf = self.arkkos_font.render('Pontuação: ' + str(self.battle_screen.battle.curr_score), False, 'white')
                    self.battle_screen.battle.scoreboard_rect = self.battle_screen.battle.scoreboard_surf.get_rect(topleft = (20, 20))
                    self.screen.blit(self.battle_screen.battle.scoreboard_surf, self.battle_screen.battle.scoreboard_rect)

                    # questoes


                    # caixa de texto
                    pygame.draw.rect(self.screen, self.battle_screen.battle.text_box.color_border, self.battle_screen.battle.text_box.border_rect)
                    pygame.draw.rect(self.screen, self.battle_screen.battle.text_box.color, self.battle_screen.battle.text_box.rect)

                    # texto da caixa de texto
                    #   associar textos
                    if len(self.battle_screen.battle.text_box_text) > 0:
                        self.battle_screen.battle.text_box_text_surf_line1 = self.arkkos_font.render(self.battle_screen.battle.text_box_text[0:70].rstrip(), False, 'white')
                        self.battle_screen.battle.text_box_text_rect_line1 = self.battle_screen.battle.text_box_text_surf_line1.get_rect(topleft = (30, HEIGHT/1.75))
                        if len(self.battle_screen.battle.text_box_text) > 70:
                            self.battle_screen.battle.text_box_text_surf_line2 = self.arkkos_font.render(self.battle_screen.battle.text_box_text[70:140].rstrip(), False, 'white')
                            self.battle_screen.battle.text_box_text_rect_line2 = self.battle_screen.battle.text_box_text_surf_line2.get_rect(topleft = (30, HEIGHT/1.75 + 40))
                            self.screen.blit(self.battle_screen.battle.text_box_text_surf_line2, self.battle_screen.battle.text_box_text_rect_line2)
                            if len(self.battle_screen.battle.text_box_text) > 140:
                                self.battle_screen.battle.text_box_text_surf_line3 = self.arkkos_font.render(self.battle_screen.battle.text_box_text[140:210].rstrip(), False, 'white')
                                self.battle_screen.battle.text_box_text_rect_line3 = self.battle_screen.battle.text_box_text_surf_line3.get_rect(topleft = (30, HEIGHT/1.75 + 80))
                                self.screen.blit(self.battle_screen.battle.text_box_text_surf_line3, self.battle_screen.battle.text_box_text_rect_line3) 
                    self.screen.blit(self.battle_screen.battle.text_box_text_surf_line1, self.battle_screen.battle.text_box_text_rect_line1)
                    #   pressione espaco pra prosseguir
                    self.battle_screen.battle.press_space_alpha = 100
                    self.battle_screen.battle.press_space_alpha_timer = 0
                    self.battle_screen.battle.press_space_surf = self.arkkos_font_smaller.render('Pressione ESPAÇO', False, 'white')
                    self.battle_screen.battle.press_space_surf.set_alpha(self.battle_screen.battle.press_space_alpha)
                    self.battle_screen.battle.press_space_rect = self.battle_screen.battle.press_space_surf.get_rect(topleft = (770, HEIGHT/1.75 + 125))
                    if self.battle_screen.battle.proceedable == True:
                        self.screen.blit(self.battle_screen.battle.press_space_surf, self.battle_screen.battle.press_space_rect)
                    # alternativas
                    # caixa de alternativa 1
                    if self.battle_screen.battle.alternative1.hover == True and self.proceedable == False: self.battle_screen.battle.alternative1.color_border = self.battle_screen.battle.alternative1.color_border_active
                    else: self.battle_screen.battle.alternative1.color_border = self.battle_screen.battle.alternative1.color_border_inactive
                    pygame.draw.rect(self.screen, self.battle_screen.battle.alternative1.color_border, self.battle_screen.battle.alternative1.border_rect)
                    if self.battle_screen.battle.alternative1.clicked == True: self.battle_screen.battle.alternative1.color = self.battle_screen.battle.alternative1.color_active
                    else: self.battle_screen.battle.alternative1.color = self.battle_screen.battle.alternative1.color_inactive
                    pygame.draw.rect(self.screen, self.battle_screen.battle.alternative1.color, self.battle_screen.battle.alternative1.rect)
                    # texto alternativa 1
                    if self.battle_screen.battle.alternative1.clicked == True and self.proceedable == False: 
                        self.battle_screen.battle.alternative1.color_text = self.battle_screen.battle.alternative1.color_inactive
                    else: 
                        self.battle_screen.battle.alternative1.color_text = self.battle_screen.battle.alternative1.color_active
                        
                    self.battle_screen.battle.alternative1_text_surf = self.arkkos_font_smaller.render(self.battle_screen.battle.alternative1_text, False, self.battle_screen.battle.alternative1.color_text)
                    self.battle_screen.battle.alternative1_text_rect = self.battle_screen.battle.alternative1_text_surf.get_rect(topleft = (15, HEIGHT/1.7 + 190))
                    self.screen.blit(self.battle_screen.battle.alternative1_text_surf, self.battle_screen.battle.alternative1_text_rect)
                    
                    # caixa de alternativa 2
                    if self.battle_screen.battle.alternative2.hover == True and self.proceedable == False: self.battle_screen.battle.alternative2.color_border = self.battle_screen.battle.alternative2.color_border_active
                    else: self.battle_screen.battle.alternative2.color_border = self.battle_screen.battle.alternative2.color_border_inactive
                    pygame.draw.rect(self.screen, self.battle_screen.battle.alternative2.color_border, self.battle_screen.battle.alternative2.border_rect)
                    if self.battle_screen.battle.alternative2.clicked == True and self.proceedable == False: self.battle_screen.battle.alternative2.color = self.battle_screen.battle.alternative2.color_active
                    else: self.battle_screen.battle.alternative2.color = self.battle_screen.battle.alternative2.color_inactive
                    pygame.draw.rect(self.screen, self.battle_screen.battle.alternative2.color, self.battle_screen.battle.alternative2.rect)
                    # texto alternativa 2
                    if self.battle_screen.battle.alternative2.clicked == True and self.proceedable == False: 
                        self.battle_screen.battle.alternative2.color_text == self.battle_screen.battle.alternative2.color_inactive
                    else:
                        self.battle_screen.battle.alternative2.color_text == self.battle_screen.battle.alternative2.color_active
                    self.battle_screen.battle.alternative2_text_surf = self.arkkos_font_smaller.render(self.battle_screen.battle.alternative2_text, False, self.battle_screen.battle.alternative2.color_text)
                    self.battle_screen.battle.alternative2_text_rect = self.battle_screen.battle.alternative2_text_surf.get_rect(topleft = (WIDTH/2 + 15, HEIGHT/1.7 + 190))
                    self.screen.blit(self.battle_screen.battle.alternative2_text_surf, self.battle_screen.battle.alternative2_text_rect)

                    # caixa de alternativa 3
                    if self.battle_screen.battle.alternative3.hover == True and self.proceedable == False: self.battle_screen.battle.alternative3.color_border = self.battle_screen.battle.alternative3.color_border_active
                    else: self.battle_screen.battle.alternative3.color_border = self.battle_screen.battle.alternative3.color_border_inactive
                    pygame.draw.rect(self.screen, self.battle_screen.battle.alternative3.color_border, self.battle_screen.battle.alternative3.border_rect)
                    if self.battle_screen.battle.alternative3.clicked == True and self.proceedable == False: self.battle_screen.battle.alternative3.color = self.battle_screen.battle.alternative3.color_active
                    else: self.battle_screen.battle.alternative3.color = self.battle_screen.battle.alternative3.color_inactive
                    pygame.draw.rect(self.screen, self.battle_screen.battle.alternative3.color, self.battle_screen.battle.alternative3.rect)
                    # texto alternativa 3
                    if self.battle_screen.battle.alternative3.clicked == True and self.proceedable == False: 
                        self.battle_screen.battle.alternative3.color_text == self.battle_screen.battle.alternative3.color_inactive
                    else:
                        self.battle_screen.battle.alternative3.color_text == self.battle_screen.battle.alternative3.color_active
                    self.battle_screen.battle.alternative3_text_surf = self.arkkos_font_smaller.render(self.battle_screen.battle.alternative3_text, False, self.battle_screen.battle.alternative3.color_text)
                    self.battle_screen.battle.alternative3_text_rect = self.battle_screen.battle.alternative3_text_surf.get_rect(topleft = (15, HEIGHT/1.7 + 290))
                    self.screen.blit(self.battle_screen.battle.alternative3_text_surf, self.battle_screen.battle.alternative3_text_rect)

                    # caixa de alternativa 4
                    if self.battle_screen.battle.alternative4.hover == True and self.proceedable == False: self.battle_screen.battle.alternative4.color_border = self.battle_screen.battle.alternative4.color_border_active
                    else: self.battle_screen.battle.alternative4.color_border = self.battle_screen.battle.alternative4.color_border_inactive
                    pygame.draw.rect(self.screen, self.battle_screen.battle.alternative4.color_border, self.battle_screen.battle.alternative4.border_rect)
                    if self.battle_screen.battle.alternative4.clicked == True and self.proceedable == False: self.battle_screen.battle.alternative4.color = self.battle_screen.battle.alternative4.color_active
                    else: self.battle_screen.battle.alternative4.color = self.battle_screen.battle.alternative4.color_inactive
                    pygame.draw.rect(self.screen, self.battle_screen.battle.alternative4.color, self.battle_screen.battle.alternative4.rect)
                    # texto alternativa 4
                    if self.battle_screen.battle.alternative4.clicked == True and self.proceedable == False:  self.battle_screen.battle.alternative4.color_text == self.battle_screen.battle.alternative4.color_inactive
                    else: self.battle_screen.battle.alternative4.color_text == self.battle_screen.battle.alternative4.color_active
                    self.battle_screen.battle.alternative4_text_surf = self.arkkos_font_smaller.render(self.battle_screen.battle.alternative4_text, False, self.battle_screen.battle.alternative4.color_text)
                    self.battle_screen.battle.alternative4_text_rect = self.battle_screen.battle.alternative4_text_surf.get_rect(topleft = (WIDTH/2 + 15, HEIGHT/1.7 + 290))
                    self.screen.blit(self.battle_screen.battle.alternative4_text_surf, self.battle_screen.battle.alternative4_text_rect)
                # perder batalha
                if self.battle_screen.battle.battle_status == 1:
                    # background
                    self.screen.fill('black')
                    # defeat label
                    self.battle_screen.battle.defeat_label_surf = self.arkkos_font_big.render(self.battle_screen.battle.defeat.defeat_label, False, 'white')
                    self.battle_screen.battle.defeat_label_rect = self.battle_screen.battle.defeat_label_surf.get_rect(center = (WIDTH/2, HEIGHT/3 - 150))
                    self.screen.blit(self.battle_screen.battle.defeat_label_surf,self.battle_screen.battle.defeat_label_rect)
                    # enemy defeat label
                    self.battle_screen.battle.defeat_player_label_surf = self.arkkos_font.render(self.battle_screen.battle.defeat.defeat_player_label, False, 'white')
                    self.battle_screen.battle.defeat_player_label_rect = self.battle_screen.battle.defeat_player_label_surf.get_rect(center = (WIDTH/2, HEIGHT/3 - 100))
                    self.screen.blit(self.battle_screen.battle.defeat_player_label_surf,self.battle_screen.battle.defeat_player_label_rect)
                    # try again button
                    pygame.draw.rect(self.screen, self.battle_screen.battle.defeat.try_again_button.color, self.battle_screen.battle.defeat.try_again_button.rect)
                    pygame.draw.rect(self.screen, self.battle_screen.battle.defeat.try_again_button.color_border, self.battle_screen.battle.defeat.try_again_button.rect, 4)
                    self.battle_screen.battle.defeat.try_again_button.try_again_button_label_surf = self.arkkos_font.render(self.battle_screen.battle.defeat.try_again_button.try_again_button_label, False, 'white')
                    self.battle_screen.battle.defeat.try_again_button.try_again_button_label_rect = self.battle_screen.battle.defeat.try_again_button.try_again_button_label_surf.get_rect(center = (self.battle_screen.battle.defeat.try_again_button.rect.x + 115, self.battle_screen.battle.defeat.try_again_button.rect.y + 45))
                    self.screen.blit(self.battle_screen.battle.defeat.try_again_button.try_again_button_label_surf,self.battle_screen.battle.defeat.try_again_button.try_again_button_label_rect)
                # vencer batalha
                elif self.battle_screen.battle.battle_status == 2:
                    # background
                    self.screen.fill('black')
                    # victory label
                    self.battle_screen.battle.victory_label_surf = self.arkkos_font_big.render(self.battle_screen.battle.victory.victory_label, False, 'white')
                    self.battle_screen.battle.victory_label_rect = self.battle_screen.battle.victory_label_surf.get_rect(center = (WIDTH/2, HEIGHT/3 - 150))
                    self.screen.blit(self.battle_screen.battle.victory_label_surf,self.battle_screen.battle.victory_label_rect)
                    # enemy defeat label
                    self.battle_screen.battle.enemy_defeat_label_surf = self.arkkos_font.render(self.battle_screen.battle.victory.enemy_defeat_label, False, 'white')
                    self.battle_screen.battle.enemy_defeat_label_rect = self.battle_screen.battle.enemy_defeat_label_surf.get_rect(center = (WIDTH/2, HEIGHT/3 - 100))
                    self.screen.blit(self.battle_screen.battle.enemy_defeat_label_surf,self.battle_screen.battle.enemy_defeat_label_rect)
                    # pontuacao label
                    self.battle_screen.battle.points_obtained_surf = self.arkkos_font.render(self.battle_screen.battle.victory.points_obtained, False, 'white')
                    self.battle_screen.battle.points_obtained_rect = self.battle_screen.battle.points_obtained_surf.get_rect(center = (WIDTH/2, HEIGHT/3))
                    self.screen.blit(self.battle_screen.battle.points_obtained_surf,self.battle_screen.battle.points_obtained_rect)
                    # continue button
                    pygame.draw.rect(self.screen, self.battle_screen.battle.victory.continue_button.color, self.battle_screen.battle.victory.continue_button.rect)
                    pygame.draw.rect(self.screen, self.battle_screen.battle.victory.continue_button.color_border, self.battle_screen.battle.victory.continue_button.rect, 4)
                    self.battle_screen.battle.victory.continue_button.continue_button_label_surf = self.arkkos_font.render(self.battle_screen.battle.victory.continue_button.continue_button_label, False, 'white')
                    self.battle_screen.battle.victory.continue_button.continue_button_label_rect = self.battle_screen.battle.victory.continue_button.continue_button_label_surf.get_rect(center = (self.battle_screen.battle.victory.continue_button.rect.x + 115, self.battle_screen.battle.victory.continue_button.rect.y + 45))
                    self.screen.blit(self.battle_screen.battle.victory.continue_button.continue_button_label_surf,self.battle_screen.battle.victory.continue_button.continue_button_label_rect)
            # tela sala
    def tela_sala(self):
                # background
                self.screen.fill('black')
                # construir sala
                #   room bg
                self.room_screen.room.room_bg.draw(self.screen)
                self.room_screen.room.room_bg.update()
                #   titulo da sala
                self.room_screen.room.room_title.surf = self.arkkos_font_big.render(self.room_screen.room.room_title.room_title_text, False, 'white')
                self.room_screen.room.room_title.rect = self.room_screen.room.room_title.surf.get_rect(center = (WIDTH/2, HEIGHT/5 - 100))
                self.screen.blit(self.room_screen.room.room_title.surf, self.room_screen.room.room_title.rect)
                #   codigo da sala
                self.room_screen.room.token_text.image = self.arkkos_font.render(self.room_screen.room.token_text.text + self.room_screen.room.token, False, self.room_screen.room.token_text.color)
                self.room_screen.room.token_text.rect = self.room_screen.room.token_text.image.get_rect(center = (WIDTH/2, HEIGHT/5 + 50 - 65))
                self.screen.blit(self.room_screen.room.token_text.image, self.room_screen.room.token_text.rect)
                #   rotulo capacidade
                self.room_screen.room.capacity.surf = self.arkkos_font.render(str(self.room_screen.room.get_player_qty()) + '/' + str(self.room_screen.room.capacity.cap) + ' jogadores presentes', False, 'white')
                self.room_screen.room.capacity.rect = self.room_screen.room.capacity.surf.get_rect(center = (WIDTH/2, HEIGHT/5 + 50 - 100))
                self.screen.blit(self.room_screen.room.capacity.surf, self.room_screen.room.capacity.rect)
                #   mini jogadores
                self.room_screen.room.players.draw(self.screen)
                self.room_screen.room.players.update()
                for player in self.room_screen.room.players.sprites():
                    player.animate()
                self.room_screen.room.update_players()
                if self.room_screen.room_side == 'owner':
                    #   botao de fechar sala
                    pygame.draw.rect(self.screen, self.room_screen.room.close_room_button.color, self.room_screen.room.close_room_button.rect)
                    pygame.draw.rect(self.screen, self.room_screen.room.close_room_button.color_border, self.room_screen.room.close_room_button.rect, 4)
                    #       rotulo botao de fechar sala
                    self.room_screen.room.close_room_button.join_room_label_surf = self.arkkos_font.render(self.room_screen.room.close_room_button.join_room_label, False, 'white')
                    self.room_screen.room.close_room_button.join_room_label_rect = self.room_screen.room.close_room_button.join_room_label_surf.get_rect(bottomleft = (self.room_screen.room.close_room_button.rect.x + 45, self.room_screen.room.close_room_button.rect.y + 57))
                    self.screen.blit(self.room_screen.room.close_room_button.join_room_label_surf, self.room_screen.room.close_room_button.join_room_label_rect)
                else:
                    #   botao de entrar no jogo
                    pygame.draw.rect(self.screen, self.room_screen.room.start_game_button.color, self.room_screen.room.start_game_button.rect)
                    pygame.draw.rect(self.screen, self.room_screen.room.start_game_button.color_border, self.room_screen.room.start_game_button.rect, 4)
                    #       rotulo botao de entrar no jogo
                    self.room_screen.room.start_game_button.join_room_label_surf = self.arkkos_font.render(self.room_screen.room.start_game_button.join_room_label, False, 'white')
                    self.room_screen.room.start_game_button.join_room_label_rect = self.room_screen.room.start_game_button.join_room_label_surf.get_rect(bottomleft = (self.room_screen.room.start_game_button.rect.x + 45, self.room_screen.room.start_game_button.rect.y + 57))
                    self.screen.blit(self.room_screen.room.start_game_button.join_room_label_surf, self.room_screen.room.start_game_button.join_room_label_rect)
                self.room_screen.return_button.draw(self.screen)
                self.room_screen.return_button.update()
            # tela roadmap
    def tela_roadmap(self):
                # background
                self.screen.fill('black')
                # ui
                # titulo campanha 
                # nivel atual

                # botao de iniciar nivel
                try:
                    if self.roadmap_screen.mini_player.sprite.rect.y == self.roadmap_screen.levels.sprites()[self.roadmap_screen.roadmap.curr_lvl].rect.y:
                        pygame.draw.rect(self.screen, self.roadmap_screen.start_level_button.color, self.roadmap_screen.start_level_button.rect)
                        pygame.draw.rect(self.screen, self.roadmap_screen.start_level_button.color_border, self.roadmap_screen.start_level_button.rect, 4)
                        self.roadmap_screen.start_level_button.start_level_button_label_surf = self.arkkos_font_big.render(self.roadmap_screen.start_level_button.start_level_button_label, False, 'white')
                        self.roadmap_screen.start_level_button.start_level_button_label_rect = self.roadmap_screen.start_level_button.start_level_button_label_surf.get_rect(bottomleft = (self.roadmap_screen.start_level_button.rect.x + 45, self.roadmap_screen.start_level_button.rect.y + 75))
                        self.screen.blit(self.roadmap_screen.start_level_button.start_level_button_label_surf, self.roadmap_screen.start_level_button.start_level_button_label_rect)
                except:
                    pass

                # começar nivel
                if self.roadmap_screen.roadmap.start_lvl == True:
                    self.battle_screen.play_battle_music()
                    self.battle_screen.battle = ''
                    self.battle_screen.battle = Battle(Player(self.user.name, 5, 5), self.campaign.level_list[self.roadmap_screen.roadmap.curr_lvl], self.user.curr_score, self.room_screen.room.subject)
                    self.change_game_state(6)
                    self.roadmap_screen.roadmap.start_lvl = False
                elif self.roadmap_screen.roadmap.start_lvl == False:
                    try:
                        self.roadmap_screen.walk_to_lvl()
                    except:
                        self.roadmap_screen.roadmap.end = True
                if self.roadmap_screen.roadmap.end == True:
                    self.change_game_state(4)
                    self.victory_screen.play_victory_music()
                # roadmap
                # caminhos
                self.roadmap_screen.roads.draw(self.screen)
                self.roadmap_screen.levels.update()
                # niveis
                self.roadmap_screen.levels.draw(self.screen)
                self.roadmap_screen.levels.update()
                # mini jogador
                self.roadmap_screen.mini_player.draw(self.screen)
                self.roadmap_screen.mini_player.update()
                #   animacao
                self.roadmap_screen.mini_player.sprite.idle_timer += 1
                if self.roadmap_screen.mini_player.sprite.idle_timer == 15:
                    if self.roadmap_screen.mini_player.sprite.idle_index == 0: self.roadmap_screen.mini_player.sprite.idle_index += 1
                    elif self.roadmap_screen.mini_player.sprite.idle_index == 1: self.roadmap_screen.mini_player.sprite.idle_index -= 1
                    self.roadmap_screen.mini_player.sprite.image = self.roadmap_screen.mini_player.sprite.idle[self.roadmap_screen.mini_player.sprite.idle_index]
                    if self.roadmap_screen.mini_player.sprite.rect.y != self.roadmap_screen.levels.sprites()[self.roadmap_screen.roadmap.curr_lvl].rect.y:
                        pygame.mixer.Sound.play(self.roadmap_screen.mini_player.sprite.step)
                    self.roadmap_screen.mini_player.sprite.idle_timer = 0
    def tela_vitoria(self):
        self.screen.fill('black')

        # titulo
        self.victory_screen.victory_title.image = self.arkkos_font.render('Parabéns, ' + self.user.name + '! Você derrotou todos os monstros!', False, self.victory_screen.victory_title.color)
        self.victory_screen.victory_title.rect = self.victory_screen.victory_title.image.get_rect(center = (WIDTH/2, HEIGHT/3 - 150))
        self.screen.blit(self.victory_screen.victory_title.image, self.victory_screen.victory_title.rect)

        # pontuação
        self.victory_screen.score_result.image = self.arkkos_font.render(self.victory_screen.score_result.text + str(self.user.curr_score), False, self.victory_screen.score_result.color)
        self.victory_screen.score_result.rect = self.victory_screen.score_result.image.get_rect(center = (WIDTH/2, HEIGHT/3))
        self.screen.blit(self.victory_screen.score_result.image, self.victory_screen.score_result.rect)

        # botao voltar menu
        pygame.draw.rect(self.screen, self.victory_screen.return_menu_button.color, self.victory_screen.return_menu_button .rect)
        pygame.draw.rect(self.screen, self.victory_screen.return_menu_button.color_border, self.victory_screen.return_menu_button .rect, 4)
        self.victory_screen.return_menu_button.return_label_surf = self.arkkos_font.render(self.victory_screen.return_menu_button.return_label, False, 'white')
        self.victory_screen.return_menu_button.return_label_rect = self.victory_screen.return_menu_button.return_label_surf.get_rect(bottomleft = (self.victory_screen.return_menu_button .rect.x + 15, self.victory_screen.return_menu_button .rect.y + 50))
        self.screen.blit(self.victory_screen.return_menu_button.return_label_surf, self.victory_screen.return_menu_button.return_label_rect)

    def quit_game(self):
        if self.room_screen.room_side == 'player':
            self.user.exit_room()
        pygame.quit()
        sys.exit()

    # rodar o jogo
    def run(self):

        while True:
            # loop de eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                # eventos tela login
                if self.game_state == 0:
                    if self.login_screen.submit_button.loading == False:
                        # input login
                            # selecionar input login
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.login_screen.login_input.input_rect.collidepoint(event.pos):
                                self.login_screen.login_input.active = True
                                self.login_screen.password_input.active = False
                            else:
                                self.login_screen.login_input.active = False
                            # escrever texto no input login
                        if event.type == pygame.KEYDOWN:
                            if self.login_screen.login_input.active == True:
                                if event.type == pygame.K_BACKSPACE and len(self.login_user_text) > 0:
                                    self.login_user_text = self.login_user_text[len(self.login_user_text) - 1]
                                elif event.type != pygame.K_BACKSPACE and len(self.login_user_text) < 20:
                                        self.login_user_text += event.unicode
                        # input password
                            # selecionar input password
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.login_screen.password_input.input_rect.collidepoint(event.pos):
                                self.login_screen.password_input.active = True
                                self.login_screen.login_input.active = False
                            else:
                                self.login_screen.password_input.active = False
                            # escrever texto no input password
                        if event.type == pygame.KEYDOWN:
                            if self.login_screen.password_input.active == True:
                                if event.type == pygame.K_BACKSPACE and len(self.password_user_text) > 0:
                                    self.password_user_text = self.password_user_text.replace(self.password_user_text[len(self.password_user_text) - 1], '')
                                elif event.type != pygame.K_BACKSPACE and len(self.password_user_text) < 20:
                                        self.password_user_text += event.unicode
                        
                    # botão de conexão
                        # pressionar botao de conexão
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.login_screen.submit_button.rect.collidepoint(event.pos):
                            self.login_screen.submit_button.active = True
                            self.login_screen.submit_button.loading = True
                            self.login_screen.submit_button.connection_failed = False
                # eventos main menu
                if self.game_state == 1:
                    if self.main_menu_screen.curr_menu != 0:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                if self.main_menu_screen.return_button.sprite.rect.collidepoint(event.pos):
                                    pygame.mixer.Sound.play(self.main_menu_screen.select_audio)
                                    self.main_menu_screen.curr_menu = self.main_menu_screen.return_button.sprite.update_menu(0) 
                    if self.main_menu_screen.curr_menu == 0:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.main_menu_screen.main_menu.join_room_button.rect.collidepoint(event.pos):
                                pygame.mixer.Sound.play(self.main_menu_screen.select_audio)
                                self.main_menu_screen.curr_menu = self.main_menu_screen.return_button.sprite.update_menu(1)
                            if self.main_menu_screen.main_menu.create_room_button.rect.collidepoint(event.pos):
                                pygame.mixer.Sound.play(self.main_menu_screen.select_audio)
                                self.main_menu_screen.create_room_menu.room_to_create = RoomToCreate()
                                for button in self.main_menu_screen.create_room_menu.levelsbuttons.sprites():
                                    button.active = False
                                for button in self.main_menu_screen.create_room_menu.subjectbuttons.sprites():
                                    button.active = False
                                self.main_menu_screen.curr_menu = self.main_menu_screen.return_button.sprite.update_menu(2)
                    # tela de entrar em sala
                    elif self.main_menu_screen.curr_menu == 1:
                        # input token
                        #   selecionar input token
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.main_menu_screen.join_room_menu.room_token_input.input_rect.collidepoint(event.pos):
                                self.main_menu_screen.join_room_menu.room_token_input.active = True
                            else:
                                self.main_menu_screen.join_room_menu.room_token_input.active = False
                        #   escrever texto no input login
                        if event.type == pygame.KEYDOWN:
                            if self.main_menu_screen.join_room_menu.room_token_input.active == True:
                                if event.type == pygame.K_BACKSPACE and len(self.room_token_text) > 0 and len(self.room_token_text) < 6:
                                    self.room_token_text = self.room_token_text[len(self.room_token_text) - 1]
                                elif event.type != pygame.K_BACKSPACE and len(self.room_token_text) < 6:
                                        pygame.mixer.Sound.play(self.main_menu_screen.select_audio)
                                        self.room_token_text += event.unicode
                        #   deletar texto do input
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.main_menu_screen.join_room_menu.room_token_input.delete_input_button.rect.collidepoint(event.pos):
                                pygame.mixer.Sound.play(self.main_menu_screen.select_audio)
                                self.room_token_text = self.main_menu_screen.join_room_menu.room_token_input.delete_input_button.deletar_texto(self.room_token_text)
                        # submeter codigo
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.main_menu_screen.join_room_menu.room_connect_button.rect.collidepoint(event.pos) and len(self.room_token_text) <= 6:
                                pygame.mixer.Sound.play(self.main_menu_screen.select_audio)
                                try:
                                    self.room_screen.room = self.main_menu_screen.join_room_menu.room_connect_button.connect_room(self.room_token_text)
                                    self.user.update_user_room(self.room_screen.room)
                                    self.room_screen.set_room_side(self.user)
                                    if self.room_screen.room_side == 'player':
                                        self.main_menu_screen.join_room_menu.room_connect_button.increase_capacity(self.room_screen.room.room_id)
                                    self.change_game_state(2)
                                except:
                                    self.main_menu_screen.join_room_menu.room_error_popup.active = True

                                # if self.room_screen.room.room_connect(self.room_token_text) == True:
                                #     self.change_game_state(2)
                                # else:
                                #     print('erro')
                    # tela de criar sala
                    elif self.main_menu_screen.curr_menu == 2:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.main_menu_screen.create_room_menu.subjectbuttons.sprites()[0].rect.collidepoint(event.pos):
                                for button in self.main_menu_screen.create_room_menu.subjectbuttons.sprites():
                                    if button == self.main_menu_screen.create_room_menu.subjectbuttons.sprites()[0]:
                                        button.active = True
                                        self.main_menu_screen.create_room_menu.room_to_create.subj = 'lp'
                                    else:
                                        button.active = False
                                pygame.mixer.Sound.play(self.main_menu_screen.select_audio)
                            elif self.main_menu_screen.create_room_menu.subjectbuttons.sprites()[1].rect.collidepoint(event.pos):
                                for button in self.main_menu_screen.create_room_menu.subjectbuttons.sprites():
                                    if button == self.main_menu_screen.create_room_menu.subjectbuttons.sprites()[1]:
                                        button.active = True
                                        self.main_menu_screen.create_room_menu.room_to_create.subj = 'poo'
                                    else:
                                        button.active = False
                                pygame.mixer.Sound.play(self.main_menu_screen.select_audio)
                            elif self.main_menu_screen.create_room_menu.subjectbuttons.sprites()[2].rect.collidepoint(event.pos):
                                for button in self.main_menu_screen.create_room_menu.subjectbuttons.sprites():
                                    if button == self.main_menu_screen.create_room_menu.subjectbuttons.sprites()[2]:
                                        button.active = True
                                        self.main_menu_screen.create_room_menu.room_to_create.subj = 'moo'
                                    else:
                                        button.active = False
                                pygame.mixer.Sound.play(self.main_menu_screen.select_audio)
                            elif self.main_menu_screen.create_room_menu.subjectbuttons.sprites()[3].rect.collidepoint(event.pos):
                                for button in self.main_menu_screen.create_room_menu.subjectbuttons.sprites():
                                    if button == self.main_menu_screen.create_room_menu.subjectbuttons.sprites()[3]:
                                        button.active = True
                                        self.main_menu_screen.create_room_menu.room_to_create.subj = 'bd'
                                    else:
                                        button.active = False
                                pygame.mixer.Sound.play(self.main_menu_screen.select_audio)
                            
                            if self.main_menu_screen.create_room_menu.levelsbuttons.sprites()[0].rect.collidepoint(event.pos):
                                for button in self.main_menu_screen.create_room_menu.levelsbuttons.sprites():
                                    if button == self.main_menu_screen.create_room_menu.levelsbuttons.sprites()[0]:
                                        button.active = True
                                        self.main_menu_screen.create_room_menu.room_to_create.levels = 5
                                    else:
                                        button.active = False
                                pygame.mixer.Sound.play(self.main_menu_screen.select_audio)
                            elif self.main_menu_screen.create_room_menu.levelsbuttons.sprites()[1].rect.collidepoint(event.pos):
                                for button in self.main_menu_screen.create_room_menu.levelsbuttons.sprites():
                                    if button == self.main_menu_screen.create_room_menu.levelsbuttons.sprites()[1]:
                                        button.active = True
                                        self.main_menu_screen.create_room_menu.room_to_create.levels = 10
                                    else:
                                        button.active = False
                                pygame.mixer.Sound.play(self.main_menu_screen.select_audio)
                            elif self.main_menu_screen.create_room_menu.levelsbuttons.sprites()[2].rect.collidepoint(event.pos):
                                for button in self.main_menu_screen.create_room_menu.levelsbuttons.sprites():
                                    if button == self.main_menu_screen.create_room_menu.levelsbuttons.sprites()[2]:
                                        button.active = True
                                        self.main_menu_screen.create_room_menu.room_to_create.levels = 15
                                    else:
                                        button.active = False
                                pygame.mixer.Sound.play(self.main_menu_screen.select_audio)
                
                            if self.main_menu_screen.create_room_menu.confirm_room_button.rect.collidepoint(event.pos):
                                try:
                                    self.main_menu_screen.create_room_menu.room_to_create.gerar_token()
                                    self.main_menu_screen.create_room_menu.room_to_create.inserir_dados(self.user)
                                    self.room_screen.room = self.main_menu_screen.join_room_menu.room_connect_button.connect_room(self.main_menu_screen.create_room_menu.room_to_create.token)
                                    self.user.update_user_room(self.room_screen.room)
                                    self.room_screen.set_room_side(self.user)
                                    self.change_game_state(2)
                                except:
                                    self.main_menu_screen.create_room_menu.create_error_popup.active = True
                # eventos tela sala
                if self.game_state == 2:
                        # botão iniciar jogo
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.room_screen.room_side == 'player':
                                if self.room_screen.room.start_game_button.rect.collidepoint(event.pos):
                                    pygame.mixer.Sound.play(self.main_menu_screen.select_audio)
                                    self.campaign.build_campaign(self.inimigos, self.chefes)
                                    self.roadmap_screen.roadmap = Roadmap(5)
                                    self.roadmap_screen.gen_levels()
                                    self.roadmap_screen.play_dungeon_music()
                                    self.change_game_state(3)
                            else:
                                if self.room_screen.room.close_room_button.rect.collidepoint(event.pos):
                                    pygame.mixer.Sound.play(self.main_menu_screen.select_audio)
                                    self.room_screen.room.close_room_button.close_room(self.user)
                                    self.main_menu_screen.curr_menu = 0
                                    self.change_game_state(1)
                                    del self.room_screen.room
                            
                            if self.room_screen.return_button.sprite.rect.collidepoint(event.pos):
                                pygame.mixer.Sound.play(self.main_menu_screen.select_audio)
                                if self.room_screen.room_side == 'player':
                                    self.user.exit_room()
                                self.main_menu_screen.curr_menu = 0
                                self.change_game_state(1)
                                del self.room_screen.room
                # eventos tela roadmap
                if self.game_state == 3:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.roadmap_screen.start_level_button.rect.collidepoint(event.pos):
                            pygame.mixer.Sound.play(self.roadmap_screen.join_battle_audio)
                            self.roadmap_screen.roadmap.start_lvl = True
                # eventos batalha
                if self.game_state == 6:
                # botões de alternativa
                    # passar mouse por cima
                    # botão de alternativa 1
                    if self.battle_screen.battle.proceedable == False and self.battle_screen.battle.player.sprite.dead == False and self.battle_screen.battle.enemy.sprite.dead == False and self.battle_screen.battle.battle_status == 0:
                        if self.battle_screen.battle.alternative1.border_rect.collidepoint(pygame.mouse.get_pos()):
                            self.battle_screen.battle.alternative1.hover = True
                        else:
                            self.battle_screen.battle.alternative1.hover = False
                        # botão de alternativa 2
                        if self.battle_screen.battle.alternative2.border_rect.collidepoint(pygame.mouse.get_pos()):
                            self.battle_screen.battle.alternative2.hover = True
                        else:
                            self.battle_screen.battle.alternative2.hover = False
                        # botão de alternativa 3
                        if self.battle_screen.battle.alternative3.border_rect.collidepoint(pygame.mouse.get_pos()):
                            self.battle_screen.battle.alternative3.hover = True
                        else:
                            self.battle_screen.battle.alternative3.hover = False
                        # botão de alternativa 4
                        if self.battle_screen.battle.alternative4.border_rect.collidepoint(pygame.mouse.get_pos()):
                            self.battle_screen.battle.alternative4.hover = True
                        else:
                            self.battle_screen.battle.alternative4.hover = False
                    
                    # clicar nos botoes
                        # alternative 1
                    if self.battle_screen.battle.proceedable == False and self.battle_screen.battle.player.sprite.dead == False and self.battle_screen.battle.enemy.sprite.dead == False and self.battle_screen.battle.battle_status == 0:
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.battle_screen.battle.alternative1.border_rect.collidepoint(pygame.mouse.get_pos()):
                                self.battle_screen.battle.alternative1.clicked = True
                                self.battle_screen.battle.selecionar_alternativa(0)
                        else: 
                                self.battle_screen.battle.alternative1.clicked = False
                            # alternative 2
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.battle_screen.battle.alternative2.border_rect.collidepoint(pygame.mouse.get_pos()):
                                self.battle_screen.battle.alternative2.clicked = True
                                self.battle_screen.battle.selecionar_alternativa(1)
                        else:
                                self.battle_screen.battle.alternative2.clicked = False
                            # alternative 3
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.battle_screen.battle.alternative3.border_rect.collidepoint(pygame.mouse.get_pos()):
                                self.battle_screen.battle.alternative3.clicked = True
                                self.battle_screen.battle.selecionar_alternativa(2)
                        else:
                                self.battle_screen.battle.alternative3.clicked = False
                            # alternative 4
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            if self.battle_screen.battle.alternative4.border_rect.collidepoint(pygame.mouse.get_pos()):
                                self.battle_screen.battle.alternative4.clicked = True
                                self.battle_screen.battle.selecionar_alternativa(3)
                        else:
                                self.battle_screen.battle.alternative4.clicked = False
                        
                    # clicar no botao de continuar
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.battle_screen.battle.victory.continue_button.rect.collidepoint(pygame.mouse.get_pos()) and self.battle_screen.battle.battle_status == 2:
                            self.user.update_score(self.battle_screen.battle.curr_score)
                            self.roadmap_screen.roadmap.curr_lvl = self.roadmap_screen.roadmap.up_level()
                            self.roadmap_screen.play_dungeon_music()
                            self.change_game_state(3)


                    # clicar no botao de tentar novamente
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.battle_screen.battle.defeat.try_again_button.rect.collidepoint(pygame.mouse.get_pos()) and self.battle_screen.battle.battle_status == 1:
                            self.roadmap_screen.roadmap.curr_lvl = 0
                            self.user.curr_score = 0
                            self.roadmap_screen.reset_walk()
                            self.roadmap_screen.play_dungeon_music()
                            self.change_game_state(3)


                    # avançar texto
                    if self.battle_screen.battle.proceedable == True and self.battle_screen.battle.battle_status == 0:
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_SPACE:
                                pygame.mixer.Sound.play(self.battle_screen.battle.select_audio)
                                self.battle_screen.battle.proceed_text()
                # eventos tela vitoria
                if self.game_state == 4:
                   if event.type == pygame.MOUSEBUTTONDOWN:
                       if self.victory_screen.return_menu_button.rect.collidepoint(event.pos):
                           pygame.mixer.Sound.play(self.roadmap_screen.join_battle_audio)
                           self.main_menu_screen.play_title_music()
                           self.change_game_state(2)
                           self.roadmap_screen.reset_walk()
                           self.campaign.level_list = []
            if self.game_state == 0:
                self.tela_login()
            elif self.game_state == 1:
                self.tela_main_menu()
            elif self.game_state == 2:
                self.tela_sala()
            elif self.game_state == 3:
                self.tela_roadmap()
            elif self.game_state == 4:
                self.tela_vitoria()
            elif self.game_state == 5:
                pass
            elif self.game_state == 6:
                self.tela_batalha()
            pygame.display.update()
            self.clock.tick(FPS)